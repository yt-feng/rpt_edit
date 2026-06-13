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
CHINA EDUCATION MAY-26 TRACKER

# Learning tablet GMV growth pressured by high base, yet ASP upward trend sustained; Student visa decline narrowed

We summarize key findings from the May 2026 updates of our China Education tracker, including AI education apps, AI learning tablets, mobile user engagement, tutoring licenses, overseas study trends, and East Buy.

■ Mobile user engagement/learning center capacity: i) ByteDance: Doubao Study DAU growth accelerated to +146% yoy as of May-end and sustained the position of the 6th largest AI native app in China in terms of DAUs (Exhibit 1), while Gauth maintained its leadership with monthly billings +24% yoy to c.US\$1.1mn; ii) TAL: MAU growth for Xueersi.com decelerated to +10% yoy in May and Peiyou MAU maintained +19% yoy growth. On the other hand, offline non-academic tutoring licenses # continued the downward trend in May (Exhibit 18).  
AI learning tablets: Combined online GMV of 6 major learning device brands dropped -35% yoy in May (vs. -2% yoy in Apr) on major e-commerce platforms against the high base last year. TAL sold c.96k units for c.Rmb355mn GMV in May (-24% yoy), with ASP yoy decline narrowing to -4%. For TAL's 1QFY26 (May-Q), our tracked GMV dropped -1% yoy (vs. GSe of +11% yoy).  
- Overseas study: Student visas # granted to Chinese for Canada, Australia and UK combined dropped -9% yoy in 1Q26 (Exhibit 20), narrowing down vs. -22%/-16% yoy in 1Q25/2025.  
East Buy's GMV on Douyin grew +38% yoy/+7% mom to c.Rmb1.0bn in May (vs. +42% yoy in Apr), driven by new platforms' GMV +246% yoy (vs. -2% yoy decline for the original 3 platforms, Exhibit 27). East Buy app MAUs increased +38% yoy in May (vs. +42% yoy in Apr).

Within our China Education coverage, we are Buy rated on New Oriental (EDU/9901.HK, details in our recent upgrade note Up to Buy; Valuation too compelling to ignore) and TAL Education (TAL); New Oriental is trading at 11x CY26E P/E or 3x ex.cash, while TAL is trading at 12x CY26E P/E or 4x ex.cash. We are Sell on East Buy (1797.HK) and Offcn Education (002607.SZ).

Mobile user engagement: Doubao Study/Gauth continued scaling up in

Timothy Zhao

+852-2978-2673

timothy.zhao@gs.com

GS (Asia) L.L.C.

Ronald Keung, CFA

+852-2978-0856

ronald.keung@gs.com

GS (Asia) L.L.C.

Eunice Liu

+852-2978-7472 | eunice.liu@gs.com

GS (Asia) L.L.C.

Jason Sun

+852-2978-2616 | jinshi.sun@gs.com

GS (Asia) L.L.C.

## May; Peiyou app MAU steady growth vs. Xueersi.com growth moderated

## AI education apps

Exhibit 1: Doubao Study DAU growth accelerated to +146% yoy as of May-end and sustained the position of the 6th largest AI native app in China in terms of DAUs DAUs of major AI apps as of Apr-end  
![](images/db4ac1b140f1a7fa18081af30029817483939f083cc6df0ae3876a117c87993d.jpg)

<details>
<summary>bar-line hybrid</summary>

| Company | DAU May-end (mn) | May-end yoy (%) | Apr-end yoy (%) |
| :--- | :--- | :--- | :--- |
| Doubao | 161.3 | 356 | 365 |
| DeepSeek | 31.5 | 2 | -18 |
| Qwen | 27.6 | | 93 |
| Tencent Yuanbao | 8.4 | 111 | |
| AQ | 5.6 | | 128 |
| Doubao Study | 3.3 | 146 | 60 |
| Maoxiang | 1.7 | | 56 |
| Jimeng AI | 1.7 | 47 | 45 |
| Kimi | 1.1 | -53 | -60 |
| Kuaidui AI | 0.9 | -40 | -44 |
</details>

Qwen: 75x/78x for Apr-end/May-end yoy growth  
Source: Questmobile, Data compiled by GS Global Investment Research

Exhibit 3: Gauth has outperformed global AI-native education peers in terms of MAUs
MAUs by AI education apps (mn)  
![](images/d8f0cbe157a71400ed420005dd437d72f2ee5a26e98b4e5641c26e2252bf4de2.jpg)

<details>
<summary>line chart</summary>

| Month | Gauth | Brainly | QANDA | Knowunity | Question.AI | Gizmo | Solvely | Symbolab | Answer.AI | StudyX |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Jan-24 | 5 | 50 | 20 | 5 | 5 | 18 | 5 | 5 | 5 | 5 |
| Feb-24 | 5 | 55 | 18 | 5 | 5 | 17 | 5 | 5 | 5 | 5 |
| Mar-24 | 5 | 53 | 17 | 5 | 5 | 16 | 5 | 5 | 5 | 5 |
| Apr-24 | 5 | 52 | 16 | 5 | 5 | 15 | 5 | 5 | 5 | 5 |
| May-24 | 8 | 33 | 15 | 5 | 5 | 14 | 5 | 5 | 5 | 5 |
| Jun-24 | 8 | 33 | 14 | 5 | 5 | 13 | 5 | 5 | 5 | 5 |
| Jul-24 | 8 | 33 | 14 | 5 | 5 | 13 | 5 | 5 | 5 | 5 |
| Aug-24 | 8 | 33 | 14 | 5 | 5 | 13 | 5 | 5 | 5 | 5 |
| Sep-24 | 8 | 33 | 14 | 5 | 5 | 13 | 5 | 5 | 5 | 5 |
| Oct-24 | 24 | 33 | 14 | 5 | 5 | 13 | 5 | 5 | 5 | 5 |
| Nov-24 | 20 | 33 | 14 | 5 | 5 | 13 | 5 | 5 | 5 | 5 |
| Dec-24 | 20 | 33 | 14 | 5 | 5 | 13 | 5 | 5 | 5 | 5 |
| Jan-25 | 20 | 33 | 14 | 5 | 5 | 13 | 5 | 5 | 5 | 5 |
| Feb-25 | 20 | 33 | 14 | 5 | 5 | 13 | 5 | 5 | 5 | 5 |
| Mar-25 | 20 | 33 | 14 | 5 | 5 | 13 | 5 | 5 | 5 | 5 |
| Apr-25 | 20 | 33 | 14 | 5 | 5 | 13 | 5 | 5 | 5 | 5 |
| May-25 | 20 | 33 | 14 | 5 | 5 | 13 | 5 | 5 | 5 | 5 |
| Jun-25 | 14 | 33 | 14 | 5 | 5 | 13 | 5 | 5 | 5 | 5 |
| Jul-25 | 14 | 33 | 14 | 5 | 5 | 13 | 5 | 5 | 5 | 5 |
| Aug-25 | 14 | 33 | 14 | 5 | 5 | 13 | 5 | 5 | 5 | 5 |
| Sep-25 | 14 | 33 | 14 | 5 | 5 | 13 | 5 | 5 | 5 | 5 |
| Oct-25 | 36 | 33 | 14 | 5 | 5 | 13 | 5 | 5 | 5 | 5 |
| Nov-25 | - | - | - | - | - | - | - | - | - | - |
| Dec-25 | - | - | - | - | - | - | - | - | - | - |
| Jan-26 | - | - | - | - | - | - | - | - | - | - |
| Feb-26 | - | - | - | - | - | - | - | - | - | - |
| Mar-26 | - | - | - | - | - | - | - | - | - | - |
| Apr-26 | - | - | - | - | - | - | - | - | - | - |
| May-26 | - | - | - | - | - | - | - | - | - | - |
</details>

Source: Sensor Tower, Data compiled by GS Global Investment Research

Exhibit 2: Doubao Study continued to expand time spent market share among major K-12 learning tool/study companion apps in May  
Time spent share among major K-12 learning tool/study companion apps  
![](images/5b4c43630e428246bc2bf7e9f371a799c45a098b718719c0041ba442c2e4418f.jpg)  
Source: Questmobile, Data compiled by GS Global Investment Research

Exhibit 4: Gauth achieved c.US\$1.1mn billings with +24% yoy growth in May (vs. +35% yoy in Apr), bringing LTM billings to US\$13.2mn  
LTM billings by app (US\$ mn)  
![](images/c9152b5aadc4f8b3341dde4c145f21e6b0e1c94d80ff7ea2d17df3e5d8f09e2c.jpg)

<details>
<summary>bar chart</summary>

| Category | Value (USD mm) |
|---|---|
| Speak | 45.5 |
| Gauth | 13.2 |
| Solvely | 5.7 |
| Knowunity | 5.5 |
| Question.AI | 5.2 |
| Brainly | 4.5 |
| Gizmo | 2.1 |
| OANDA | 1.8 |
| Answer.AI | 1.6 |
| Knowt | 1.4 |
</details>

Source: Sensor Tower, Data compiled by GS Global Investment Research

Exhibit 5: Gauth monthly billings per avg. DAU grew +39% yoy to US\$0.4 in May (vs. +49% yoy in Apr)  
Gauth monthly billings (US\$ mn) and monthly billings per avg. DAU (US\$)  
![](images/755a7d8b39b293b2671bd2bae5f78e1f2e1d70129f150bafadd55e4869571cad.jpg)

<details>
<summary>bar-line hybrid chart</summary>

| Month | Monthly billings (US$ mn) | Monthly billings per avg. DAU (RHS) |
|---|---|---|
| Jan-24 | 0.3 | 1.4 |
| Feb-24 | 0.3 | 1.0 |
| Mar-24 | 0.3 | 0.9 |
| Apr-24 | 0.25 | 0.8 |
| May-24 | 0.25 | 0.5 |
| Jun-24 | 0.25 | 0.4 |
| Jul-24 | 0.2 | 0.6 |
| Aug-24 | 0.15 | 0.55 |
| Sep-24 | 0.25 | 0.3 |
| Oct-24 | 0.15 | 0.15 |
| Nov-24 | 0.5 | 0.25 |
| Dec-24 | 0.7 | 0.4 |
| Jan-25 | 0.4 | 0.2 |
| Feb-25 | 0.5 | 0.2 |
| Mar-25 | 1.0 | 0.4 |
| Apr-25 | 0.75 | 0.3 |
| May-25 | 0.85 | 0.35 |
| Jun-25 | 0.7 | 0.55 |
| Jul-25 | 0.7 | 0.55 |
| Aug-25 | 0.7 | 0.5 |
| Sep-25 | 1.4 | 0.45 |
| Oct-25 | 1.3 | 0.4 |
| Nov-25 | 1.45 | 0.4 |
| Dec-25 | 1.3 | 0.65 |
| Jan-26 | 1.15 | 0.45 |
| Feb-26 | 1.3 | 0.45 |
| Mar-26 | 1.25 | 0.45 |
| Apr-26 | 1.1 | 0.4 |
| May-26 | 1.05 | 0.45 |
| Jun-26 | 1.1 | 0.45 |
</details>

Source: Sensor Tower, Data compiled by GS Global Investment Research

## K-12 tutoring user engagement

Online K-12 tutoring: MAU growth for non-academic tutoring platforms decelerated to +2% yoy in May (excluding Youdao with continued MAU yoy decline) vs. +6%/+14% yoy in Mar/Apr, while MAUs for not-for-profit subject tutoring platforms dropped -26% yoy in May (vs. -20%/-21% yoy in Mar/Apr).  
TAL's Xueersi.com MAU yoy growth decelerated in May: Among pure online education apps, MAU growth for Xueersi.com decelerated to +10% yoy in May (vs. +10%/+22% yoy in Mar/Apr). MAU growth of TAL Xueersi (for Peiyou enrichment learning course registration and Peiyou Online course attendance) maintained +19% yoy in May (vs. +26%/+19% yoy in Mar/Apr), while MAU for EDU (for course registration) dropped -8% yoy in May (vs. +6%/+6% yoy in Mar/Apr).

Exhibit 6: MAU growth of Xueersi.com grew +10% yoy in May (vs. +22% yoy in Apr)  
MAU yoy growth of major tutoring platforms (%)  
![](images/0b08e0acd486ef9ce4438de6eefb169b1c36fddc48e16d0c651ea1b5abfe1fec.jpg)

<details>
<summary>line chart</summary>

| Month   | TAL  | EDU  | Gaotu | Xueersi.com | Youdao |
|---------|------|------|-------|-------------|--------|
| Jan-23  | -50% | -75% | -75%  | -75%        | -25%   |
| Mar-23  | 40%  | 10%  | 10%   | -25%        | -25%   |
| May-23  | 60%  | 25%  | 25%   | -10%        | -25%   |
| Jul-23  | 70%  | 30%  | 30%   | -5%         | -25%   |
| Sep-23  | 80%  | 40%  | 40%   | 0%          | -25%   |
| Nov-23  | 90%  | 50%  | 50%   | 10%         | -30%   |
| Jan-24  | 100% | 160% | 60%   | -10%        | -35%   |
| Mar-24  | 80%  | 50%  | 40%   | 10%         | -35%   |
| May-24  | 60%  | 30%  | 30%   | 40%         | -35%   |
| Jul-24  | 50%  | 20%  | 20%   | 80%         | -35%   |
| Sep-24  | 40%  | 10%  | 10%   | 120%        | -35%   |
| Nov-24  | 30%  | 5%   | 5%    | 140%        | -35%   |
| Jan-25  | 20%  | 0%   | 120%  | 180%        | -35%   |
| Mar-25  | 10%  | -5%  | 60%   | 160%        | -35%   |
| May-25  | 5%   | -10% | 40%   | 140%        | -35%   |
| Jul-25  | 0%   | -15% | 20%   | 120%        | -35%   |
| Sep-25  | -5%  | -20% | 10%   | 80%         | -35%   |
| Nov-25  | -10% | -25% | -5%   | 40%         | -35%   |
| Jan-26  | -15% | -30% | -10%  | 20%         | -35%   |
| Mar-26  | -20% | -35% | -15%  | 10%         | -35%   |
| May-26  | -25% | -40% | -20%  | -5%         | -35%   |
</details>

Source: Questmobile, Data compiled by GS Global Investment Research

Exhibit 7: Xueersi.com and TAL still led MAU yoy growth within non-academic tutoring in May  
MAUs of major non-academic tutoring platforms (mn)  
![](images/86d819b76659b44141ad660455e1b529208934cb08312760607bde9bae973663.jpg)

<details>
<summary>bar-line hybrid chart</summary>

| Company | May MAU (mn) (%) | Apr MAU (mn) (%) | Mar MAU (mn) (%) | May yoy (%) (%) | Apr yoy (%) (%) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| TAL | 19 | 1.15 | 1.05 | 19 | 19 |
| EDU | -8 | 0.5 | 0.45 | 6 | 6 |
| Gaotu | 1 | 1.35 | 1.55 | 1 | 1 |
| Xueersi.com | 22 | 2.3 | 1.75 | 10 | 22 |
| Youdao | -31 | 0.25 | 0.2 | -26 | -26 |
| Xiwangxue | -42 | 1.05 | 1.15 | -42 | -42 |
| Zuoyebang Live | -48 | 0.75 | 1.0 | -48 | -48 |
| Yuanfudao | 19 | 1.6 | 1.45 | -34 | 31 |
| Knowbox Class | -34 | 1.25 | 2.15 | -22 | -12 |
| Tutu Classroom | -22 | 0.95 | 1.35 | 7 | 12 |
| Ledu | 7 | 0.65 | 0.55 | 20 | 20 |
| Jinshu | 29 | 0.35 | 0.35 | 20 | 29 |
</details>

Source: Questmobile, Data compiled by GS Global Investment Research

Exhibit 8: Not-for-profit subject tutoring platforms: Combined MAUs dropped -26% yoy in May (vs. -21% yoy in Apr)  
MAUs of not-for-profit subject tutoring platforms  
![](images/91097201c142849126792139a131b2fae5dd64ec7d0513201517051a058e6481.jpg)

<details>
<summary>bar-line hybrid</summary>

| Month | Xiwangxue (mn) | Tutu Classroom (mn) | Yuanfudao (mn) | Zuoyebang Live (mn) | Knowbox Class (mn) | Jinshu (mn) | Ledu (mn) | Total MAU yoy (%) |
|---|---|---|---|---|---|---|---|---|
| Mar-23 | 1.5 | 1.8 | 1.9 | 1.7 | 4.0 | 0.0 | 0.0 | 20% |
| May-23 | 1.6 | 1.9 | 2.0 | 1.8 | 4.2 | 0.0 | 0.0 | 21% |
| Jul-23 | 2.0 | 2.1 | 2.2 | 2.0 | 4.5 | 0.0 | 0.0 | 56% |
| Sep-23 | 1.8 | 1.7 | 1.6 | 1.6 | 4.8 | 0.0 | 0.0 | 31% |
| Nov-23 | 1.9 | 1.8 | 1.7 | 1.7 | 4.9 | 0.0 | 0.0 | 16% |
| Jan-24 | 2.1 | 1.9 | 1.8 | 1.9 | 5.0 | 0.0 | 0.0 | 47% |
| Mar-24 | 1.7 | 1.6 | 1.5 | 1.5 | 4.8 | 0.0 | 0.0 | 11% |
| May-24 | 1.8 | 1.7 | 1.6 | 1.6 | 4.9 | 0.0 | 0.0 | 16% |
| Jul-24 | 2.0 | 1.8 | 1.7 | 1.7 | 5.0 | 0.0 | 0.0 | -3% |
| Sep-24 | 2.2 | 2.0 | 1.8 | 1.8 | 5.1 | 0.0 | 0.0 | 12% |
| Nov-24 | 2.3 | 2.1 | 1.9 | 1.9 | 5.2 | 0.0 | 0.0 | 9% |
| Jan-25 | 1.8 | 1.5 | 1.3 | 1.3 | 4.5 | -0.5 | -0.5 | -18% |
| Mar-25 | 2.0 | 1.6 | 1.4 | 1.4 | 4.6 | -0.5 | -0.5 | -6% |
| May-25 | 1.7 | 1.4 | 1.2 | 1.2 | 4.7 | -0.5 | -0.5 | -16% |
| Jul-25 | 1.6 | 1.3 | 1.1 | 1.1 | 4.8 | -0.5 | -0.5 | -8% |
| Sep-25 | 1.8 | 1.5 | 1.3 | 1.3 | 4.9 | -0.5 | -0.5 | -7% |
| Nov-25 | 2.0 | 1.6 | 1.4 | 1.4 | 5.0 | -0.5 | -0.5 | -20% |
| Jan-26 | 1.7 | 1.3 | 1.2 | 1.2 | 4.8 | -0.5 | -0.5 | -26% |
| Mar-26 | 1.5 | 1.2 | 1.1 | 1.1 | 4.7 | -0.5 | -0.5 | -36% |
| May-26 | -1.5 | -1.3 | -1.4 | -1.4 | -4.8 | -36% | -36% | -40% |
The chart displays a stacked bar chart with a line overlay showing the total annual year-over-year growth rate for each program from Mar-23 to May-26.
</details>

Source: Questmobile, Data compiled by GS Global Investment Research

Exhibit 9: Not-for-profit subject tutoring platforms: Total time spent dropped -33% yoy in May (vs. -21% yoy in Apr)  
![](images/149639e4dbfd98868efc97b10cccdd4e744b73dcd596963e3236ab2e484e604b.jpg)

<details>
<summary>bar-line hybrid</summary>

| Month | Xiwangxue (mn min) | Tutu Classroom (mn min) | Yuanfudao (mn min) | Zuoyebang Live (mn min) | Knowbox Class (mn min) | Jinshu (mn min) | Ledu (mn min) | Total time spent yoy (%) |
|---|---|---|---|---|---|---|---|---|
| Mar-23 | 150 | 180 | 200 | 100 | 100 | 100 | 0 | -6% |
| May-23 | 140 | 170 | 210 | 90 | 90 | 100 | 0 | 3% |
| Jul-23 | 350 | 150 | 150 | 100 | 110 | 120 | 0 | 35% |
| Sep-23 | 150 | 160 | 180 | 100 | 100 | 100 | 0 | -11% |
| Nov-23 | 160 | 170 | 200 | 100 | 110 | 100 | 0 | -4% |
| Jan-24 | 220 | 180 | 220 | 100 | 120 | 110 | 0 | 26% |
| Mar-24 | 250 | 190 | 230 | 100 | 120 | 110 | 0 | -16% |
| May-24 | 240 | 180 | 220 | 100 | 110 | 100 | 0 | -26% |
| Jul-24 | 320 | 250 | 250 | 150 | 130 | 150 | 0 | -16% |
| Sep-24 | 280 | 260 | 240 | 150 | 130 | 140 | 0 | -6% |
| Nov-24 | 230 | 270 | 260 | 150 | 140 | 150 | 0 | -21% |
| Jan-25 | 80 | 350 | 350 | 150 | 140 | 140 | 0 | -50% |
| Mar-25 | 85 | 360 | 360 | 150 | 145 | 145 | 0 | -2% |
| May-25 | 85 | 365 | 365 | 155 | 145 | 145 | 0 | -33% |
| Jul-25 | 85 | 375 | 375 | 155 | 145 | 145 | 0 | -50% |
| Sep-25 | 85 | 385 | 385 | 165 | 145 | 145 | -3% | -16% |
| Nov-25 | 85 | 395 | 395 | 165 | 145 | 145 | -3% | -27% |
| Jan-26 | 85 | 405 | 405 | 175 | 145 | 145 | -3% | -3% |
| Mar-26 | 85 | 415 | 415 | 175 | 145 | 145 | -3% | -28% |
| May-26 | 85 | 425 | 425 | 185 | 145 | 145 | -3% | -33% |
Total time spent yoy (%)
</details>

Source: Questmobile, Data compiled by GS Global Investment Research

## AI learning tablets: TAL tablet GMV -35% yoy in May or flattish yoy in May-Q; ASP yoy decline continued narrowing

GMV: Combined GMV of 6 major learning device brands dropped -35% yoy or increased +46% mom in May (vs. -2% yoy/-47% mom in Apr) on Douyin/Taobao/Tmall/JD. By brand, GMV of (+) Yuanfudao increased +31% yoy in May, while (-) iFlytek/TAL/Xiaodu/BBK/Zuoyebang dropped -23%/-24%/-51%/-60%/-64% yoy.
Specifically, TAL sold c.96k units for c.Rmb355mn GMV on major eCommerce platforms in May, with -21% yoy/+99% mom for shipments and -24% yoy/+85% mom for GMV (vs. +20% yoy/-42% mom for GMV in Apr). ASP of TAL learning tablets saw the yoy decline narrowing to -4%, while decreasing -7% mom to c.Rmb3.7k in May due to 618 promotional campaigns (vs. -5% yoy/+6% mom in Apr). For TAL's 1QFY26 (May-Q), our tracked GMV dropped -1% yoy (below GSe of +11% yoy).

## Exhibit 10: TAL's learning tablets GMV dropped -24% yoy or increased +85% mom in May on major eCommerce platforms (vs. +20% yoy/-42% mom in Apr)

TAL's monthly online GMV on major eCommerce platforms

![](images/bd8652ce9e425f02671c3a5e95dcbf29b7b49628641eeaf7d843abdada816f9e.jpg)  
Source: Moojing, Chanmama, Data compi

[中间内容因长度限制已省略]

es, including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

© 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
