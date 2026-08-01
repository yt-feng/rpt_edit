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
# Weekend Healthcare Pulse: Is Japan the land of cheap executives? Not a sign of frugality and some undesirable consequence perhaps

Miki Sogi, Ph.D. +81 3 6777 6991 miki.sogi@bernsteinsg.com

Courtney Breen +1 917 344 8407 courtney.breen@bernsteinsg.com

Eve Burstein +1 917 344 8313 eve.burstein@bernsteinsg.com

Lee Hambright +1 917 344 8429 lee.hambright@bernsteinsg.com

Rebecca Liang, Ph.D. +852 2123 2656 rebecca.liang@bernsteinsg.com

Delphine Le Louet +33 1 42 13 92 93 delphine.le-louet@bernsteinsg.com

Susannah Ludwig +41 582 723 127 susannah.ludwig@bernsteinsg.com

Justin Smith +44 20 7762 5899 justin.smith@bernsteinsg.com

Lance Wilkes +1 917 344 8501 lance.wilkes@bernsteinsg.com

Jeffrey Walch, MD, Ph.D. +1 917 344 8613 jeffrey.walch@bernsteinsg.com

## SIGNIFICANT COMPENSATION GAP EXISTS BETWEEN JAPANESE EXECUTIVES AND THEIR US & EU PEERS. THERE ARE CONSEQUENCES

An investor arriving from the US, where the debate over CEO overpay rarely quiets down, cannot help but notice the opposite phenomenon in Japan: executives there are paid strikingly little relative to their global peers. A recent survey shows Japanese CEOs earn just a fraction of what their US and European counterparts take home, with the gap running 3-7x (Exhibit 1). Company size and profitability explain part of this, since US firms tend to be larger and more profitable in dollar terms. Yet, the scale alone falls well short of accounting for a gap this wide. Pharma makes the puzzle even more striking. It is one of the most globalized industries in the world, with Japanese, European, and US companies competing head-to-head for the innovations, therapeutic markets, talents, and capital. However, the executive compensation practices remain stubbornly local. Based on data we compiled across public pharmaceutical companies in Japan, Europe, and the US, executives at US/EU pharma companies earn roughly 6x their Japanese counterparts on average (Exhibit 2). In this report, we examine the structural and cultural drivers behind this disparity, along with early signs that Japanese companies are beginning to rework executive incentive structures to close the gap and, hopefully and most importantly, improve their performance.

EXHIBIT 1: Japanese CEO are paid substantially less than their US/EU peers  
Median CEO compensation (2023)  
![](images/0c01635eadfac0a66f8ef48df481eaa3c33414b535c6d5d73988c6dd5bef4301.jpg)  
Median of companies with revenue above JPY 1Tn Source: WTW analysis, Bernstein analysis

EXHIBIT 2: Japanese pharma CEOs are paid far less than their peers in the US and Europe  
![](images/ccb91a38b020e1f319e74c660f96b95ed744d603b5ff6126a7a0c527acbf1022.jpg)  
Lilly, Pfizer, Gilead, Amgen, Merck, BMS and Abbvie are covered by Breen, JNJ is covered by Lee, AstraZeneca, Novartis, GSK, Sanofi and Novo Nordisk are covered by Smith Source: Company reports, Bernstein analysis

## CULTURE, LABOR REGULATION AND MARKET DYNAMICS, AND LACK OF EQUITY-BASED COMPCONtribute TO THE DIFFERENCE IN CEO COMPENSATION

Culture plays a big role. Japanese corporations have traditionally rewarded tenure and organizational loyalty over individual output, a norm rooted in the seniority based employment system and the country's well known lifetime employment practice: many company employees, aka salary men, work for the same company through their career, \~40 years. Because executives are almost universally promoted from within, it becomes structurally difficult to pay someone dramatically differently in year 36 of service versus year 35 without upending internal pay norms built over decades. These dynamics are visible in the data: across CEOs in the US, EU, and Japan, Japanese pharma chiefs have spent an average of \~37 years at their company before taking the top job, versus just \~21 years for their global peers (Exhibit 3). That 16-year gap is not a rounding error, but rather reflects a fundamentally different path to the corner office, one built on internal progression rather than external hiring or rapid promotion, and it naturally compresses how much pay can deviate from the incumbent structure at any single step.

byproduct of the lifetime employment practice is limited external executive mobility in the labor market. Because career paths are largely internal, and it is difficult to dismiss an executive (or any employee for that matter), CEOs are rarely recruited externally, thus less need to pay premium to attract and retain leadership talents. As shown in Exhibit 3, for pharmaceutical executives, in the US and EU we can observe a good mix of internal promotion and external hires, while Japanese CEOs (except Takeda) are universally long-time veterans within the same organization.

Lack of equity-based compensation. Historically, Japanese executive remuneration consisted mainly of fixed cash salary, with performance-based pay, and stock options were rarely used. In the US, equity awards (stock options and RSUs, Restricted Stock Unit, a form of employee compensation, restricted through a vesting period that may last several years), performance shares) make up the majority of CEO pay.

Years with Company    Years as CEO    US/EU average    Japan average

EXHIBIT 3: Japanese pharma CEOs typically stay in the same company for their life  
![](images/8e660b2caf2dba00075c0a110bc2ee284e357a8c7e91ee9b77443cebf1542636.jpg)  
Source: Company reports, Bernstein analysis

## JAPANESE EXECUTIVES HAVE BEEN COMPENSATED WITH FAR LESS EQUITY THAN THEIR US PEERS AS THERE IS LITTLE INSTITUTIONAL PRESSURE FOR THE JAPANESE CORPORATE TO ADOPT THE US PRACTICE

In the US, equity has become the dominant form of executive pay, but that was historically not always the case: the shift away from cash and bonus took multiple decades to unfold (Exhibit 4). No single factor drove the change, but rather it was a product of corporate governance reform, shifting tax incentives, and evolving accounting rules that together made equity-based pay both more attractive to the companies and recipients and easier to justify to their shareholders. The underlying logic is straightforward: paying executives in shares ties their financial incentives directly to the outcomes shareholders care about, thus a cleaner alignment mechanism than cash bonuses tied to short term targets (e.g., this year's financial and operational achievement). That logic has since hardened into formal policy. Many US pharma companies now mandate a minimum equity holding for executives, typically expressed as a multiple of annual base salary. Eli Lilly is a good example, where the CEO is required to hold stock worth 12x annual base salary.

Japanese pharma CEOs still take home most of their pay in cash and bonus, a sharp contrast to their US counterparts (Exhibit 5). It can partly be explained by structural rather than cultural: Japanese public companies have long operated within complex cross-shareholding networks, arrangements that were explicitly designed to ensure the job security of executives and shield them from the equity market discipline. Under that system, a manager's job security rested on goodwill from peer companies and banks rather than on an activist shareholder base who holds the management accountable. With little institutional pressure to hold personal equity or tie personal wealth to the share price, there was simply no structural incentive pushing Japanese executives toward equity based pay the way there was in the US.

EXHIBIT 4: US CEO pay has evolved from mostly cash to mostly equity  
CEO pay structure of largest 50 firms in the US  
![](images/f1c1df64356a3b05d7bf5f398b42085e72b5396e31918f6a21864b8c1715a943.jpg)  
Source: Frydman and Jenter, published on NBER.org

EXHIBIT 5: Japanese CEOs still gets most of their compensation in non-stock form  
![](images/5bf4acf554684d8752518360221d13a26271f3ba9f213639c68659c1dbfa92d5.jpg)  
Source: Company reports, Bernstein analysis

Shionogi

## MANAGEMENT OWNING EQUITY IS GOOD FOR CORPORATE AND SHARE PERFORMANCE. JAPAN IS SLOWLY BUT SURELY MOVING IN THE RIGHT DIRECTION, AND WE WANT MORE

Management not having their wealth tied to stock is suboptimal for shareholders. The salary & bonus-based compensation scheme does incentivize Japanese executives to drive accounting metrics. However, multiple researches have shown Japanese top managers historically had little financial incentive to maximize shareholder wealth, as their wealth will not go up when the stock performance is good, and they receive little punishment for poor results. In addition, since the bigger firms tend to pay more under salary & bonus-based schemes, Japanese executives had incentives to grow the firm size (i.e., topline and headcounts), which benefits managerial prestige rather than to raise return on equity. Intuitively, this is not a great alignment of executive's interest and shareholders'. For companies that operate globally, such as Japan pharmaceutical companies, an extra problem will emerge when these companies hire US or EU nationals as executives in Japan or elsewhere. We have seen non-Japanese non-CEO executives receive higher pay than CEOs at multiple Japanese pharma companies. The awkwardness does not stop there: since the US executives' pay follows the US compensation structure, it has created situations where an employee who owns the most shares only influences a division within a company (e.g., the US commercial org, Exhibit 6). One way of solving this issue is to grant more shares to the Japanese executives and require them to hold more equity ownership as in the US.

## The government has been pushing reforms to increase

company executives' equity ownership. Japan's governance reform push traces back to the Stewardship Code in 2014 and the Corporate Governance Code in 2015, both part of the Abe administration's broader effort to lift capital efficiency and profitability across corporate Japan. Subsequent revisions in 2018 and 2021 went further moving the framework from broad principles toward more prescriptive rules for Prime Market listed companies: explicitly recommending CEO succession planning, independent remuneration committees, and closer links between pay and shareholder value. The Ministry of Economy, Trade and Industry, METI, has reinforced this from the policy side, repeatedly updating its guidebook on board members' incentive plans since 2017 to push companies toward stock-based and performance-linked compensation as a lever for bolder, faster decision-making.

The CEO equity incentive has been increasing. Data suggest that the equity as a form of compensation is increasing (Exhibit 8), but at this moment the percentage of stock based incentives is still considerably lower than US/EU. Going forward, more equity ownership should bring executive incentives to be more aligned with shareholders.

EXHIBIT 6: Japan pharmaceutical companies typically pay more and in different ways to their US executives

CEO and US manager salary

![](images/b8cf76602bbbe9de3cd662307e4295b15597cb09eedae83b8c677c79620198bc.jpg)  
\*Total comp, cash and non cash

Highest paid (per disclosed information) US manager: Daiichi Sakyo-Head of global oncology business/Head of oncology business unit; Shionogi-SVP, R&D supervisory unit; Eisai: VP/Chief clinical officer
Source: Company reports, Bernstein analysis

## EXHIBIT 7: Executives mentioned in Exhibit 6

Daiichi Sankyo

Hiroyuki Okuzawa Representative Director President & CEO

Joseph Kenneth Keller  
Director  
Head of Global Oncology Business  
Head of Oncology Business Unit

![](images/df81f34118d5b40f82b3579f9b0692aa11de1ebf425e76108d895a7726d26719.jpg)  
Isao Teshirogi (CEO) John Keller Senior executive officer SVP, R&D supervisory unit  
Haruo Naito  
Representative Corporate Officer and CEO  
Lynn Kramer  
Vice President  
Chief Clinical Officer  
Source: Company reports, Bernstein analysis

EXHIBIT 8: Japan CEO variable compensation is growing  
![](images/d0642a0df1a999b2d20ea06ab8b7eae971100275c7b44194edf65a06fee9ea77.jpg)  
Source: Hideaki et al, RIETI, Bernstein analysis

## BERNSTEIN TICKER TABLE

<table><tr><td rowspan="2">Ticker</td><td colspan="4">30 Jul 2026</td><td rowspan="2">TTMRel.</td><td colspan="4">Reported EPS</td><td colspan="3">Reported P/E (x)</td></tr><tr><td>Rating</td><td>Cur</td><td>Closing Price</td><td>Price Target</td><td>Cur</td><td>2025A</td><td>2026E</td><td>2027E</td><td>2025A</td><td>2026E</td><td>2027E</td></tr><tr><td>4503.JP (Astellas)</td><td>M</td><td>JPY</td><td>2,287.00</td><td>2,200.00</td><td>16.3%</td><td>JPY</td><td>162.77</td><td>170.69</td><td>171.70</td><td>14.1</td><td>13.4</td><td>13.3</td></tr><tr><td>4578.JP (Otsuka)</td><td>M</td><td>JPY</td><td>11,305</td><td>11,600</td><td>18.9%</td><td>JPY</td><td>685.06</td><td>582.89</td><td>634.28</td><td>16.5</td><td>19.4</td><td>17.8</td></tr><tr><td>4568.JP (Daiichi Sankyo)</td><td>O</td><td>JPY</td><td>2,889.00</td><td>4,500.00</td><td>(58.3)%</td><td>JPY</td><td>140.37</td><td>152.26</td><td>216.35</td><td>20.6</td><td>19.0</td><td>13.4</td></tr><tr><td>4502.JP (Takeda)</td><td>O</td><td>JPY</td><td>5,718.00</td><td>6,900.00</td><td>(4.3)%</td><td>JPY</td><td>517.00</td><td>483.65</td><td>523.12</td><td>11.1</td><td>11.8</td><td>10.9</td></tr><tr><td>4519.JP (Chugai)</td><td>O</td><td>JPY</td><td>7,069.00</td><td>9,700.00</td><td>(41.0)%</td><td>JPY</td><td>263.73</td><td>317.24</td><td>370.07</td><td>26.8</td><td>22.3</td><td>19.1</td></tr><tr><td>4507.JP (Shionogi)</td><td>M</td><td>JPY</td><td>3,041.00</td><td>3,000.00</td><td>(17.1)%</td><td>JPY</td><td>241.11</td><td>247.55</td><td>264.99</td><td>12.6</td><td>12.3</td><td>11.5</td></tr><tr><td>4523.JP (Eisai)</td><td>O</td><td>JPY</td><td>5,031.00</td><td>5,300.00</td><td>(17.6)%</td><td>JPY</td><td>136.78</td><td>195.67</td><td>231.26</td><td>36.8</td><td>25.7</td><td>21.8</td></tr><tr><td>JPL</td><td></td><td></td><td>2,570.52</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

O - Outperform, M - Market-Perform, U - Underperform, NR - Not Rated, CS - Coverage Suspended

4502.JP estimate is Adjusted EPS; 4502.JP valuation is Adjusted P/E (x);

Source: Bloomberg, Bernstein estimates and analysis.

## I. REQUIRED DISCLOSURES

References to "Bernstein" or the "Firm" in these disclosures relate to the following entities: Bernstein Institutional Services LLC (April 1, 2024 onwards), Bernstein & Co., LLC (pre April 1, 2024), Bernstein Autonomous LLP, BSG France S.A. (April 1, 2024 onwards), Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited, Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社) and analysts employed by SG Africa Technologies & Services to produce Bernstein under a Global Services Agreement in place between Bernstein and SG.

Bernstein is part of a joint venture between SG (SG) and AllianceBernstein, L.P. (AB). Unless specifically noted otherwise, for purposes of these disclosures, references to Bernstein's “affiliates” relate to both SG and AB and their respective affiliates.

## VALUATION METHODOLOGY

This research publication covers six or more companies. For valuation methodology and other company disclosures: Please visit: https://bernstein-autonomous.bluematrix.com/sellside/Disclosures.action.

Or, you can also write to the Director of Compliance, Bernstein Institutional Services LLC, 245 Park Avenue, New York, NY 10167.

## RISKS

This research publication covers six or more companies. For risks and other company disclosures:
Please visit: https://bernstein-autonomous.bluematrix.com/sellside/Disclosures.action.
Or, you can also write to the Director of Compliance, Bernstein Institutional Services LLC, 245 Park Avenue, New York, NY 10167.

[中间内容因长度限制已省略]

e you of any change in the reported information or in the opinions herein.

Any references to SG herein are purely factual, based upon publicly available information, and included for comparative purposes only. They do not constitute an opinion or recommendation with respect to the securities of SG.

This publication was prepared and issued by the entity referred to herein for distribution to eligible counterparties or professional clients. The information in this report is intended for general circulation and does not constitute an offer to buy or sell any security, investment, legal or tax advice nor a personal recommendation, as defined by any of the aforementioned regulators. It does not take into account the particular investment objectives, financial situations, or needs of individual investors. The report has not been reviewed by any of the aforementioned regulators and does not represent any official recommendation from the aforementioned regulators. The investments referred to herein may not be suitable for you. Investors must make their own investment decisions in consultation with advice sought from a financial adviser regarding the suitability of the investment product, taking into account the specific investment objectives, financial situation or particular needs of any recipient of the recommendation, before the recipient makes a commitment to purchase the investment product.

The analysis contained herein is based on numerous assumptions. Different assumptions could result in materially different results. The information in this report does not constitute, or form part of, any offer to sell or issue, or any offer to purchase or subscribe for shares, or to induce engagement in any other investment activity. The value of any securities or financial instruments mentioned in this report may fluctuate subject to market conditions. Information about past performance of an investment is not necessarily a guide to, indicative of, or assurance of future performance. Estimates of future performance mentioned by the research analyst in this report are based on assumptions that may not be realized due to unforeseen factors like market volatility/fluctuation. In relation to securities or financial instruments denominated in a foreign currency other than the clients' home currency, movements in exchange rates will have an effect on the value, either favorable or unfavorable. Before acting on any recommendations in this report, recipients should consider the appropriateness of investing in the subject securities or financial instruments mentioned in this report and, if necessary, seek independent professional advice.

The securities described herein may not be eligible for sale in all jurisdictions or to certain categories of investors where that permission profile is not consistent with the licenses held by the entities noted herein. This document is for distribution only as may be permitted by law. It is not directed to, or intended for distribution to or use by, any person or entity who is a citizen or resident of or located in any locality, state, country or other jurisdiction where such distribution, publication, availability or use would be contrary to law or regulation or would subject the entities noted herein to any regulation or licensing requirement within such jurisdiction.

Source: Bloomberg Index Services Limited. BLOOMBERG® is a trademark and service mark of Bloomberg Finance L.P. and its affiliates (collectively “Bloomberg”). Bloomberg or Bloomberg’s licensors own all proprietary rights in the Bloomberg Indices. Neither Bloomberg nor Bloomberg’s licensors approves or endorses this material, or guarantees the accuracy or completeness of any information herein, or makes any warranty, express or implied, as to the results to be obtained therefrom and, to the maximum extent allowed by law, neither shall have any liability or responsibility for injury or damages arising in connection therewith.

No part of this material may be reproduced, distributed or transmitted or otherwise made available without prior consent of the entities noted herein. Copyright Bernstein Institutional Services LLC Bernstein Autonomous LLP, BSG France S.A., Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited and Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社). All rights reserved. The trademarks and service marks contained herein are the property of their respective owners. Any unauthorized use or disclosure is strictly prohibited. The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands.
"""
