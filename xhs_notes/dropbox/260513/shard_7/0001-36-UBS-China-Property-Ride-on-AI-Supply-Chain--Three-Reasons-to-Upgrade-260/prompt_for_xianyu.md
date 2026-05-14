你是闲鱼资料类商品文案编辑，擅长把一份投研/行业/公司研报改写成适合闲鱼发布的商品说明。

【目标】
- 基于下面研报解析内容，生成一份可以复制到闲鱼商品详情里的中文文案。
- 风格参考用户提供的闲鱼对标笔记：标题直给、信息密度高、用途明确、适合人群明确、交付方式清楚。
- 语言要自然，像真实卖家发布，不要像公众号文章、小红书笔记或 AI 摘要。
- 不要使用太夸张的营销词，不要承诺收益，不要说“稳赚”“内幕”“必涨”。
- 可以适度口语化，但不要低俗。

【必须输出结构】
1. `闲鱼标题：` 一行，控制在 30 字以内，适合商品标题。
2. `建议价格：` 一行，给一个资料类商品常见价格区间，例如 `8-20 元`，不要承诺成交价。
3. `商品描述：` 正文，适合直接粘贴到闲鱼详情页。
4. `搜索关键词：` 一行，给 8-15 个关键词，用空格分隔。

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

【合规与避坑】
- 默认避免出现具体投行品牌名，比如“GS”“GS”“MS”，统一写作“投行研报”或“投行研报”。
- 不要写“原版/内部/独家/无水印/全网最低”等容易违规或夸张的词。
- 不要承诺投资收益。
- 不要伪造页数、日期、作者、公司覆盖范围。研报未给出时就不写。
- 不要输出解释说明，只输出闲鱼文案本身。

【研报解析内容】
"""
# China Property

# Ride on AI Supply Chain; Three Reasons to Upgrade

# Demand: Rising industrial profits and positive PPI; Prefer tier 1 Cities

We are turning more positive on the China property sector, due to 1) increased housing demand visibility from rising industrial profits (AI supply chain) and positive PPI (our strategy note: Green shoots emerging?); 2) positive wealth effect from companies with rising profitability/share prices, and mapping of their headquarters indicates a strong concentration in Beijing and Shanghai; 3) falling vacancy rate in tier 1 Cities suburb districts, suggesting shadow inventory has been digested. In 2026, we expect property prices in tier 1 Cities to stabilize (previously -10%) and in tier 2 Cities to still decline by 5% (previously -10%). In 2027, we expect prices in tier 1 Cities to increase by 2% and in tier 2 Cities to stabilize (previously -5%). We upgrade COLI (added to Key Call list), BEKE, Jinmao and CMSK to Buy on their high exposure to tier 1 Cities. We also like CR Land for its high tier 1 Cities exposure and value unlock from asset securitization.

# Demand: Mapping the headquarters of emerging sectors/companies

The surge of AI-related materials, government anti-involution measures and export growth caused industrial profits to grow by 15% YoY in 1Q26 with positive PPI. Historically, industrial profits have a 0.63 correlation to tier 1 Cities property price. Among sectors, computer, communication, electronic equipment, non-ferrous metals and chemical sectors' profit surged the most and related sectors' share prices outperformed. Those companies' headquarters are located in Beijing, Shanghai, Suzhou and Dongguan, which is in line with a stronger secondary transaction volume YTD than other Cities. This makes us think the recovery this time could be different and more driven by improved profitability at industrial enterprises rather than policy previously.

# Supply: Falling vacancy rate in tier 1 Cities suburb districts vs three years ago

Apart from falling secondary listing in tier 1 Cities, vacancy rate in tier 1 Cities suburb districts improved compared to three years ago (2023), which we view as positive. Looking ahead, we expect a declining supply for commodity housing and social housing due to sUBStantial decline in new home starts/land sales during the past three years.

# Valuation: Further 30% upside potential

Despite recent share outperformance, we see potential for further 30% share price upside if the sector P/BV reverts to its 15-year average level of 0.85x, vs current trading P/BV at 0.66x. As the market recovery is more confined to tier 1 Cities, we prefer COLI, CMSK, Jinmao and BEKE for high tier 1 Cities exposure (\~41% vs peer group below 25%). We raise our price targets for CR Land and C&D and maintain our Buy ratings.

Figure 1: Rating and PT changes 

<table><tr><td rowspan="2">Company</td><td rowspan="2">Shr pr(LCY/shr)</td><td rowspan="2">Mkt cap(USD bn)</td><td colspan="3">Rating</td><td colspan="4">Price target(LCY/share)</td><td colspan="2">Earnings estimateNew vs Old</td><td colspan="2">P/BV</td><td colspan="2">PE</td></tr><tr><td>New</td><td>Old</td><td>Chg</td><td>New</td><td>Old</td><td>Chg</td><td>% upside</td><td>2026E</td><td>2027E</td><td>2026E</td><td>2027E</td><td>2026E</td><td>2027E</td></tr><tr><td>COLI</td><td>16.0</td><td>22.4</td><td>Buy</td><td>Neutral</td><td>▲</td><td>25.00</td><td>13.80</td><td>81%</td><td>56%</td><td>14%</td><td>49%</td><td>0.38</td><td>0.38</td><td>13.0</td><td>11.4</td></tr><tr><td>BEKE</td><td>19.2</td><td>20.7</td><td>Buy</td><td>Neutral</td><td>▲</td><td>23.00</td><td>18.00</td><td>28%</td><td>20%</td><td>23%</td><td>30%</td><td>1.92</td><td>1.69</td><td>20.3</td><td>16.5</td></tr><tr><td>CMSK</td><td>9.7</td><td>12.8</td><td>Buy</td><td>Neutral</td><td>▲</td><td>12.00</td><td>9.80</td><td>22%</td><td>24%</td><td>-65%</td><td>-29%</td><td>0.89</td><td>0.87</td><td>75.1</td><td>30.4</td></tr><tr><td>Jinmao</td><td>1.9</td><td>3.3</td><td>Buy</td><td>Neutral</td><td>▲</td><td>2.30</td><td>1.50</td><td>53%</td><td>19%</td><td>-7%</td><td>42%</td><td>0.59</td><td>0.58</td><td>27.7</td><td>15.5</td></tr><tr><td>CR Land</td><td>38.1</td><td>34.7</td><td>Buy</td><td>Buy</td><td>■</td><td>45.00</td><td>36.00</td><td>25%</td><td>18%</td><td>4%</td><td>8%</td><td>0.78</td><td>0.74</td><td>10.2</td><td>9.7</td></tr><tr><td>C&amp;D International</td><td>18.2</td><td>5.2</td><td>Buy</td><td>Buy</td><td>■</td><td>21.00</td><td>17.00</td><td>24%</td><td>16%</td><td>-12%</td><td>6%</td><td>1.17</td><td>1.16</td><td>10.2</td><td>8.4</td></tr><tr><td>Greentown China</td><td>10.9</td><td>3.5</td><td>Buy</td><td>Buy</td><td>■</td><td>15.00</td><td>15.00</td><td>0%</td><td>37%</td><td>0%</td><td>0%</td><td>0.66</td><td>0.64</td><td>22.7</td><td>8.8</td></tr><tr><td>Seazen H</td><td>2.4</td><td>2.1</td><td>Buy</td><td>Buy</td><td>■</td><td>3.30</td><td>3.30</td><td>0%</td><td>40%</td><td>0%</td><td>0%</td><td>0.30</td><td>0.29</td><td>12.7</td><td>10.2</td></tr><tr><td>Simple Average</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>29%</td><td>29%</td><td>-5%</td><td>13%</td><td>0.84</td><td>0.79</td><td>24.0</td><td>13.9</td></tr></table>

Source: Company data, UBSe. Date as of 12 May 2026.

# Equities

China Emerging

Real Estate

John Lam, CFA

Analyst

john-za.lam@UBS.com

+852-2971 6358

Vera Gong, CFA

Analyst

vera.gong@UBS.com

+852-2971 8950

Mark Leung

Analyst

mark.leung@UBS.com

+852-2971 8636

Ben Ho

Associate Analyst

ben.ho@UBS.com

+852-3712 2819

# WHAT IS DIFFERENT THIS TIME?

# Breaking the negative feedback loop

Over the past five years, there have been false alarms on property recovery, due to a weak job market, enterprises' difficulties to make profit, and rising supply from shadow inventory (vacant property). Since there is a long supply chain related to the property sector, the decline in property sales/price acts as a further drag on industrial enterprise (IE) demand/profitability, i.e. more layoffs and lower income expectations, and hence is negative to housing demand. This causes a negative feedback loop and might explain why IE profit has a good correlation with tier 1 Cities property price at 0.63 correlation. See Figure 2 - Figure 4, and our strategy note on A-share Q126 earnings review.

Figure 2: A strong correlation between tier 1 Cities property price and IE profit   
![](images/1d4a3d1bf5fd79b5eecf292b26afb9984d604d8e7cab25aa2b03e86697986465.jpg)

<details>
<summary>line</summary>

| Date   | IE profit monthly rolling 12m | Tier-1 Cities property price index |
|--------|-------------------------------|------------------------------------|
| Jan-13 | 500                           | 400                                |
| May-13 | 550                           | 450                                |
| Sep-13 | 570                           | 480                                |
| Jan-14 | 580                           | 500                                |
| May-14 | 590                           | 520                                |
| Sep-14 | 600                           | 550                                |
| Jan-15 | 580                           | 580                                |
| May-15 | 570                           | 600                                |
| Sep-15 | 560                           | 620                                |
| Jan-16 | 550                           | 650                                |
| May-16 | 570                           | 700                                |
| Sep-16 | 580                           | 750                                |
| Jan-17 | 560                           | 800                                |
| May-17 | 550                           | 820                                |
| Sep-17 | 540                           | 830                                |
| Jan-18 | 530                           | 840                                |
| May-18 | 520                           | 850                                |
| Sep-18 | 510                           | 860                                |
| Jan-19 | 500                           | 870                                |
| May-19 | 490                           | 880                                |
| Sep-19 | 480                           | 890                                |
| Jan-20 | 470                           | 900                                |
| May-20 | 460                           | 910                                |
| Sep-20 | 450                           | 920                                |
| Jan-21 | 440                           | 930                                |
| May-21 | 430                           | 940                                |
| Sep-21 | 420                           | 950                                |
| Jan-22 | 410                           | 960                                |
| May-22 | 400                           | 970                                |
| Sep-22 | 390                           | 980                                |
| Jan-23 | 380                           | 990                                |
| May-23 | 370                           | 1000                               |
| Sep-23 | 360                           | 990                                |
| Jan-24 | 350                           | 980                                |
| May-24 | 340                           | 970                                |
| Sep-24 | 330                           | 960                                |
| Jan-25 | 320                           | 950                                |
| May-25 | 310                           | 940                                |
| Sep-25 | 300                           | 930                                |
| Jan-26 | 290                           | 920                                |
</details>

Source: NBS, Centraline, UBS

Figure 3: PPI in China picked up in Mar 2026 for the first time since Sept 2022   
![](images/f1dbdb21c2e23e88b2d6d10d6e8c45c17c4a2dd754f3c2ffa61b833257c33db4.jpg)

<details>
<summary>line</summary>

| Date   | Tier-1 Cities property price index | PPI YoY RHS |
|--------|------------------------------------|-------------|
| May-26 | 600                                | 2.8%        |
</details>

Source: NBS, Centraline, UBS.

Figure 4: All A-share profit (excl. financials, Sinopec & Petro China) recorded 12% growth in Q126   
![](images/575bd74efaba104e11582d383b9cbdaf86590e4b77682946bdb4ee304549e7b0.jpg)

<details>
<summary>line</summary>

| Date       | A share excl. financials, Sinopec & Petro China (quarterly) YoY |
| ---------- | --------------------------------------------------------------- |
| 3/1/2013   | ~15%                                                            |
| 9/1/2013   | ~25%                                                            |
| 3/1/2014   | ~10%                                                            |
| 9/1/2014   | ~-5%                                                            |
| 3/1/2015   | ~-20%                                                           |
| 9/1/2015   | ~-10%                                                           |
| 3/1/2016   | ~50%                                                            |
| 9/1/2016   | ~40%                                                            |
| 3/1/2017   | ~60%                                                            |
| 9/1/2017   | ~30%                                                            |
| 3/1/2018   | ~-5%                                                            |
| 9/1/2018   | ~-20%                                                           |
| 3/1/2019   | ~-30%                                                           |
| 9/1/2019   | ~-25%                                                           |
| 3/1/2020   | ~-40%                                                           |
| 9/1/2020   | ~-10%                                                           |
| 3/1/2021   | ~60%                                                            |
| 9/1/2021   | ~20%                                                            |
| 3/1/2022   | ~-20%                                                           |
| 9/1/2022   | ~-30%                                                           |
| 3/1/2023   | ~-40%                                                           |
| 9/1/2023   | ~-50%                                                           |
| 3/1/2024   | ~-60%                                                           |
| 9/1/2024   | ~-40%                                                           |
| 3/1/2025   | ~-30%                                                           |
| 9/1/2025   | ~-25%                                                           |
| 3/1/2026   | ~-15%                                                           |
</details>

Source: NBS, Centraline, UBS

# Which sectors drive industrial profit? AI-related

However, it seems the negative feedback loop is unwinding this year. In 1Q26, industrial enterprise profit grew by 15% YoY with rising PPI (Figure 3). Breaking down the industrial enterprise by sectors, the strongest profit growth is in AI-related sectors, i.e. manufacture of computers, communication and other electronic equipment. This sub-sector accounts for 13% of industrial profit, and grew by 125% YoY in 1Q26. Next are non-ferrous metals smelting & pressing, and chemical materials & products, due to rise in commodity prices, capacity reduction and government anti-involution campaign. If we break down the 15% growth in industrial profit, 8.2ppt is contributed by computer, communication & other electronic equipment (i.e. AI-related), 5.2ppt is from non-ferrous metal smelting & pressing, and 2.8ppt is from chemical materials & products. In addition, in April 2026, export growth accelerated to 14% YoY, and shipments of tech exports expanded 0.5% MoM (Figure 6). The continued strength in tech exports likely signals that China is becoming increasingly integrated into the AI supply chain.

Figure 5: Computer, communication & other electronic equipment contributed 8.2ppt to Q126 total profit growth   
![](images/871a9753c75b5ccaf8e39074780bb996bb7c61dacb2d53af6ad38216e2e30b67.jpg)

<details>
<summary>bar</summary>

Q126 industrial enterprise profit YoY growth contribution (%)
| Category | Contribution (%) |
| :--- | :--- |
| Total profit | 15.5 |
| Non Ferrous Metal Smelting & Pressing | 5.21 |
| Chemical Material & Product | 2.81 |
| Computer, Communication & Other Electronic Equipment | 8.19 |
| Other | -0.71 |
</details>

Source: CEIC, UBS

Figure 6: Tech dominated recent export growth, as of April 2026   
![](images/5ed44b7e63d2825bba51052aa11a5f0ee476a30785ee2565fdb18dbb086b418c.jpg)

<details>
<summary>line</summary>

| Date     | Hi-tech | Autos | Other products |
| -------- | ------- | ----- | -------------- |
| 4/2026   | 143     | 160   | 100            |
</details>

Source: CEIC, UBS estimate

# Where are they based? Beijing and Shanghai

Furthermore, we look at the stock market to see which companies outperformed the most and where they are located. There are 514 stocks with over Rmb10bn market cap whose share prices have increased by over 50% in the past 12 months. Most of them are located in Beijing, Shanghai and Shenzhen, followed by Suzhou and Chengdu. This is due to more AI or related supply chain companies being located in Beijing and Shanghai, which echoes with stronger secondary transactions in Beijing and Shanghai.

Figure 7: Beijing had 43 listed companies of Rmb10bn+ market cap with one-year return over 50%, followed by 50 in Shanghai and 48 in Shenzhen   
![](images/3528ff8290b8dfeaf95a90c634b544a89e7d1df5046c386a80

[中间内容因长度限制已省略]

 legislation and does not provide banking and other financial services in Ukraine. UBS has not made, and will not make, any offer of the mentioned products to the public in Ukraine. No action has been taken to authorize an offer of the mentioned products to the public in Ukraine and the distribution of this document shall not constitute financial services for the purposes of the Law of Ukraine "On Financial Services and Financial Companies" dated 14 December 2021. Any offer of the mentioned products shall not constitute an investment advice, public offer, circulation, transfer, safekeeping, holding or custody of securities in the territory of Ukraine. Accordingly, nothing in this document or any other document, information or communication related to the mentioned products shall be interpreted as containing an offer, a public offer or invitation to offer or to a public offer, or solicitation of securities in the territory of Ukraine or investment advice under Ukrainian law. Electronic communication must not be considered as an offer to enter into an electronic agreement or other electronic instrument within the meaning of the Law of Ukraine "On Electronic Commerce" dated 3 September 2015. This document is strictly for private use by its holder and may not be passed on to third parties or otherwise publicly distributed. USA: Distributed to US persons only by UBS Financial Services Inc. or UBS LLC, sUBSidiaries of UBS AG. UBS Switzerland AG, UBS Europe SE, UBS Bank, S.A., UBS BB Corretora de Câmbio, Títulos e Valores Mobiliários S.A., UBS Asesores México, S.A. de C.V., UBS SuMi TRUST Wealth Management Co., Ltd., UBS Wealth Management Israel Ltd. and UBS Menkul Degerler AS are affiliates of UBS AG. UBS Financial Services Inc. accepts responsibility for the content of a report prepared by a non-US affiliate when it distributes reports to US persons. All transactions by a US person in the securities mentioned in this report should be effected through a US-registered broker dealer affiliated with UBS, and not through a non-US affiliate. The contents of this report have not been and will not be approved by any securities or investment authority in the United States or elsewhere. UBS Financial Services Inc. is not acting as a municipal advisor to any municipal entity or obligated person within the meaning of Section 15B of the Securities Exchange Act (the "Municipal Advisor Rule") and the opinions or views contained herein are not intended to be, and do not constitute, advice within the meaning of the Municipal Advisor Rule. For information on the ways in which UBS LLC manages conflicts and maintains independence of its UBS Global Research product; historical performance information; certain additional disclosures concerning UBS Global Research recommendations; and terms and conditions for certain third party data used in research report, please visit https://www.UBS.com/disclosures

© UBS 2026. The key symbol and UBS are among the registered and unregistered trademarks of UBS. All rights reserved.

# CS Wealth Management Disclaimer

This disclaimer must be read in conjunction with "Risk information" and "Important Information About Sustainable Investing Strategies" sections of the Global Wealth Management Disclaimer above. You receive this document in your capacity as a client of CS Wealth Management. Your personal data will be processed in accordance with the CS privacy statement accessible at your domicile through the official CS website https://www.credit-suisse.com. In order to provide you with marketing materials concerning our products and services, UBS Group AG and its sUBSidiaries may process your basic personal data (i.e. contact details such as name, e-mail address) until you notify us that you no longer wish to receive them. You can optout from receiving these materials at any time by informing your Relationship Manager.

Except as otherwise specified herein and/or depending on the local CS entity from which you are receiving this report, this report is distributed by UBS Switzerland AG, authorised and regulated by the Swiss Financial Market Supervisory Authority (FINMA). Saudi Arabia: This document is being distributed by CS Saudi Arabia I Part of UBS Group (CR Number 1010228645, NUN Number 7001515373), duly licensed and regulated by the Saudi Arabian Capital Market Authority pursuant to License Number 08104-37 dated 23/03/1429H corresponding to 21/03/2008AD. CS Saudi Arabia's principal place of business is at King Khaled Road, Laysen Valley, Building number 6, 12329-2376, Riyadh, Saudi Arabia. Website: https://www.credit-suisse.com/sa/en/cssa.html.

© UBS 2026. The key symbol and UBS are among the registered and unregistered trademarks of UBS. All rights reserved.

![](images/22fa7372c18df416231d3cab47f7061d207a1a80348758a18576a622de5a2071.jpg)
"""
