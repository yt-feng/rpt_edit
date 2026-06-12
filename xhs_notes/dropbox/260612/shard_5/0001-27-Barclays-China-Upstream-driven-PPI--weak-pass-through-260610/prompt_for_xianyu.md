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
## China

# Upstream-driven PPI, weak pass-through

Oil continued to lift PPI and support energy CPI, while core and services inflation softened, pointing to limited second-round effects amid weak domestic demand. PPI gains remained concentrated in upstream, while downstream sectors may struggle to pass-through higher input costs.

• May: 1.2% y/y for CPI, and 3.9% y/y for PPI  
- Bloomberg consensus forecast (BARC): $1.3\%$ $(1.2\%)$ y/y for CPI, and $3.9\%$ $(4.0\%)$ y/y for PPI  
• April: 1.2% y/y for CPI, and 2.8% y/y for PPI

The May price data suggest oil prices continued to push up PPI inflation and energy-related components of CPI, while the impact on core and services CPI remained contained, pointing to limited second-round effects. On a month-on-month basis, PPI began to normalize alongside somewhat lower-though-still-elevated oil prices. Price declines emerged in oil and gas extraction, while price increases in chemicals, fibers, rubber, and plastics moderated.

The May PPI breakdown underscores the uneven impact of the Middle East conflict on prices. Upstream segments continued to lead, with raw materials rising by 9.2% y/y (April: 7.1%) and mining by 15.8% (April: 10.6%). While select manufacturing segments such as electrical machinery and electronics saw some price gains, overall manufacturing inflation remained more subdued at 2.3% y/y (April: 1.5%). Meanwhile, price declines in downstream consumer goods persisted (May: -0.8%, April: -1.0%), suggesting that firms are still struggling to pass through higher input costs along the value chain.

CPI was unchanged at 1.2% y/y in May, with larger support from energy in May compared with April. Despite lower oil prices in the month, a favourable year-ago base pushed domestic gasoline inflation higher (23.5% y/y versus 19.3%), lifting its contribution to headline CPI to around 0.66pp (from 0.56pp previously). Elsewhere, both core and services CPI edged lower, with continued weakness in housing rents and auto prices, reinforcing the view that soft domestic demand is limiting demand-driven reflation and preventing meaningful second-round effects.

## CPI breakdown: Slower core and services inflation

Looking at the breakdown, we highlight some of the key developments in the CPI data:

\- Goods CPI inflation rose by $1.6\%$ y/y in May versus $1.4\%$ in April, as faster gasoline price inflation more than offset the declines in food prices. Supported by a favourable year-ago base, domestic gasoline price inflation accelerated to $23.5\%$ y/y from $19.3\%$ , contributing

## Ying Zhang

+852 2903 2652

ying.zhang3@BARC.com

BARC Bank, Hong Kong

## Yingke Zhou

+852 2903 2653

yingke.zhou@BARC.com

BARC Bank, Hong Kong

## Jian Chang

+852 2903 2654

jian.chang@BARC.com

BARC Bank, Hong Kong

about 0.66pp to headline CPI, up from 0.56pp previously. In contrast, food CPI fell for a second month, down $1.7\%$ y/y (April: $-1.6\%$ ), subtracting 0.3pp from the headline print, mainly driven by a deeper decline in pork prices and softer fruit prices.

Core CPI eased slightly to 1.1% y/y from 1.2%, below its pre-conflict average of 1.3% in January–February. Within that, gold jewellery remained a contributor, adding 0.17pp to headline inflation, although its impact has moderated (0.2pp in April) alongside easing gold price growth. Vehicle prices continued to decline, down 1.1% y/y and 0.4% m/m. Prices in other key goods categories stayed stable, with household appliances and clothing rising 3.4% and 1.5% y/y, respectively, together adding about 0.12pp to CPI inflation.

\- Services CPI inflation edged down to $0.8\%$ y/y in May from $0.9\%$ in April. Travel-related service prices moderated by 0.9pp to $2.8\%$ y/y. Prices of basic public services remained largely stable, with healthcare services (May: $3.2\%$ , April: $3.4\%$ ), household services (steady at $1.1\%$ ) and education services (steady at $0.5\%$ ) continuing to rise. Housing rents declines held at $0.6\%$ y/y in May, still the fastest pace of decline since January 2023, while data from the China Index Academy show rents in major cities declined at a much sharper rate of $3.2\%$ y/y.

## PPI breakdown: Notable rise in upstream sectors

May PPI advanced for a second month, rising by $3.9\%$ following a $2.8\%$ gain in April. The notable improvement was supported by surging prices in non-ferrous metals and energy-related sectors, with rising copper prices amid strong AI and green tech-related demand and supply concerns amid the Middle East conflict. On a m/m basis, the increase in PPI moderated to $0.5\%$ , after picking up $1.7\%$ in April, which was the fastest pace since late 2021.

Looking at the breakdown, PPI gains remain highly concentrated in upstream sectors. The producer goods PPI for mining (May: 15.8% y/y, April: 10.6%, March: 2.0%) and raw materials (May: 9.2%, April: 7.1%, March: 1.1%) accelerated, while manufacturing PPI picked up at a much measured pace (May: 2.3%, April: 1.5%, March: 0.9%). According to the NBS, non-ferrous mining and processing led the upside, alongside strong gains in coal and selected manufacturing segments such as electrical machinery and electronics, contributing 2.56pp to the headline PPI print (April: 2.05pp). Energy and chemicals were another key driver, with oil and gas extraction, refined fuels, and chemical products all saw strong price increases, jointly adding close to 2pp to the headline print, again with a larger contribution than in April (1.5pp). In contrast, the consumer goods PPI remained in deflation, despite some narrowing (May: -0.8%, April: -1%, March: -1.3%).

FIGURE 1. PPI continued to accelerate...  
![](images/f47fd11110670faae09d10c29ca105c158702dd0c0765c7509a8462f8f7743d8.jpg)

<details>
<summary>line chart</summary>

| Date    | PPI   | PPI: producer goods | Consumer goods |
|---------|-------|--------------------|----------------|
| May-23  | -5.0  | -7.0               | 0.0            |
| Nov-23  | -2.5  | -3.0               | -1.0           |
| May-24  | -1.0  | -1.0               | -1.0           |
| Nov-24  | -2.5  | -3.0               | -1.0           |
| May-25  | -3.0  | -4.0               | -1.0           |
| Nov-25  | -2.0  | -2.0               | -1.0           |
| May-26  | 4.0   | 5.0                | -1.0           |
</details>

Source: Wind, BARC

FIGURE 2. ...led by non-ferrous metals and energy-related sectors  
![](images/ac5707395974722d78e3248cbdb89789c9689396ff5ef5f46e5313ad45db22ea.jpg)

<details>
<summary>line chart</summary>

| Date   | PPI: Oil and gas extraction | Coal mining and washing | Ferrous metals processing | Non-ferrous metals processing | Non-metal minerals processing |
|--------|-----------------------------|--------------------------|----------------------------|-------------------------------|--------------------------------|
| May-23 | -25                         | -15                      | -10                        | 5                             | 0                              |
| Nov-23 | 5                           | -15                      | 15                         | 10                            | 0                              |
| May-24 | 10                          | -10                      | 5                          | 15                            | 0                              |
| Nov-24 | -10                         | -5                       | -5                         | 20                            | 0                              |
| May-25 | -15                         | -20                      | -10                        | 10                            | 0                              |
| Nov-25 | -10                         | -10                      | 0                          | 20                            | 0                              |
| May-26 | 35                          | 10                       | 5                          | 40                            | 0                              |
</details>

Source: Wind, BARC

FIGURE 3. Energy remains a key driver of headline CPI...  
![](images/ba06b288d2365d9e64718d41a729f2e4e98058eef97ccf0d212e1e9735be0b66.jpg)

<details>
<summary>bar-line hybrid</summary>

pp contribution to CPI inflation (% y/y)
| Date | Core (%) | Energy (%) | Pork (%) | Vegetables (%) | Other food (%) | CPI (%) |
|---|---|---|---|---|---|---|
| May-23 | 0.7 | -0.1 | -0.8 | 0.5 | 0.9 | 0.2 |
| Nov-23 | 0.4 | 0.6 | -1.1 | -0.7 | -1.1 | -0.3 |
| May-24 | 0.9 | 0.7 | 1.1 | 0.9 | -0.8 | 0.3 |
| Nov-24 | 0.8 | 0.5 | 0.6 | 1.1 | -0.7 | 0.6 |
| May-25 | 0.6 | -0.1 | 0.5 | -0.6 | -0.8 | -0.1 |
| Nov-25 | 0.9 | 0.8 | -0.3 | 1.3 | 1.5 | 0.8 |
| May-26 | 0.8 | 1.6 | -0.4 | 1.6 | 1.9 | 1.2 |
</details>

Source: Wind, BARC

FIGURE 4. ...while core and services CPI moderated  
![](images/fdbf65e9307ba7a547aa21afa7ccc15cdd8d11753204103a0ae1412cc5a3fcbe.jpg)

<details>
<summary>line chart</summary>

| Date   | Core CPI | CPI services |
|--------|----------|--------------|
| May-14 | 1.7      | 2.7          |
| May-16 | 1.5      | 2.3          |
| May-18 | 2.4      | 3.6          |
| May-20 | 0.5      | -0.5         |
| May-22 | 0.8      | 1.5          |
| May-24 | 0.2      | 1.9          |
| May-26 | 1.2      | 0.8          |
</details>

Source: Wind, BARC

FIGURE 5. Auto prices continued to drop...  
![](images/c84675ac8a73b11d03c617ba38fb8b2a1c882c7ada22d3a24827c9a715d55ca5.jpg)

<details>
<summary>line chart</summary>

| Date   | CPI vehicles, % y/y | CPI vehicles, % m/m (RHS) |
|--------|---------------------|----------------------------|
| May-21 | -1.5                | 0.0                        |
| May-22 | -0.5                | 0.0                        |
| May-23 | -4.5                | -1.5                       |
| May-24 | -5.5                | -0.5                       |
| May-25 | -3.0                | 0.0                        |
| May-26 | -1.0                | -0.5                       |
</details>

Source: Wind, BARC

FIGURE 6. ...and so did housing rentals  
![](images/d03ebc7d77cec78fc478820029217ac454452e926027a26f751016f52fd7ec8e.jpg)

<details>
<summary>line chart</summary>

| Date | NBS CPI housing rents (%) | CREIS average rental in 50 major cities (%) |
|---|---|---|
| May-24 | -0.1 | -1.5 |
| Nov-24 | -0.3 | -3.0 |
| May-25 | -0.1 | -3.5 |
| Nov-25 | 0.0 | -3.7 |
| May-26 | -0.6 | -3.0 |
</details>

Source: Wind, BARC

FIGURE 7. CPI breakdown and PPI

<table><tr><td></td><td>May-26</td><td>Apr-26</td><td>Mar-26</td><td>Feb-26</td><td>Jan-26</td><td>Dec-25</td><td>Nov-25</td><td>Oct-25</td><td>Sep-25</td><td>Aug-25</td><td>Jul-25</td><td>Jun-25</td><td>May-25</td></tr><tr><td colspan="14">CPI %y/y</td></tr><tr><td>Headline</td><td>1.2</td><td>1.2</td><td>1.0</td><td>1.3</td><td>0.2</td><td>0.8</td><td>0.7</td><td>0.2</td><td>-0.3</td><td>-0.4</td><td>0.0</td><td>0.1</td><td>-0.1</td></tr><tr><td>Headline (%m/m)</td><td>-0.1</td><td>0.3</td><td>-0.7</td><td>1.0</td><td>0.2</td><td>0.2</td><td>-0.1</td><td>0.2</td><td>0.1</td><td>0.0</td><td>0.4</td><td>-0.1</td><td>-0.2</td></tr><tr><td>Services</td><td>0.8</td><td>0.9</td><td>0.8</td><td>1.6</td><td>0.1</td><td>0.6</td><td>0.7</td><td>0.8</td><td>0.6</td><td>0.6</td><td>0.5</td><td>0.5</td><td>0.5</td></tr><tr><td>Services (%m/m)</td><td>-0.1</td><td>0.5</td><td>-1.1</td><td>1.1</td><td>0.2</td><td>0.0</td><td>-0.4</td><td>0.2</td><td>-0.3</td><td>0.0</td><td>0.6</td><td>0.0</td><td>0.0</td></tr><tr><td>Goods</td><td>1.6</td><td>1.4</td><td>1.3</td><td>1.1</td><td>0.3</td><td>1.0</td><td>0.6</td><td>-0.2</td><td>-0.8</td><td>-1.0</td><td>-0.4</td><td>-0.2</td><td>-0.5</td></tr><tr><td>Goods (%m/m)</td><td>-0.2</td><td>0.1</td><td>-0.3</td><td>0.8</td><td>0.2</td><td>0.3</td><td>0.1</td><td>0.2</td><td>0.3</td><td>0.1</td><td>0.2</td><td>-0.1</td><td>-0.3</td></tr><tr><td>Food</td><td>-1.7</td><td>-1.6</td><td>0.3</td><td>1.7</td><td>-0.7</td><td>1.1</td><td>0.2</td><td>-2.9</td><td>-4.4</td><td>-4.3</td><td>-1.6</td><td>-0.3</td><td>-0.4</td></tr><tr><td>Food (%m/m)</td><td>-0.4</td><td>-1.6</td><td>-2.7</td><td>1.9</td><td>0.0</td><td>0.3</td><td>0.5</td><td>0.3</td><td>0.7</td><td>0.5</td><td>-0.2</td><td>-0.4</td><td>-0.2</td></tr><tr><td>Core (excluding food and energy)</td><td>1.1</td><td>1.2</td><td>1.1</td><td>1.8</td><td>0.8</td><td>1.2</td><td>1.2</td><td>1.2</td><td>1.0</td><td>0.9</td><td>0.8</td><td>0.7</td><td>0.6</td></tr><tr><td>Core (excluding food and energy, %m/m)</td><td>-0.1</td><td>0.2</td><td>-0.7</td><td>0.7</td><td>0.3</td><td>0.2</td><td>-0.1</td><td>0.2</td><td>0.0</td><td>0.0</td><td>0.4</td><td>0.0</td><td>0.0</td></tr><tr><td>Non food</td><td>1.9</td><td>1.8</td><td>1.2</td><td>1.3</td><td>0.4</td><td>0.8</td><td>0.8</td><td>0.9</td><td>0.7</td><td>0.5</td><td>0.3</td><td>0.1</td><td>0.0</td></tr><tr><td>Non food (%m/m)</td><td>-0.1</td><td>0.7</td><td>-0.2</td><td>0.8</td><td>0.2</td><td>0.1</td><td>-0.2</td><td>0.2</td><td>-0.1</td><td>-0.1</td><td>0.5</td><td>0.0</td><td>-0.2</td></tr><tr><td>Housing</td><td>-0.2</td><td>-0.2</td><td>-0.2</td><td>-0.2</td><td>-0.1</td><td>-0.2</td><td>0.0</td><td>0.1</td><td>0.1</td><td>0.1</td><td>0.1</td><td>0.1</td><td>0.1</td></tr><tr><td>Recreation</td><td>1.3</td><td>1.3</td><td>1.1</td><td>2.0</td><td>0.0</td><td>0.9</td><td>0.8</td><td>0.9</td><td>0.8</td><td>1.0</td><td>0.9</td><td>1.0</td><td>0.9</td></tr><tr><td>Transportation</td><td>5.4</td><td>4.6</td><td>0.9</td><td>-0.7</td><td>-3.4</td><td>-2.6</td><td>-2.3</td><td>-1.5</td><td>-2.0</td><td>-2.4</td><td>-3.1</td><td>-3.7</td><td>-4.3</td></tr><tr><td>Medical</td><td>2.1</td><td>2.2</td><td>1.9</td><td>1.9</td><td>1.7</td><td>1.8</td><td>1.6</td><td>1.4</td><td>1.1</td><td>0.9</td><td>0.5</td><td>0.4</td><td>0.3</td></tr><tr><td>Clothing</td><td>1.4</td><td>1.5</td><td>1.6</td><td>1.9</td><td>1.9</td><td>1.7</td><td>1.9</td><td>1.7</td><td>1.7</td><td>1.8</td><td>1.7</td><td>1.6</td><td>1.5</td></tr><tr><td>Household facilities</td><td>1.8</td><td>1.4</td><td>1.5</td><td>2.8</td><td>2.6</td><td>2.2</td><td>2.1</td><td>1.9</td><td>2.2</td><td>1.8</td><td>1.2</td><td>0.7</td><td>0.1</td></tr><tr><td>PPI % y/y</td><td>3.9</td><td>2.8</td><td>0.5</td><td>-0.9</td><td>-1.4</td><td>-1.9</td><td>-2.2</td><td>-2.1</td><td>-2.3</td><td>-2.9</td><td>-3.6</td><td>-3.6</td><td>-3.3</td></tr><tr><td>PPI % m/m</td><td>0.5</td><td>1.7</td><td>1.0</td><td>0.4</td><td>0.4</td><td>0.2</td><td>0.1</td><td>0.1</td><td>0.0</td><td>0.0</td><td>-0.2</td><td>-0.4</td><td>-0.4</td></tr></table>

Source: Wind, BARC

## Analyst(s) Certification(s):

We, Yingke Zhou, Jian Chang and Ying Zhang, hereby certify (1) that the views expressed in this research report accurately reflect our personal views about any or all of the subject securities or issuers referred to in this research report and (2) no part of our compensation was, is or will be directly or indirectly related to the specific recommendations or views expressed in this research report.

## Important Disclosures:

BARC is produced by the Investment Bank of BARC Bank PLC and its affiliates (collectively and each individually, "BARC").

All authors contributing to this research report are Research Analysts unless otherwise indicated. The publication date at the top of the report reflects the local time where the report was produced and may differ from the release date provided in GMT.

## Availability of Disclosures:

For current important disclosures regarding any issuers which are the subject of this research report please refer to https://publicresearch.barlays.com or alternatively send a written request to: BARC Compliance, 745 Seventh Avenue, 13th Floor, New York, NY 10019 or call +1-212-526-1072.

BARC Capital Inc. and/or one of its affiliates does and seeks to do business with companies covered in its research reports. As a result, inves

[中间内容因长度限制已省略]

 and accordingly should not be construed as such. Furthermore, this information is being made available on the basis that the recipient acknowledges and understands that the entities and securities to which it may relate have not been approved, licensed by or registered with the UAE Central Bank, the Dubai Financial Services Authority or any other relevant licensing authority or governmental agency in the UAE. The content of this report has not been approved by or filed with the UAE Central Bank or Dubai Financial Services Authority. BARC Bank PLC in the Qatar Financial Centre (Registered No. 00018) is authorised by the Qatar Financial Centre Regulatory Authority (QFCRA). BARC Bank PLC-QFC Branch may only undertake the regulated activities that fall within the scope of its existing QFCRA licence. Principal place of business in Qatar: Qatar Financial Centre, Office 1002, 10th Floor, QFC Tower, Diplomatic Area, West Bay, PO Box 15891, Doha, Qatar. Related financial products or services are only available to Business Customers as defined by the Qatar Financial Centre Regulatory Authority.

Russia: This material is not intended for investors who are not Qualified Investors according to the laws of the Russian Federation as it might contain information about or description of the features of financial instruments not admitted for public offering and/or circulation in the Russian Federation and thus not eligible for non-Qualified Investors. If you are not a Qualified Investor according to the laws of the Russian Federation, please dispose of any copy of this material in your possession.

Sustainable Investing Related Research: There is currently no globally accepted framework or definition (legal, regulatory or otherwise) of, nor market consensus as to what constitutes a ‘sustainable’, ‘ESG’, ‘green’, ‘climate-friendly’ or an equivalent company, investment, strategy or consideration or what precise attributes are required to be eligible to be categorised by such terms. This means there are different ways to evaluate a company or an investment and so different values may be placed on certain sustainability credentials as well as adverse ESG-related impacts of companies and ESG controversies. The evolving nature of sustainable investing considerations, models and methodologies means it can be challenging to definitively and universally classify a company or investment under a sustainable investing label and there may be areas where such companies and investments could improve or where adverse ESG-related impacts or ESG controversies exist. The evolving nature of sustainable finance related regulations and the development of jurisdiction-specific regulatory criteria also means that there is likely to be a degree of divergence as to the interpretation of such terms in the market. We expect industry guidance, market practice, and regulations in this field to continue to evolve.

Any information, data, image, or other content including from a third party source contained, referred to herein or used for whatsoever purpose by BARC or a third party (“Information”), in relation to any actual or potential ‘ESG’, ‘sustainable’ or equivalent objective, issue, factor or consideration is not intended to be relied upon for ESG or sustainability classification, regulatory regime or industry initiative purposes (“ESG Regimes”), unless otherwise stated. Nothing in these materials, including any images included therein, is intended to convey, suggest or indicate that BARC considers or represents any product, service, person or body mentioned in these materials as meeting or qualifying for any ESG or sustainability classification, label or similar standards that may exist under ESG Regimes. BARC has not conducted any assessment of compliance with ESG Regimes. Parties are reminded to make their own assessments for these purposes.

IRS Circular 230 Prepared Materials Disclaimer: BARC does not provide tax advice and nothing contained herein should be construed to be tax advice. Please be advised that any discussion of U.S. tax matters contained herein (including any attachments) (i) is not intended or written to be used, and cannot be used, by you for the purpose of avoiding U.S. tax-related penalties; and (ii) was written to support the promotion or marketing of the transactions or other matters addressed herein. Accordingly, you should seek advice based on your particular circumstances from an independent tax advisor.

© Copyright BARC Bank PLC (2026). All rights reserved. No part of this publication may be reproduced or redistributed in any manner without the prior written permission of BARC. BARC Bank PLC is registered in England No. 1026167. Registered office 1 Churchill Place, London, E14 5HP. Additional information regarding this publication will be furnished upon request.
"""
