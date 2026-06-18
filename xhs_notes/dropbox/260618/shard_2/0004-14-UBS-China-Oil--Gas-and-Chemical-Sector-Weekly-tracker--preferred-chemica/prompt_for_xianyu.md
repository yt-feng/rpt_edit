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
# China Oil, Gas and Chemical Sector

# Weekly tracker: preferred chemical stocks on Middle East conflict de-escalation

## Refining: Brent price might average at \$85/bbl in Q326 if a quick resolution

Global crude: The US and Iran have agreed a deal that would reopen the Strait of Hormuz after the signing ceremony on Friday in Switzerland (link). Iranian officials confirmed that an agreement has been found and that the US blockade would be lifted immediately and completely. UBS expects that a quick resolution implies Brent at US\$85/bbl on average in Q326E. While the crude price may fall before the deal is signed and there is confirmation that the supply of oil has resumed, a rebound in crude demand should support prices. China refining: SOE refineries' average utilisation declined 0.6ppt WoW to 67.18% last week. Utilisation at teapot refineries declined 2.5ppt WoW to 48.6%. As per Kpler data, overall China crude inventories decreased 16MMbbl to 1,280MMbbl last week.

## Chemicals: MDI utilisation up 9ppt WoW

Ethylene: naphtha-based ethylene utilisation declined 2ppt WoW to 77% and was broadly flat YoY, while MTO route utilisation was flat WoW at 83%. Polyolefins: PE utilisation declined 1ppt/2ppt WoW/YoY to 80%, while PP utilisation decreased 1ppt/14ppt WoW/YoY to 63%. PDH utilisation decreased 1ppt WoW to 63%. PVC utilisation was broadly flat WoW at 70%. Aromatics chain: PX utilisation decreased 1ppt WoW to 77%, while PTA utilisation increased 2ppt WoW to 65%. Polyester filament utilisation declined 4ppt WoW to 76%. TDI utilisation fell 3ppt WoW to 63%, while MDI utilisation rose 9ppt WoW to 83%. TiO2 utilisation was broadly flat WoW at 79%.

## PE/PVC/Polyester filament inventory fell WoW

According to sample inventory data, PP inventory increased 4% WoW but fell 21% YoY to 460kt. PE inventory declined 1% WoW and 16% YoY to 476kt. PVC inventory fell 1% WoW and 22% YoY to 413kt. TiO2 inventory rose 27% WoW but declined 49% YoY to 166kt. Polyester filament inventory fell 16% WoW but rose 66% YoY. Silicone DMC inventory declined 1% WoW and 15% YoY to 42kt.

## Stock picks

Since the outbreak of the Middle East conflict, chemical companies' share prices have trended down in general (Wind chemical stock index down 9% in May) due to rising costs, lower demand and geopolitical uncertainties. If the de-escalation is successful, we believe beneficiaries would include: 1) companies impacted by raw material prices, including polyester filament (Tongkun) and phosphate chemicals; 2) chemicals leaders with re-rating potential (Wanhua and Yangnong). Olefin producers with alternative production routes (Baofeng and Satellite) could face pressure in the short term. We like Jereh as a beneficiary of AI development (note), select MLCC companies (note) and fluorochemical materials companies. We will host calls with chemical material companies that may benefit from AI development (registration link) this week.

## Equities

China

Chemicals

Amily Guo

Analyst

amily.guo@ubs.com

+86-105-832 8845

Henri Patricot, CFA

Analyst

henri.patricot@ubs.com

+33-14-888 3033

Cheryl Wen

Analyst

S1460525030002

cheryl.wen@ubs.com

+86-21-3866 8916

Richard Li

Analyst

S1460121090003

richard-ze.li@ubs.com

+86-21-3866 8802

Nayoung Kim

Analyst

nayoung.kim@ubs.com

+44-20-7568 4010

Jay LIN

Analyst

S1460525070001

jay.lin@ubs.com

+86-105-832 8044

Crude inventory and refinery utilisation  
Figure 1: China crude oil inventory  
![](images/616f037e6071cbbbd150acc2b0a9004b9d759b568a407961d8d8220fdec206ec.jpg)

<details>
<summary>line chart</summary>

| Date     | Value |
| -------- | ----- |
| 2021-W01 | 1150  |
| 2021-W11 | 1180  |
| 2021-W21 | 1130  |
| 2021-W31 | 1120  |
| 2021-W41 | 1100  |
| 2021-W51 | 1090  |
| 2022-W09 | 1110  |
| 2022-W19 | 1140  |
| 2022-W29 | 1160  |
| 2022-W39 | 1170  |
| 2022-W49 | 1150  |
| 2023-W07 | 1180  |
| 2023-W17 | 1200  |
| 2023-W27 | 1220  |
| 2023-W37 | 1200  |
| 2023-W47 | 1180  |
| 2024-W05 | 1150  |
| 2024-W15 | 1130  |
| 2024-W25 | 1160  |
| 2024-W35 | 1180  |
| 2024-W45 | 1200  |
| 2024-W55 | 1180  |
| 2024-W65 | 1160  |
| 2024-W75 | 1140  |
| 2024-W85 | 1170  |
| 2024-W95 | 1190  |
| 2024-W105| 1210  |
| 2024-W115| 1230  |
| 2024-W125| 1250  |
| 2024-W135| 1270  |
| 2024-W145| 1290  |
| 2024-W155| 1310  |
| 2024-W165| 1330  |
| 2024-W175| 1350  |
| 2024-W185| 1370  |
| 2024-W195| 1390  |
| 2024-W205| 1410 |
| 2024-W215| 1430 |
</details>

Source: Kpler, UBS

Figure 2: Utilisation of China SOE/teapot refiners  
![](images/086202d1cba17858c0b9e879caeffdead4668efd4ac2404b4a2042a95b138a04.jpg)

<details>
<summary>line chart</summary>

| Date       | SOE refiners | Teapot refiners |
| ---------- | ------------ | --------------- |
| 2026/1/30  | 83.0         | 53.0            |
| 2026/2/28  | 84.0         | 51.0            |
| 2026/3/31  | 73.0         | 54.0            |
| 2026/4/30  | 68.0         | 56.0            |
| 2026/5/31  | 67.18        | 48.86           |
</details>

Source: SCI99, Wind

Chemical utilisation  
Figure 3: China ethylene (naphtha cracking) capacity utilisation  
![](images/c645061d79242ab5447e34445cff169e3fd77daec98e48a09e6f2cbb5e3b6c5d.jpg)

<details>
<summary>line chart</summary>

| Week | 2024 | 2025 | 2026 |
|------|------|------|------|
| W1   | 83   | 83   | 83   |
| W3   | 84   | 84   | 84   |
| W5   | 85   | 85   | 85   |
| W7   | 86   | 86   | 100  |
| W9   | 87   | 87   | 85   |
| W11  | 86   | 86   | 80   |
| W13  | 85   | 85   | 75   |
| W15  | 84   | 84   | 73   |
| W17  | 83   | 83   | 72   |
| W19  | 82   | 82   | 75   |
| W21  | 81   | 81   | 76   |
| W23  | 80   | 80   | 77   |
| W25  | 81   | 81   | 78   |
| W27  | 82   | 82   | 79   |
| W29  | 83   | 83   | 80   |
| W31  | 84   | 84   | 81   |
| W33  | 85   | 85   | 82   |
| W35  | 86   | 86   | 83   |
| W37  | 87   | 87   | 84   |
| W39  | 86   | 86   | 83   |
| W41  | 85   | 85   | 82   |
| W43  | 84   | 84   | 81   |
| W45  | 83   | 83   | 80   |
| W47  | 82   | 82   | 79   |
</details>

Source: Wind, Oilchem

Figure 4: China ethylene (MTO) capacity utilisation  
![](images/4f85c120217a4d61f400a5a6794dad84f21dfba3f1a8bf0b5ed58936dc40b118.jpg)

<details>
<summary>line chart</summary>

| Week | 2024 | 2025 | 2026 |
|------|------|------|------|
| W1   | 90   | 85   | 90   |
| W3   | 88   | 83   | 87   |
| W5   | 87   | 82   | 86   |
| W7   | 89   | 81   | 88   |
| W9   | 95   | 83   | 89   |
| W11  | 98   | 84   | 90   |
| W13  | 97   | 85   | 91   |
| W15  | 95   | 86   | 89   |
| W17  | 90   | 80   | 87   |
| W19  | 92   | 85   | 86   |
| W21  | 90   | 95   | 85   |
| W23  | 85   | 87   | 83   |
| W25  | 75   | 85   | 82   |
| W27  | 73   | 86   | 81   |
| W29  | 78   | 87   | 82   |
| W31  | 80   | 88   | 83   |
| W33  | 85   | 89   | 84   |
| W35  | 87   | 90   | 85   |
| W37  | 89   | 91   | 86   |
| W39  | 90   | 92   | 87   |
| W41  | 92   | 93   | 88   |
| W43  | 100  | 94   | 89   |
| W45  | 90   | 93   | 88   |
| W47  | 87   | 92   | 87   |
</details>

Source: Wind, Oilchem

Figure 5: China PE capacity utilisation  
![](images/bbd74143acf6d8f85bf7ac97e8c74c239fd64d500f0c5f780110941f89741e27.jpg)

<details>
<summary>line chart</summary>

| Week | 2024 | 2025 | 2026 |
|------|------|------|------|
| W1   | 85   | 88   | 84   |
| W3   | 86   | 89   | 85   |
| W5   | 87   | 90   | 86   |
| W7   | 88   | 91   | 87   |
| W9   | 89   | 92   | 88   |
| W11  | 90   | 93   | 89   |
| W13  | 88   | 90   | 86   |
| W15  | 85   | 87   | 82   |
| W17  | 82   | 85   | 78   |
| W19  | 80   | 83   | 75   |
| W21  | 78   | 81   | 73   |
| W23  | 76   | 79   | 71   |
| W25  | 74   | 77   | 69   |
| W27  | 72   | 75   | 67   |
| W29  | 70   | 73   | 65   |
| W31  | 68   | 71   | 63   |
| W33  | 66   | 69   | 61   |
| W35  | 64   | 67   | 59   |
| W37  | 62   | 65   | 57   |
| W39  | 60   | 63   | 55   |
| W41  | 58   | 61   | 53   |
| W43  | 56   | 59   | 51   |
| W45  | 54   | 57   | 49   |
| W47  | 52   | 55   | 47   |
| W49  | 50   | 53   | 45   |
| W51  | 48   | 51   | 43   |
</details>

Source: Baiinfo

Figure 6: China PP capacity utilisation  
![](images/5cdd46d9849b465520b6cc190e33a3e8ba8b9e44a76d3232f200a515a52ae132.jpg)

<details>
<summary>line chart</summary>

| Week | 2024 | 2025 | 2026 |
|------|------|------|------|
| W1   | 80   | 82   | 75   |
| W3   | 85   | 83   | 74   |
| W5   | 84   | 84   | 73   |
| W7   | 83   | 85   | 72   |
| W9   | 84   | 83   | 71   |
| W11  | 85   | 82   | 70   |
| W13  | 86   | 81   | 68   |
| W15  | 87   | 79   | 65   |
| W17  | 88   | 77   | 62   |
| W19  | 86   | 75   | 63   |
| W21  | 85   | 76   | 64   |
| W23  | 84   | 77   | 63   |
| W25  | 85   | 78   | 64   |
| W27  | 86   | 79   | 65   |
| W29  | 85   | 78   | 64   |
| W31  | 86   | 79   | 63   |
| W33  | 87   | 80   | 62   |
| W35  | 86   | 79   | 61   |
| W37  | 85   | 78   | 60   |
| W39  | 84   | 77   | 59   |
| W41  | 83   | 76   | 58   |
| W43  | 82   | 75   | 57   |
| W45  | 81   | 74   | 56   |
| W47  | 80   | 73   | 55   |
| W49  | 79   | 72   | 54   |
| W51  | 80   | 73   | 53   |
</details>

Source: Baiinfo

Figure 7: China PVC capacity utilisation  
![](images/3f5f7a63f3585d28208a7de1238989674135306e17756c3dd06faff297b2cf73.jpg)

<details>
<summary>line chart</summary>

| Week | 2024 | 2025 | 2026 |
|------|------|------|------|
| W1   | 87   | 81   | 78   |
| W3   | 86   | 81   | 77   |
| W5   | 85   | 81   | 76   |
| W7   | 84   | 81   | 77   |
| W9   | 85   | 81   | 78   |
| W11  | 84   | 81   | 77   |
| W13  | 83   | 81   | 76   |
| W15  | 82   | 80   | 75   |
| W17  | 81   | 79   | 74   |
| W19  | 80   | 78   | 73   |
| W21  | 79   | 77   | 72   |
| W23  | 78   | 76   | 71   |
| W25  | 77   | 75   | 70   |
| W27  | 76   | 74   | 69   |
| W29  | 75   | 73   | 68   |
| W31  | 74   | 72   | 67   |
| W33  | 73   | 71   | 66   |
| W35  | 72   | 70   | 65   |
| W37  | 71   | 69   | 64   |
| W39  | 70   | 68   | 63   |
| W41  | 69   | 67   | 62   |
| W43  | 68   | 66   | 61   |
| W45  | 67   | 65   | 60   |
| W47  | 66   | 64   | 59   |
| W49  | 65   | 63   | 58   |
| W51  | 64   | 62   | 57   |
</details>

Source: Baiinfo

Figure 8: China PDH capacity utilisation  
![](images/c7d9237730e2099424d12c3c81e5047178b3e514195ca30ed8aba554cbb11360.jpg)

<details>
<summary>line chart</summary>

| Week | 2024 | 2025 | 2026 |
|------|------|------|------|
| W1   | 70   | 62   | 75   |
| W3   | 65   | 63   | 68   |
| W5   | 68   | 64   | 65   |
| W7   | 67   | 65   | 67   |
| W9   | 66   | 66   | 66   |
| W11  | 67   | 67   | 65   |
| W13  | 68   | 68   | 63   |
| W15  | 69   | 69   | 60   |
| W17  | 70   | 70   | 55   |
| W19  | 72   | 71   | 50   |
| W21  | 73   | 72   | 55   |
| W23  | 74   | 73   | 60   |
| W25  | 75   | 74   | 62   |
| W27  | 76   | 75   | 64   |
| W29  | 77   | 76   | 66   |
| W31  | 78   | 77   | 68   |
| W33  | 79   | 78   | 70   |
| W35  | 80   | 79   | 72   |
| W37  | 81   | 80   | 74   |
| W39  | 82   | 81   | 76   |
| W41  | 83   | 82   | 78   |
| W43  | 84   | 83   | 80   |
| W45  | 85   | 84   | 82   |
| W47  | 86   | 85   | 84   |
| W49  | 87   | 86   | 86   |
| W51  | 88   | 87   | 88   |
</details>

Source: Baiinfo

Figure 9: China PX capacity utilisation  
![](images/188f5e5e382b1eb0ddcafd78364828568e873d3393c5ab5d998bbc180be284f7.jpg)

<details>
<summary>line chart</summary>

| Week | 2024 | 2025 | 2026 |
|------|------|------|------|
| W1   | 79   | 88   | 86   |
| W3   | 84   | 87   | 87   |
| W5   | 85   | 87   | 87   |
| W7   | 85   | 87   | 87   |
| W9   | 85   | 87   | 91   |
| W11  | 85   | 87   | 87   |
| W13  | 85   | 87   | 85   |
| W15  | 85   | 87   | 83   |
| W17  | 68   | 75   | 79   |
| W19  | 80   | 75   | 79   |
| W21  | 70   | 75   | 79   |
| W23  | 70   | 85   | 79   |
| W25  | 80   | 85   | 79   |
| W27  | 85   | 85   | 79   |
| W29  | 85   | 85   | 79   |
| W31  | 85   | 85   | 79   |
| W33  | 85   | 85   | 79   |
| W35  | 85   | 85   | 79   |
| W37  | 85   | 85   | 79   |
| W39  | 85   | 85   | 79   |
| W41  | 85   | 85   | 79   |
| W43  | 85   | 85   | 79   |
| W45  | 85   | 85   | 79   |
| W47  | 85   | 85   | 79   |
| W49  | 85   | 85   | 79   |
| W51  | 85   | 85   | 79   |
</details>

Source: Baiinfo

Figure 10: China PTA capacity utilisation  
![](images/ef556c74f90d407005c146c4f6d4fe144ab6d228a0c4808544619ca446c1d1b6.jpg)

<details>
<summary>line chart</summary>

| Week | 2024 | 2025 | 2026 |
|------|------|------|------|
| W1   | 81   | 79   | 76   |
| W3   | 83   | 78   | 75   |
| W5   | 82   | 79   | 74   |
| W7   | 83   | 78   | 75   |
| W9   | 83   | 77   | 74   |
| W11  | 83   | 76   | 75   |
| W13  | 82   | 75   | 76   |
| W15  | 80   | 74   | 78   |
| W17  | 70   | 73   | 65   |
| W19  | 81   | 72   | 63   |
| W21  | 70   | 71   | 60   |
| W23  | 75   | 73   | 58   |
| W25  | 76   | 75   | 64   |
| W27  | 78   | 77   | -    |
| W29  | 80   | 79   | -    |
| W31  | 81   | 80   | -    |
| W33  | 82   | 81   | -    |
| W35  | 83   | 80   | -    |
| W37  | 84   | 79   | -    |
| W39  | 85   | 78   | -    |
| W41  | 84   | 79   | -    |
| W43  | 83   | 78   | -    |
| W45  | 82   | 77   | -    |
| W47  | 81   | 76   | -    |
| W49  | 86   | 74   | -    |
| W51  | 80   | 74   | -    |
</details>

Source: Baiinfo

Figure 11: China Polyester filament capacity utilisation  
![](images/fbc19b5bc50e86a57e7e3dae2fc30a9d3a9bb679af5d52e51b86d489c8cfc7ed.jpg)

<details>
<summary>line chart</summary>

| Week | 2024 (%) | 2025 (%) | 2026 (%) |
|---|---|---|---|
| W1 | 83 | 87 | 89 |
| W3 | 80 | 84 | 87 |
| W5 | 78 | 79 | 85 |
| W7 | 75 | 78 | 77 |
| W9 | 76 | 85 | 78 |
| W11 | 90 | 91 | 85 |
| W13 | 91 | 94 | 85 |
| W15 | 92 | 94 | 84 |
| W17 | 91 | 93 | 83 |
| W19 | 90 | 92 | 82 |
| W21 | 86 | 90 | 83 |
| W23 | 86 | 89 | 76 |
| W25 | 86 | 89 | - |
| W27 | 85 | 89 | - |
| W29 | 84 | 89 | - |
| W31 | 84 | 89 | - |
| W33 | 84 | 89 | - |
| W35 | 83 | 89 | - |
| W37 | 84 | 89 | - |
| W39 | 87 | 90 | - |
| W41 | 89 | 90 | - |
| W43 | 90 | 90 | - |
| W45 | 91 | 90 | - |
| W47 | 90 | 90 | - |
| W49 | 90 | 89 | - |
| W51 | 89 | 89 | - |
</details>

Source: Baiinfo

Figure 12: China MDI capacity utilisation  
![](images/8ce0176c4a99dace9319252ae6556d49d2fdcfb77f5e87b033e5ae452b5b1e30.jpg)

<details>
<summary>line chart</summary>

| Week | 2024 | 2025 | 2026 |
|------|------|------|------|
| W1   | 50   | 75   | 45   |
| W3   | 70   | 95   | 85   |
| W5   | 75   | 90   | 85   |
| W7   | 80   | 85   | 85   |
| W9   | 85   | 85   | 85   |
| W11  | 80   | 85   | 85   |
| W13  | 80   | 80   | 80   |
| W15  | 80   | 75   | 80   |
| W17  | 85   | 90   | 80   |
| W19  | 85   | 85   | 80   |
| W21  | 80   | 80   | 75   |
| W23  | 70   | 75   | 75   |
| W25  | 75   | 75   | 85   |
| W27  | 80   | 80   | 80   |
| W29  | 85   | 80   | 80   |
| W31  | 75   | 90   | 80   |
| W33  | 65   | 90   | 80   |
| W35  | 65   | 90   | 80   |
| W37  | 90   | 95   | 80   |
| W39  | 85   | 95   | 80   |
| W41  | 80   | 95   | 80   |
| W43  | 75   | 95   | 80   |
| W45  | 75   | 95   | 80   |
| W47  | 70   | 65   | 75   |
| W49  | 60   | 60   | 65   |
| W51  | 75   | 45   | -    |
</details>

Source: Baiinfo

Figure 13: China TDI capacity utilisation  
![](images/785b654b49b2d0f521d066bbb5fe7c09b7c6431e2275155cfa161ccbb1f60dae.jpg)

<details>
<summary>line chart</summary>

| Week | 2024 | 2025 | 2026 |
|------|------|------|------|
| W1   | 80   | 88   | 60   |
| W3   | 78   | 85   | 50   |
| W5   | 82   | 87   | 65   |
| W7   | 83   | 89   | 70   |
| W9   | 81   | 88   | 72   |
| W11  | 75   | 86   | 75   |
| W13  | 72   | 84   | 80   |
| W15  | 70   | 82   | 85   |
| W17  | 90   | 60   | 92   |
| W19  | 90   | 85   | 85   |
| W21  | 90   | 80   | 70   |
| W23  | 75   | 75   | 65   |
| W25  | 70   | 70   | 60   |
| W27  | 85   | 70   | 65   |
| W29  | 85   | 70   | 65   |
| W31  | 70   | 65   | 60   |
| W33  | 

[中间内容因长度限制已省略]

legislation and does not provide banking and other financial services in Ukraine. UBS has not made, and will not make, any offer of the mentioned products to the public in Ukraine. No action has been taken to authorize an offer of the mentioned products to the public in Ukraine and the distribution of this document shall not constitute financial services for the purposes of the Law of Ukraine "On Financial Services and Financial Companies" dated 14 December 2021. Any offer of the mentioned products shall not constitute an investment advice, public offer, circulation, transfer, safekeeping, holding or custody of securities in the territory of Ukraine. Accordingly, nothing in this document or any other document, information or communication related to the mentioned products shall be interpreted as containing an offer, a public offer or invitation to offer or to a public offer, or solicitation of securities in the territory of Ukraine or investment advice under Ukrainian law. Electronic communication must not be considered as an offer to enter into an electronic agreement or other electronic instrument within the meaning of the Law of Ukraine "On Electronic Commerce" dated 3 September 2015. This document is strictly for private use by its holder and may not be passed on to third parties or otherwise publicly distributed. USA: Distributed to US persons only by UBS Financial Services Inc. or UBS LLC, subsidiaries of UBS AG. UBS Switzerland AG, UBS Europe SE, UBS Bank, S.A., UBS BB Corretora de Câmbio, Títulos e Valores Mobiliários S.A., UBS Asesores México, S.A. de C.V., UBS SuMi TRUST Wealth Management Co., Ltd., UBS Wealth Management Israel Ltd. and UBS Menkul Degerler AS are affiliates of UBS AG. UBS Financial Services Inc. accepts responsibility for the content of a report prepared by a non-US affiliate when it distributes reports to US persons. All transactions by a US person in the securities mentioned in this report should be effected through a US-registered broker dealer affiliated with UBS, and not through a non-US affiliate. The contents of this report have not been and will not be approved by any securities or investment authority in the United States or elsewhere. UBS Financial Services Inc. is not acting as a municipal advisor to any municipal entity or obligated person within the meaning of Section 15B of the Securities Exchange Act (the "Municipal Advisor Rule") and the opinions or views contained herein are not intended to be, and do not constitute, advice within the meaning of the Municipal Advisor Rule. For information on the ways in which UBS LLC manages conflicts and maintains independence of its UBS Global Research product; historical performance information; certain additional disclosures concerning UBS Global Research recommendations; and terms and conditions for certain third party data used in research report, please visit https://www.ubs.com/disclosures

© UBS 2026. The key symbol and UBS are among the registered and unregistered trademarks of UBS. All rights reserved.

## CS Wealth Management Disclaimer

This disclaimer must be read in conjunction with "Risk information" and "Important Information About Sustainable Investing Strategies" sections of the Global Wealth Management Disclaimer above. You receive this document in your capacity as a client of CS Wealth Management. Your personal data will be processed in accordance with the CS privacy statement accessible at your domicile through the official CS website https://www.credit-suisse.com. In order to provide you with marketing materials concerning our products and services, UBS Group AG and its subsidiaries may process your basic personal data (i.e. contact details such as name, e-mail address) until you notify us that you no longer wish to receive them. You can optout from receiving these materials at any time by informing your Relationship Manager.

Except as otherwise specified herein and/or depending on the local CS entity from which you are receiving this report, this report is distributed by UBS Switzerland AG, authorised and regulated by the Swiss Financial Market Supervisory Authority (FINMA). Saudi Arabia: This document is being distributed by CS Saudi Arabia I Part of UBS Group (CR Number 1010228645, NUN Number 7001515373), duly licensed and regulated by the Saudi Arabian Capital Market Authority pursuant to License Number 08104-37 dated 23/03/1429H corresponding to 21/03/2008AD. CS Saudi Arabia's principal place of business is at King Khaled Road, Laysen Valley, Building number 6, 12329-2376, Riyadh, Saudi Arabia. Website: https://www.credit-suisse.com/sa/en/cssa.html.

© UBS 2026. The key symbol and UBS are among the registered and unregistered trademarks of UBS. All rights reserved.

![](images/731b4bf474440ea7586e02b4f548aa6131fa593de9e2478b86b51e4abf2d703d.jpg)
"""
