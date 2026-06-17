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
## Lithium Value Chain Survey: Temporary Pullback, Diverging Signals

Our survey of lithium converters (77% of sales in China) and battery materials producers (73%) highlights decelerating battery volumes and a weaker backlog, translating into converters expecting $>10\%$ price declines in Q3. New orders have decelerated and confidence in those orders has decreased. Inventories are lower YoY: converters believe battery producer inventories are too low, but battery producers believe their customers have a modest overhang.

Chart 1 - Lithium Prices, % Chg. Next 3 Months  
![](images/2e86e4bba24bb1787a52c00f1443cf6f365e05372e554bf5d93a3296d4077120.jpg)

<details>
<summary>line chart</summary>

| Month    | Converter | Battery Producer |
| -------- | --------- | ---------------- |
| Jan-24   | -6%       | -14%             |
| Mar-24   | -2%       | -4%              |
| May-24   | -12%      | -4%              |
| Jul-24   | -8%       | -4%              |
| Sep-24   | -10%      | -4%              |
| Nov-24   | -6%       | -8%              |
| Jan-25   | -6%       | -10%             |
| Mar-25   | -8%       | -4%              |
| May-25   | -10%      | -8%              |
| Jul-25   | -10%      | -8%              |
| Sep-25   | -8%       | -4%              |
| Nov-25   | 0%        | -2%              |
| Jan-26   | 4%        | -4%              |
| Mar-26   | 0%        | -6%              |
| May-26   | -12%      | -4%              |
</details>

Source: JEF Proprietary Survey

Chart 2 - Volumes, % YoY  
![](images/d59f3e74b2c0e4cf32f65f66939adef84c1775ba5f614224a5b8076f7cf633cf.jpg)

<details>
<summary>line chart</summary>

| Month   | Converter | Battery Producer |
|---------|-----------|------------------|
| Jan-24  | -15%      | -5%              |
| Mar-24  | -5%       | 0%               |
| May-24  | -10%      | 5%               |
| Jul-24  | -15%      | -5%              |
| Sep-24  | -10%      | 5%               |
| Nov-24  | -5%       | -5%              |
| Jan-25  | 0%        | -5%              |
| Mar-25  | 5%        | 0%               |
| May-25  | 0%        | 5%               |
| Jul-25  | -5%       | 0%               |
| Sep-25  | -10%      | -5%              |
| Nov-25  | -5%       | 5%               |
| Jan-26  | -10%      | 0%               |
| Mar-26  | -5%       | -5%              |
| May-26  | 0%        | -5%              |
</details>

Source: JEF Proprietary Survey

Chart 3 - Inventories % YoY - Volumes % YoY  
![](images/e2d9424e1f665a1c0654eb15babbb7dbbb19aadb83b74fe4f705c45d368bf01e.jpg)

<details>
<summary>line chart</summary>

| Month   | Converter | Battery Producer |
|---------|-----------|------------------|
| Jan-24  | 10%       | 0%               |
| Mar-24  | 3%        | -5%              |
| May-24  | -5%       | -10%             |
| Jul-24  | 15%       | -5%              |
| Sep-24  | 10%       | -5%              |
| Nov-24  | 0%        | -5%              |
| Jan-25  | -5%       | -5%              |
| Mar-25  | 0%        | -10%             |
| May-25  | 5%        | 5%               |
| Jul-25  | 3%        | -5%              |
| Sep-25  | 0%        | 0%               |
| Nov-25  | -5%       | -5%              |
| Jan-26  | -10%      | -5%              |
| Mar-26  | -5%       | -5%              |
| May-26  | 0%        | 0%               |
</details>

Source: JEF Proprietary Survey

Chart 4 - Order Backlog: >50% = Expanding  
![](images/b578108aafd6a76d6905103375f721fe6d2f921a1bb279b2a5ea79f97ab91b99.jpg)

<details>
<summary>line chart</summary>

| Month    | Converter | Battery Producer |
| -------- | --------- | ---------------- |
| Jan-24   | 50%       | 70%              |
| Mar-24   | 50%       | 60%              |
| May-24   | 20%       | 40%              |
| Jul-24   | 40%       | 60%              |
| Sep-24   | 40%       | 70%              |
| Nov-24   | 30%       | 50%              |
| Jan-25   | 40%       | 70%              |
| Mar-25   | 50%       | 50%              |
| May-25   | 40%       | 70%              |
| Jul-25   | 30%       | 70%              |
| Sep-25   | 20%       | 70%              |
| Nov-25   | 40%       | 50%              |
| Jan-26   | 50%       | 60%              |
| Mar-26   | 70%       | 30%              |
| May-26   | 60%       | 30%              |
</details>

Source: JEF Proprietary Survey

Chart 5 - Sales Next Month, % YoY  
![](images/4ed3426b00987daebc8276ad3da5ea559c4d8e244fca6f8cba5e71cd220f00d5.jpg)

<details>
<summary>line chart</summary>

| Month    | Converter | Battery Producer |
| -------- | --------- | ---------------- |
| Jan-24   | -18%      | 3%               |
| Mar-24   | 0%        | 5%               |
| May-24   | -10%      | 1%               |
| Jul-24   | -8%       | 3%               |
| Sep-24   | -6%       | 4%               |
| Nov-24   | -8%       | 5%               |
| Jan-25   | -10%      | 5%               |
| Mar-25   | -4%       | 3%               |
| May-25   | -6%       | 0%               |
| Jul-25   | -8%       | 0%               |
| Sep-25   | -6%       | 3%               |
| Nov-25   | -4%       | 0%               |
| Jan-26   | -2%       | 0%               |
| Mar-26   | -2%       | 0%               |
| May-26   | -4%       | -5%              |
</details>

Source: JEF Proprietary Survey

Chart 6 - New Orders, % YoY  
![](images/52c5ac496db5e97a94afd86102d5ac9db1a3faacf363796b44969f83f2d2c343.jpg)

<details>
<summary>line chart</summary>

| Month    | Converter | Battery Producer |
| -------- | --------- | ---------------- |
| Jan-24   | -15%      | 0%               |
| Mar-24   | -5%       | 5%               |
| May-24   | -10%      | 5%               |
| Jul-24   | -10%      | 5%               |
| Sep-24   | -10%      | 5%               |
| Nov-24   | -10%      | 5%               |
| Jan-25   | -5%       | 5%               |
| Mar-25   | -5%       | 5%               |
| May-25   | -10%      | 5%               |
| Jul-25   | -10%      | 5%               |
| Sep-25   | -5%       | 5%               |
| Nov-25   | 0%        | 5%               |
| Jan-26   | 0%        | 0%               |
| Mar-26   | 0%        | 0%               |
| May-26   | 0%        | 0%               |
</details>

Source: JEF Proprietary Survey

Chart 7 - Customer Inventories: >50% = "Too High"  
![](images/12c14d09c13ba62e5c4e40b5de145e33bb7b0f9dcff68fd878c5e12d752f065f.jpg)

<details>
<summary>line chart</summary>

| Month   | Converter | Battery Producer |
|---------|-----------|------------------|
| Jan-24  | 20%       | 60%              |
| Mar-24  | 20%       | 50%              |
| May-24  | 20%       | 60%              |
| Jul-24  | 30%       | 40%              |
| Sep-24  | 50%       | 60%              |
| Nov-24  | 30%       | 30%              |
| Jan-25  | 50%       | 60%              |
| Mar-25  | 30%       | 40%              |
| May-25  | 50%       | 60%              |
| Jul-25  | 20%       | 50%              |
| Sep-25  | 30%       | 30%              |
| Nov-25  | 50%       | 40%              |
| Jan-26  | 20%       | 60%              |
| Mar-26  | 10%       | 40%              |
| May-26  | 20%       | 60%              |
</details>

Source: JEF Proprietary Survey

Chart 8 - Expected Sales % YoY - New Orders % YoY  
![](images/7f911863ceb6b1bb6908063ede057cda35681b2b6cf5d0148592d10a1a7c8938.jpg)

<details>
<summary>line chart</summary>

| Month   | Converter | Battery Producer |
|---------|-----------|------------------|
| Jan-24  | -1.0%     | 2.0%             |
| Mar-24  | 6.0%      | 4.0%             |
| May-24  | 0.0%      | -3.0%            |
| Jul-24  | 7.0%      | -1.0%            |
| Sep-24  | 1.0%      | -1.0%            |
| Nov-24  | 0.0%      | -1.0%            |
| Jan-25  | -1.0%     | -2.0%            |
| Mar-25  | 2.0%      | -4.0%            |
| May-25  | 4.0%      | -7.0%            |
| Jul-25  | 2.0%      | -1.0%            |
| Sep-25  | 1.0%      | -1.0%            |
| Nov-25  | 0.0%      | -1.0%            |
| Jan-26  | -1.0%     | -1.0%            |
| Mar-26  | 1.0%      | -1.0%            |
| May-26  | -4.0%     | -3.0%            |
</details>

Source: JEF Proprietary Survey

Chart 9 - Inventories, % YoY  
![](images/644ec8ea720b3c5f2386350f90390d04b4f1ae58fdb7286a4afb9c8fafc27404.jpg)

<details>
<summary>line chart</summary>

| Month   | Converter | Battery Producer |
|---------|-----------|------------------|
| Jan-24  | -8.0%     | -4.0%            |
| Feb-24  | 3.0%      | -2.0%            |
| Mar-24  | -6.0%     | -4.0%            |
| Apr-24  | 0.0%      | -2.0%            |
| May-24  | -6.0%     | -4.0%            |
| Jun-24  | -8.0%     | -2.0%            |
| Jul-24  | -10.0%    | 0.0%             |
| Aug-24  | -8.0%     | 2.0%             |
| Sep-24  | -6.0%     | 0.0%             |
| Oct-24  | -4.0%     | -2.0%            |
| Nov-24  | -2.0%     | -4.0%            |
| Dec-24  | -4.0%     | -6.0%            |
| Jan-25  | -6.0%     | -8.0%            |
| Feb-25  | -8.0%     | -10.0%           |
| Mar-25  | -10.0%    | -8.0%            |
| Apr-25  | -8.0%     | -6.0%            |
| May-25  | -6.0%     | -4.0%            |
| Jun-25  | -4.0%     | -2.0%            |
| Jul-25  | -2.0%     | 0.0%             |
| Aug-25  | 0.0%      | 2.0%             |
| Sep-25  | 2.0%      | 0.0%             |
| Oct-25  | 4.0%      | -2.0%            |
| Nov-25  | 6.0%      | -4.0%            |
| Dec-25  | 8.0%      | -6.0%            |
| Jan-26  | 10.0%     | -8.0%            |
| Feb-26  | 8.0%      | -6.0%            |
| Mar-26  | 6.0%      | -4.0%            |
| Apr-26  | 4.0%      | -2.0%            |
| May-26  | 2.0%      | 0.0%             |
</details>

Source: JEF Proprietary Survey

Laurence Alexander \* | Equity Analyst

(212) 284-2553 | lalexander@JEF.com

Kevin Estok \* | Equity Associate

(212) 778-8516 | kestok@JEF.com

Daniel Rizzo \* | Equity Analyst

(212) 336-6284 | drizzo@JEF.com

Xianrao Zhu \* | Equity Associate

+1 (212) 778-8742 | xzhu@JEF.com

Carol Jiang \* | Equity Associate

+1 (212) 284-1714 | cjiang@JEF.com

## Analyst Certification:

I, Laurence Alexander, certify that all of the views expressed in this research report accurately reflect my personal views about the subject security(ies) and subject company(ies). I also certify that no part of my compensation was, is, or will be, directly or indirectly, related to the specific recommendations or views expressed in this research report.  
I, Kevin Estok, certify that all of the views expressed in this research report accurately reflect my personal views about the subject security(ies) and subject company(ies). I also certify that no part of my compensation was, is, or will be, directly or indirectly, related to the specific recommendations or views expressed in this research report.  
I, Daniel Rizzo, certify that all of the views expressed in this research report accurately reflect my personal views about the subject security(ies) and subject company(ies). I also certify that no part of my compensation was, is, or will be, directly or indirectly, related to the specific recommendations or views expressed in this research report.  
I, Xianrao Zhu, certify that all of the views expressed in this research report accurately reflect my personal views about the subject security(ies) and subject company(ies). I also certify that no part of my compensation was, is, or will be, directly or indirectly, related to the specific recommendations or views expressed in this research report.  
I, Carol Jiang, certify that all of the views expressed in this research report accurately reflect my personal views about the subject security(ies) and subject company(ies). I also certify that no part of my compensation was, is, or will be, directly or indirectly, related to the specific recommendations or views expressed in this research report.

As is the case with all JEF employees, the analyst(s) responsible for the coverage of the financial instruments discussed in this report receives compensation based in part on the overall performance of the firm, including investment banking income. We seek to update our research as appropriate, but various regulations may prevent us from doing so. Aside from certain industry reports published on a periodic basis, the large majority of reports are published at irregular intervals as appropriate in the analyst's judgement.

# Investment Recommendation Record

(Article 3(1)e and Article 7 of MAR)

Recommendation Published

June 15, 2026 11:29 A.M.

Recommendation Distributed

June 15, 2026 11:29 A.M.

## Explanation of JEF Ratings

Buy - Describes securities that we expect to provide a total return (price appreciation plus yield) of 15% or more within a 12-month period.

Hold - Describes securities that we expect to provide a total return (price appreciation plus yield) of plus 15% or minus 10% within a 12-month period.

Underperform - Describes securities that we expect to provide a total return (price appreciation plus yield) of minus 10% or less within a 12-month period.

The expected total return (price appreciation plus yield) for Buy rated securities with an average security price consistently below \$10 is 20% or more within a 12-month period as these companies are typically more volatile than the overall stock market. For Hold rated securities with an average security price consistently below \$10, the expected total return (price appreciation plus yield) is plus or minus 20% within a 12-month period. For Underperform rated securities with an average security price consistently below \$10, the expected total return (price appreciation plus yield) is minus 20% or less within a 12-month period.

NR - The investment rating and price target have been temporarily suspended. Such suspensions are in compliance with applicable regulations and/or JEF policies.

CS - Coverage Suspended. JEF has suspended coverage of this company.

NC - Not covered. JEF does not cover this company.

Restricted - Describes issuers where, in conjunction with JEF engagement in certain transactions, company policy or applicable securities regulations prohibit certain types of communications, including investment recommendations.

Monitor - Describes securities whose company fundamentals and financials are being monitored, and for which no financial projections or opinions on the investment merits of the company are provided.

## Valuation Methodology

JEF' methodology for assigning ratings may include the following: market capitalization, maturity, growth/value, volatility and expected total return over the next 12 months. The price targets are based on several methodologies, which may include, but are not restricted to, analyses of market risk, growth rate, revenue stream, discounted cash flow (DCF), EBITDA, EPS, cash flow (CF), free cash flow (FCF), EV/EBITDA, P/E, PE/growth, P/CF, P/FCF, premium (discount)/average group EV/EBITDA, premium (discount)/average group P/E, sum of the parts, net asset value, dividend returns, and return on equity (ROE) over the next 12 months.

## JEF Franchise Picks

JEF Franchise Picks include stock selections from among the best stock ideas from our equity analysts over a 12 month period. Stock selection is based on fundamental analysis and may take into account other factors such as analyst conviction, differentiated analysis, a favorable risk/reward ratio and investment themes that JEF analysts are recommending. JEF Franchise Picks will include only Buy rated stocks and the number can vary depending on analyst recommendations for inclusion. Stocks will be added as new opportunities arise and removed when the reason for inclusion changes, the stock has met its desired return, if it is no longer rated Buy and/or if it triggers a stop loss. Stocks having 120 day volatility in the bottom quartile of S&P stocks will continue to have a 15% stop loss, and the remai

[中间内容因长度限制已省略]

 the recipient based on this report is consistent with a recipient's investment objectives, portfolio holdings, strategy, financial situation, or needs.

By providing this report, neither JRS nor any other JEF entity accepts any authority, discretion, or control over the management of the recipient's assets. Any action taken by the recipient of this report, based on the information in the report, is at the recipient's sole judgment and risk. The recipient must perform his or her own independent review of any prospective investment. If the recipient uses the services of JEF LLC (or other affiliated broker-dealers), in connection with a purchase or sale of a security that is a subject of these materials, such broker-dealer may act as principal for its own accounts or as agent for another person. Only JRS is registered with the SEC as an investment adviser; and therefore neither JEF LLC nor any other JEF affiliate has any fiduciary duty in connection with distribution of these reports.

The price and value of the investments referred to herein and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

This report may contain forward looking statements that may be affected by inaccurate assumptions or by known or unknown risks, uncertainties, and other important factors. As a result, the actual results, events, performance or achievements of the financial product may be materially different from those expressed or implied in such statements.

This report has been prepared independently of any issuer of securities mentioned herein and not as agent of any issuer of securities. No Equity Research personnel have authority whatsoever to make any representations or warranty on behalf of the issuer(s). Any comments or statements made herein are those of the JEF entity producing this report and may differ from the views of other JEF entities.

This report may contain information obtained from third parties, including ratings from credit ratings agencies such as Standard & Poor's, and information derived from third-party or proprietary generative artificial intelligence (Gen AI) models. JEF does not guarantee the accuracy, completeness, timeliness or availability of this information, and is not responsible for any errors or omissions (negligent or otherwise), regardless of the cause, or for the results obtained from the use of such content. Neither JEF nor any third-party content providers, including providers of Gen AI models, give any express or implied warranties, including, but not limited to, any warranties of merchantability or fitness for a particular purpose or use. Neither JEF nor any third-party content provider shall be liable for any direct, indirect, incidental, exemplary, compensatory, punitive, special or consequential damages, costs, expenses, legal fees, or losses (including lost income or profits and opportunity costs) in connection with any use of their content, including ratings. Credit ratings are statements of opinions and are not statements of fact or recommendations to purchase, hold or sell securities. They do not address the suitability of securities or the suitability of securities for investment purposes, and should not be relied on as investment advice. Reproduction and distribution of third party content in any form is prohibited except with the prior written permission of the related third party.

JEF reports are disseminated and available electronically, and, in some cases, also in printed form. Electronic research is simultaneously made available to all clients. This report or any portion hereof may not be copied, reprinted, sold, or redistributed or disclosed by the recipient or any third party, by content scraping or extraction, automated processing, or any other form or means, without the prior written consent of JEF. Any unauthorized use is prohibited. Neither JEF nor any of its respective directors, officers or employees, is responsible for guaranteeing the financial success of any investment, or accepts any liability whatsoever for any direct, indirect or consequential damages or losses arising from any use of this report or its contents. Nothing herein shall be construed to waive any liability JEF has under applicable U.S. federal or state securities laws.

For Important Disclosure information relating to JRS, please see https://adviserinfo.sec.gov/IAPD/Content/Common/crd\_iapd\_Brochure.aspx?BRCHR\_VRSN\_ID=483878 and https://adviserinfo.sec.gov/Firm/292142 or visit our website at https://avatar.bluematrix.com/sellside/Disclosures.action, or www.JEF.com, or call 1.888.JEF.

© 2026 JEF
"""
