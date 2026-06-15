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
## Greater China Technology Hardware | Asia Pacific

# Monthly Databook: iPhone Build Strength to Carry into 3Q26 for New Premium Models Debut

## Key Takeaways

2Q26e iPhone builds estimate stays at 52mn units (down 7% QoQ, up 12% YoY).  
3Q26e iPhone builds introduced at 54mn units (up 4% QoQ, down 2% YoY).  
We keep 2Q26e iPad builds at 13mn units (up 8% QoQ, down 10% YoY).  
3Q26 iPad builds introduced at 13mn units (flat QoQ, down 7% YoY).

We keep our 2Q26 iPhone build estimate at 52mn units, down 7% QoQ (+12% YoY), vs. the historical 15-25% QoQ declines previously seen for 2Q. Our checks suggest better-than-seasonal builds this quarter from major assembly partners including Hon Hai, with iPhone shipments in May up MoM. This indicates to us that iPhone sell-through continues to trend well amid memory cost hikes.

We introduce our preliminary 3Q26 iPhone build estimate at 54mn units, up 4% QoQ (-2% YoY). The slower run rate mainly reflects new model SKUs shifting to the premium segment (18 Pro/Pro Max and iPhone Fold), while the iPhone 18 model is scheduled for introduction in 1H27. We currently expect 7-8mn iPhone Fold builds in 2H26 and will closely monitor the ramp-up progress.

We keep our 2Q26 iPad build forecast at 13mn units, up 8% QoQ (-10% YoY). The YoY decline reflects a higher base in 2Q25 given product launches. We introduce our preliminary 3Q26 iPad build forecast at 13mn units, flat QoQ (-7% YoY), as we expect stocking to remain normal, although memory and material price hikes could have an impact.

Exhibit 1: iPhone Sell-in Data, by Quarter

<table><tr><td>Unit units</td><td>1Q22</td><td>2Q22</td><td>3Q22</td><td>4Q22</td><td>2022</td><td>1Q23</td><td>2Q23</td><td>3Q23</td><td>4Q23</td><td>2023</td><td>1Q24</td><td>2Q24</td><td>3Q24</td><td>4Q24</td><td>2024</td><td>1Q25</td><td>2Q25</td><td>3Q25</td><td>4Q25</td><td>2025</td><td>1Q26</td><td>2Q26e</td><td>3Q26e</td></tr><tr><td colspan="24">iPhone Sell in</td></tr><tr><td>iPhone SE1 (SE 5G/16e/17e)</td><td>3.0</td><td>13.0</td><td>6.0</td><td>2.0</td><td>24.0</td><td>1.0</td><td>2.5</td><td>5.0</td><td>3.0</td><td>11.5</td><td>1.0</td><td>2.0</td><td>5.0</td><td>3.0</td><td>11.0</td><td>4.0</td><td>9.0</td><td>4.0</td><td>1.0</td><td>18.0</td><td>2.0</td><td>10.0</td><td>8.0</td></tr><tr><td>iPhone XR</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>iPhone 11</td><td>1.0</td><td>1.0</td><td>0.5</td><td>0.5</td><td>3.0</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>iPhone 12 mini (5.4&quot;)</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>iPhone 12 (5.1&quot;)</td><td>2.0</td><td>1.0</td><td>1.0</td><td>0.5</td><td>4.5</td><td>0.5</td><td>-</td><td>0.5</td><td>-</td><td>1.0</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>iPhone 12 Pro (5.1&quot;)</td><td>1.0</td><td>0.5</td><td>0.5</td><td>0.5</td><td>2.5</td><td>0.5</td><td>-</td><td>-</td><td>-</td><td>0.5</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>iPhone 12 Pro Mat (6.7&quot;)</td><td>1.0</td><td>0.5</td><td>0.5</td><td>0.5</td><td>2.5</td><td>0.5</td><td>-</td><td>-</td><td>-</td><td>0.5</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>iPhone 13 mini (5.4&quot;)</td><td>5.0</td><td>2.0</td><td>2.0</td><td>1.0</td><td>10.0</td><td>1.0</td><td>0.5</td><td>-</td><td>-</td><td>1.5</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>iPhone 13 (5.1&quot;)</td><td>10.0</td><td>11.5</td><td>8.0</td><td>3.0</td><td>38.5</td><td>1.0</td><td>0.5</td><td>-</td><td>-</td><td>1.5</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>iPhone 13 Pro (5.1&quot;)</td><td>13.0</td><td>8.0</td><td>6.0</td><td>3.5</td><td>30.5</td><td>1.0</td><td>2.0</td><td>1.0</td><td>-</td><td>4.0</td><td>0.5</td><td>0.5</td><td>-</td><td>-</td><td>1.0</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>iPhone 13 Pro Mat (5.7&quot;)</td><td>12.0</td><td>7.5</td><td>5.0</td><td>4.0</td><td>28.5</td><td>2.0</td><td>2.0</td><td>1.0</td><td>-</td><td>5.0</td><td>0.5</td><td>0.5</td><td>-</td><td>-</td><td>1.0</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>iPhone 14 (6.1&quot;)</td><td></td><td></td><td>6.5</td><td>13.0</td><td>19.5</td><td>7.0</td><td>4.0</td><td>5.0</td><td>2.0</td><td>18.0</td><td>1.0</td><td>0.5</td><td>-</td><td>-</td><td>1.5</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>iPhone 14 Plus (5.7&quot;)</td><td></td><td></td><td>2.0</td><td>13.5</td><td>15.5</td><td>5.0</td><td>3.0</td><td>1.0</td><td>1.0</td><td>10.0</td><td>1.0</td><td>0.5</td><td>-</td><td>-</td><td>1.5</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>iPhone 14 Pro (5.1&quot;)</td><td></td><td></td><td>6.0</td><td>16.5</td><td>22.0</td><td>10.5</td><td>12.0</td><td>7.0</td><td>3.0</td><td>37.0</td><td>2.0</td><td>2.0</td><td>1.5</td><td>1.0</td><td>6.0</td><td>1.0</td><td>1.0</td><td>1.0</td><td>-</td><td>3.0</td><td>-</td><td>-</td><td>-</td></tr><tr><td>iPhone 14 Pro Mat (6.7&quot;)</td><td></td><td></td><td>6.0</td><td>19.0</td><td>25.0</td><td>19.5</td><td>14.0</td><td>9.0</td><td>4.0</td><td>46.5</td><td>2.0</td><td>2.0</td><td>1.0</td><td>1.0</td><td>6.0</td><td>1.0</td><td>1.0</td><td>1.0</td><td>-</td><td>3.0</td><td>-</td><td>-</td><td>-</td></tr><tr><td>iPhone 15 (6.1&quot;)</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>6.0</td><td>12.0</td><td>18.0</td><td>6.0</td><td>5.0</td><td>4.0</td><td>1.0</td><td>16.0</td><td>1.0</td><td>0.5</td><td>0.5</td><td>0.5</td><td>2.5</td><td>-</td><td>-</td><td>-</td></tr><tr><td>iPhone 15 Plus (6.7&quot;)</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>5.0</td><td>10.0</td><td>15.0</td><td>4.0</td><td>3.0</td><td>1.0</td><td>1.0</td><td>9.0</td><td>1.0</td><td>0.5</td><td>0.5</td><td>0.5</td><td>2.5</td><td>-</td><td>-</td><td>-</td></tr><tr><td>iPhone 15 Pro (5.1&quot;)</td><td></td><td></td><td></td><td></td><td></td><td></td><td>8.0</td><td>16.0</td><td>24.0</td><td>12.0</td><td>10.0</td><td>8.5</td><td>2.0</td><td>32.5</td><td>2.0</td><td>2.0</td><td>2.0</td><td>1.0</td><td>7.0</td><td>1.0</td><td>1.0</td><td>-</td><td>-</td></tr><tr><td>iPhone 15 Pro Mat (6.7&quot;)</td><td></td><td></td><td></td><td></td><td></td><td></td><td>2.0</td><td>24.0</td><td>26.0</td><td>18.0</td><td>13.0</td><td>10.5</td><td>3.0</td><td>44.5</td><td>3.0</td><td>3.0</td><td>2.0</td><td>1.0</td><td>9.0</td><td>1.0</td><td>1.0</td><td>-</td><td>-</td></tr><tr><td>iPhone 16 (5.1&quot;)</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>6.0</td><td>12.0</td><td>18.0</td><td>5.0</td><td>4.0</td><td>4.0</td><td>1.0</td><td>14.0</td><td>2.0</td><td>2.0</td><td>1.0</td><td></td></tr><tr><td>iPhone 16 Plus (6.7&quot;)</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>5.0</td><td>6.0</td><td>11.0</td><td>4.0</td><td>3.0</td><td>1.0</td><td>1.0</td><td>8.0</td><td>-</td><td>-</td><td>-</td><td></td></tr><tr><td>iPhone 16 Pro (5.2&quot;)</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>8.0</td><td>17.0</td><td>25.0</td><td>11.5</td><td>9.5</td><td>4.0</td><td>2.0</td><td>27.0</td><td>2.0</td><td>2.0</td><td>2.0</td><td></td></tr><tr><td>iPhone 16 Pro Mat (5.9&quot;)</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>4.0</td><td>26.0</td><td>30.0</td><td>16.5</td><td>13.0</td><td>10.0</td><td>4.0</td><td>43.5</td><td>5.0</td><td>3.0</td><td>2.0</td></tr><tr><td>iPhone 17 (5.1&quot;)</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>6.0</td><td>16.0</td><td>22.0</td><td>10.0</td><td>8.0</td></tr><tr><td>iPhone Air (5.7&quot;)</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>4.0</td><td>4.0</td><td>8.0</td><td></td><td></td></tr><tr><td>iPhone 17 Pro (5.3&quot;)</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>8.0</td><td>22.0</td><td>30.0</td><td>18.0</td><td>13.0</td></tr><tr><td>iPhone 17 Pro Mat (6.9&quot;)</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>7.0</td><td>23.0</td><td>30.0</td><td>15.0</td><td>12.0</td></tr><tr><td>iPhone 18 Pro (5.3&quot;)</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>8.0</td></tr><tr><td>iPhone 18 Pro Mat (6.9&quot;)</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>8.0</td></tr><tr><td>iPhone Fold</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>1.0</td></tr><tr><td>Total</td><td>54.0</td><td>45.0</td><td>50.0</td><td>17.0</td><td>226.0</td><td>54.0</td><td>41.0</td><td>50.0</td><td>75.0</td><td>220.0</td><td>48.0</td><td>39.0</td><td>54.0</td><td>73.0</td><td>214.0</td><td>50.0</td><td>46.5</td><td>55.0</td><td>76.0</td><td>227.5</td><td>56.0</td><td>52.0</td><td>54.0</td></tr><tr><td>YoY</td><td>7%</td><td>1%</td><td>0%</td><td>-9%</td><td>-2%</td><td>0%</td><td>-9%</td><td>0%</td><td>-3%</td><td>-3%</td><td>-11%</td><td>-5%</td><td>8%</td><td>-3%</td><td>-3%</td><td>-4%</td><td>-15%</td><td>2%</td><td>4%</td><td>6%</td><td>-12%</td><td>12%</td><td>-2%</td></tr><tr><td>QoQ</td><td>-36%</td><td>-17%</td><td>11%</td><td>54%</td><td></td><td>-30%</td><td>-24%</td><td>22%</td><td>50%</td><td></td><td>-36%</td><td>-19%</td><td>38%</td><td>35%</td><td></td><td>-32%</td><td>-7%</td><td>18%</td><td>38%</td><td></td><td>-26%</td><td>-7%</td><td>4%</td></tr></table>

Source: Company data, MS. e = MS Asia Research estimates based on company announcements and supply chain checks.

MS TAIWAN LIMITED+

## Sharon Shih

Equity Analyst

Sharon.Shih@morganstanley.com +886 2 2730-2865

## Derrick Yang

Equity Analyst

Derrick.Yang@morganstanley.com +886 2 2730-2862

## Howard Kao

Equity Analyst

Howard.Kao@morganstanley.com +886 2 2730-2989

MS ASIA LIMITED+

## Andy Meng, CFA

Equity Analyst

Andy.Meng@morganstanley.com +852 2239-7689

MS TAIWAN LIMITED+

## Vivi Huang

Research Associate

Vivi.Huang@morganstanley.com +886 2 2730-2860

## Irene Yen

Research Associate

Irene.Yen@morganstanley.com +886 2 2730-2869

MS ASIA LIMITED+

## Betty Chen

Research Associate

Betty.H.Chen@morganstanley.com +852 2239-7213

## Asia Summer School 2026

![](images/0455946f612eac8945b8320bf986adc4edfee6b236d984e8276ddb1471a3e3b6.jpg)

## GREATER CHINA TECHNOLOGY HARDWARE

Asia Pacific

Industry View

In-Line

MS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.

## For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

+= Analysts employed by non-U.S. affiliates are not registered with FINRA, may not be associated persons of the member and may not be subject to FINRA restrictions on communications with a subject company, public appearances and trading securities held by a research analyst account.

Exhibit 2: iPad Sell-in Data, by Quarter

<table><tr><td>Unit units</td><td>1Q22</td><td>2Q22</td><td>3Q22</td><td>4Q22</td><td>2022</td><td>1Q23</td><td>2Q23</td><td>3Q23</td><td>4Q23</td><td>2023</td><td>1Q24</td><td>2Q24</td><td>3Q24</td><td>4Q24</td><td>2024</td><td>1Q25</td><td>2Q25</td><td>3Q25</td><td>4Q25</td><td>2025</td><td>1Q26</td><td>2Q26e</td><td>3Q26e</td></tr><tr><td>iPad Sell-in</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>iPad mini</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>iPad mini</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>iPad miniS</td><td>1.5</td><td>1.5</td><td>1.0</td><td>1.0</td><td>5.0</td><td>0.5</td><td>-</td><td>-</td><td>-</td><td>0.5</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>iPad miniS</td><td></td><td></td><td></td><td></td><td></td><td>1.0</td><td>2.5</td><td>3.0</td><td>2.0</td><td>8.5</td><td>1.0</td><td>1.0</td><td>2.0</td><td>3.0</td><td>7.0</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>iPad miniY</td><td></td><td></td><td></td><td></td><td></td><td></td><td>-</td><td>-</td><td>-</td><td></td><td></td><td></td><td>1.0</td><td>1.5</td><td>2.5</td><td>2.0</td><td>2.0</td><td>1.5</td><td>0.5</td><td>6.0</td><td>0.5</td><td>0.5</td><td>0.5</td></tr><tr><td>The iPad (8&#x27;7&#x27;)</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>The iPad 10&#x27;12&quot;</td><td>4.5</td><td>3.3</td><td>3.5</td><td>-</td><td>11.3</td><td>-</td><td>-</td><td>-</td><td>-</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>The iPad (10&#x27;9&#x27;)</td><td>-</td><td>-</td><td>3.0</td><td>7.0</td><td>10.0</td><td>4.0</td><td>4.5</td><td>4.5</td><td>6.0</td><td>19.0</td><td>3.5</td><td>2.5</td><td>5.5</td><td>5.5</td><td>17.0</td><td>5.5</td><td>6.0</td><td>6.0</td><td>6.0</td><td>23.5</td><td>5.5</td><td>6.0</td><td>6.0</td></tr><tr><td>iPad Air (10 S10/9&#x27;11&quot;)</td><td>3.5</td><td>5.0</td><td>4.0</td><td>3.0</td><td>15.5</td><td>3.0</td><td>2.0</td><td>3.0</td><td>4.0</td><td>12.0</td><td>2.0</td><td>2.0</td><td>3.0</td><td>2.5</td><td>9.5</td><td>2.5</td><td>3.0</td><td>3.0</td><td>3.5</td><td>12.0</td><td>3.0</td><td>3.5</td><td>3.5</td></tr><tr><td>iPad Air (12 9&#x27;13&#x27;F)</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>1.0</td><td>2.0</td><td>2.0</td><td>1.5</td><td>6.5</td><td>1.0</td><td>1.5</td><td>1.5</td><td>2.0</td><td>6.0</td><td>2.0</td><td>2.0</td><td>2.0</td></tr><tr><td>iPad Pro 12&#x27;3&quot;</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>iPad Pro 10&#x27;5&quot;</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>iPad Pro 12&#x27;5&#x27; Face ID (2018)</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>iPad Pro 11&#x27; Face ID (2018)</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>iPad Pro 12&#x27;5&#x27; Face ID (2020)</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>iPad Pro 11&#x27; Face ID (2020)</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>iPad Pro 12&#x27;5&#x27; Face ID (2021)</td><td>1.5</td><td>1.0</td><td>0.5</td><td>-</td><td>3.0</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>iPad Pro 11&#x27; Face ID (2021)</td><td>1.0</td><td>1.0</td><td>0.5</td><td>-</td><td>2.5</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</t

[中间内容因长度限制已省略]

ptical Fibre and Cable JSC Ltd (601869.SS)</td><td>U (10/13/2021)</td><td>Rmb436.50</td></tr><tr><td>Yangtze Optical Fibre and Cable JSC Ltd (6869.HK)</td><td>E (04/20/2023)</td><td>HK$226.60</td></tr><tr><td>Yongxin Optics Co Ltd (603297.SS)</td><td>E (11/15/2022)</td><td>Rmb117.30</td></tr><tr><td>Zhejiang Crystal-Optech Co Ltd (002273.SZ)</td><td>O (11/15/2022)</td><td>Rmb32.39</td></tr><tr><td>Zhongji Innolight Co Ltd (300308.SZ)</td><td>++</td><td>Rmb1,149.00</td></tr><tr><td>ZTE Corporation (0763.HK)</td><td>O (06/04/2026)</td><td>HK$26.00</td></tr><tr><td>ZTE Corporation (000063.SZ)</td><td>E (06/04/2026)</td><td>Rmb36.35</td></tr></table>

Derrick Yang

<table><tr><td>Accton Technology Corporation (2345.TW)</td><td>O (06/06/2024)</td><td>NT$2,335.00</td></tr><tr><td>Advantech (2395.TW)</td><td>O (01/20/2021)</td><td>NT$473.00</td></tr><tr><td>AirTAC International (1590.TW)</td><td>O (04/16/2025)</td><td>NT$1,290.00</td></tr><tr><td>AU Optronics (2409.TW)</td><td>E (02/10/2026)</td><td>NT$23.50</td></tr><tr><td>Bizlink (3665.TW)</td><td>O (03/10/2025)</td><td>NT$2,310.00</td></tr><tr><td>BOE Technology (000725.SZ)</td><td>O (09/06/2019)</td><td>Rmb5.57</td></tr><tr><td>Chenbro (8210.TW)</td><td>O (07/23/2025)</td><td>NT$1,475.00</td></tr><tr><td>Chroma Ate Inc. (2360.TW)</td><td>O (10/05/2021)</td><td>NT$2,295.00</td></tr><tr><td>E Ink Holdings Inc. (8069.TWO)</td><td>O (05/11/2026)</td><td>NT$196.00</td></tr><tr><td>Ennostar Inc (3714.TW)</td><td>U (09/23/2022)</td><td>NT$64.40</td></tr><tr><td>Hiwin Technologies Corp. (2049.TW)</td><td>O (03/30/2026)</td><td>NT$323.50</td></tr><tr><td>Innolux (3481.TW)</td><td>E (04/07/2025)</td><td>NT$48.55</td></tr><tr><td>King Slide Works Co. Ltd. (2059.TW)</td><td>O (11/08/2023)</td><td>NT$6,910.00</td></tr><tr><td>Lens Technology (300433.SZ)</td><td>E (07/22/2020)</td><td>Rmb41.14</td></tr><tr><td>Radiant Opto-Electronics Corporation (6176.TW)</td><td>E (03/01/2024)</td><td>NT$91.30</td></tr><tr><td>Sanan Optoelectronics (600703.SS)</td><td>U (08/21/2023)</td><td>Rmb13.92</td></tr><tr><td>TCL Corp. (000100.SZ)</td><td>E (04/07/2025)</td><td>Rmb4.55</td></tr><tr><td>Tianma Microelectronics (000050.SZ)</td><td>U (01/24/2018)</td><td>Rmb7.51</td></tr><tr><td>Wuhan Jingce Electronic Group Co Ltd (300567.SZ)</td><td>E (11/26/2021)</td><td>Rmb196.30</td></tr></table>

Howard Kao

<table><tr><td>Acer Inc. (2353.TW)</td><td>U (04/23/2025)</td><td>NT$36.70</td></tr><tr><td>Asustek Computer Inc. (2357.TW)</td><td>U (11/16/2025)</td><td>NT$785.00</td></tr><tr><td>Compal Electronics (2324.TW)</td><td>U (04/23/2025)</td><td>NT$36.35</td></tr><tr><td>FIT Hon Teng Ltd (6088.HK)</td><td>O (11/03/2025)</td><td>HK$7.36</td></tr><tr><td>Giga-Byte Technology Co. Ltd. (2376.TW)</td><td>E (11/16/2025)</td><td>NT$342.00</td></tr><tr><td>Gold Circuit Electronics Ltd. (2368.TW)</td><td>O (10/06/2022)</td><td>NT$1,320.00</td></tr><tr><td>Inspur Electronic Information (000977.SZ)</td><td>E (08/28/2023)</td><td>Rmb57.86</td></tr><tr><td>Lenovo (0992.HK)</td><td>E (11/16/2025)</td><td>HK$22.34</td></tr><tr><td>Lotes Co. Ltd. (3533.TW)</td><td>E (05/12/2025)</td><td>NT$2,240.00</td></tr><tr><td>Nan Ya PCB (8046.TW)</td><td>O (02/23/2026)</td><td>NT$819.00</td></tr><tr><td>Pegatron Corporation (4938.TW)</td><td>E (03/25/2026)</td><td>NT$93.10</td></tr><tr><td>Quanta Computer Inc. (2382.TW)</td><td>O (05/01/2023)</td><td>NT$372.00</td></tr><tr><td>Shengyi Technology Co Ltd. (600183.SS)</td><td>E (05/26/2022)</td><td>Rmb151.28</td></tr><tr><td>Shennan Circuits Co Ltd (002916.SZ)</td><td>E (08/24/2023)</td><td>Rmb379.50</td></tr><tr><td>Unimicron (3037.TW)</td><td>O (02/23/2026)</td><td>NT$902.00</td></tr><tr><td>Wistron Corporation (3231.TW)</td><td>O (07/12/2023)</td><td>NT$156.00</td></tr><tr><td>Wiwynn Corp (6669.TW)</td><td>O (11/10/2025)</td><td>NT$4,850.00</td></tr><tr><td>Yageo Corp. (2327.TW)</td><td>O (10/28/2025)</td><td>NT$855.00</td></tr><tr><td>Zhen Ding (4958.TW)</td><td>O (05/18/2026)</td><td>NT$552.00</td></tr><tr><td colspan="3">Sharon Shih</td></tr><tr><td>Asia Vital Components Co. Ltd. (3017.TW)</td><td>O (07/30/2024)</td><td>NT$2,405.00</td></tr><tr><td>Auras Technology Co Ltd (3324.TWO)</td><td>E (05/04/2023)</td><td>NT$1,055.00</td></tr><tr><td>Catcher Technology (2474.TW)</td><td>U (11/17/2025)</td><td>NT$205.50</td></tr><tr><td>Delta Electronics Inc. (2308.TW)</td><td>O (07/13/2017)</td><td>NT$2,215.00</td></tr><tr><td>Fositek Corp (6805.TW)</td><td>O (06/25/2025)</td><td>NT$1,825.00</td></tr><tr><td>Foxconn Industrial Internet Co. Ltd. (601138.SS)</td><td>O (07/10/2019)</td><td>Rmb70.13</td></tr><tr><td>Foxconn Technology (2354.TW)</td><td>U (04/23/2025)</td><td>NT$57.00</td></tr><tr><td>GoerTek Inc (002241.SZ)</td><td>U (04/23/2025)</td><td>Rmb23.01</td></tr><tr><td>Hon Hai Precision (2317.TW)</td><td>O (03/15/2024)</td><td>NT$260.50</td></tr><tr><td>LandMark Optoelectronics Corporation (3081.TWO)</td><td>E (03/26/2026)</td><td>NT$2,195.00</td></tr><tr><td>Lingyi Itech Guangdong Co (002600.SZ)</td><td>U (04/23/2025)</td><td>Rmb14.01</td></tr><tr><td>Lite-On Technology (2301.TW)</td><td>E (01/15/2025)</td><td>NT$217.00</td></tr><tr><td>Luxshare Precision Industry Co., Ltd. (002475.SZ)</td><td>O (10/24/2016)</td><td>Rmb63.76</td></tr><tr><td>Sunonwealth Electric Machine Industry Co (2421.TW)</td><td>E (02/23/2024)</td><td>NT$144.00</td></tr><tr><td>Tong Hsing (6271.TW)</td><td>E (03/18/2019)</td><td>NT$238.50</td></tr><tr><td>Visual Photonics Epitaxy Co Ltd (2455.TW)</td><td>E (09/11/2023)</td><td>NT$352.00</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.  
\* Historical prices are not split adjusted.

© 2026 MS
"""
