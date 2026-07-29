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
Asian Autos

# Asian Autos: BYD's Kei-car BEV ‘Racco’ arrives - can it make a meaningful impact on Japan's auto market?

![](images/26f5fc7d11772966aa2b8aac91599a7c54429c5ae7127ca03a0f4251b33cb4a5.jpg)

Masahiro Akita

+81 3 6777 6998

masahiro.akita@bernsteinsg.com

![](images/a45b6251c36b46afad6154883d44d301d655ab58e6f9e79657d4278cd31a3842.jpg)

Eunice Lee, CFA

+852 2123 2606

eunice.lee@bernsteinsg.com

![](images/a8d8c4807ea4d312a54ffecc3a68bee6dbb9412b23228fd9b835eb0a8e089721.jpg)

Tomohiro Kashimoto

+81 3 6777 6975

tomohiro.kashimoto@bernsteinsg.com

![](images/249c383fe8c3557164c64f052a74c0d6ab60af347b7967fb7bacf8c6d3a68bed.jpg)

Seunghyeok Kim

+81 3 6777 6974

seunghyeok.kim@bernsteinsg.com

![](images/8d295fd8af4d7e17067cbff86d3249697db8f2a6933fd1a5d9a4593c147d87a9.jpg)

Ethan Xu

+852 2123 2634

ethan.xu@bernsteinsg.com

On July 28, BYD launched the Racco, its first Kei-car BEV in Japan. After subsidies, the model is priced <JPY 2 mn, making it one of the most competitively priced BEVs in the market, although BYD adopted a more cautious pricing strategy than we had anticipated. The company is targeting annual sales of 10K units. With 2026 increasingly viewed as a potential inflection point for BEV adoption in Japan, the launch of the Racco could mark an important development. In this report, we revisit the key question; how significantly could Racco reshape Japan's auto landscape, and could it help accelerate the EV transition?

BYD's ‘Racco’ starts at JPY 1,995k after subsidies: BYD's Racco is the company's first Kei-car BEV developed specifically for Japan and is positioned in the highly popular super-height wagon (SHW) segment. The model is offered in three grades - 200, 300 Plus, and 300 Premium - with prices ranging from JPY 2,145k to JPY 2,497k. After applying the JPY 150k CEV subsidy, the entry-grade Racco 200 is available at a purchase price of JPY 1,995k, making it one of the most competitively priced BEVs in Japan. The Racco offers a WLTC driving range of 210 km for the 200 grade and up to 320 km for the 300 Plus and 300 Premium, while also featuring a wide range of user-friendly features.

Japan's Kei-car market, accounting for \~40% of total sales: Japan's Kei-car market accounts for 40% of vehicle sales, supported by favorable tax treatment and ownership costs. Despite Japan's auto demand shrinking to below 5 mn units, Kei-car demand has remained resilient at around 1.7 mn units annually. The market is dominated by Suzuki and Daihatsu, which together account for nearly 70% of sales, while the SHW segment, where BYD's Racco is positioned, represents the largest category.

2026 increasingly seen as a potential inflection point for BEV adoption in Japan: Japan's BEV adoption remains low, but new model launches and enhanced government subsidies are increasingly positioning 2026 as a potential inflection point. The number of Kei-car BEV models in Japan is set to more than double in 2026 vs 2025. Against this backdrop, the BYD Racco is priced more than $10\%$ below existing Kei-car BEVs on average despite being positioned in the larger SHW segment. Combined with a descent driving range, we believe the model is well positioned for market acceptance.

Can BYD Racco make a meaningful impact on Japan's auto market?: BYD's presence in Japan remains limited, with only 3.7k units sold in 2025. While we believe its entry into Japan's Kei-car market, the country's most price-sensitive segment, is strategically sound, achieving its 10k-unit sales target would raise its overall/Kei-car market share to 0.3%/0.6%. The Racco's competitive pricing, spacious SHW packaging, and EV-specific advantages should help attract customers considering models such as the Honda N-BOX, Suzuki Spacia, and Daihatsu Tanto/Move, while also supporting broader BEV adoption over time. That said, we do not expect the Racco to materially disrupt the market in the near term, given Japanese consumers' preference for domestic brands and BYD's limited sales and service network. However, given the importance of the N-BOX, Japan's best-selling model, to Honda's domestic sales, successful market penetration by the Racco could be slightly negative for Honda.

## BERNSTEIN TICKER TABLE

<table><tr><td rowspan="2"></td><td colspan="4">28 Jul 2026</td><td rowspan="2">TTMRel.</td><td colspan="4">Reported EPS</td><td colspan="3">Reported P/E (x)</td></tr><tr><td>Rating</td><td>Cur</td><td>Closing Price</td><td>Price Target</td><td>Cur</td><td>2025A</td><td>2026E</td><td>2027E</td><td>2025A</td><td>2026E</td><td>2027E</td></tr><tr><td>Ticker</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>7269.JP (Suzuki)</td><td>O</td><td>JPY</td><td>2,078.50</td><td>2,550.00</td><td>23.4%</td><td>JPY</td><td>227.69</td><td>234.71</td><td>255.99</td><td>9.1</td><td>8.9</td><td>8.1</td></tr><tr><td>7203.JP (Toyota)</td><td>O</td><td>JPY</td><td>3,008.00</td><td>4,200.00</td><td>7.2%</td><td>JPY</td><td>295.25</td><td>308.93</td><td>367.29</td><td>10.2</td><td>9.7</td><td>8.2</td></tr><tr><td>7267.JP (Honda)</td><td>M</td><td>JPY</td><td>1,612.00</td><td>1,300.00</td><td>(2.8)%</td><td>JPY</td><td>(106.06)</td><td>161.84</td><td>147.24</td><td>(15.2)</td><td>10.0</td><td>10.9</td></tr><tr><td>7270.JP (Subaru)</td><td>U</td><td>JPY</td><td>2,680.00</td><td>2,350.00</td><td>(6.8)%</td><td>JPY</td><td>125.50</td><td>222.96</td><td>249.75</td><td>21.4</td><td>12.0</td><td>10.7</td></tr><tr><td>7201.JP (Nissan)</td><td>U</td><td>JPY</td><td>337.40</td><td>350.00</td><td>2.2%</td><td>JPY</td><td>(152.58)</td><td>4.78</td><td>53.06</td><td>(2.2)</td><td>70.5</td><td>6.4</td></tr><tr><td>7261.JP (Mazda)</td><td>U</td><td>JPY</td><td>1,182.50</td><td>1,000.00</td><td>23.1%</td><td>JPY</td><td>55.64</td><td>116.61</td><td>142.17</td><td>21.3</td><td>10.1</td><td>8.3</td></tr><tr><td>1211.HK (BYD)</td><td>O</td><td>HKD</td><td>90.00</td><td>136.00</td><td>(29.7)%</td><td>CNY</td><td>3.58</td><td>4.90</td><td>6.90</td><td>21.7</td><td>15.8</td><td>11.3</td></tr><tr><td>002594.CH (BYD)</td><td>O</td><td>CNY</td><td>93.35</td><td>124.00</td><td>(16.9)%</td><td>CNY</td><td>3.58</td><td>4.90</td><td>6.90</td><td>26.1</td><td>19.0</td><td>13.5</td></tr><tr><td>JPL</td><td></td><td></td><td>--</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>ASIAX</td><td></td><td></td><td>--</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

O - Outperform, M - Market-Perform, U - Underperform, NR - Not Rated, CS - Coverage Suspended

Source: Bloomberg, Bernstein estimates and analysis.

## INVESTMENT IMPLICATIONS

We rate Suzuki Outperform with a price target of JPY 2,550.00.

We rate Toyota Outperform with a price target of JPY 4,200.00.

We rate Honda Market-Perform with a price target of JPY 1,300.00.

We rate Subaru Underperform with a price target of JPY 2,350.00.

We rate Nissan Underperform with a price target of JPY 350.00.

We rate Mazda Underperform with a price target of JPY 1,000.00.

We rate BYD Outperform with price targets for 1211.HK at HK\$136.00 and for 002594.CH at RMB 124.00.

## DETAILS

## BYD'S KEI-CAR BEV 'RACCO' ARRIVES - CAN IT MAKE A MEANINGFUL IMPACT ON JAPAN'S AUTO MARKET?

On July 28, BYD launched the Racco, its first Kei-car BEV in Japan (Exhibit 1). Priced at a highly attractive sub-JPY 2 million level after government subsidies, the model offers a compelling value proposition for Japanese consumers, although BYD adopted a more cautious pricing strategy than we had originally anticipated. BYD has set a sales target of 10,000 units for the Racco. With 2026 increasingly viewed as a potential inflection point for BEV adoption in Japan, the launch of the Racco could represent an important development for the industry. In this report, we revisit the key question: how significant an impact could BYD's new Kei-car have on Japan's automotive landscape, and could it help accelerate the country's transition to EVs?

## BYD'S RACCO STARTS AT JPY 1,995K MN AFTER SUBSIDIES

BYD's Racco is the company's first Kei-car BEV developed specifically for the Japanese market, marking an important milestone in its efforts to strengthen its presence in Japan. Importantly, the model is positioned within the super-height wagon segment, the largest and most popular category in Japan's Kei-car market, where practicality, spacious interiors, and family-oriented features have historically driven strong demand. The Racco is offered in three grades - 200, 300 Plus, and 300 Premium - with prices ranging from JPY 2,145k to JPY 2,497k. Following the application of the JPY 150k government subsidy available for the model, the entry-grade version is expected to be priced at an effective JPY 1,995k for consumers, making it one of the most attractively priced BEVs in the Japanese market (Exhibit 2).

The entry-grade 200 is equipped with a 22.4 kWh Blade Battery delivering a WLTC range of 210 km, while the 300 Plus and 300 Premium feature a larger 35.84 kWh battery providing up to 320 km of WLTC range. All variants are powered by a front-mounted electric motor producing 47 kW (64 PS) and 160 Nm of torque and support both AC and DC charging. In addition to its battery technology, BYD has equipped the Racco with a relatively comprehensive feature set for the Kei-car market, including powered sliding doors with hands-free operation, a digital instrument cluster, touchscreen infotainment system, Apple CarPlay and Android Auto connectivity, NFC smartphone key functionality, battery pre-heating, V2L capability on higher-grade models, and a variety of family-oriented convenience features.

The vehicle also incorporates a suite of ADAS technologies, including autonomous emergency braking, forward collision warning, lane-keeping assistance, adaptive cruise control, and other ADAS functions designed to enhance everyday usability and safety. Measuring 3,395 mm in length, 1,475 mm in width, and 1,800 mm in height, the cabin accommodates four passengers and offers a highly flexible interior layout, with cargo capacity expanding to a substantial volume when the rear seats are folded. Overall, BYD appears to be positioning the Racco as a value-for-money BEV, with its highly attractive pricing likely to be the model's key differentiator. Coupled with a long driving range, advanced connectivity, comprehensive safety features, and strong everyday practicality, the Racco offers a compelling package for cost-conscious Japanese consumers, in our view.

## EXHIBIT 1: BYD'S Racco starts at JPY 1,995k after subsidies

![](images/cb383da7c7512529d3579f25a269c732cc51d93e190d6e44e5b82dc51333c98f.jpg)

Source: Company website

EXHIBIT 2: The Racco is offered in three trims - the 200, 300 Plus, and 300 Premium

<table><tr><td>OEM</td><td>BYD</td><td>BYD</td><td>BYD</td></tr><tr><td>Model</td><td>RACCO</td><td>RACCO</td><td>RACCO</td></tr><tr><td>Edition</td><td>200</td><td>300 Plus</td><td>300 Premium</td></tr><tr><td>Model type</td><td>Super-Height Wagon</td><td>Super-Height Wagon</td><td>Super-Height Wagon</td></tr><tr><td>Sales price (JPY k)</td><td>2,145</td><td>2,398</td><td>2,497</td></tr><tr><td>L x W x H (m)</td><td>3.4 x 1.5 x 1.8</td><td>3.4 x 1.5 x 1.8</td><td>3.4 x 1.5 x 1.8</td></tr><tr><td>Cubic meter (m3)</td><td>9.0</td><td>9.0</td><td>9.0</td></tr><tr><td>Vehicle weight (kg)</td><td>1,160</td><td>1,220</td><td>1,230</td></tr><tr><td>Fast charging time (min)</td><td>30</td><td>30</td><td>30</td></tr><tr><td>EV Range (km)</td><td>210</td><td>320</td><td>320</td></tr><tr><td>Battery capacity (kWh)</td><td>22.4</td><td>35.8</td><td>35.8</td></tr><tr><td>Electric Mileage (km/kWh)</td><td>9.4</td><td>8.9</td><td>8.9</td></tr><tr><td>Price (JPY k) / m3</td><td>238.3</td><td>266.4</td><td>277.4</td></tr><tr><td>Price (JPY k)/ Electric Mileage</td><td>228.8</td><td>268.6</td><td>279.7</td></tr></table>

Source: BYD, Bernstein analysis

## JAPAN'S KEI-CAR MARKET, ACCOUNTING FOR \~40% OF TOTAL AUTO SALES

## Japan's unique Kei-car standard

The Kei-car standard that BYD's Racco complies with is a unique vehicle category in Japan, characterized by strict restrictions on vehicle dimensions and powertrain output (Exhibit 3). Specifically, these cars must have an engine displacement of 660 cc or less, a length of no more than 3.4 meters, a width within 1.48 meters, and a height up to 2.0 meters. This classification positions Kei-cars as smaller and more economical compared to regular passenger vehicles. Historically, the standard was established in 1949, initially limiting engine displacement to 250 cc, but it has since expanded to the current 660 cc limit. Due to their compact size and fuel efficiency, Kei-cars are highly convenient for urban use, and they benefit from favorable tax treatments—such as lower acquisition tax, vehicle tax, and weight tax—making their ownership and maintenance costs significantly cheaper than those of standard cars. Additionally, insurance premiums and inspection fees for Kei-cars tend to be relatively low. Overall, the Kei-car standard is well integrated into Japan's transportation environment and economic conditions, contributing to reduced environmental impact and alleviating traffic congestion.

The Kei-car market, originally centered around small passenger models such as compact sedans and hatchbacks, as well as commercial models like trucks and vans—reflecting its roots in affordability and functionality—has evolved through gradual expansions in engine displacement and dimension regulations, resulting in a wide variety of model segments available today (Exhibit 4, Exhibit 5). However, in recent years, the Japanese Kei-car market has offered a wide range of segment models—comparable to those in the global automobile market—including more spacious height wagons and super-height wagons that reflect consumer needs in Japan, SUVs with added value such as enhanced off-road capability, and sports models focused on driving performance and design for niche customer segments.

EXHIBIT 3: The Kei-car standard sets limits on vehicle dimensions and powertrain output, offering owners favorable benefits in ownership and maintenance costs

<table><tr><td>Type</td><td>Kei-car (minicar)</td><td>Registration car (Normal PV)</td></tr><tr><td>Size</td><td>Length ≤ 3.4m, Width ≤ 1.48m, Height ≤ 2.0 m</td><td>Compact car: Width ≤ 1.7 m, Height ≤ 3.8m, no length limitStandard car: Height ≤ 3.8m, no width/length limit</td></tr><tr><td>Engine displacement</td><td>Up to 660 cc</td><td>Compact car: up to 2,000 ccStandard car: no upper limit</td></tr><tr><td>Power output capacity*</td><td>Up to 64 hp (47kW)</td><td>No upper limit</td></tr><tr><td>Seating capacity</td><td>Up to 4 occupants</td><td>Up to 10 occupants</td></tr><tr><td>Annual automobile tax</td><td>JPY 10,800 (private use)</td><td>&gt;JPY 25,000 (depending on the engine displacement)</td></tr><tr><td>Weight tax*</td><td>JPY 6,600 - 8,800</td><td>JPY 8,200 - 75,600</td></tr><tr><td>Environmental performance tax</td><td>Up to 2% of taxable purchase price</td><td>Up to 3% of taxable purchase price</td></tr><tr><td>Highway toll rates</td><td>~20% discount vs. registered vehicle</td><td>Standard rates</td></tr><tr><td>License plate</td><td>Yellow</td><td>Green</td></tr></table>

Note: Power output limits are self imposed by each manufacturer.  
Source: Keikenkyo, Zenkeijikyo, Ministry of Land, Infrastructure, Transport and Tourism of Japan, AIRIA, Bernstein analysis

EXHIBIT 4: Diverse segments in the Kei-car market #1

<table><tr><td></td><td>Super-height wagon</td><td>Height wagon</td><td>SUV</td></tr><tr><td>Image</td><td><img src="images/a849d016d8a78f6a184468b500c4001be9b25174be3e5fe88521df086f15fc11.jpg"/>N-

[中间内容因长度限制已省略]

e you of any change in the reported information or in the opinions herein.

Any references to SG herein are purely factual, based upon publicly available information, and included for comparative purposes only. They do not constitute an opinion or recommendation with respect to the securities of SG.

This publication was prepared and issued by the entity referred to herein for distribution to eligible counterparties or professional clients. The information in this report is intended for general circulation and does not constitute an offer to buy or sell any security, investment, legal or tax advice nor a personal recommendation, as defined by any of the aforementioned regulators. It does not take into account the particular investment objectives, financial situations, or needs of individual investors. The report has not been reviewed by any of the aforementioned regulators and does not represent any official recommendation from the aforementioned regulators. The investments referred to herein may not be suitable for you. Investors must make their own investment decisions in consultation with advice sought from a financial adviser regarding the suitability of the investment product, taking into account the specific investment objectives, financial situation or particular needs of any recipient of the recommendation, before the recipient makes a commitment to purchase the investment product.

The analysis contained herein is based on numerous assumptions. Different assumptions could result in materially different results. The information in this report does not constitute, or form part of, any offer to sell or issue, or any offer to purchase or subscribe for shares, or to induce engagement in any other investment activity. The value of any securities or financial instruments mentioned in this report may fluctuate subject to market conditions. Information about past performance of an investment is not necessarily a guide to, indicative of, or assurance of future performance. Estimates of future performance mentioned by the research analyst in this report are based on assumptions that may not be realized due to unforeseen factors like market volatility/fluctuation. In relation to securities or financial instruments denominated in a foreign currency other than the clients' home currency, movements in exchange rates will have an effect on the value, either favorable or unfavorable. Before acting on any recommendations in this report, recipients should consider the appropriateness of investing in the subject securities or financial instruments mentioned in this report and, if necessary, seek independent professional advice.

The securities described herein may not be eligible for sale in all jurisdictions or to certain categories of investors where that permission profile is not consistent with the licenses held by the entities noted herein. This document is for distribution only as may be permitted by law. It is not directed to, or intended for distribution to or use by, any person or entity who is a citizen or resident of or located in any locality, state, country or other jurisdiction where such distribution, publication, availability or use would be contrary to law or regulation or would subject the entities noted herein to any regulation or licensing requirement within such jurisdiction.

Source: Bloomberg Index Services Limited. BLOOMBERG® is a trademark and service mark of Bloomberg Finance L.P. and its affiliates (collectively “Bloomberg”). Bloomberg or Bloomberg’s licensors own all proprietary rights in the Bloomberg Indices. Neither Bloomberg nor Bloomberg’s licensors approves or endorses this material, or guarantees the accuracy or completeness of any information herein, or makes any warranty, express or implied, as to the results to be obtained therefrom and, to the maximum extent allowed by law, neither shall have any liability or responsibility for injury or damages arising in connection therewith.

No part of this material may be reproduced, distributed or transmitted or otherwise made available without prior consent of the entities noted herein. Copyright Bernstein Institutional Services LLC Bernstein Autonomous LLP, BSG France S.A., Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited and Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社). All rights reserved. The trademarks and service marks contained herein are the property of their respective owners. Any unauthorized use or disclosure is strictly prohibited. The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands.
"""
