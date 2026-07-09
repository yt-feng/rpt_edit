你是财经类 AI Podcast 制作人，擅长把研报内容改写成中文、英文两条独立的访谈式播客脚本。

【目标】
- 基于下面研报解析内容，写两份 podcast 脚本：一份中文，一份英文。
- 每份目标时长约 5 分钟。
- 两份都要是“访谈聊天式”，不是单人念稿。
- 听感：像一位主持人和一位研究员围绕报告做深度但自然的讨论。
- 不要使用 emoji。
- 不要把全文讲完，要留下 1-2 个“完整报告里会继续展开”的悬念。

【输出格式必须严格遵守】
- 中文部分只能使用 `ZH_A:` 和 `ZH_B:` 开头。
- 英文部分只能使用 `EN_A:` 和 `EN_B:` 开头。
- 每一句独立成行。
- 不要输出 Markdown 标题。
- 不要输出舞台说明、音效说明或括号注释。
- 先输出完整中文脚本，再输出完整英文脚本。

【角色设定】
- A 是主持人：负责提问、转场、替听众追问“所以这意味着什么”。
- B 是研究员：负责解释报告逻辑、给出结构化判断和保留悬念。
- 两个角色必须频繁轮换，避免一个人连续说超过 3 句。
- 每句要适合 TTS 朗读：短句、自然、不要太书面。

【中文脚本结构】
1. 开场：A 用一个问题引出报告价值，B 给出主判断。
2. 第一部分：这份报告真正要回答的问题是什么。
3. 第二部分：2-3 个关键洞察，每个洞察都要有“这意味着什么”。
4. 第三部分：哪些问题仍然没有完全展开，为什么值得继续读完整报告。
5. 结尾：自然引导听众加入社群/阅读完整报告，不要硬广。

【英文脚本结构】
- 英文不是中文逐句翻译，而是面向英文听众重新组织。
- 保留同样的主线和洞察，但表达更口语、更 podcast。
- Use natural conversational English.
- Avoid long sentences and avoid reading like a research memo.

【内容边界】
- 可以基于研报内容做适度发散，但必须是从原文逻辑推出的判断。
- 不要编造具体数据、公司动作或引用。
- 对不确定内容要用“这里仍需要继续验证”或 “the report does not fully answer this yet” 表达。
- 默认避免出现具体投行品牌名，比如“GS”“GS”，统一写作“投行研报”或 “a global investment bank report”。

【研报解析内容】
"""
# Tencent Holdings (0700.HK)

## 2Q26E Preview: Gaming & Ads Solid with Continuing AI Investment

## CITI'S TAKE

Tencent will report 2Q26 results on Aug 12. While we expect solid revs growth thanks to continued strength in gaming despite softer seasonality and steady growth of ad revs, we are cautious on AI spend and profit drag as we have more conservative profit assumption than consensus. Into 2H26, we expect focus remains on Agentic AI testing within WeChat, integration of Mini Program with Hy3, release of next iteration/upgrade of Hy model and capex spend. Moreover, we believe Tencent will continue to evaluate its investment portfolio with rotation and rebalance between strategic AI-related investment vs maturing industry with limited future synergies. Opportunistic buyback and AI investment as well as strengthening core business growth empowering with AI enhancement will remain as key priorities, in our view. Our TP is adjusted to HK\$758 (from HK\$763) reflecting changes in investment portfolio value. Maintain Buy on AI play.

Official HY 3, WorkBuddy traction & AI Mini Program — Tencent Cloud is rapidly advancing its AI agent ecosystem, following the June 5th launch of its "Agent-Ready" data platform and a new "Productivity Agent Suite". The advanced and cost-effective Hy3 model was officially launched on July $6^{\text{th}}$ following its preview on April 23 which has attracted a 20x increase in daily token consumption since its preview, signaling strong adoption across many industries. On July $7^{\text{th}}$ , WeChat announced the upgrade of its AI Mini Program Growth Plan to boost the adoption of Hy3 within WeChat ecosystem.

2Q26 preview — We model 2Q26 total revs to up 9.3% yoy to Rmb201.7bn and non-GAAP net profit to +5.1% yoy to Rmb66.25bn or 32.8% margin, vs. Bloomberg cons. of Rmb203.9bn (+10.5% yoy) and Rmb69.1bn (34% margin). We forecast total online games +8.3% yoy to Rmb64.1bn with domestic/International games +8%/+9% yoy to Rmb43.6bn/Rmb20.5bn. We model online ad revs +19% yoy to Rmb42.5bn and FBS revs up 9% yoy to Rmb60.5bn, of which cloud revs +24% yoy to Rmb14bn and fintech revs +5.2% yoy to Rmb46.5bn. We model GP/OP to +9.3%/+5.7% yoy to Rmb114.8bn/Rmb73.2bn. We expect result likely inline with potential small deviation on upside risk to our gaming forecast and downside to FBS.

New games pipeline— Into 3Q26E, Tencent has released Just Dance: Party/Rust on Jul 2/9 and Control Resonant to be released by Sep 24. Pipeline includes Monster Hunter Outlanders, Rainbow Six Siege and Animula Nook.

## Earnings Summary

<table><tr><td>Year to 31 Dec</td><td>Net Profit (RmbM)</td><td>Diluted EPS (Rmb)</td><td>EPS growth (%)</td><td>P/E (x)</td><td>P/B (x)</td><td>ROE (%)</td><td>Yield (%)</td></tr><tr><td>2024A</td><td>222,703</td><td>23.672</td><td>44.3</td><td>16.5</td><td>3.7</td><td>25.0</td><td>1.2</td></tr><tr><td>2025A</td><td>259,626</td><td>28.086</td><td>18.6</td><td>13.9</td><td>3.1</td><td>24.4</td><td>1.4</td></tr><tr><td>2026E</td><td>267,621</td><td>29.177</td><td>3.9</td><td>13.4</td><td>2.8</td><td>22.3</td><td>1.3</td></tr><tr><td>2027E</td><td>283,476</td><td>30.913</td><td>5.9</td><td>12.6</td><td>2.6</td><td>21.9</td><td>1.3</td></tr><tr><td>2028E</td><td>313,569</td><td>34.202</td><td>10.6</td><td>11.4</td><td>2.4</td><td>22.2</td><td>1.4</td></tr></table>

Source: Powered by dataCentral

## Buy

Price (06 Jul 26 16:10) HK\$452.00

Target price HK\$758.00↓

Expected share price return 67.7%

Expected dividend yield 1.3%

Expected total return 69.0%

Market Cap HK\$4,109,752M

## Price Performance

![](images/e18dab2d28554e8a8f98b84d3686e4f2307b84eb120042f449de84749d840fea.jpg)

Alicia Yap, CFA $^{AC}$ +852-2501-2773
alicia.yap@citi.com

Nelson Cheung
nelson.cheung@citi.com

Vicky Wei, CFA
vicky.wei@citi.com

Price: HK\$452.00; TP: HK\$758.00; Market Cap: HK\$4,109,752m; Recomm: Buy

<table><tr><td>Profit &amp; Loss (Rmbm)</td><td>2024</td><td>2025</td><td>2026E</td><td>2027E</td><td>2028E</td></tr><tr><td>Sales revenue</td><td>660,257</td><td>751,766</td><td>820,970</td><td>893,678</td><td>967,569</td></tr><tr><td>Cost of sales</td><td>-311,011</td><td>-329,173</td><td>-356,184</td><td>-385,010</td><td>-413,213</td></tr><tr><td>Gross profit</td><td>349,246</td><td>422,593</td><td>464,787</td><td>508,667</td><td>554,356</td></tr><tr><td>Gross Margin (%)</td><td>52.9</td><td>56.2</td><td>56.6</td><td>56.9</td><td>57.3</td></tr><tr><td>EBITDA (Adj)</td><td>287,736</td><td>339,449</td><td>363,114</td><td>434,475</td><td>480,483</td></tr><tr><td>EBITDA Margin (Adj) (%)</td><td>43.6</td><td>45.2</td><td>44.2</td><td>48.6</td><td>49.7</td></tr><tr><td>Depreciation</td><td>-27,332</td><td>-32,799</td><td>-44,332</td><td>-96,517</td><td>-109,200</td></tr><tr><td>Amortisation</td><td>-28,881</td><td>-33,229</td><td>-29,555</td><td>-32,172</td><td>-33,091</td></tr><tr><td>EBIT (Adj)</td><td>237,811</td><td>280,656</td><td>295,678</td><td>312,097</td><td>344,505</td></tr><tr><td>EBIT Margin (Adj) (%)</td><td>36.0</td><td>37.3</td><td>36.0</td><td>34.9</td><td>35.6</td></tr><tr><td>Net interest</td><td>4,023</td><td>1,779</td><td>4,770</td><td>6,701</td><td>11,027</td></tr><tr><td>Associates</td><td>29,363</td><td>33,908</td><td>22,002</td><td>22,298</td><td>22,570</td></tr><tr><td>Non-Op/Except/Other Adj</td><td>-29,712</td><td>-39,094</td><td>-35,443</td><td>-37,807</td><td>-38,998</td></tr><tr><td>Pre-tax profit</td><td>241,485</td><td>277,249</td><td>287,008</td><td>303,289</td><td>339,104</td></tr><tr><td>Tax</td><td>-45,018</td><td>-47,448</td><td>-57,185</td><td>-60,658</td><td>-67,821</td></tr><tr><td>Extraord./Min.Int./Pref.div.</td><td>-2,394</td><td>-4,959</td><td>-5,151</td><td>-5,011</td><td>-4,871</td></tr><tr><td>Reported net profit</td><td>194,073</td><td>224,842</td><td>224,672</td><td>237,621</td><td>266,412</td></tr><tr><td>Net Margin (%)</td><td>29.4</td><td>29.9</td><td>27.4</td><td>26.6</td><td>27.5</td></tr><tr><td>Core NPAT</td><td>222,703</td><td>259,626</td><td>267,621</td><td>283,476</td><td>313,569</td></tr></table>

<table><tr><td>Valuation ratios</td><td>2024</td><td>2025</td><td>2026E</td><td>2027E</td><td>2028E</td></tr><tr><td>PE (x)</td><td>16.5</td><td>13.9</td><td>13.4</td><td>12.6</td><td>11.4</td></tr><tr><td>PB (x)</td><td>3.7</td><td>3.1</td><td>2.8</td><td>2.6</td><td>2.4</td></tr><tr><td>EV/EBITDA (x)</td><td>10.2</td><td>8.4</td><td>7.7</td><td>6.3</td><td>5.5</td></tr><tr><td>FCF yield (%)</td><td>5.2</td><td>6.0</td><td>6.2</td><td>7.9</td><td>8.9</td></tr><tr><td>Dividend yield (%)</td><td>1.2</td><td>1.4</td><td>1.3</td><td>1.3</td><td>1.4</td></tr><tr><td>Payout ratio (%)</td><td>19</td><td>19</td><td>17</td><td>16</td><td>16</td></tr><tr><td>ROE (%)</td><td>21.8</td><td>21.1</td><td>18.8</td><td>18.3</td><td>18.9</td></tr></table>

<table><tr><td>Cashflow (Rmbm)</td><td>2024</td><td>2025</td><td>2026E</td><td>2027E</td><td>2028E</td></tr><tr><td>EBITDA</td><td>264,312</td><td>307,590</td><td>334,123</td><td>402,980</td><td>447,797</td></tr><tr><td>Working capital</td><td>21,881</td><td>16,484</td><td>13,630</td><td>16,194</td><td>17,688</td></tr><tr><td>Other</td><td>-27,672</td><td>-21,022</td><td>-25,739</td><td>-30,459</td><td>-37,630</td></tr><tr><td>Operating cashflow</td><td>258,521</td><td>303,052</td><td>322,014</td><td>388,714</td><td>427,856</td></tr><tr><td>Capex</td><td>-69,451</td><td>-87,324</td><td>-98,512</td><td>-107,237</td><td>-110,300</td></tr><tr><td>Net acq/disposals</td><td>-4,941</td><td>-34,717</td><td>-296</td><td>-126</td><td>62</td></tr><tr><td>Other</td><td>-47,795</td><td>-83,691</td><td>10,594</td><td>-96,352</td><td>-113,001</td></tr><tr><td>Investing cashflow</td><td>-122,187</td><td>-205,732</td><td>-88,214</td><td>-203,715</td><td>-223,239</td></tr><tr><td>Dividends paid</td><td>-28,859</td><td>-37,535</td><td>-48,151</td><td>-46,058</td><td>-45,148</td></tr><tr><td>Financing cashflow</td><td>-176,494</td><td>-87,155</td><td>-104,722</td><td>-101,808</td><td>-113,126</td></tr><tr><td>Net change in cash</td><td>-39,801</td><td>8,522</td><td>127,106</td><td>80,825</td><td>88,653</td></tr><tr><td>Free cashflow to s/holders</td><td>189,070</td><td>215,728</td><td>223,502</td><td>281,477</td><td>317,556</td></tr></table>

<table><tr><td>Per share data</td><td>2024</td><td>2025</td><td>2026E</td><td>2027E</td><td>2028E</td></tr><tr><td>Reported EPS (Rmb)</td><td>20.629</td><td>24.323</td><td>24.495</td><td>25.912</td><td>29.058</td></tr><tr><td>Core EPS (Rmb)</td><td>23.672</td><td>28.086</td><td>29.177</td><td>30.913</td><td>34.202</td></tr><tr><td>DPS (Rmb)</td><td>4.500</td><td>5.300</td><td>5.099</td><td>5.000</td><td>5.312</td></tr><tr><td>CFPS (Rmb)</td><td>27.479</td><td>32.784</td><td>35.107</td><td>42.389</td><td>46.667</td></tr><tr><td>FCFPS (Rmb)</td><td>20.097</td><td>23.337</td><td>24.367</td><td>30.695</td><td>34.637</td></tr><tr><td>BVPS (Rmb)</td><td>105.033</td><td>127.039</td><td>137.364</td><td>149.884</td><td>163.029</td></tr><tr><td>Wtd avg ord shares (m)</td><td>9,269</td><td>9,085</td><td>9,032</td><td>9,030</td><td>9,028</td></tr><tr><td>Wtd avg diluted shares (m)</td><td>9,408</td><td>9,244</td><td>9,172</td><td>9,170</td><td>9,168</td></tr></table>

<table><tr><td>Growth rates</td><td>2024</td><td>2025</td><td>2026E</td><td>2027E</td><td>2028E</td></tr><tr><td>Sales revenue (%)</td><td>8.4</td><td>13.9</td><td>9.2</td><td>8.9</td><td>8.3</td></tr><tr><td>EBIT (Adj) (%)</td><td>23.9</td><td>18.0</td><td>5.4</td><td>5.6</td><td>10.4</td></tr><tr><td>Core NPAT (%)</td><td>41.2</td><td>16.6</td><td>3.1</td><td>5.9</td><td>10.6</td></tr><tr><td>Core EPS (%)</td><td>44.3</td><td>18.6</td><td>3.9</td><td>5.9</td><td>10.6</td></tr></table>

<table><tr><td>Balance Sheet (Rmbm)</td><td>2024</td><td>2025</td><td>2026E</td><td>2027E</td><td>2028E</td></tr><tr><td>Cash &amp; cash equiv.</td><td>132,519</td><td>141,041</td><td>268,147</td><td>348,972</td><td>437,625</td></tr><tr><td>Accounts receivables</td><td>48,203</td><td>49,930</td><td>53,982</td><td>58,762</td><td>63,621</td></tr><tr><td>Inventory</td><td>440</td><td>530</td><td>657</td><td>715</td><td>774</td></tr><tr><td>Net fixed &amp; other tangibles</td><td>282,037</td><td>322,741</td><td>363,008</td><td>376,132</td><td>379,673</td></tr><tr><td>Goodwill &amp; intangibles</td><td>196,127</td><td>205,999</td><td>201,444</td><td>194,272</td><td>186,181</td></tr><tr><td>Financial &amp; other assets</td><td>1,121,669</td><td>1,318,745</td><td>1,276,460</td><td>1,339,877</td><td>1,414,490</td></tr><tr><td>Total assets</td><td>1,780,995</td><td>2,038,986</td><td>2,163,697</td><td>2,318,730</td><td>2,482,363</td></tr><tr><td>Accounts payable</td><td>118,712</td><td>121,127</td><td>129,787</td><td>139,237</td><td>147,172</td></tr><tr><td>Short-term debt</td><td>61,508</td><td>53,160</td><td>56,574</td><td>58,574</td><td>60,574</td></tr><tr><td>Long-term debt</td><td>146,521</td><td>208,369</td><td>209,881</td><td>211,881</td><td>213,881</td></tr><tr><td>Provisions &amp; other liab</td><td>400,358</td><td>415,265</td><td>434,681</td><td>458,475</td><td>486,924</td></tr><tr><td>Total liabilities</td><td>727,099</td><td>797,921</td><td>830,924</td><td>868,166</td><td>908,551</td></tr><tr><td>Shareholders&#x27; equity</td><td>973,548</td><td>1,154,152</td><td>1,240,709</td><td>1,353,488</td><td>1,471,866</td></tr><tr><td>Minority interests</td><td>80,348</td><td>86,913</td><td>92,064</td><td>97,075</td><td>101,946</td></tr><tr><td>Total equity</td><td>1,053,896</td><td>1,241,065</td><td>1,332,773</td><td>1,450,563</td><td>1,573,812</td></tr><tr><td>Net debt (Adj)</td><td>75,510</td><td>120,488</td><td>-1,692</td><td>-78,517</td><td>-163,170</td></tr><tr><td>Net debt to equity (Adj) (%)</td><td>7.2</td><td>9.7</td><td>-0.1</td><td>-5.4</td><td>-10.4</td></tr></table>

For definitions of the items in this table, please click here.

# Business Update & 2Q26E Preview

## Latest updates on Tencent Cloud and AI development

Tencent Cloud upgrades Data Platform for Agents

On June 5 $^{th}$ Tencent Cloud announced a significant upgrade to its data platform, making it "Agent-Ready" to support AI Agents as a new class of user. The new three-tier architecture includes the production-grade data agent DataBuddy, the intelligent data platform WeData, and an AI-native data infrastructure. This system is designed to facilitate seamless collaboration between humans and AI, allowing Agents to execute complex data tasks such as modeling, ETL development, and report generation through natural language commands, thereby boosting R&D efficiency by five to ten times.

A core part of the upgrade is the WeData platform, which acts as a unified control plane with a new semantic layer, enabling Agents to better understand business context and achieve over 90% accuracy in converting natural language to SQL. The underlying AI-native infrastructure has been rebuilt for intelligence across storage, computing, data, and systems, featuring a multi-Agent collaboration system and autonomous operational capabilities. These enhancements, also available for on-premises deployment, aim to accelerate the large-scale adoption of Agents in enterprise environments.

## Productivity Agent Suite Debuts

On June 5 $^{th}$ Tencent Cloud launched a comprehensive "Productivity Agent Suite" designed to integrate AI into various workflows for both individual and enterprise users. This new suite features a range of tools, including the upgraded WorkBuddy for personal productivity, CodeBuddy for software development, and the new WorkBuddy Enterprise AI Workspace, which integrates with Tencent Docs and Tencent LearnShare. The launch reflects Tencent's strategy of building practical, scalable AI solutions that solve real-world problems, with a focus on the co-design of models and products to enhance usability.

Supporting this initiative, Tencent Cloud also upgraded its core infrastructure with the Hy3 Preview model, the TokenHub platform for efficient model inference, and a new Agent Runtime for optimized performance and security. These tools have already proven effective within Tencent, with CodeBuddy reportedly reducing coding time by 40% for its engineers. The suite is now being deployed across more than 20 industries, including finance, retail, and healthcare, to foster large-scale human-AI collaboration.

## Workbuddy further gains traction

On July 6, news media Gelonghui cited Analysys that Tencent's WorkBuddy ranked as top office agent with 8.85mn monthly visits in Mar 2026 compared with over 20mn monthly visits among top office agent products. The article suggested that WorkBuddy has conducted 43 version upgrades 3 months after launch. Gelonghui suggested that Tencent internally has already positioned WorkBuddy as the third phenomenal product following QQ and WeChat leveraging its straightforward deployment, WeChat ecosystem authorization, full integration with tools within Tencent ecosystem and external applications.

Figure 1. Product pricing related to WorkBuddy

<table><tr><td colspan="5">Tencent Cloud Coding Plan</td></tr><tr><td>Package</td><td colspan="2">Lite</td><td colspan="2">Pro</td></tr><tr><td>Standard pricing</td><td colspan="2">Rmb40/ month</td><td colspan="2">Rmb200/ month</td></tr><tr><td>Usage limit</td><td colspan="2">1,200 requests per 5 hours, 9,000 requests per week, 18,000 requests per month</td><td colspan="2">6,000 requests per 5 hours, 45,000 requests per week, 90,000 requests per month</td></tr><tr><td colspan="5">Code Assistant (Joint Subscription for CodeBuddy and WorkBuddy)</td></tr><tr><td>Package</td><td>Experience</td><td>Standard</td><td>Premium</td><td>Flagship</td></tr><tr><td>Standard pricing</td><td>Free</td><td>Rmb99/ month</td><td>Rmb199/ month</td><td>Rmb999/ month</td></tr><tr><td>Consecutive monthly subscription</td><td>Free</td><td>Rmb70/ month</td><td>Rmb140/ month</td><td>Rmb700/ month</td></tr><tr><td>Model deployment</td><td>Automatic</td><td>All available</td><td>All available</td><td>All available</td></tr><tr><td>Scenario</td><td>Beginner</td><td>Daily light assistance</td><td>High-frequency, office</td><td>Complex</td></tr><tr><td colspan="5">Enterprise Solution (CodeBuddy and WorkBuddy Inclusive)</td></tr><tr><td>Package</td><td colspan="2">Enterprise SaaS</td><td colspan="2">Enterprise Private Cloud</td></tr><tr><td>Standard pricing</td><td colspan="2">Rmb198/ pp / month</td><td colspan="2">Rmb316/ pp / month</td></tr></table>

© 2026 Citi Inc. No redistribution without Citi's written permission.  
Source: Company Reports, Citi

## Hy3 is officially released on July 6 $^{th}$

On July 6 $^{th}$ , Tencent announced it has officially launched Hy3, following its release of preview version on April 23. Tencent noted that the model demonstrates significantly enhanced performance relative to models of the same size, while achieving intelligence comparable to flagship models with two to five times its parameter scale. Compared with the preview version, it also delivers greater stability and cost efficiency. Hy3 has already been adopted across Tencent products and services, including WorkBuddy/CodeBuddy, Yuanbao, Marvis, ima and others. Its API is now available on Tencent Cloud TokenHub, with global third-party developer platforms set to integrate Hy3 progressively.

Compared to Hy3 preview, Hy3 takes another leap across a wide range of tasks through strengthened reinforcement learning and enhanced data quality and diversity, delivering performance comparable to larger-scale flagship models. Hy3 has made particularly notable progress in productivity tasks such as software development, office productivity, financial modeling, front-end design and game production, making it a reliable and cost-efficient choice. Tencent also noted that since the launch of Hy3 preview, its average daily token consumption has increased twenty-fold, reflecting growing market recognition of its positioning as a practical and cost-effective model.

Figure 2. Tencent Cloud Hunyuan major milestones and achievements in 2026

<table><tr><td>Date</td><td>Event</td><td>Milestones</td></tr><tr><td>28-Jan-26</td><td>Open source</td><td>Open-sourced Hunyuan-Image 3.0-Instruct</td></tr><tr><td>30-Jan-26</td><td>Product launch</td><td>Launch of CodeBuddy Code 2.0</td></tr><tr><td>9-Mar-26</td><td>Product launch</td><td>Launch of WorkBuddy as all-scenario AI agent</td></tr><tr><td>1-Apr-26</td><td>Product launch</td><td>Launch of ADP Agent Portal as cross-platform enterprise agent portal</td></tr><tr><td>2-Apr-26</td><td>Product launch</td><td>Launch of ClawPro as enterprise-level OpenClaw</td></tr><tr><td>3-Ap

[中间内容因长度限制已省略]

lar investor. Accordingly, investors should, before acting on the advice, consider the appropriateness of the advice, having regard to their objectives, financial situation and needs. Prior to acquiring any financial product, it is the client's responsibility to obtain the relevant offer document for the product and consider it before making a decision as to whether to purchase the product.

Card Insights. Where this report references Card Insights data, Card Insights consists of selected data from a subset of Citi's proprietary credit card transactions. Such data has undergone rigorous security protocols to keep all customer information confidential and secure; the data is highly aggregated and anonymized so that all unique customer identifiable information is removed from the data prior to receipt by the report's author or distribution to external parties. This data should be considered in the context of other economic indicators and publicly available information. Further, the selected data represents only a subset of Citi's proprietary credit card transactions due to the selection methodology or other limitations and should not be considered as indicative or predictive of the past or future financial performance of Citi or its credit card business.

Citi product may source data from dataCentral. dataCentral is a Citi proprietary database, which includes the Firm's estimates, data from company reports and feeds from LSEG Data & Analytics. The source for all referenced prices, unless otherwise stated, is DataCentral. Past performance is not a guarantee or reliable indicator of future results. Forecasts are not a guarantee or reliable indicator of future performance. The printed and printable version of the research report may not include all the information <(e.g. certain financial summary information and comparable company data) that is linked to the online version available on the Firm's proprietary electronic distribution platforms.

Where included in this report, MSCI sourced information is the exclusive property of MS Capital International Inc. (MSCI). Without prior written permission of MSCI, this information and any other MSCI intellectual property may not be reproduced, redisseminated or used to create any financial products, including any indices. This information is provided on an "as is" basis. The user assumes the entire risk of any use made of this information. MSCI, its affiliates and any third party involved in, or related to, computing or compiling the information hereby expressly disclaim all warranties of originality, accuracy, completeness, merchantability or fitness for a particular purpose with respect to any of this information. Without limiting any of the foregoing, in no event shall MSCI, any of its affiliates or any third party involved in, or related to, computing or compiling the information have any liability for any damages of any kind. MSCI, MS Capital International and the MSCI indexes are services marks of MSCI and its affiliates. Where data is attributed to Morningstar that data is © 2026 Morningstar, Inc. All Rights Reserved. That information: (1) is proprietary to Morningstar and/or its content providers; (2) may not be copied or distributed; and (3) is not warranted to be accurate, complete or timely. Neither Morningstar nor its content providers are responsible for any damages or losses arising from any use of this information.

The Firm accepts no liability whatsoever for the actions of third parties. The Product may provide the addresses of, or contain hyperlinks to, websites. Except to the extent to which the Product refers to website material of the Firm, the Firm has not reviewed the linked site. Equally, except to the extent to which the Product refers to website material of the Firm, the Firm takes no responsibility for, and makes no representations or warranties whatsoever as to, the data and information contained therein. Such address or hyperlink (including addresses or hyperlinks to website material of the Firm) is provided solely for your convenience and information and the content of the linked site does not in any way form part of this document. Accessing such website or following such link through the Product or the website of the Firm shall be at your own risk and the Firm shall have no liability arising out of, or in connection with, any such referenced website.

© 2026 Citi Global Markets Inc. Citi is a division of Citi Global Markets Inc. Citi and Citi and Arc Design are trademarks and service marks of Citi Inc. and its affiliates and are used and registered throughout the world. All rights reserved. The research data in this report are not intended to be used for the purpose of (a) determining the price of or amounts due in respect of (or to value) one or more financial products or instruments and/or (b) measuring or comparing the performance of, or defining the asset allocation of a financial product, a portfolio of financial instruments, or a collective investment undertaking, and any such use is strictly prohibited without the prior written consent of Citi. Any unauthorized use, duplication, redistribution or disclosure of this report (the “Product”), including, but not limited to, redistribution of the Product by electronic mail, posting of the Product on a website or page, and/or providing to a third party a link to the Product, is prohibited by law and will result in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.

ADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST
"""
