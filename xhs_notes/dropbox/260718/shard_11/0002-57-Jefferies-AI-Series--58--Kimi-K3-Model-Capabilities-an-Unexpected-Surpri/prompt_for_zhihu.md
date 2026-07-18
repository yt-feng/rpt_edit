你是知乎商业/行业研究作者，擅长把英文/中文研报改写成适合知乎发布的长文。

【目标】
- 基于下面研报解析内容，生成一篇中文知乎文章。
- 风格接近微信公众号文章，但更适合知乎：论证更完整、语气更克制、有问题意识、有推理链条。
- 文章不需要把研报所有内容讲完，要留下继续阅读完整报告或加入社群讨论的空间。
- 目标长度：约 2200 字，允许上下浮动 20%。

【结构要求】
1. 第一行：知乎标题，直接讲观点，不要标题党，不要夸张极限词。
2. 开头 2-3 段：用一个真实问题或市场分歧切入，说明为什么这份报告值得看。
3. 正文按金字塔原则组织：先给核心判断，再展开 3-5 个支撑逻辑。
4. 每个小标题都要像观点句，不要写“核心判断”“支撑逻辑一”“对读者的启发”这种模板名。
5. 内容要比小红书更理性，比微信更像问答式分析，可以适度提出反问。
6. 结尾自然留下讨论空间，可使用这类表达：`完整报告里还有不少细节，适合放在社群里继续拆。`

【平台发布合规要求】
- 不要出现“投资建议”“买入”“卖出”“强烈推荐”“稳赚”“保本”“必涨”“抄底”“上车”“内幕”“翻倍”等金融操作或收益承诺表达。
- 不要写“非投资建议”“仅做学习交流”这种免责声明，也不要出现包含“投资”的免责声明。
- “投资”相关词尽量改成“投研”“研究”“观察”“学习参考”。
- 不要写“关注”“点赞”“求关注”“评论区留言”等直接互动诱导。
- 不要使用“爆款”“震惊”“必看”“必读”“最强”“最全”“唯一”“全网首发”等极限词。

【内容要求】
- 只能基于研报原文和解析内容推导，不要编造数据、页数、作者、结论或引用。
- 可以基于报告内容做适度发散，但必须明确哪些是报告内容，哪些是你的延展观察。
- 默认避免具体投行品牌名，比如“GS”“GS”，统一写作“投行研报”或使用 GS/JPM/MS 等缩写。
- 不要输出解释说明，只输出知乎文章正文。

【研报解析内容】
"""
# AI Series #58: Kimi K3 Model Capabilities an Unexpected Surprise for Market

Moonshot AI released the first open 2.8T model K3 which ranked No. 3 in Artificial Analysis and behind Fable5 and GPT-5.6 Sol (Max). It ranked No. 1 in Frontend Code Arena. We view the breakthrough as unexpected and drives sector innovation amid fast model iterations. According to Token Expenditure Index, it reflects continued appeal for a cost-efficient model (Exhibit 3), which is positive for China models with strong cost performance (Exhibit 2)

In this report, we provide investors with data points on model pricing by companies, pricing comparison between China and US, model intelligence from Artificial Analysis, token consumption in OpenRouter, Token Expenditure Index trends and other industry data for analysis.

Moonshot AI released the first open 2.8T model and ranked top positions across different metrics (Exhibit 5-6). K3 is built for long-horizon coding, knowledge work and reasoning. Highlights (1) 1M context and native multimodal; (2) No 3 in Artificial Analysis Index and behind Fable5 and GPT-5.6 Sol (Max); (3) No. 1 in Frontend Code Arena; It has leading positions in coding, general agents and visual agents vs global peers. The full model weights will be released on 27 Jul.

Cost performance vs global peers. We compare the input / output price of K3 with global peers on its cost performance (Exhibit 1). K3 is built on Delta Attention and Attention Residuals. Highlights (1) Delta Attention enables up to 6.3x faster decoding in million token contexts; (2) Attention Residuals deliver 25% higher training efficiency at less than 2% additional costs. The architectural updates leads to (1) activates 16 out of 896 experts effectively when paired with Stable LatentMoE framework; (2) 2.5x improvement in overall scaling efficiency vs K2.

Silicon Data LLM Token Expenditure Index : The week of 12 Jul showed continued softness. The index (Exhibit 3) is weighted by where usage is concentrated (e.g. expenditure goes up when demand shifts towards premium models). On the other hand, media reports (e.g. The Information, Economic Observer) highlight tech and internet companies set upper limit on token consumption among employees. According to our checks, the index ranged from 1.57 to 1.61 the week of 12 Jul (vs 1.63 to 1.65 the week of 5 Jul), vs 2.04 on 31 May. Based on Artificial Analysis, China models DeepSeek, Qwen, Kimi, MiniMax and Zhipu are highly cost-efficient vs US models and API cost is a fraction vs US models (Exhibit 2), thanks to former's refined architecture such as MoE (Mixture of Experts), attention mechanism (Group-Query Attention GQA, sparse attention) and MLU (Model FLOPs Utilization).

OpenRouter: Token consumption up vs prior week. Based on analysis of the week of 6 Jul (vs week of 29 Jun) (Exhibit 4), number of weekly tokens consumed increased by 12.6% at 52.6tn. In terms of ranking, DeepSeek V4 Flash ranked no 1, followed by Xiaomi MiMo-V2.5 and MiniMax M3.

BAT, KC, AI labs and Kling are Beneficiaries on Rising AI Demand. We expect the surge in token consumption on rising demand for AI models and agents to benefit CSPs like Baidu, Alibaba, Tencent (BAT), Kingsoft Cloud (KC), AI labs and Kling. According to analysis from Artificial Analysis: (1) there is a narrowing intelligence gap between US and China models; (2) API cost is just a fraction vs US benefiting from MoE, linear attention, and MFU; (3) Coding, Workspace scenario and mid- to long-form content should see significant opportunities ahead

Continued overleaf...

Exhibit 1 - Input and output prices for flagship models by companies

<table><tr><td>Models</td><td>Total parameters</td><td>Input Price (USD)</td><td>Output Price (USD)</td></tr><tr><td>Kimi-3</td><td>2.8T</td><td>3.00</td><td>15.00</td></tr><tr><td>DeepSeek-V4-Pro</td><td>1.6T</td><td>0.87</td><td>1.74</td></tr><tr><td>Qwen3.7 Max</td><td>1.2T</td><td>2.50</td><td>7.50</td></tr><tr><td>GLM-5.2</td><td>744B</td><td>1.40</td><td>4.40</td></tr><tr><td>MiniMax M3</td><td>428B</td><td>0.60</td><td>2.40</td></tr><tr><td>Hy3</td><td>295B</td><td>0.06</td><td>0.22</td></tr><tr><td>Claude Opus 4.8</td><td>Not disclosed</td><td>5.00</td><td>25.00</td></tr><tr><td>Claude Sonnet 5</td><td>Not disclosed</td><td>3.00</td><td>15.00</td></tr></table>

Source: Company, JEF
Note: Pricing for Qwen is based on official prices after end of promotion, pricing for DeepSeek-V4-Pro is during peak hours

Exhibit 2 - Blended prices for China models vs US models (2Q26)  
![](images/1954d24e804065d5d69e245bd325b7b13d69c42c0e3591d778e20c8b7d0958cb.jpg)  
Source: Artificial Analysis, JEF

Exhibit 3 - Silicon Data LLM Token Expenditure Index  
![](images/f3d8d35ccf7ded4637ef74acb60cda58e3262c36b1a12ef008f12944fb258c44.jpg)  
Source: Bloomberg, JEF

Exhibit 4 - Weekly token consumption over the past 12 months as of 13 Jul (tn)  
![](images/94e598ccb3d28ad7312de43e976a6e337b1232780ac12b355aa647ab9433b80c.jpg)  
Source: OpenRouter, JEF

Zoey Zong \* | Equity Analyst
852 3743 8163 | zoey.zong@JEF.com

Visual Agents All maxed out on thinking effort: max or xhigh.

Exhibit 5 - Coding Assessment: K3 vs Global Peers

Coding All maxed out on thinking effort: max or xhigh.

![](images/130b0534893147217343aeda53a9e3537826e4713b7fb6ec6fdf94761df0d1e7.jpg)

![](images/cf698f818e131cb3793524493f107d2787a55398d543b9f8109e1192fa5115b0.jpg)

![](images/b39ef430c93ab6f7ba4fadb314d69186fc54129e79021ee5ecd803f0448dd9ed.jpg)

![](images/f8cff3a6eaf0dabef9ee18ac583bfc45c7ce1316c67a83ed23676759c6181118.jpg)

![](images/56a2d631a9d56f96f5667ec80ee7859f6d294b72a51a671517587aa81f117655.jpg)  
Note: All Fable 5 results are with potential fallbacks. All GPT-5.6 Sol results include potential cyberguards.

![](images/9474b4c7191923489b73a99bc289b6ed1b72b48100f5368f30ba630707669e84.jpg)  
Source: Moonshot AI, JEF

Exhibit 6 - General Assessment: K3 vs Global Peers  
General Agents All maxed out on thinking effort: max or xhigh.  
![](images/0b011e53dae3db14a7780eaf7a39ebd0f3fc146ef69537d0f28d36162955f9ce.jpg)

![](images/5b83f8d16a96af22adc5d07a58b16434126493259c4a74e6b0c8305c9ea18305.jpg)

![](images/6b4e0fa0de068d530ae21c5fbd887a8866206557cb5ebf48a81245d7d7b4cc7b.jpg)

![](images/c798f20d5476ac5cd98ad400614da58ebe8e85cfe41341c8944c65ba6d8634c0.jpg)

![](images/ae78b057f6fa8ad445a61b4ef806a1fe1b4ab77bb89f3ea38f4e482f596505fc.jpg)

![](images/227c6f0ce227fc26bbb6f5fa55776d8370c729b52234dbea0cb8ebe08967fc00.jpg)

![](images/be172889abe0db85e29788a132a9406ed18662c2a853e9292e326053c0fb8fd5.jpg)  
Source: Moonshot AI, JEF

![](images/2ddd38e6e32cd9ace97397e0cac66c122924050ad7d3b1a058905e1717e0b578.jpg)  
Note: All Fable 5 results are with potential fallbacks. All GPT-5.6 Sol results include potential cyberguards.

Exhibit 7 - Coding Cost Per Task Assessment: K3 vs Global Peers  
![](images/f605ae1d3afd96d276304bf315633bda7ee561e72da2b9c30ad53b4029ff3cc1.jpg)  
Source: Moonshot AI, JEF

Exhibit 8 - Browsing Cost Per Task Assessment: K3 vs Global Peers  
BrowseComp · Score vs Cost per Task  
![](images/781a52408134638c50cc57bb56d9ceb4654fd546099dfe1bb0b1e5b3250278f8.jpg)  
Source: Moonshot AI, JEF

Exhibit 9 - Full Benchmark Table  
Full Benchmark Table

<table><tr><td>Benchmark</td><td>Kimi K3 (max)</td><td>Claude Fable 5 (max, with fallback)</td><td>GPT 5.6 Sol (max)</td><td>Claude Opus 4.8 (max)</td><td>GPT 5.5 (xhigh)</td><td>GLM-5.2 (max)</td></tr><tr><td colspan="7">Coding</td></tr><tr><td>DeepSWE</td><td>67.5</td><td>70.0</td><td>73.0</td><td>59.0</td><td>67.0</td><td>46.2</td></tr><tr><td>Program Bench</td><td>77.8</td><td>76.8</td><td>77.6</td><td>71.9</td><td>70.8</td><td>63.7</td></tr><tr><td>Terminal Bench 2.1</td><td>88.3</td><td>84.6</td><td>88.8</td><td>84.6</td><td>83.4</td><td>82.7</td></tr><tr><td>FrontierSWE</td><td>81.2</td><td>86.6</td><td>71.3</td><td>66.7</td><td>64.9</td><td>67.3</td></tr><tr><td>SWE Marathon</td><td>42.0</td><td>35.0</td><td>39.0</td><td>40.0</td><td>14.0</td><td>13.0</td></tr><tr><td>PostTrain Bench</td><td>36.6</td><td>41.4</td><td>34.6</td><td>34.1</td><td>28.4</td><td>34.3</td></tr><tr><td>MLS Bench</td><td>48.3</td><td>49.9</td><td>46.2</td><td>42.8</td><td>35.5</td><td>40.4</td></tr><tr><td>Kimi Code Bench 2.0 (Internal)</td><td>72.9</td><td>76.9</td><td>64.8</td><td>71.7</td><td>69.0</td><td>64.2</td></tr></table>

Source: Moonshot AI, JEF

Exhibit 10 - Full Benchmark Table (cont'd)

<table><tr><td colspan="7">Agentic</td></tr><tr><td>GDPval-AA v2 (Elo-score)</td><td>1668.0</td><td>1760.0</td><td>1748.0</td><td>1600.0</td><td>1494.0</td><td>1514.0</td></tr><tr><td>BrowseComp</td><td>91.2</td><td>88.0</td><td>90.4</td><td>84.3</td><td>84.4</td><td>—</td></tr><tr><td>DeepSearchQA (f1-score)</td><td>95.0</td><td>94.2</td><td>—</td><td>93.1</td><td>—</td><td>—</td></tr><tr><td>Toolathlon-Verified</td><td>73.2</td><td>77.9</td><td>74.9</td><td>76.2</td><td>73.5</td><td>59.9</td></tr><tr><td>MCP Atlas</td><td>84.2</td><td>84.7</td><td>83.6</td><td>83.6</td><td>82.8</td><td>82.6</td></tr><tr><td>Automation Bench</td><td>30.8</td><td>29.1</td><td>29.7</td><td>27.2</td><td>22.7</td><td>12.9</td></tr><tr><td>Job Bench</td><td>52.9</td><td>57.4</td><td>46.5</td><td>48.4</td><td>38.3</td><td>43.4</td></tr><tr><td>AA-Briefcase (Elo-score)</td><td>1548.0</td><td>1583.0</td><td>1495.0</td><td>1354.0</td><td>1158.0</td><td>1260.0</td></tr><tr><td>APEX-Agents</td><td>37.6</td><td>43.3</td><td>39.9</td><td>39.4</td><td>38.5</td><td>35.6</td></tr><tr><td>Office QA Pro</td><td>63.3</td><td>69.9*</td><td>63.2*</td><td>63.9*</td><td>60.9*</td><td>41.4</td></tr><tr><td>SpreadsheetBench 2</td><td>34.8</td><td>34.7*</td><td>32.4*</td><td>31.6*</td><td>29.1*</td><td>28.1</td></tr><tr><td>DECK-Bench (Internal)</td><td>73.5</td><td>73.0</td><td>74.7</td><td>66.9</td><td>68.2</td><td>68.6</td></tr></table>

Source: Moonshot AI, JEF

Exhibit 11 - Full Benchmark Table (cont'd)

<table><tr><td colspan="7">Reasoning &amp; Knowledge</td></tr><tr><td>GPQA-Diamond</td><td>93.5</td><td>92.6</td><td>94.1</td><td>91.0</td><td>93.5</td><td>91.2</td></tr><tr><td>HLE-Full</td><td>43.5</td><td>53.3</td><td>44.5</td><td>49.8*</td><td>41.4*</td><td>—</td></tr><tr><td>HLE-Full w/ tools</td><td>56.0</td><td>63.0</td><td>58.0</td><td>57.9*</td><td>52.2*</td><td>—</td></tr><tr><td colspan="7">Vision</td></tr><tr><td>MMMU-Pro</td><td>81.6</td><td>81.2</td><td>83.0</td><td>78.9</td><td>81.2</td><td>—</td></tr><tr><td>MMMU-Pro w/ python</td><td>83.4</td><td>86.5</td><td>84.6</td><td>82.7</td><td>83.2</td><td>—</td></tr><tr><td>CharXiv (RQ)</td><td>84.8</td><td>88.9</td><td>84.6</td><td>80.5</td><td>84.1</td><td>—</td></tr><tr><td>CharXiv (RQ) w/ python</td><td>91.3</td><td>93.5</td><td>89.1</td><td>89.9</td><td>89.0</td><td>—</td></tr><tr><td>MathVision</td><td>94.3</td><td>94.8</td><td>95.8</td><td>86.7</td><td>92.2</td><td>—</td></tr><tr><td>MathVision w/ python</td><td>97.8</td><td>98.6</td><td>97.8</td><td>97.1</td><td>96.8</td><td>—</td></tr><tr><td>BabyVision w/ python</td><td>85.7</td><td>90.5</td><td>88.9</td><td>81.2</td><td>83.6</td><td>—</td></tr><tr><td>ZeroBench_main (pass@5)</td><td>23.0</td><td>23.0</td><td>17.0</td><td>17.0</td><td>22.0</td><td>—</td></tr><tr><td>ZeroBench_main w/ python (pass@5)</td><td>41.0</td><td>46.0</td><td>35.0</td><td>34.0</td><td>41.0</td><td>—</td></tr><tr><td>WorldVQA ForceAnswer</td><td>51.0</td><td>56.7</td><td>41.8</td><td>39.1</td><td>38.5</td><td>—</td></tr><tr><td>OmniDocBench</td><td>91.1</td><td>89.8</td><td>85.8</td><td>87.9</td><td>89.4</td><td>—</td></tr><tr><td>PerceptionBench</td><td>58.5</td><td>57.2</td><td>59.7</td><td>47.2</td><td>55.8</td><td>—</td></tr></table>

Source: Moonshot AI, JEF  
Exhibit 12 - Artificial Analysis Intelligence Index  
Artificial Analysis Intelligence Index v4.1 incorporates 9 evaluations: GDPval-AA v2, $\tau^3$ -Banking, Terminal-Bench v2.1, SciCode, Humanity's Last Exam, GPQA Diamond, CritPt, AA-Omniscience, AA-LCR

Artificial Analysis Intelligence Index

Artificial Analysis  
![](images/8b8f1cdd0b1863e90f946f32cc1815aaf15c916cc260b905b3d27e6efbe2f9e9.jpg)  
Reasoning models are indicated by a lightbulb icon  
Source: Artificial Analysis, JEF

## China vs US comparison

## AI Models

According to OpenRouter, token consumption went up significantly in Feb-26 due to (a) a surge in adoption of coding / agents, which allows people using AI from "to chat" to "to work". It connects with large models which can be deployed locally or on servers, which allows you to automate

According to OpenRouter, rising adoption of Coding / Agents and release of high-performance and cost-efficient China models are driving token consumption

workflow through natural language chat; (b) release of a number of high-performance and cost-efficient models which include Kimi K2.5 (Jan-26), M2.5 (Feb-26) and GLM-5 (Feb-26).

Exhibit 13 - Top 10 ranking in terms of token consumption by model the latest week

<table><tr><td>No</td><td>Company</td><td>Model</td><td>Tokens</td></tr><tr><td>1</td><td>Tencent</td><td>Hy3 (free)</td><td>6.13T</td></tr><tr><td>2</td><td>Xiaomi</td><td>MiMo-V2.5</td><td>5.95T</td></tr><tr><td>3</td><td>DeepSeek</td><td>DeepSeek V4 Flash</td><td>5.22T</td></tr><tr><td>4</td><td>MiniMax</td><td>MiniMax M3</td><td>4.26T</td></tr><tr><td>5</td><td>Z.AI</td><td>GLM 5.2</td><td>3.19T</td></tr><tr><td>6</td><td>DeepSeek</td><td>DeepSeek V4 Pro</td><td>2.83T</td></tr><tr><td>7</td><td>Anthropic</td><td>Claude Opus 4.7</td><td>2.26T</td></tr><tr><td>8</td><td>NVIDIA</td><td>Nemotron 3 Ultra (free)</td><td>2.04T</td></tr><tr><td>9</td><td>Anthropic</td><td>Claude Opus 4.8</td><td>2.03T</td></tr><tr><td>10</td><td>StepFun</td><td>Step 3.7 Flash</td><td>1.22T</td></tr></table>

Source: OpenRouter, JEF

Exhibit 14 - Weekly token consumption over the past 12 months as of 13 Jul (tn)  
![](images/690ebaf462554cb1adc7ba32818dafbe24d86bae1dfbaa1f57260afdfe9ba33a.jpg)  
Source: OpenRouter, JEF

According to OpenRouter (between 6 Jul and 12 Jul), China models' token consumption increased by 17.7% compared to prior week at 27.6tn. This compares to US models at 6.3tn token consumption. DeepSeek V4 Flash weekly token consumptions under rapid growth

Exhibit 15 - Market share: weekly token consumption by company as of 13 Jul  
![](images/caec1b0debcdb9861e020c3917169b0876fe96e2dda88a6d0e3f902ffa924c23.jpg)  
Source: OpenRouter, JEF

In OpenRouter, China models surpassed US models in terms of token consumption the week of 6 Jul

Exhibit 16 - Weekly token consumption since Jan-26 (bn)  
![](images/17d1c0e8c44b924abca7cd9503fcdad478be12a2034eb98339e7856d867d444e.jpg)  
Source: OpenRouter, JEF

On token consumption by company, Google (27%) comes first, followed by DeepSeek (20.2%), OpenAI (16.6%), Qwen (5.2%), and Anthropic (5.1%). The top 5 in weekly token consumption by model are Hy3 (free) (6.13tn), MiMo V2.5 (5.95tn), and DeepSeek V4 Flash (5.22tn), followed by MiniMax M3 (4.26tn) and GLM 5.2 (3.19tn).

Exhibit 17 - Top 10 ranking in terms of token consumption by model the latest week

<table><tr><td>No</td><td>Company</td><td>Model</td><td>Tokens</td></tr><tr><td>1</td><td>Tencent</td><td>Hy3 (free)</td><td>6.13T</td></tr><tr><td>2</td><td>Xiaomi</td><td>MiMo-V2.5</td><td>5.95T</td></tr><tr><td>3</td><td>DeepSeek</td><td>DeepSeek V4 Flash</td><td>5.22T</td></tr><tr><td>4</td><td>MiniMax</td><td>MiniMax M3</td><td>4.26T</td></tr><tr><td>5</td><td>Z.AI</td><td>GLM 5.2</td><td>3.19T</td></tr><tr><td>6</td><td>DeepSeek</td><td>DeepSeek V4 Pro</td><td>2.83T</td></tr><tr><td>7</td><td>Anthropic</td><td>Claude Opus 4.7</td><td>2.26T</td></tr><tr><td>8</td><td>NVIDIA</td><td>Nemotron 3 Ultra (free)</td><td>2.04T</td></tr><tr><td>9</td><td>Anthropic</td><td>Claude Opus 4.8</td><td>2.03T</td></tr><tr><td>10</td><td>StepFun</td><td>Step 3.7 Flash</td><td>1.22T</td></tr></table>

Source: OpenRouter, JEF

Hy3 (free) ranked first in terms of token consumption the week of 6 Jul

Exhibit 18 - No 11-20 ranking in terms of token consumption by model in latest week

<table><tr><td>No</td><td>Company</td><td>Model</td><td>Tokens</td></tr><tr><td>11</td><td>Anthropic</td><td>Claude Sonnet 4.6</td><td>995B</td></tr><tr><td>12</td><td>Google</td><td>Gemini 3 Flash Preview</td><td>937B</td></tr><tr><td>13</td><td>Anthropic</td><td>Claude Sonnet 5</td><td>923B</td></tr><tr><td>14</td><td>OpenAI</td><td>GPT 5.5</td><td>873B</td></tr><tr><td>15</td><td>Google</td><td>Gemini 2.5 Flash</td><td>612B</td></tr><tr><td>16</td><td>Xiaomi</td><td>MiMo-V2.5-Pro</td><td>606B</td></tr><tr><td>17</td><td>Google</td><td>Gemini 2.5 Flash Lite</td><td>561B</td></tr><tr><td>18</td><td>Poolside</td><td>Laguna M.1 (free)</td><td>544B</td></tr><tr><td>19</td><td>Google</td><td>Gemini 3.1 Flash Lite</td><td>507B</td></tr><tr><td>20</td><td>OpenAI</td><td>gpt-oss-120b</td><td>505B</td></tr></table>

Source: OpenRouter, JEF

Based on Artificial Analysis, China models DeepSeek, Qwen, Kimi, MiniMax and Zhipu are closing the gap with US models in terms of intelligence. China models are highly cost-efficient on Mixture of Experts (MoE) architecture, linear attention, and MLU (Model Flog Utilization). According to 2026 Stanford AI Index Report (Apr-26), the top US model leads Chinese models by 2.7%. Separately, Anthropic (1503), xAI (1495), Google (1494), OpenAI (1481), Alibaba (1449) and DeepSeek (1424) occupy the top tier of Arena Elo ratings as of Mar-26.

China models are narrowing the gap with US models in terms of intelligence. On Input/Output API, China large models are highly efficient vs US models.

Exhibit 19 - Artificial Intelligence vs Blended Price  
![](images/e2d23ae8a697ab9bdfd53a6b3c045995d9cb40e9dc79c26742d28906366746c1.jpg)  
Source: Artificial Analysis, JEF

Exhibit 20 - Quarterly Input / Output prices for China models  
![](images/7e5dc3d234a4a5a882250b5b763f70db2613d5125376c29c957b885336dcdda7.jpg)  
Source: Artificial Analysis, JEF

Exhibit 21 - Quarterly Input / Output prices for US models  
![](images/dd829836ca9c2b95bfffe1103902a2d6b475c946280c610292e47cc390a7e3fa.jpg)  
Source: Artificial Analysis, JEF  
In terms of Input/Output API price, China models are just a fraction vs US models.

Exhibit 22 - Frontier Language Model Intelligence over time as of 13 Jul  
![](images/bb6738485b1562e0d55019923ad8cdf188addfbfb1277e37e88ab1abe72485c7.jpg)  
Source: Artificial Analysis, JEF

## Model Input/Output Price By Companies

Exhibit 23 - DeepSeek: Input price  
![](images/c2441daab012beb27b0d2283b33619716736b6b00ecea008a573a36b62b0ed1b.jpg)  
Exhibit 24 - DeepSeek: Output price  
Source: Artificial Analysis, JEF

![](images/cc5b8054f722c52b3812c135aff67988aab9f4205be64d54f52c906ff221fd6c.jpg)

[中间内容因长度限制已省略]

ional purposes and is not tailored to any recipient, and is not based on, and does not take into account, the particular investment objectives, portfolio holdings, strategy, financial situation, or needs of any recipient. As such, any advice or recommendation in this report may not be suitable for a particular recipient. JEF assumes recipients of this report are capable of evaluating the information contained herein and of exercising independent judgment. A recipient of this report should not make any investment decision without first considering whether any advice or recommendation in this report is suitable for the recipient based on the recipient's particular circumstances and, if appropriate or otherwise needed, seeking professional advice, including tax advice. JEF does not perform any suitability or other analysis to check whether an investment decision made by the recipient based on this report is consistent with a recipient's investment objectives, portfolio holdings, strategy, financial situation, or needs.

By providing this report, neither JRS nor any other JEF entity accepts any authority, discretion, or control over the management of the recipient's assets. Any action taken by the recipient of this report, based on the information in the report, is at the recipient's sole judgment and risk. The recipient must perform his or her own independent review of any prospective investment. If the recipient uses the services of JEF LLC (or other affiliated broker-dealers), in connection with a purchase or sale of a security that is a subject of these materials, such broker-dealer may act as principal for its own accounts or as agent for another person. Only JRS is registered with the SEC as an investment adviser; and therefore neither JEF LLC nor any other JEF affiliate has any fiduciary duty in connection with distribution of these reports.

The price and value of the investments referred to herein and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

This report may contain forward looking statements that may be affected by inaccurate assumptions or by known or unknown risks, uncertainties, and other important factors. As a result, the actual results, events, performance or achievements of the financial product may be materially different from those expressed or implied in such statements.

This report has been prepared independently of any issuer of securities mentioned herein and not as agent of any issuer of securities. No Equity Research personnel have authority whatsoever to make any representations or warranty on behalf of the issuer(s). Any comments or statements made herein are those of the JEF entity producing this report and may differ from the views of other JEF entities.

This report may contain information obtained from third parties, including ratings from credit ratings agencies such as Standard & Poor's, and information derived from third-party or proprietary generative artificial intelligence (Gen AI) models. JEF does not guarantee the accuracy, completeness, timeliness or availability of this information, and is not responsible for any errors or omissions (negligent or otherwise), regardless of the cause, or for the results obtained from the use of such content. Neither JEF nor any third-party content providers, including providers of Gen AI models, give any express or implied warranties, including, but not limited to, any warranties of merchantability or fitness for a particular purpose or use. Neither JEF nor any third-party content provider shall be liable for any direct, indirect, incidental, exemplary, compensatory, punitive, special or consequential damages, costs, expenses, legal fees, or losses (including lost income or profits and opportunity costs) in connection with any use of their content, including ratings. Credit ratings are statements of opinions and are not statements of fact or recommendations to purchase, hold or sell securities. They do not address the suitability of securities or the suitability of securities for investment purposes, and should not be relied on as investment advice. Reproduction and distribution of third party content in any form is prohibited except with the prior written permission of the related third party.

JEF reports are disseminated and available electronically, and, in some cases, also in printed form. Electronic research is simultaneously made available to all clients. This report or any portion hereof may not be copied, reprinted, sold, or redistributed or disclosed by the recipient or any third party, by content scraping or extraction, automated processing, or any other form or means, without the prior written consent of JEF. Any unauthorized use is prohibited. Neither JEF nor any of its respective directors, officers or employees, is responsible for guaranteeing the financial success of any investment, or accepts any liability whatsoever for any direct, indirect or consequential damages or losses arising from any use of this report or its contents. Nothing herein shall be construed to waive any liability JEF has under applicable U.S. federal or state securities laws.

For Important Disclosure information relating to JRS, please see https://adviserinfo.sec.gov/IAPD/Content/Common/crd\_iapd\_Brochure.aspx?BRCHR\_VRSN\_ID=483878 and https://adviserinfo.sec.gov/Firm/292142 or visit our website at https://javatar.bluematrix.com/sellside/Disclosures.action, or www.JEF.com, or call 1.888.JEF.

© 2026 JEF
"""
