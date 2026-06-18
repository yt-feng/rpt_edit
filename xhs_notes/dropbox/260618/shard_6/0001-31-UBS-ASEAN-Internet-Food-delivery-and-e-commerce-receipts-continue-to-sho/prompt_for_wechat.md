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
- `# 标题` 必须包含报告机构的中文名称。已识别机构名：`UBS`。标题格式建议：`# UBS：一句主判断`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、摩根斯坦利、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
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
1. `# 标题`：机构中文名 + 一句主判断，不超过 40 字。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份UBS研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
# ASEAN Internet

# Food delivery and e-commerce receipts continue to show healthy growth in May'26

## What did we learn from the May'26 ASEAN Food Delivery and E-commerce Receipts data?

Leveraging UBS Evidence Lab Food Delivery (> Access Dataset) and e-commerce receipts, we conclude that: 1) Grab's food delivery volume growth remained healthy at 21% YoY in May'26, though moderating from 26-28% in Mar/Apr'26, partly due to weakness in Indonesia; 2) Similarly, Shopee's e-commerce GMV growth also posted healthy +21% YoY GMV growth, moderating from 22/33% in Mar/Apr'26, due to seasonality; 3) Competitive intensity for both ASEAN food delivery and e-commerce sectors ticked up in May'26, with discounts trending up MoM. We attribute part of the slowdown to changing timing for Lebaran, but also see weak macro as a factor that needs to be closely monitored.

## Growth momentum remains healthy in May'26

- Food delivery: Grab's ASEAN "GMV weighted average" order volumes grew 21% YoY in May'26, healthy albeit moderating from 26-28% in Mar-Apr'26. This was partly due to continued weakness in Indonesia (-2.6% YoY orders) amid a weak macro backdrop. AOV was flat MoM (-0.3%) and slightly down (-1.1%) YoY, as Grab continues to push affordability focused products to drive growth. In comparing peers, Grab gained 69/136bps market share vs foodpanda in Philippines/Malaysia, although it lost some (17bps) share in Singapore.  
- E-commerce: Shopee's ASEAN e-commerce GMV grew 20.6% YoY in May'26 - healthy but, similar to food delivery, moderating from 23/33% in Mar/Apr'26 as we move past Lebaran seasonality. Volumes grew at a healthy pace of 28% YoY, although AOV was down 5.6% YoY.

## Competitive intensity broadly inched up in May'26

- Food delivery: On a MoM basis, competitive intensity inched up slightly in May'26, with higher discounting and lower delivery fees. Grab's discounts as a % AOV increased 5-140bps MoM across ASEAN with the exception of Vietnam (-38bps) and Philippines (-390bps). foodpanda took the opposite approach of Grab by lowering discounts in Malaysia (-22bps) and Singapore (-200bps) while increasing in Philippines (+70bps). Delivery fees as a % AOV were down 5-105bps MoM across ASEAN for both Grab and foodpanda, except Vietnam (+8bps for Grab) and Malaysia (+23bps for foodpanda).  
- E-commerce: Competitive intensity was up with both Shopee and seller funded promotions trending higher MoM in May'26. Shopee funded discounts were flat in Singapore but up 60-125bps MoM in Malaysia, Vietnam and Thailand. That said, it was down 30/73bps in Indonesia/Philippines. Meanwhile, seller funded discounts were up 10-95bps MoM across all ASEAN markets.

## Sector view: Maintain Buy on both Grab (PT US\$5.9) and Sea (PT US\$125)

Overall, receipts data continue to indicate robust growth and a generally healthy competitive environment, supporting our thesis that: 1) Grab's affordability initiatives to expand TAM continue to drive structural growth, reinforcing its position as the leading pan-ASEAN food delivery platform; 2) Shopee continues to outgrow the e-commerce market as its moat around logistics, scale and customer engagement via ShopeeVIP starts to differentiate it vs peers. Maintain Buy on Grab (PT US\$5.9) and Sea (PT US \$125).

## Equities

Asia Emerging

Internet Services

Navin Killa

Analyst

navin.killa@ubs.com

+852-2971 7594

Calvin Chur

Associate Analyst

calvin.chur@ubs.com

+65-6495 3992

## GRAB ASEAN

Figure 1: Grab ASEAN avg daily orders MoM %  
![](images/4f1083364af41f6cdfb1e705a860f569671965d6e29c50bc922f9858372c5fd7.jpg)

<details>
<summary>line chart</summary>

| Month    | Grab ASEAN avg daily orders MoM % (GMV weighted) |
| -------- | ----------------------------------------------- |
| Jan-21   | 2%                                              |
| Feb-21   | 10%                                             |
| Mar-21   | 5%                                              |
| Apr-21   | 18%                                             |
| May-21   | 10%                                             |
| Jun-21   | 0%                                              |
| Jul-21   | -5%                                             |
| Aug-21   | 25%                                             |
| Sep-21   | 0%                                              |
| Oct-21   | 7%                                              |
| Nov-21   | 4%                                              |
| Dec-21   | 3%                                              |
| Jan-22   | 0%                                              |
| Feb-22   | 4%                                              |
| Mar-22   | 5%                                              |
| Apr-22   | 4%                                              |
| May-22   | 3%                                              |
| Jun-22   | 0%                                              |
| Jul-22   | 4%                                              |
| Aug-22   | 5%                                              |
| Sep-22   | 3%                                              |
| Oct-22   | 0%                                              |
| Nov-22   | 4%                                              |
| Dec-22   | 5%                                              |
| Jan-23   | 3%                                              |
| Feb-23   | 0%                                              |
| Mar-23   | 4%                                              |
| Apr-23   | 10%                                             |
| May-23   | 3%                                              |
| Jun-23   | 0%                                              |
| Jul-23   | 4%                                              |
| Aug-23   | 5%                                              |
| Sep-23   | 3%                                              |
| Oct-23   | 0%                                              |
| Nov-23   | 4%                                              |
| Dec-23   | 5%                                              |
| Jan-24   | 3%                                              |
| Feb-24   | 0%                                              |
| Mar-24   | 4%                                              |
| Apr-24   | 5%                                              |
| May-24   | 3%                                              |
| Jun-24   | 0%                                              |
| Jul-24   | 4%                                              |
| Aug-24   | 5%                                              |
| Sep-24   | 3%                                              |
| Oct-24   | 0%                                              |
| Nov-24   | 4%                                              |
| Dec-24   | 5%                                              |
| Jan-25   | 3%                                              |
| Feb-25   | 0%                                              |
| Mar-25   | 4%                                              |
| Apr-25   | 5%                                              |
| May-25   | 3%                                              |
| Jun-25   | 0%                                              |
| Jul-25   | 4%                                              |
| Aug-25   | 5%                                              |
| Sep-25   | 3%                                              |
| Oct-25   | 0%                                              |
| Nov-25   | 4%                                              |
| Dec-25   | 5%                                              |
| Jan-26   | 3%                                              |
| Feb-26   | 0%                                              |
| Mar-26   | 4%                                              |
| Apr-26   | 5%                                              |
| May-26   | 3%                                              |
</details>

Source: UBS Evidence Lab

Figure 2: Grab ASEAN total orders YoY %  
![](images/14929816c294fdbe2b050748fa4633b26a5ceaee327d6c28c67f06a57c9dd1dc.jpg)

<details>
<summary>line chart</summary>

| Month    | Grab ASEAN total orders YoY % (GMV weighted) |
| -------- | ------------------------------------------- |
| Jan-21   | ~85%                                        |
| Mar-21   | ~75%                                        |
| May-21   | ~90%                                        |
| Jul-21   | ~120%                                       |
| Sep-21   | ~95%                                        |
| Nov-21   | ~105%                                       |
| Jan-22   | ~115%                                       |
| Mar-22   | ~100%                                       |
| May-22   | ~60%                                        |
| Jul-22   | ~45%                                        |
| Sep-22   | ~75%                                        |
| Nov-22   | ~20%                                        |
| Jan-23   | ~5%                                         |
| Mar-23   | ~10%                                        |
| May-23   | ~20%                                        |
| Jul-23   | ~15%                                        |
| Sep-23   | ~25%                                        |
| Nov-23   | ~30%                                        |
| Jan-24   | ~35%                                        |
| Mar-24   | ~30%                                        |
| May-24   | ~35%                                        |
| Jul-24   | ~30%                                        |
| Sep-24   | ~35%                                        |
| Nov-24   | ~30%                                        |
| Jan-25   | ~25%                                        |
| Mar-25   | ~30%                                        |
| May-25   | ~35%                                        |
| Jul-25   | ~40%                                        |
| Sep-25   | ~35%                                        |
| Nov-25   | ~30%                                        |
| Jan-26   | ~20%                                        |
| Mar-26   | ~25%                                        |
| May-26   | ~20%                                        |
</details>

Source: UBS Evidence Lab

Figure 3: Grab's MoM daily avg order volumes across markets  
![](images/428945cc793803973cfc75944ff8f61b58d1ebe9089f9cbe8d66098458ba65ab.jpg)

<details>
<summary>bar chart</summary>

Grab ASEAN avg daily order May-26 vs Apr-26 (MoM)
| Company | Value (%) |
| :--- | :--- |
| ID | 0.4 |
| MY | 2.5 |
| PH | 6.3 |
| SG | 0.9 |
| TH | 1.5 |
| VN | 9.8 |
| ASEAN | 2.8 |
</details>

Source: UBS Evidence Lab

Figure 4: Grab's YoY total orders across markets  
![](images/6aca29783e081ba4e2526b35584e1372f27023890574c6291f64045f85335a0f.jpg)

<details>
<summary>bar chart</summary>

Grab ASEAN total order May-26 vs May-25 (YoY)
| Country | Grab ASEAN total order (%) |
| :--- | :--- |
| ID | -2.6 |
| MY | 17.1 |
| PH | 29.0 |
| SG | 28.4 |
| TH | 32.2 |
| VN | 42.2 |
| ASEAN | 21.1 |
</details>

Source: UBS Evidence Lab

Figure 5: Grab's MoM AOV across markets  
![](images/2ca2a8b1b75fbf2bcb6458b6b69647381346dbcec1196b4ad14e2f7fab07b85a.jpg)

<details>
<summary>bar chart</summary>

Grab ASEAN AOV May-26 vs Apr-26 (MoM)
| Country | Value (%) |
| :--- | :--- |
| ID | -1.7 |
| MY | 3.4 |
| PH | -0.3 |
| SG | 2.9 |
| TH | -4.2 |
| VN | -0.8 |
| ASEAN | -0.3 |
</details>

Source: UBS Evidence Lab

Figure 6: Grab's YoY AOV across markets  
![](images/bc33e72441a0b810f72fd98300bf5c53791fdced01e5cd7e0ae69c08a7ea0bd4.jpg)

<details>
<summary>bar chart</summary>

Grab ASEAN AOV May-26 vs May-25 (YoY)
| Entity | Value (%) |
|---|---|
| ID | 1.7 |
| MY | 6.6 |
| PH | -8.9 |
| SG | 1.3 |
| TH | -5.6 |
| VN | -3.8 |
| ASEAN | -1.1 |
</details>

Source: UBS Evidence Lab

## SHOPEE ASEAN

Figure 7: Shopee's ASEAN avg daily GMV MoM %  
![](images/77f097a174e6c31567d40787d3db34b315dc5003bba12be6e5837821a97de88d.jpg)

<details>
<summary>line chart</summary>

| Month    | Shopee ASEAN avg daily GMV MoM % |
| -------- | ---------------------------------- |
| Oct-24   | 5%                                 |
| Nov-24   | 7%                                 |
| Dec-24   | 12%                                |
| Jan-25   | -5%                                |
| Feb-25   | 3%                                 |
| Mar-25   | 7%                                 |
| Apr-25   | -10%                               |
| May-25   | 10%                                |
| Jun-25   | 2%                                 |
| Jul-25   | 5%                                 |
| Aug-25   | 0%                                 |
| Sep-25   | 3%                                 |
| Oct-25   | 5%                                 |
| Nov-25   | 5%                                 |
| Dec-25   | 5%                                 |
| Jan-26   | -3%                                |
| Feb-26   | 1%                                 |
| Mar-26   | 3%                                 |
| Apr-26   | -5%                                |
| May-26   | 0%                                 |
</details>

Source: UBS Evidence Lab

Figure 8: Shopee's ASEAN GMV YoY %  
![](images/40ba0cfa624067b89969312d231b28a2ca730ee21840823fec9ce9716ca39d07.jpg)

<details>
<summary>line chart</summary>

| Month    | Shopee ASEAN GMV YoY % |
| -------- | ---------------------- |
| Oct-24   | 32%                    |
| Nov-24   | 26%                    |
| Dec-24   | 38%                    |
| Jan-25   | 42%                    |
| Feb-25   | 40%                    |
| Mar-25   | 38%                    |
| Apr-25   | 31%                    |
| May-25   | 36%                    |
| Jun-25   | 38%                    |
| Jul-25   | 37%                    |
| Aug-25   | 32%                    |
| Sep-25   | 38%                    |
| Oct-25   | 39%                    |
| Nov-25   | 37%                    |
| Dec-25   | 29%                    |
| Jan-26   | 31%                    |
| Feb-26   | 29%                    |
| Mar-26   | 24%                    |
| Apr-26   | 33%                    |
| May-26   | 21%                    |
</details>

Source: UBS Evidence Lab

Figure 9: Shopee's ASEAN avg daily orders MoM %  
![](images/be15cb73d8439b3d1c246f42b1f77a5042959eba4e4d78e616186bd71693db11.jpg)

<details>
<summary>line chart</summary>

| Month    | Shopee ASEAN Orders MoM % |
| -------- | ------------------------- |
| Oct-24   | 5%                        |
| Nov-24   | 0%                        |
| Dec-24   | 12%                       |
| Jan-25   | -5%                       |
| Feb-25   | -7%                       |
| Mar-25   | 25%                       |
| Apr-25   | -15%                      |
| May-25   | 13%                       |
| Jun-25   | 0%                        |
| Jul-25   | 9%                        |
| Aug-25   | -1%                       |
| Sep-25   | 0%                        |
| Oct-25   | 8%                        |
| Nov-25   | 0%                        |
| Dec-25   | 7%                        |
| Jan-26   | -10%                      |
| Feb-26   | -10%                      |
| Mar-26   | 15%                       |
| Apr-26   | -7%                       |
| May-26   | 6%                        |
</details>

Source: UBS Evidence Lab

Figure 10: Shopee's ASEAN total orders YoY %  
![](images/4e05b79a8c2bca0c842f206e90b7914f46aad25f18522ef6d381769480f3f61e.jpg)

<details>
<summary>line chart</summary>

| Month    | Shopee ASEAN Orders YoY % |
| -------- | ------------------------- |
| Oct-24   | 31%                       |
| Nov-24   | 32%                       |
| Dec-24   | 43%                       |
| Jan-25   | 38%                       |
| Feb-25   | 35%                       |
| Mar-25   | 31%                       |
| Apr-25   | 30%                       |
| May-25   | 37%                       |
| Jun-25   | 39%                       |
| Jul-25   | 39%                       |
| Aug-25   | 34%                       |
| Sep-25   | 40%                       |
| Oct-25   | 42%                       |
| Nov-25   | 40%                       |
| Dec-25   | 34%                       |
| Jan-26   | 41%                       |
| Feb-26   | 37%                       |
| Mar-26   | 26%                       |
| Apr-26   | 38%                       |
| May-26   | 28%                       |
</details>

Source: UBS Evidence Lab

Figure 11: Shopee ASEAN AOV MoM %  
![](images/7f1a54427c01df11651ad4a2ea669cb9bfeabb79921715dffa73106710eaa695.jpg)

<details>
<summary>line chart</summary>

| Month    | Shopee ASEAN AOV MoM % (GMV weighted) |
| -------- | ------------------------------------- |
| Oct-24   | 1.5%                                  |
| Nov-24   | 0.5%                                  |
| Dec-24   | 2.5%                                  |
| Jan-25   | 3.8%                                  |
| Feb-25   | -2.5%                                 |
| Mar-25   | -5.5%                                 |
| Apr-25   | 1.0%                                  |
| May-25   | 0.5%                                  |
| Jun-25   | -3.0%                                 |
| Jul-25   | -1.0%                                 |
| Aug-25   | 1.0%                                  |
| Sep-25   | 0.0%                                  |
| Oct-25   | -0.5%                                 |
| Nov-25   | 1.5%                                  |
| Dec-25   | 0.5%                                  |
| Jan-26   | -1.0%                                 |
| Feb-26   | 0.0%                                  |
| Mar-26   | -1.5%                                 |
| Apr-26   | -0.5%                                 |
| May-26   | -2.5%                                 |
</details>

Source: UBS Evidence Lab

Figure 12: Shopee ASEAN AOV YoY %  
![](images/a087b8c2c2bf2c4c3180623a7251f07b4cc922e61542545ffa2f71ad8a7ba38e.jpg)

<details>
<summary>line chart</summary>

| Month    | Shopee ASEAN AOV YoY % (GMV weighted) |
| -------- | ------------------------------------ |
| Oct-24   | 1.0%                                 |
| Nov-24   | -4.0%                                |
| Dec-24   | -3.0%                                |
| Jan-25   | 3.0%                                 |
| Feb-25   | 4.0%                                 |
| Mar-25   | 6.0%                                 |
| Apr-25   | 1.0%                                 |
| May-25   | 0.0%                                 |
| Jun-25   | -1.0%                                |
| Jul-25   | -1.5%                                |
| Aug-25   | -2.0%                                |
| Sep-25   | -1.5%                                |
| Oct-25   | -2.5%                                |
| Nov-25   | -3.0%                                |
| Dec-25   | -4.0%                         

[中间内容因长度限制已省略]

 Kingdom, UBS AG is authorised by the Prudential Regulation Authority and is subject to regulation by the Financial Conduct Authority and limited regulation by the Prudential Regulation Authority. Details about the extent of regulation by the Prudential Regulation Authority are available from us on request. A member of the London Stock Exchange. This publication is distributed to retail clients of UBS Wealth Management. Ukraine: UBS is a premier global financial services firm offering wealth management services to individual, corporate and institutional investors. UBS is established in Switzerland and operates under Swiss law and in over 50 countries and from all major financial centers. UBS is not registered and licensed as a bank/financial institution under Ukrainian legislation and does not provide banking and other financial services in Ukraine. UBS has not made, and will not make, any offer of the mentioned products to the public in Ukraine. No action has been taken to authorize an offer of the mentioned products to the public in Ukraine and the distribution of this document shall not constitute financial services for the purposes of the Law of Ukraine "On Financial Services and Financial Companies" dated 14 December 2021. Any offer of the mentioned products shall not constitute an investment advice, public offer, circulation, transfer, safekeeping, holding or custody of securities in the territory of Ukraine. Accordingly, nothing in this document or any other document, information or communication related to the mentioned products shall be interpreted as containing an offer, a public offer or invitation to offer or to a public offer, or solicitation of securities in the territory of Ukraine or investment advice under Ukrainian law. Electronic communication must not be considered as an offer to enter into an electronic agreement or other electronic instrument within the meaning of the Law of Ukraine "On Electronic Commerce" dated 3 September 2015. This document is strictly for private use by its holder and may not be passed on to third parties or otherwise publicly distributed. USA: Distributed to US persons only by UBS Financial Services Inc. or UBS LLC, subsidiaries of UBS AG. UBS Switzerland AG, UBS Europe SE, UBS Bank, S.A., UBS BB Corretora de Câmbio, Títulos e Valores Mobiliários S.A., UBS Asesores México, S.A. de C.V., UBS SuMi TRUST Wealth Management Co., Ltd., UBS Wealth Management Israel Ltd. and UBS Menkul Degerler AS are affiliates of UBS AG. UBS Financial Services Inc. accepts responsibility for the content of a report prepared by a non-US affiliate when it distributes reports to US persons. All transactions by a US person in the securities mentioned in this report should be effected through a US-registered broker dealer affiliated with UBS, and not through a non-US affiliate. The contents of this report have not been and will not be approved by any securities or investment authority in the United States or elsewhere. UBS Financial Services Inc. is not acting as a municipal advisor to any municipal entity or obligated person within the meaning of Section 15B of the Securities Exchange Act (the "Municipal Advisor Rule") and the opinions or views contained herein are not intended to be, and do not constitute, advice within the meaning of the Municipal Advisor Rule. For information on the ways in which UBS LLC manages conflicts and maintains independence of its UBS Global Research product; historical performance information; certain additional disclosures concerning UBS Global Research recommendations; and terms and conditions for certain third party data used in research report, please visit https://www.ubs.com/disclosures.

© UBS 2026. The key symbol and UBS are among the registered and unregistered trademarks of UBS. All rights reserved.

## CS Wealth Management Disclaimer

This disclaimer must be read in conjunction with "Risk information" and "Important Information About Sustainable Investing Strategies" sections of the Global Wealth Management Disclaimer above. You receive this document in your capacity as a client of CS Wealth Management. Your personal data will be processed in accordance with the CS privacy statement accessible at your domicile through the official CS website https://www.credit-suisse.com. In order to provide you with marketing materials concerning our products and services, UBS Group AG and its subsidiaries may process your basic personal data (i.e. contact details such as name, e-mail address) until you notify us that you no longer wish to receive them. You can optout from receiving these materials at any time by informing your Relationship Manager.

Except as otherwise specified herein and/or depending on the local CS entity from which you are receiving this report, this report is distributed by UBS Switzerland AG, authorised and regulated by the Swiss Financial Market Supervisory Authority (FINMA). Saudi Arabia: This document is being distributed by CS Saudi Arabia I Part of UBS Group (CR Number 1010228645, NUN Number 7001515373), duly licensed and regulated by the Saudi Arabian Capital Market Authority pursuant to License Number 08104-37 dated 23/03/1429H corresponding to 21/03/2008AD. CS Saudi Arabia's principal place of business is at King Khaled Road, Laysen Valley, Building number 6, 12329-2376, Riyadh, Saudi Arabia. Website: https://www.credit-suisse.com/sa/en/cssa.html.

© UBS 2026. The key symbol and UBS are among the registered and unregistered trademarks of UBS. All rights reserved.

![](images/d8476cf39621eab9659d9b8cd95ea28ec260aaa4b7b2e7883c56ebd59c0bd26a.jpg)
"""
