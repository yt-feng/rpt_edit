你是闲鱼资料类商品文案编辑，擅长把一份投研/行业/公司研报改写成适合闲鱼发布的商品说明。

【目标】
- 基于下面研报解析内容，生成一份可以复制到闲鱼商品详情里的中文文案。
- 风格参考用户提供的闲鱼对标笔记：标题直给、信息密度高、用途明确、适合人群明确、交付方式清楚。
- 语言要自然，像真实卖家发布，不要像公众号文章、小红书笔记或 AI 摘要。
- 不要使用太夸张的营销词，不要承诺收益，不要说“稳赚”“内幕”“必涨”。
- 可以适度口语化，但不要低俗。

【必须输出结构】
1. `闲鱼标题：` 一行，控制在 30 字以内，适合商品标题。
2. `商品描述：` 正文，适合直接粘贴到闲鱼详情页。
3. `Hashtag：` 一行，给 6-10 个平台可用标签，用 `#` 开头，空格分隔。

【严禁输出】
- 不要输出 `建议价格：`。
- 不要输出 `搜索关键词：`。
- 不要输出“搜索词”“关键词”“搜索关键词”等栏目。
- 不要给具体价格区间、成交承诺或价格建议。

【商品描述写法】
- 第一段：直接说明这是什么报告，页数/语言/主题/公司或行业。如果页数、日期、语言不确定，就不要编。
- 第二段：说明适合谁，比如投研、券商面试、PE/VC、行业研究、学习参考、写报告等。
- 第三段：用 3-5 个亮点 bullet，风格参考：
  ✅ 三大情景框架：DCF、P/ARR、EV/Sales
  ✅ 关键变量分析
  ✅ 估值逻辑、假设、终值占比等核心内容覆盖
  ✅ 适合准备 AI 相关面试、研究 AI 估值的同学
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
# Energy - China

# Weekly: China's coal safety supervision expected to tighten further

Industry Overview

# Coal: worst coal mine disaster in over 16 years

State media Xinhua reported that at least 82 people were killed in a gas explosion at a coal mine in Qinyuan County, Changzhi City (Shanxi) on 22 May. According to Mysteel (23 May), all 25 coal mines in Qinyuan—representing total capacity of 25.6mntpa—have suspended production. Local authorities indicated that comprehensive grid-style inspections will be conducted across the coal sector. Over the weekend, Mysteel estimated that the number of suspended coking coal mines in Shanxi increased to 73, with combined capacity of 78.9mntpa. While the timeline for resumption in Qinyuan remains uncertain, most other suspended mines are expected to complete self-inspections within 3–5 days before restarting operations. During the week ended 22 May 2026, the QHD 5,500kcal price was flat WoW at RMB834/t. Ports inventory (Northern +Southern) was +1.9% WoW to 23.83mnt as of 21 May 2026. Inventory at the six major IPPs edged up 0.7% WoW to 12.9mnt, daily-burn down 2.1% WoW to 739.7kt. The NEWC 6,000K price was +0.3% WoW to US\$132.05/t, at a 23.5% premium to the QHD price. The Liulin No.4 HCC price was 1,620/t, down 1.2% WoW.

# Oil & Gas: prices down with renewed hopes on agreement

Oil: Brent oil decreased by 5.2% WoW to US\$103.5/b and WTI oil prices decreased by 8.4% WoW to US\$96.6/b, during the week-ended 22 May 2026. The WTI discount to Brent expanded from US\$3.8/b to US\$6.9/b. Dirty VLCC (from Arab Gulf to China) dayrate was USD93k/day. Gas: The US Henry Hub natural gas price was down 1.8% WoW to US\$2.91/mmbtu; the Netherlands TTF natural gas price was down 4.2% WoW to US\$16.41/mmbtu, 34.7% higher YoY and the JKM swap was up 10.0% WoW to US\$18.8/mmbtu, 50.7% higher YoY.

Energy storage: In the week-ended 22 May, prices of 50/100/280/314Ah battery cell prices rose RMB0.001/0.001/0.002/0.001Wh WoW to RMB0.426/0.413/0.336/0.358Wh. The prices of 215KW string PCS, 2500KW/1725KW centralized PCS were flattish WoW at RMB0.091/0.065/0.07 per W.

# Refining runrate remained low; chemical cost slide

Refining: China's refining margin (one-month crude price lag) in May'26 was US\$11.3/b verse US\$31.5/b in Apr'26, per our calculation. The run-rate of independent refineries in Shandong in the week ended 22 May 2026 has down 1.1ppt. WoW to 52.5%. SOE refiners stayed at 67% for the third consecutive week.

Petrochemicals: North Asia naphtha prices decreased by 10.5% WoW to US\$915/t in the week ended 22 May, tracking the decrease in crude oil. Over the same period, ethylene prices slipped 6.8% WoW to USD 1,101/t, while propylene prices down 1.2% WoW to USD 1,231/t. Downstream, LLDPE decreased 0.9% WoW to USD1,133/t, while PP prices decreased by 2.0% WoW to USD 1,223/t.

# 25 May 2026

Equity

China

Energy

Matty Zhao >>

Research Analyst

BofA (Hong Kong)

+852 3508 4001

matty.zhao@bofa.com

Yiming Wang >>

Research Analyst

BofA (Hong Kong)

+852 3508 5037

yiming.wang@bofa.com

Peter Wang >>

Research Analyst

BofA (Hong Kong)

+852 3508 7185

peter.wang2@bofa.com

Edward Leung, CFA >>

Research Analyst

BofA (Hong Kong)

+852 3508 3282

edward.leung@bofa.com

Miriam Chan, CFA >>

Research Analyst

BofA (Hong Kong)

+852 3508 7478

miriam.chan@bofa.com

Yibing Xia >>

Research Analyst

BofA (Hong Kong)

+852 3508 8045

yibing.xia@bofa.com

See the Appendix for a list of abbreviations used in the report

# Weekly updates

# Coal

- The QHD 5,500kcal price was flat WoW at RMB834/t during the week-ended 15 May;   
- The NEWC 6,000K price was +0.3% WoW to US\$132.05/t, at a 23.5% premium to the QHD price;   
- The Liulin No.4 HCC price was RMB1,620/t, down 1.2% WoW, during the weekend ended 22 May 2026;   
- As of 20 May, the water inflow at the Three Gorges Reservoir was 20,000cm/s, 102% higher than the 2005-25 average of 10,881cm/s.

Exhibit 1: ASP at coal mine pits

Thermal coal prices at mine in Shanxi (Kcal5.5k)/Inner Mongolia (Kcal5.5k)/Shaanxi (Kcal5.8k) changed -0.4%/+0.3%/+0.9% WoW to RMB692/574/652/t as of 22 May 2026

![](images/719f0c8338869463eb946ca42456f5ed3dc761409babfcb97996f0999c60c141.jpg)

<details>
<summary>line</summary>

| Date    | Shanxi Datong 5,500 | Shaanxi Yulin 5,800 | IM Ordos 5,500 |
|---------|---------------------|---------------------|----------------|
| Jan-16  | ~100                | ~100                | ~100           |
| Jan-17  | ~400                | ~400                | ~350           |
| Jan-18  | ~450                | ~450                | ~400           |
| Jan-19  | ~400                | ~400                | ~350           |
| Jan-20  | ~350                | ~350                | ~300           |
| Jan-21  | ~700                | ~800                | ~600           |
| Jan-22  | ~1,150              | ~2,050              | ~1,150          |
| Jan-23  | ~1,150              | ~1,300              | ~1,150          |
| Jan-24  | ~700                | ~800                | ~700           |
| Jan-25  | ~600                | ~650                | ~550           |
| Jan-26  | ~700                | ~750                | ~650           |
</details>

Source: Sxcoal, BofA Global Research   
BofA GLOBAL RESEARCH   
NEWC 6,000K thermal coal was +0.3% WoW to US\$132.05/t as of 22 May 2026

Exhibit 3: NEWC 6,000K thermal coal

![](images/138af454f18dce435dce6e7f406a1e19328aadfd0dfe57c8a2d5f12295a21738.jpg)

<details>
<summary>line</summary>

| Year | Price (US$/t) |
|------|---------------|
| 2025 | 132.05        |
</details>

Source: Sxcoal, BofA Global Research   
BofA GLOBAL RESEARCH   
As of 22 May, ASP of QHD 5,500kcal was flat WoW at RMB834/t

Exhibit 2: ASP at Qinhuangdao port (Kcal5,500)

![](images/ec79c3a8d0fc94216e867bec2375feef3aa3f214bfcc162adfe733071809fb20.jpg)

<details>
<summary>line</summary>

| Year | QHD price (5,500 Kcal/kg) |
| ---- | -------------------------- |
| 2026 | 834                        |
</details>

Source: Sxcoal, BofA Global Research   
BofA GLOBAL RESEARCH   
Liulin No. 4 hard coking coal price was RMB1,620/t, down 1.2% WoW, during the week-ended 22 May 2026

Exhibit 4: Liulin No. 4 hard coking coal price (incl. VAT)

![](images/3f0878d53aa62b9027d93847fef08e7c06565e53814d2b538f3d4d8cef297a4a.jpg)

<details>
<summary>line</summary>

| Year | RMB/t |
| ---- | ----- |
| 2026 | 1,620 |
</details>

Source: Sxcoal, BofA Global Research   
BofA GLOBAL RESEARCH

Exhibit 5: Ports inventory (Northern and Southern)   
Ports inventory (Northern +Southern) was +1.9% WoW to 23.83mnt as of 21 May 2026   
![](images/d669f8dd4a0e1ec8722efe09d23f12872efb4b5596974147b4976eda2866d3ae.jpg)

<details>
<summary>area</summary>

| Date   | Yangtze River ports (5) | Northern ports (4) |
|--------|--------------------------|--------------------|
| Jan-17 | ~2.0                     | ~18.0              |
| Jul-17 | ~3.0                     | ~19.0              |
| Jan-18 | ~4.0                     | ~20.0              |
| Jul-18 | ~5.0                     | ~21.0              |
| Jan-19 | ~6.0                     | ~22.0              |
| Jul-19 | ~7.0                     | ~23.0              |
| Jan-20 | ~5.0                     | ~21.0              |
| Jul-20 | ~4.0                     | ~20.0              |
| Jan-21 | ~3.0                     | ~19.0              |
| Jul-21 | ~2.0                     | ~18.0              |
| Jan-22 | ~3.0                     | ~17.0              |
| Jul-22 | ~4.0                     | ~16.0              |
| Jan-23 | ~5.0                     | ~15.0              |
| Jul-23 | ~6.0                     | ~14.0              |
| Jan-24 | ~5.0                     | ~13.0              |
| Jul-24 | ~6.0                     | ~12.0              |
| Jan-25 | ~7.0                     | ~11.0              |
| Jul-25 | ~6.0                     | ~10.0              |
| Jan-26 | ~7.0                     | ~9.0               |
</details>

Source: Sxcoal, BofA Global Research   
BofA GLOBAL RESEARCH

Exhibit 7: China coal social inventory   
China coal social inventory up 2% YoY to 704.5mnt by Mar '26   
![](images/0dadb034f029e80e7cf07a3464d99efaf47f04a3e49cb551161a25f7f974bd04.jpg)

<details>
<summary>line</summary>

| Month | 2025 (mnt) | 2024 (mnt) | 2023 (mnt) | 2022 (mnt) | 2026 (mnt) |
|---|---|---|---|---|---|
| Jan | 640 | 500 | 430 | 180 | 700 |
| Feb | 630 | 490 | 435 | 170 | 690 |
| Mar | 650 | 510 | 460 | 200 | 700 |
| Apr | 680 | 550 | 500 | 250 | - |
| May | 720 | 600 | 530 | 300 | - |
| Jun | 750 | 640 | 540 | 340 | - |
| Jul | 710 | 620 | 510 | 330 | - |
| Aug | 670 | 600 | 490 | 310 | - |
| Sep | 710 | 650 | 510 | 360 | - |
| Oct | 740 | 680 | 530 | 390 | - |
| Nov | 760 | 700 | 540 | 430 | - |
| Dec | 750 | 670 | 520 | 420 | - |
</details>

Source: Sxcoal, BofA Global Research   
BofA GLOBAL RESEARCH

Exhibit 9: China monthly coal imports   
Total coal (including lignite) imports was 33mnt. down 13% YoY in Apr'26.   
![](images/6322c6b657e200e233ddcc68c5b49112a81accc6ca773ece24c2dd329e74ddfa.jpg)

<details>
<summary>bar</summary>

| Month | 2026 (mmt) | 2025 (mmt) | 2024 (mmt) | 2023 (mmt) |
|---|---|---|---|---|
| Jan-Feb | 78 | 76 | 75 | 60 |
| Mar | 33 | 33 | 34 | 34 |
| Apr | 31 | 33 | 47 | 34 |
| May | - | 32 | 45 | 33 |
| Jun | - | 31 | 46 | 33 |
| Jul | - | 32 | 49 | 33 |
| Aug | - | 35 | 47 | 46 |
| Sep | - | 50 | 51 | 44 |
| Oct | - | 35 | 48 | 32 |
| Nov | - | 46 | 58 | 45 |
| Dec | - | 59 | 57 | 54 |
</details>

Source: China Customs, Wind, BofA Global Research   
Note: Since 2020, no single-month trade data are available for Jan-Feb   
BofA GLOBAL RESEARCH

Exhibit 8: China six major IPPs (unit: kt)   
Inventory at the six major IPPs increased by 0.7% WoW to 12.9mnt, as of 22 May 2026; daily-burn down 2.1% WoW to 739.7kt   
![](images/14f943e08726170d5b4d9b5bf1547cc06b8d1cd891b01921b309cdd7d40019db.jpg)

<details>
<summary>line</summary>

| Year | W01 | W04 | W07 | W10 | W13 | W16 | W19 | W22 | W25 | W28 | W31 | W34 | W40 | W43 | W46 | W49 | W52 |
|------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
| 2021 | 850 | 800 | 350 | 650 | 650 | 650 | 650 | 650 | 650 | 850 | 850 | 850 | 650 | 650 | 650 | 650 | 850 |
| 2022 | 850 | 850 | 850 | 850 | 850 | 850 | 850 | 850 | 850 | 850 | 850 | 850 | 850 | 850 | 850 | 850 | 850 |
| 2023 | 850 | 850 | 850 | 850 | 850 | 850 | 850 | 850 | 850 | 850 | 850 | 850 | 850 | 850 | 850 | 850 | 850 |
| 2024 | 850 | 850 | 850 | 850 | 850 | 850 | 850 | 850 | 850 | 850 | 850 | 850 | 850 | 850 | 850 | 850 | 850 |
| 2025 | 850 | 850 | 850 | 850 | 850 | 850 | 850 | 850 | 850 | 850 | 850 | 850 | 850 | 850 | 850 | 850 | 850 |
| 2026 | 850 | 850 | 600 | 650 | 650 | 650 | 650 | 650 | 650 | 650 | 650 | 650 | 650 | 650 | 650 | 650 | 650 |
| Other (labeled) - Series: Red dots (W7, W13, W16, W19, W22, W28, W31, W34, W43, W49, W52) — Values range from ~35 to ~95. The series are labeled as '2' (e.g., '2', '3', '4', '6', '7', '9', '11', '13', '15', '17', '19', '21', '23') but not explicitly labeled in the image.
</details>

Source: Sxcoal, BofA Global Research   
BofA GLOBAL RESEARCH

Exhibit 8: YTD China coal production   
China coal production was 385.6mnt, down 1% YoY in Apr '26   
![](images/b8261e424046178606f54b341ca421e885d48eeb8c6d53cb5beb7cc8fc17830b.jpg)

<details>
<summary>line</summary>

| Month | Prior 5 year range | Prior 5 year average | 2026 |
|-------|---------------------|----------------------|------|
| Jan   | ~370                | ~380                 | 385  |
| Feb   | ~260                | ~320                 | 370  |
| Mar   | ~320                | ~385                 | 440  |
| Apr   | ~320                | ~375                 | 380  |
| May   | ~320                | ~375                 | -    |
| Jun   | ~320                | ~380                 | -    |
| Jul   | ~315                | ~375                 | -    |
| Aug   | ~320                | ~375                 | -    |
| Sep   | ~320                | ~380                 | -    |
| Oct   | ~320                | ~380                 | -    |
| Nov   | ~325                | ~385                 | -    |
| Dec   | ~330                | ~390                 | -    |
</details>

Source: China NBS, Wind, BofA Global Research   
BofA GLOBAL RESEARCH

# Oil

Brent oil decreased by 5.2% WoW to US\$103.5/b and WTI oil prices decreased by 8.4% WoW to US\$96.6/b, during the week-ended 22 May 2026. The WTI discount to Brent expanded from US\$3.8/b to US\$6.9/b in the week ended 15 May.

Factors supporting oil prices include the following:

- Bloomberg reported Iran has refused to make concessions on its uranium stockpile and the issue of tolls for transit through the Strait of Hormuz, leaving US–Iran negotiations at a stalemate;   
- Bloomberg reported Iran is in discussions with Oman regarding the establishment of a permanent tolling system for the Strait of Hormuz;   
- The US total oil inventory (one-week lag) was down 18mb WoW to 819mb through the week ended 15 May 2026.

Factors suppressing oil prices include the following:

- US Secretary of State Marco Rubio said there had been “slight progress” in mediated talks with Iran. Tehran is currently reviewing the latest US proposal delivered through Pakistan, although no timeline has been provided for an official response;   
- Bloomberg reported The United States has issued a new waiver for Russian crude oil, with validity extended through June 17;   
- Bloomberg reported crude loadings at Russia's Black Sea port of Novorossiysk have fully resumed, with exports recovering to approximately 3.6mbd;

Exhibit 12: Brent and WTI weekly prices   
Brent oil decreased by 5.2% WoW to US\$103.5/b and WTI oil prices decreased by 8.4% WoW to US\$96.6/b   
![](images/0dfad97fab30a72d145a056cd90b799e2bd28f34f9a0c9b898ccd5857e129a76.jpg)

<details>
<summary>line</summary>

| Date   | Brent crude oil price (USD/b) | WTI crude oil price (USD/b) |
|--------|-------------------------------|-----------------------------|
| Jan-19 | ~60                           | ~55                         |
| Jan-20 | ~40                           | ~20                         |
| Jan-21 | ~70                           | ~60                         |
| Jan-22 | ~120                          | ~110                        |
| Jan-23 | ~90                           | ~85                         |
| Jan-24 | ~85                           | ~80                         |
| Jan-25 | ~75                           | ~70                         |
| Jan-26 | ~110                          | ~105                        |
</details>

Source: Bloomberg, BofA Global Research   
BofA GLOBAL RESEARCH

Exhibit 11: US weekly oil and gas rig count   
Oil rigs was +10 WoW to 425 and gas rigs -3 WoW to 125; total rig counts of 550 through the week ended 22 May 2026   
![](images/220aeb4ab35423f106b83c82fcf1d96b24a195c6cfa12501e15bda0a06aa6b22.jpg)

<details>
<summary>area</summary>

| Date   | US oil rigs | US gas rigs |
|--------|-------------|-------------|
| Jan-19 | 850         | 400         |
| Jan-20 | 600         | 200         |
| Jan-21 | 300         | 150         |
| Jan-22 | 500         | 300         |
| Jan-23 | 600         | 400         |
| Jan-24 | 550         | 350         |
| Jan-25 | 500         | 300         |
| Jan-26 | 450         | 250         |
</details>

Source: Baker Hughes, Bloomberg, BofA Global Research   
BofA GLOBAL RESEARCH

Exhibit 12: US crude oil production (one-week lag)   
Flat WoW at 13.7mbd   
![](images/5f0d90595d6325edf1b4c3609085e205c6c5b7b00acd923fba2960ec878ae4cb.jpg)

<details>
<summary>line</summary>

| Date   | US crude oil production (mbd) - LHS | WoW changes (%) - RHS |
|--------|-------------------------------------|--------

[中间内容因长度限制已省略]

lect information known to, professionals in other business areas of BofA, including investment banking personnel. BofA has established information barriers between BofA Global Research and certain business groups. As a result, BofA does not disclose certain client relationships with, or compensation received from, such issuers. To the extent this material discusses any legal proceeding or issues, it has not been prepared as nor is it intended to express any legal conclusion, opinion or advice. Investors should consult their own legal advisers as to issues of law relating to the subject matter of this material. BofA Global Research personnel's knowledge of legal proceedings in which any BofA entity and/or its directors, officers and employees may be plaintiffs, defendants, co-defendants or co-plaintiffs with or involving issuers mentioned in this material is based on public information. Facts and views presented in this material that relate to any such proceedings have not been reviewed by, discussed with, and may not reflect information known to, professionals in other business areas of BofA in connection with the legal proceedings or matters relevant to such proceedings.

This information has been prepared independently of any issuer of securities mentioned herein and not in connection with any proposed offering of securities or as agent of any issuer of any securities. None of BofAS any of its affiliates or their research analysts has any authority whatsoever to make any representation or warranty on behalf of the issuer(s). BofA Global Research policy prohibits research personnel from disclosing a recommendation, investment rating, or investment thesis for review by an issuer prior to the publication of a research report containing such rating, recommendation or investment thesis.

Any information relating to sustainability in this material is limited as discussed herein and is not intended to provide a comprehensive view on any sustainability claim with respect to any issuer or security.

Any information relating to the tax status of financial instruments discussed herein is not intended to provide tax advice or to be used by anyone to provide tax advice. Investors are urged to seek tax advice based on their particular circumstances from an independent tax professional.

The information herein (other than disclosure information relating to BofA and its affiliates) was obtained from various sources and we do not guarantee its accuracy. This information may contain links to third-party websites. BofA is not responsible for the content of any third-party website or any linked content contained in a third-party website. Content contained on such third-party websites is not part of this information and is not incorporated by reference. The inclusion of a link does not imply any endorsement by or any affiliation with BofA. Access to any third-party website is at your own risk, and you should always review the terms and privacy policies at third-party websites before submitting any personal information to them. BofA is not responsible for such terms and privacy policies and expressly disclaims any liability for them.

All opinions, projections and estimates constitute the judgment of the author as of the date of publication and are subject to change without notice. Prices also are subject to change without notice. BofA is under no obligation to update this information and BofA ability to publish information on the subject issuer(s) in the future is subject to applicable quiet periods. You should therefore assume that BofA will not update any fact, circumstance or opinion contained herein.

Certain outstanding reports or investment opinions relating to securities, financial instruments and/or issuers may no longer be current. Always refer to the most recent research report relating to an issuer prior to making an investment decision.

In some cases, an issuer may be classified as Restricted or may be Under Review or Extended Review. In each case, investors should consider any investment opinion relating to such issuer (or its security and/or financial instruments) to be suspended or withdrawn and should not rely on the analyses and investment opinion(s) pertaining to such issuer (or its securities and/or financial instruments) nor should the analyses or opinion(s) be considered a solicitation of any kind. Sales persons and financial advisors affiliated with BofAS or any of its affiliates may not solicit purchases of securities or financial instruments that are Restricted or Under Review and may only solicit securities under Extended Review in accordance with firm policies.

Neither BofA nor any officer or employee of BofA accepts any liability whatsoever for any direct, indirect or consequential damages or losses arising from any use of this information.
"""
