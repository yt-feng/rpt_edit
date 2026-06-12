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
## Oil Markets Weekly

The first thousand miles

The largest supply disruption on record has produced a surprisingly unremarkable price chart. Since the start of the conflict, Brent has averaged just \$101, closely tracking the price path implied by our framework in early March.

At the time, we concluded that only two forces could plausibly explain such a restrained outcome. Either demand losses, alongside inventory drawdowns, could prove large enough to rebalance the market outright. Or the adjustment could move down the barrel, away from crude and into refined products (Down the barrel, 8 May 2026). Under that scenario, crude prices could hover near \$100/bbl while scarcity shows up instead in gasoline, diesel, and jet fuel prices. The shock would be expressed not through materially higher flat crude prices, but through widening product cracks and sharply higher refined product prices. In March, we viewed the latter as the more likely adjustment mechanism.

The first part of that framework proved correct. The second did not. Crude prices followed the expected path. Product markets did not. After an initial spike, gasoline, diesel, and jet fuel prices have reset lower, while refining margins have narrowed rather than widened (Figure 1).

Figure 1: US petroleum product price change from February 27 to June 8  
![](images/08659c5410c21080396740868b70630d4441b27aac0f7702665f666fee82ab89.jpg)

<details>
<summary>line chart</summary>

| Date     | Jet  | Gasoline | Diesel | Naphtha |
|----------|------|----------|--------|---------|
| 27-Feb   | 0%   | 0%       | 0%     | 0%      |
| 6-Mar    | 65%  | 30%      | 40%    | 45%     |
| 13-Mar   | 68%  | 45%      | 50%    | 60%     |
| 20-Mar   | 95%  | 55%      | 70%    | 75%     |
| 27-Mar   | 75%  | 60%      | 70%    | 80%     |
| 3-Apr    | 85%  | 65%      | 75%    | 78%     |
| 10-Apr   | 60%  | 50%      | 55%    | 65%     |
| 17-Apr   | 85%  | 45%      | 40%    | 70%     |
| 24-Apr   | 90%  | 60%      | 55%    | 85%     |
| 1-May    | 100% | 70%      | 60%    | 110%    |
| 8-May    | 80%  | 65%      | 55%    | 90%     |
| 15-May   | 80%  | 75%      | 60%    | 105%    |
| 22-May   | 50%  | 60%      | 50%    | 85%     |
| 29-May   | 40%  | 50%      | 45%    | 70%     |
| 5-Jun    | 45%  | 45%      | 40%    | 60%     |
</details>

Source: Bloomberg Finance L.P., JPM Commodities Research

## Global Commodities Research

## Natasha Kaneva

(1-212) 834-3175

natasha.kaneva@JPM.com

## Lyuba Savinova

(1-212) 270-3781

lyuba.savinova@jpmchase.com

## Artem Fakhretdinov

(1-212) 272-1839

artem.fakhretdinov@JPM.com

JPM Chase Bank NA

The most plausible explanation is that the market has absorbed much of the disruption through a combination of demand losses and large-scale inventory releases. Demand has weakened in the conflict zone itself. In parts of Asia, reduced physical oil availability has curtailed consumption directly. In China, consumers have substituted away from oil more readily than many expected. In Africa, higher prices have triggered more traditional forms of demand destruction. At the same time, governments and commercial operators have drawn heavily on both crude and refined product inventories. Together, these adjustments have reduced the burden on prices to do the balancing.

For US consumers, however, this does not mean that fuel markets have fully normalized. Our forecast still calls for Brent to average around \$100 through most of the remainder of 2026. On that view, we estimate that the US retail gasoline prices will remain near \$4 per gallon for much of the year (Figure 2). While far below the levels implied by a full-blown product shortage in more extreme scenarios, they remain elevated enough to keep energy firmly in focus for households and policymakers alike.

Figure 2: JPM US retail gasoline price forecast under alternative Strait of Hormuz reopening scenarios \$ per gallon  
![](images/fac48c7b539a9091f1c5c612eee2aa353da24d32939f737a34688062c608470d.jpg)

<details>
<summary>line chart</summary>

| Month    | Actual | Baseline | July | August |
| -------- | ------ | -------- | ---- | ------ |
| Jan-26   | 2.8    | -        | -    | -      |
| Feb-26   | 2.9    | -        | -    | -      |
| Mar-26   | 3.7    | -        | -    | -      |
| Apr-26   | 4.1    | -        | -    | -      |
| May-26   | 4.5    | 4.5      | 4.5  | 4.5    |
| Jun-26   | -      | 4.3      | 4.4  | 4.4    |
| Jul-26   | -      | 4.4      | 4.6  | 4.7    |
| Aug-26   | -      | 4.4      | 4.7  | 5.0    |
| Sep-26   | -      | 4.4      | 4.8  | 5.2    |
| Oct-26   | -      | 4.2      | 4.6  | 5.1    |
| Nov-26   | -      | 4.0      | 4.5  | 5.1    |
| Dec-26   | -      | 3.8      | 4.4  | 5.0    |
</details>

Source: JPM Commodities Research

Importantly, national averages can obscure significant regional differences. Nowhere is this more evident than on the US West Coast, where fuel markets remain the tightest in the country. California is particularly exposed. A combination of unique state regulations—including high taxes and environmental mandates—and the closure of Valero’s Benicia refinery and Phillips 66’s Los Angeles refinery, which together account for 17% of California’s refining capacity, is expected to tighten fuel balances further in a market that already operates with limited flexibility.

Unlike most of the country, California cannot easily draw on supplies from neighboring states. Instead, the state relies heavily on CARB (California Air Resources Board)-compliant gasoline from Asian refiners, which account for nearly two-thirds of gasoline imports into California and roughly $20\%$ to $30\%$ of the state's total gasoline supply. Since March 1, however, many Asian refiners have been forced to reduce refined product exports as disruptions to crude flows from Hormuz have constrained feedstock availability.

The challenge is compounded by California's unique fuel specifications and the lack of major product pipelines linking the state to the rest of the country. More broadly, California's vulnerability reflects a longer-term shift. Once a major producer and exporter of oil and refined products, the state has become increasingly import-dependent as local production has steadily declined.

This structural tightness is evident at the pump. Even as crude oil prices have dipped below \$100 per barrel, pump prices have steadily declined. Today, the national average for a gallon of regular gasoline sits at roughly \$4.16, down more than 10% from a late-May peak near \$4.56. Prices nevertheless exceed \$5.0 in six states, with drivers in California paying an average of \$5.89 a gallon (Figure 3).

Diesel shows the same pattern. Nationwide, average diesel prices have eased to about \$5.32 per gallon. Yet, truckers filling up in California are still paying an average of \$7.16 at the pump.

This matters far beyond the region itself. Roughly one in five of all goods entering the United States arrives through West Coast gateways such as the Ports of Los Angeles and Long Beach. And before those imports ever reach warehouses, distribution centers, and consumers across the country, they often travel their first several hundred—or even thousand—miles powered by West Coast diesel and gasoline. In practice, this means that a meaningful share of America’s supply chain pays West Coast fuel prices. These prices influence freight costs, transportation margins, and ultimately the delivered cost of goods nationwide.

Figure 3: Average retail gasoline price by state  
\$/gallon  
![](images/d2ebdc857bc5d7809721842922bb81e0ef7824c9bd84af677da77cfaec9c9d1d.jpg)

<details>
<summary>choropleth map</summary>

| State       | Value  |
| ----------- | ------ |
| California  | $5.5   |
| Texas       | $5.0   |
| Florida     | $4.5   |
| New York    | $4.0   |
| Pennsylvania| $4.5   |
| Illinois    | $4.5   |
| Ohio        | $4.5   |
| Michigan    | $4.5   |
| Georgia     | $4.5   |
| North Carolina | $4.5  |
| Virginia    | $4.5   |
| Washington  | $4.5   |
| Arizona     | $4.5   |
| Massachusetts | $4.5  |
| Tennessee   | $4.5   |
| Indiana     | $4.5   |
| Maryland    | $4.5   |
| Missouri    | $4.5   |
| Colorado    | $4.5   |
| Minnesota   | $4.5   |
| Wisconsin   | $4.5   |
| Michigan    | $4.5   |
| Indiana     | $4.5   |
| Iowa        | $4.5   |
| Kansas      | $4.5   |
| Nebraska    | $4.5   |
| South Dakota | $4.5  |
| North Dakota| $4.5   |
| Montana     | $4.5   |
| Wyoming     | $4.5   |
| Utah        | $4.5   |
| Idaho       | $4.5   |
| Nevada      | $4.5   |
| New Hampshire | $4.5  |
| Rhode Island | $4.5  |
| Maine       | $4.5   |
| Vermont     | $4.5   |
| New Hampshire | $4.5  |
| Delaware    | $4.5   |
| Maryland    | $4.5   |
| Alaska      | $4.5   |
| Hawaii      | $4.5   |
| Maine       | $4.5   |
| Vermont     | $4.5   |
| New Hampshire | $4.5  |
| Rhode Island | $4.5  |
| Delaware    | $4.5   |
| Maine       | $4.5   |
| Vermont     | $4.5   |
| New Hampshire | $4.5  |
| Rhode Island | $4.5  |
| Delaware    | $4.5   |
| Maine       | $4.5   |
| Vermont     | $4.5   |
| New Hampshire | $4.5  |
| Rhode Island | $4.5  |
| Delaware     | $4.5   |
| Maine       | $4.5   |
| Vermont     | $4.5   |
| New Hampshire | $4.5  |
| Rhode Island | $4.5  |
| Delaware    | $4.5   |
| Maine       | $4.5   |
| Vermont     | $4.5   |
| New Hampshire | $4.5  |
| Rhode Island | $4.5  |
| Delaware```  | $4.0   |
</details>

Note: as of June 8 $^{th}$  
Source: AAA, JPM Commodity Research

Understanding where fuel prices go from here requires looking beyond crude oil to the underlying product markets.

US gasoline prices surged in May as the domestic balance tightened on both the supply and demand fronts. Inventories fell while refiners increasingly prioritized jet fuel, constraining gasoline output. At the same time, demand rebounded from the February-April lull, supported by strong Memorial Day travel and resilient consumer activity.

Higher gasoline prices have since begun to elicit a partial response: some refinery production has shifted back from jet fuel toward gasoline, and incremental imports from Canada and Northwest Europe have started to arrive, offering relief to the East Coast market. That said, this rebalancing may be short-lived. European gasoline markets remain tight, and as summer demand builds, incentives to keep barrels in-region are likely to strengthen. If so, US gasoline imports could slow later this summer, leaving domestic inventories at relatively low seasonal levels, though still comfortable overall in terms of days of demand (Figures 4 & 5).

Figure 4: US commercial inventories of gasoline and diesel  
![](images/93c2527f39ecb352d142bf1e3cb08de6e714c5ffee8fc114c9a15ceb203f789a.jpg)

<details>
<summary>line chart</summary>

| Year | Gasoline (Thousand barrels) | Diesel (Thousand barrels) |
|------|-----------------------------|---------------------------|
| 2000 | ~215,000                    | ~95,000                   |
| 2001 | ~218,000                    | ~115,000                  |
| 2002 | ~220,000                    | ~135,000                  |
| 2003 | ~215,000                    | ~95,000                   |
| 2004 | ~218,000                    | ~135,000                  |
| 2005 | ~220,000                    | ~115,000                  |
| 2006 | ~225,000                    | ~135,000                  |
| 2007 | ~230,000                    | ~145,000                  |
| 2008 | ~235,000                    | ~115,000                  |
| 2009 | ~185,000                    | ~135,000                  |
| 2010 | ~235,000                    | ~175,000                  |
| 2011 | ~245,000                    | ~175,000                  |
| 2012 | ~235,000                    | ~155,000                  |
| 2013 | ~235,000                    | ~135,000                  |
| 2014 | ~235,000                    | ~135,000                  |
| 2015 | ~245,000                    | ~145,000                  |
| 2016 | ~255,000                    | ~165,000                  |
| 2017 | ~265,000                    | ~175,000                  |
| 2018 | ~255,000                    | ~145,000                  |
| 2019 | ~265,000                    | ~135,000                  |
| 2020 | ~275,000                    | ~175,000                  |
| 2021 | ~265,000                    | ~145,000                  |
| 2022 | ~255,000                    | ~135,000                  |
| 2023 | ~245,000                    | ~135,000                  |
| 2024 | ~255,000                    | ~135,000                  |
| 2025 | ~245,000                    | ~135,000                  |
| 2026 | ~265,000                    | ~135,000                  |
</details>

Source: EIA, JPM Commodities Research

Figure 5: US commercial inventories of gasoline and diesel in days of demand coverage  
![](images/5bf6377cf8baa422561f2cd4500128d4ff84fe93496eadcb15bf39354885f4d2.jpg)

<details>
<summary>line chart</summary>

| Year | Gasoline Days | Diesel Days |
|------|---------------|-------------|
| 2003 | 24            | 38          |
| 2009 | 20            | 40          |
| 2020 | 32            | 47          |
| 2026 | 28            | 34          |
</details>

Source: EIA, JPM Commodities Research

Diesel, by contrast, is being pulled by both domestic needs and a widening global shortfall, with the US Gulf Coast increasingly acting as the marginal supplier. Diesel exports averaged 1.2 mbd in January and February, nearly 150 kbd higher than the same period last year, despite the closure of three US refineries since the start of 2025. Much of the increase appears tied to stronger demand from Brazil, where Russian diesel shipments have declined, and from Europe, where restrictions on products refined from Russian crude came into effect in January.

The closure of Hormuz has only amplified these dynamics. Since the start of the conflict, US diesel exports have risen further to 1.5 mbd, accelerating inventory draws and pushing stocks to a 23 year low, even as refinery utilization remains strong (Figures 4 & 5).

If gasoline illustrates regional tightness and diesel highlights global scarcity, jet fuel sits somewhere in between. US jet fuel inventories have remained relatively resilient despite strong domestic consumption and rising export demand as record refinery yields keep pace with demand, leaving inventories well supplied. Seasonal demand has continued to strengthen with the onset of summer travel and the approach of the World Cup, even as several airlines have already reduced flight schedules through the third quarter (Figure 6).

Figure 6: US commercial inventories of jet in days of demand coverage  
Days (LHS); Commercial inventory (RHS) in thousands of barrels  
![](images/ede68de3f9a19d98de2ef22f6a441ad6e2d23537ef67d4000617f8d2419c8d4b.jpg)

<details>
<summary>line chart</summary>

| Year | Days (LHS) | Inventory (RHS) |
|------|------------|-----------------|
| 2023 | 21 days    | 15,000          |
</details>

Source: EIA, JPM Commodities Research

Table 1: JPM crude oil price forecasts (US\$/bbl)

<table><tr><td colspan="2"></td><td>2023</td><td>2024</td><td>1Q25</td><td>2Q25</td><td>3Q25</td><td>4Q25</td><td>2025</td><td>1Q26</td><td>2Q26</td><td>3Q26</td><td>4Q26</td><td>2026</td><td>1Q27</td><td>2Q27</td><td>3Q27</td><td>4Q27</td><td>2027</td></tr><tr><td rowspan="2">Brent</td><td>Avg</td><td>81</td><td>80</td><td>75</td><td>67</td><td>68</td><td>63</td><td>68</td><td>78</td><td>103</td><td>104</td><td>98</td><td>96</td><td>85</td><td>79</td><td>69</td><td>65</td><td>75</td></tr><tr><td>EoP</td><td>86</td><td>76</td><td>75</td><td>68</td><td>67</td><td>61</td><td>61</td><td>118</td><td>101</td><td>107</td><td>95</td><td>95</td><td>82</td><td>73</td><td>69</td><td>64</td><td>64</td></tr><tr><td rowspan="2">WT

[中间内容因长度限制已省略]

rmance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised May 16, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.

Completed 09 Jun 2026 11:28 PM EDT

Disseminated 10 Jun 2026 07:00 AM EDT
"""
