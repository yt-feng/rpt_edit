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
## China Steel Exports | Europe

# May - MoM Uptick, But Still Lower YoY

China's May finished-steel net exports rose \~10% MoM day-adjusted to 9.89mt (\~119mtpa), but remain \~8% lower YoY. Europe is increasingly insulated as imports are constrained, regional HRC premiums widen and CBAM/safeguards reinforce price floors and EBITDA/t upside.

Sequentially higher, but still lower YoY. China's May finished-steel net exports increased \~10% sequentially on a day-adjusted basis to 9.89mt, implying an annualised run-rate of \~119mtpa, above our China Materials analyst's 2026 forecast of \~105mt. However, YtD, exports remain \~8% lower YoY. YtD CISA member output is down \~7% YoY, underscoring persistent demand weakness, with the latest late-May datapoint pointing to a further 4% decline vs the prior 10-year period, as buying activity slowed heading into the weaker summer season.

Steel market continues to regionalise ... Q2 indicators point to a decline in European steel imports across products vs 4Q25, suggesting policy is starting to bite. The market is also repricing supply-chain security: since the start of the Middle East conflict, CIF Antwerp HRC has risen US\$70/t vs US\$29/t for FOB China, expanding Europe's premium by US\$41/t before any incremental uplift from CBAM or tighter safeguards (see Home Advantage). We see this as evidence that buyers are increasingly paying for proximity and reliability, in light of elevated freight, insurance and disruption risks.

... and policy should reinforce Europe's price floor. CBAM implementation from 1 January 2026 and safeguard tightening from 1 July, including higher out-of-quota tariffs, should further strengthen local pricing power. The European Council formally approved the safeguards yesterday, making the final regulatory approval. While China accounts directly for only \~13% of Europe's imports, the proposed melted-and-poured clause could materially extend policy reach via intermediary countries. Even without a demand recovery, we estimate the framework could leave Europe structurally short by 10-15mt, tightening supply and supporting higher clearing prices. Consistent with this, EU HRC spreads have risen to US\$404/t, above the long-run average of US\$320/t.

We remain constructive, but selective. In Europe, the steel profit pool appears to be migrating back toward domestic mills, with higher import parity, a more robust policy framework and improving utilisation supporting an EBITDA/t re-base. We continue to prefer European carbon steel equities with local integrated assets, shipment flexibility and leverage to widening regional premia. ArcelorMittal remains our preferred play on the dynamic; relative to European peers, the company offers greater scope to flex volumes, improve fixed-cost absorption, and capture share as the policy framework redirects marginal tonnes back toward domestic supply. We

MS & CO. INTERNATIONAL PLC+

## Alain Gabriel, CFA

Equity Analyst

Alain.Gabriel@MorganStanley.com +44 20 7425-8959

## Ioannis Masvoulas, CFA

Equity Analyst

loannis.Masvoulas@morganstanley.com +44 20 7425-0427

## Adahna Ekoku

Equity Analyst

Adahna.Ekoku@morganstanley.com +44 20 7425-0578

## Ferdinand Huber

Research Associate

Ferdinand.Huber@morganstanley.com +44 20 7677-2702

EMEA - METALS & MINING

<table><tr><td colspan="2">Europe</td></tr><tr><td>Industry View</td><td>In-Line</td></tr><tr><td colspan="2">CARBON STEEL</td></tr><tr><td colspan="2">Europe</td></tr><tr><td>Industry View</td><td>In-Line</td></tr></table>

Exhibit 1: China's finished steel net exports increased 10% MoM (day-adjusted) in May  
![](images/c965e4edd97130ec83879b7072120b3b00ff33dc488c424b7c41e43355514919.jpg)

<details>
<summary>bar chart</summary>

Steel net exports from China
| Month | Net Exports (kt) |
|---|---|
| May-21 | 4000 |
| Aug-21 | 5000 |
| Nov-21 | 3500 |
| Feb-22 | 4000 |
| May-22 | 7000 |
| Aug-22 | 5500 |
| Nov-22 | 4500 |
| Feb-23 | 5500 |
| May-23 | 7500 |
| Aug-23 | 6500 |
| Nov-23 | 7500 |
| Feb-24 | 8500 |
| May-24 | 9500 |
| Aug-24 | 7500 |
| Nov-24 | 10500 |
| Feb-25 | 9500 |
| May-25 | 10000 |
| Aug-25 | 9500 |
| Nov-25 | 11000 |
| Feb-26 | 7500 |
| May-26 | 9890 |
</details>

Source: CEIC, MS.

MS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.

## For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

+= Analysts employed by non-U.S. affiliates are not registered with FINRA, may not be associated persons of the member and may not be subject to FINRA restrictions on communications with a subject company, public appearances and trading securities held by a research analyst account.

also see Salzgitter as a key beneficiary, with the earnings inflection increasingly visible. See: Earnings Inflect, Leverage Peaks – Overweight (1 Jun 2026)

![](images/89fd5be2ab0975376b5d4ea1e42fdfdce358f803f0b1ed7967b5f2032b0d264a.jpg)

<details>
<summary>text_image</summary>

European Metals & Mining
</details>

## Chart gallery: key trade data

Exhibit 2: China steel trade data

<table><tr><td rowspan="3"></td><td colspan="6">China Trade Data</td></tr><tr><td rowspan="2">Gross Exports (kt)</td><td rowspan="2">Gross Imports (kt)</td><td colspan="4">Net Exports</td></tr><tr><td>Data (kt)</td><td>MoM, %</td><td>YoY, %</td><td>YTD, %</td></tr><tr><td>May-26</td><td>10,341</td><td>451</td><td>9,890</td><td>10%</td><td>-2%</td><td>-8%</td></tr><tr><td>Apr-26</td><td>9,500</td><td>470</td><td>9,030</td><td>5%</td><td>-9%</td><td>-10%</td></tr><tr><td>Mar-26</td><td>9,130</td><td>510</td><td>8,620</td><td>15%</td><td>-13%</td><td>-10%</td></tr><tr><td>Feb-26</td><td>7,840</td><td>370</td><td>7,470</td><td>2%</td><td>0%</td><td>-7%</td></tr><tr><td>Jan-26</td><td>7,750</td><td>460</td><td>7,290</td><td>-32%</td><td>-14%</td><td>-14%</td></tr><tr><td>Dec-25</td><td>11,300</td><td>520</td><td>10,780</td><td>14%</td><td>18%</td><td>8%</td></tr><tr><td>Nov-25</td><td>9,980</td><td>500</td><td>9,480</td><td>2%</td><td>8%</td><td>7%</td></tr><tr><td>Oct-25</td><td>9,780</td><td>500</td><td>9,280</td><td>-6%</td><td>-13%</td><td>7%</td></tr><tr><td>Sep-25</td><td>10,470</td><td>550</td><td>9,920</td><td>10%</td><td>3%</td><td>10%</td></tr><tr><td>Aug-25</td><td>9,510</td><td>500</td><td>9,010</td><td>-4%</td><td>0%</td><td>11%</td></tr><tr><td>Jul-25</td><td>9,840</td><td>450</td><td>9,390</td><td>2%</td><td>28%</td><td>13%</td></tr><tr><td>Jun-25</td><td>9,680</td><td>470</td><td>9,210</td><td>-9%</td><td>13%</td><td>11%</td></tr><tr><td>May-25</td><td>10,580</td><td>480</td><td>10,100</td><td>2%</td><td>12%</td><td>10%</td></tr><tr><td>Apr-25</td><td>10,460</td><td>520</td><td>9,940</td><td>0%</td><td>16%</td><td>10%</td></tr><tr><td>Mar-25</td><td>10,460</td><td>500</td><td>9,960</td><td>33%</td><td>7%</td><td>8%</td></tr><tr><td>Feb-25</td><td>8,040</td><td>550</td><td>7,490</td><td>-11%</td><td>13%</td><td>8%</td></tr><tr><td>Jan-25</td><td>8,940</td><td>500</td><td>8,440</td><td>-7%</td><td>4%</td><td>4%</td></tr><tr><td>Dec-24</td><td>9,730</td><td>620</td><td>9,110</td><td>3%</td><td>29%</td><td>25%</td></tr><tr><td>Nov-24</td><td>9,280</td><td>470</td><td>8,810</td><td>-17%</td><td>19%</td><td>24%</td></tr><tr><td>Oct-24</td><td>11,180</td><td>540</td><td>10,640</td><td>11%</td><td>46%</td><td>25%</td></tr><tr><td>Sep-24</td><td>10,150</td><td>550</td><td>9,600</td><td>7%</td><td>29%</td><td>22%</td></tr><tr><td>Aug-24</td><td>9,500</td><td>510</td><td>8,990</td><td>23%</td><td>18%</td><td>21%</td></tr><tr><td>Jul-24</td><td>7,830</td><td>500</td><td>7,330</td><td>-10%</td><td>11%</td><td>22%</td></tr><tr><td>Jun-24</td><td>8,740</td><td>570</td><td>8,170</td><td>-9%</td><td>18%</td><td>24%</td></tr><tr><td>May-24</td><td>9,631</td><td>640</td><td>8,991</td><td>5%</td><td>16%</td><td>25%</td></tr></table>

Source: CEIC. MoM = Month on month, YoY = Year on year, YTD = Year to date, N/A = not applicable.

Exhibit 3: China finished steel net exports  
![](images/06c182d8d2b164f7ec6e47ce38576c82702a64ab9ed9705027dc0cc7b994c785.jpg)

<details>
<summary>bar chart</summary>

Steel net exports from China
| Month | Net Exports (kt) |
|---|---|
| May-21 | 4000 |
| Jun-21 | 5200 |
| Jul-21 | 4600 |
| Aug-21 | 3800 |
| Sep-21 | 3400 |
| Oct-21 | 3000 |
| Nov-21 | 3200 |
| Dec-21 | 4000 |
| Jan-22 | 3400 |
| Feb-22 | 2600 |
| Mar-22 | 4000 |
| Apr-22 | 4000 |
| May-22 | 7000 |
| Jun-22 | 6800 |
| Jul-22 | 5800 |
| Aug-22 | 5200 |
| Sep-22 | 4200 |
| Oct-22 | 4400 |
| Nov-22 | 4600 |
| Dec-22 | 4800 |
| Jan-23 | 5400 |
| Feb-23 | 5600 |
| Mar-23 | 7300 |
| Apr-23 | 7600 |
| May-23 | 7800 |
| Jun-23 | 6900 |
| Jul-23 | 6700 |
| Aug-23 | 7700 |
| Sep-23 | 7500 |
| Oct-23 | 7400 |
| Nov-23 | 7300 |
| Dec-23 | 7100 |
| Jan-24 | 8100 |
| Feb-24 | 6600 |
| Mar-24 | 9300 |
| Apr-24 | 8500 |
| May-24 | 9100 |
| Jun-24 | 8100 |
| Jul-24 | 7400 |
| Aug-24 | 9100 |
| Sep-24 | 9700 |
| Oct-24 | 10600 |
| Nov-24 | 8900 |
| Dec-24 | 9100 |
| Jan-25 | 8500 |
| Feb-25 | 7500 |
| Mar-25 | 9900 |
| Apr-25 | 10100 |
| May-25 | 10300 |
| Jun-25 | 9300 |
| Jul-25 | 9500 |
| Aug-25 | 9100 |
| Sep-25 | 9900 |
| Oct-25 | 9300 |
| Nov-25 | 9500 |
| Dec-25 | 11100 |
| Jan-26 | 7300 |
| Feb-26 | 7400 |
| Mar-26 | 8700 |
| Apr-26 | 9100 |
| May-26 | 9899 |
May-26 (May-26) is highlighted in red.
</details>

Source: CEIC, MS

Exhibit 4: China finished steel gross exports to EU28  
![](images/99de54bb680af63eb429beb5ce9447372356459796977280022907d8a7be3c16.jpg)

<details>
<summary>bar chart</summary>

Steel Gross Exports from China to EU-28
| Month | Steel Gross Exports (kt) |
|---|---|
| Oct-20 | 110 |
| Jan-21 | 160 |
| Apr-21 | 250 |
| Jul-21 | 330 |
| Oct-21 | 330 |
| Jan-22 | 290 |
| Apr-22 | 390 |
| Jul-22 | 490 |
| Oct-22 | 290 |
| Jan-23 | 300 |
| Apr-23 | 380 |
| Jul-23 | 440 |
| Oct-23 | 270 |
| Jan-24 | 350 |
| Apr-24 | 250 |
| Jul-24 | 410 |
| Oct-24 | 310 |
| Jan-25 | 400 |
| Apr-25 | 350 |
| Jul-25 | 570 |
| Oct-25 | 560 |
| Jan-26 | 380 |
| Apr-26 | 530 |
| Jul-26 | 360 |
The data is already in CSV format. The extracted values are not directly provided in the image. The table structure is a placeholder for the actual output.
</details>

Source: CEIC, MS

Exhibit5: Price spreads: EU HRC less China HRC  
![](images/174b67df7c0b61d11ccd8151dd0ebfb7ed95f1746be840b28000624dd6295a3a.jpg)

<details>
<summary>line chart</summary>

| Year | Value (US$/t) |
|------|---------------|
| Average | 160 |
| LT | 220 |
</details>

Source: Bloomberg, MS. \* China domestic prices are based on the Shanghai benchmark for HRC excluding 17% VAT.

Exhibit6: Spreads: EU HRC gross profit per tonne\*  
![](images/98ab4539636cf4c5ba0f3375a031fb6752b21a658c86eb3dc7568774a82db749.jpg)

<details>
<summary>line chart</summary>

| Year | Value (US$/t) |
|------|---------------|
| Long-term average | 322 |
| 5-Yr average | 386 |
</details>

Source: Bloomberg, MS. \* Gross profit per tonne is calculated based on EU HRC prices less the prices of iron ore and coking coal.

Exhibit 7: Monthly steel imports to EU from all destinations  
![](images/6a27309c6db5fe9a793c878e4bf43999b28c24cbf9f762be20846ff74fe7ce05.jpg)

<details>
<summary>line chart</summary>

| Month | 5-Yr Range | 5-Yr Average | 2026 |
|-------|------------|--------------|------|
| Jan   | ~4,500     | ~3,500       | ~3,000 |
| Feb   | ~2,500     | ~1,800       | ~1,500 |
| Mar   | ~3,500     | ~2,500       | ~2,000 |
| Apr   | ~4,500     | ~3,500       | ~3,000 |
| May   | ~3,500     | ~2,500       | ~2,000 |
| Jun   | ~3,000     | ~2,250       | ~2,000 |
| Jul   | ~4,500     | ~3,500       | ~3,000 |
| Aug   | ~3,500     | ~2,500       | ~2,000 |
| Sep   | ~2,500     | ~1,800       | ~1,500 |
| Oct   | ~4,500     | ~3,500       | ~3,000 |
| Nov   | ~3,500     | ~2,500       | ~2,000 |
| Dec   | ~3,500     | ~2,250       | ~2,000 |
</details>

Source: Eurofer, Eurostat, MS. Note: There is a discrepancy between data sourced from CEIC and Eurofer.

Exhibit 8: Monthly steel imports to US from all destinations  
![](images/a60f6d7268e15222168b364260d4bd0fc77de6dc7edcd1cdfecd7ea6f1de78cf.jpg)

<details>
<summary>line chart</summary>

| Month | 5-Yr Average | 2026 |
|-------|--------------|------|
| Jan   | 2.4          | 1.4  |
| Feb   | 2.0          | 1.45 |
| Mar   | 2.3          | 1.55 |
| Apr   | 2.25         | 1.7  |
| May   | 2.25         |      |
| Jun   | 2.25         |      |
| Jul   | 2.25         |      |
| Aug   | 2.1          |      |
| Sep   | 1.95         |      |
| Oct   | 1.95         |      |
| Nov   | 1.9          |      |
| Dec   | 1.95         |      |
</details>

Source: US DOC, MS

Exhibit 9: India's monthly steel imports/exports  
![](images/a7c457941b78752be307eeb03d43a7357bf70e5176cf267f23ecc6aa07c07481.jpg)

<details>
<summary>line chart</summary>

| Month | 2026  | 5-Yr Average | 5-Yr Range |
|-------|-------|--------------|------------|
| Jan   | 400   | -10          | -400 to 800 |
| Feb   | 200   | 200          | -600 to 800 |
| Mar   | 100   | 250          | -800 to 900 |
| Apr   | -200  | 250          | -100 to 900 |
| May   | -300  | 250          | -150 to 900 |
| Jun   | -400  | 250          | -200 to 900 |
| Jul   | -500  | 250          | -250 to 900 |
| Aug   | -600  | 0            | -300 to 800 |
| Sep   | -700  | -50          | -350 to 700 |
| Oct   | -800  | -100         | -400 to 600 |
| Nov   | -900  | -150         | -450 to 500 |
| Dec   | -1000 | -150         | -500 to 400 |
</details>

Source: Joint Plant Committee, MS

Exhibit 10: Russia's monthly steel imports/exports  
![](images/f3b9ee95dbf92fc8dbe1985ceda68e1abd1d5756968f18a617dcfb674fac11aa.jpg)

<details>
<summary>line chart</summary>

| Month | 2026 (mt) | 5-Yr Average (mt) |
|-------|-----------|-------------------|
| Jan   | 1.7       | 1.6               |
| Feb   | 1.5       | 1.4               |
| Mar   | 1.5       | 1.5               |
| Apr   | 1.5       | 1.5               |
| May   | 1.6       | 1.6               |
| Jun   | 1.5       | 1.5               |
| Jul   | 1.6       | 1.5               |
| Aug   | 1.5       | 1.4               |
| Sep   | 1.5       | 1.4               |
| Oct   | 1.5       | 1.4               |
| Nov   | 1.4       | 1.4               |
| Dec   | 1.5       | 1.5               |
</details>

Source: Metal Expert, MS

Exhibit 11: Turkey's monthly steel imports/exports  
![](images/3f106043a8104270521b91428fb40828b097dce893d2df797e401dec85b54537.jpg)

<details>
<summary>line chart</summary>

| Month | 5-Yr Average | 2026 |
|-------|--------------|------|
| Jan   | -0.4         | -0.4 |
| Feb   | -0.3         | -0.3 |
| Mar   | -0.1         | -0.1 |
| Apr   | -0.4         | -0.4 |
| May   | -0.5         | -0.5 |
| Jun   | 0.1          | 0.1  |
| Jul   | -0.3         | -0.3 |
| Aug   | 0.1          | 0.1  |
| Sep   | 0.2          | 0.2  |
| Oct   | -0.3         | -0.3 |
| Nov   | -0.4         | -0.4 |
| Dec   | -0.2         | -0.2 |
</details>

Source: Metal Expert, MS

Exhibit 13: EU total steel imports by geography – Turkey, S. Korea, China and Vietnam dominate  
![](images/44ca3c85644bd416d11cf1246cfbad583c3b9e0f0a4cce8358720437aa00e153.jpg)

<details>
<summary>pie chart</summary>

| Geography | Percentage (%) |
| :--- | :--- |
| Russian Federation | 11 |
| China | 10 |
| India | 7 |
| Vietnam | 6 |
| Ukraine | 6 |
| Brazil | 5 |
| Indonesia | 5 |
| Taiwan | 5 |
| Other | 21 |
| Turkey | 14 |
| South Korea | 11 |
</details>

Source: Eurofer, Eurostat, MS

Exhibit 15: EU imports from China (cold rolled sheet) – sharp declines following AD  
![](images/c6e721d2194dacb5815bcfc171e5a66

[中间内容因长度限制已省略]

fferent MS Research ratings or recommendations, in percentage terms for Investments in each sector covered, is available upon request from your sales representative.

The information in MS is being communicated by MS & Co. International plc (QFC Branch), regulated by the Qatar Financial Centre Regulatory Authority (the QFCRA), and is directed at business customers and market counterparties only and is not intended for Retail Customers as defined by the QFCRA.

As required by the Capital Markets Board of Turkey, investment information, comments and recommendations stated here, are not within the scope of investment advisory activity. Investment advisory service is provided exclusively to persons based on their risk and income preferences by the authorized firms. Comments and recommendations stated here are general in nature. These opinions may not fit to your financial status, risk and return preferences. For this reason, to make an investment decision by relying solely to this information stated here may not bring about outcomes that fit your expectations.

The trademarks and service marks contained in MS are the property of their respective owners. Third-party data providers make no warranties or representations relating to the accuracy, completeness, or timeliness of the data they provide and shall not have liability for any damages relating to such data. The Global Industry Classification Standard (GICS) was developed by and is the exclusive property of MSCI and S&P.

MS, or any portion thereof may not be reprinted, sold or redistributed without the written consent of MS.

Indicators and trackers referenced in MS may not be used as, or treated as, a benchmark under Regulation EU 2016/1011, or any other similar framework.

The issuers and/or fixed income products recommended or discussed in certain fixed income research reports may not be continuously followed. Accordingly, investors should regard those fixed income research reports as providing stand-alone analysis and should not expect continuing analysis or additional reports relating to such issuers and/or individual fixed income products. MS may hold, from time to time, material financial and commercial interests regarding the company subject to the Research report.

Registration granted by SEBI and certification from the National Institute of Securities Markets (NISM) in no way guarantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.

INDUSTRY COVERAGE: EEMEA - Metals & Mining

<table><tr><td>COMPANY (TICKER)</td><td>RATING (AS OF)</td><td>PRICE* (06/08/2026)</td></tr><tr><td colspan="3">Alain Gabriel, CFA</td></tr><tr><td>Anglo American (AGLJ.J)</td><td>++</td><td>ZAc 85,465</td></tr><tr><td>Erdemir (EREGL.IS)</td><td>U (09/14/2022)</td><td>TL 39.02</td></tr><tr><td colspan="3">Brian Morgan</td></tr><tr><td>African Rainbow Minerals (ARIJ.J)</td><td>E (04/08/2025)</td><td>ZAc 18,548</td></tr><tr><td>Exxaro Resources Limited (EXXJ.J)</td><td>O (04/08/2025)</td><td>ZAc 22,000</td></tr><tr><td>Implats Limited (IMPJ.J)</td><td>O (01/23/2026)</td><td>ZAc 18,981</td></tr><tr><td>Kumba Iron Ore (KIOJ.J)</td><td>E (10/07/2025)</td><td>ZAc 30,612</td></tr><tr><td>Northam Platinum Limited (NPHJ.J)</td><td>U (03/20/2026)</td><td>ZAc 26,585</td></tr><tr><td>Sibanye-Stillwater (SSWJ.J)</td><td>E (01/23/2026)</td><td>ZAc 4,080</td></tr><tr><td>Thungela Resources Ltd (TGAJ.J)</td><td>U (09/11/2025)</td><td>ZAc 15,234</td></tr><tr><td>Valterra Platinum Limited (VALJ.J)</td><td>E (05/30/2025)</td><td>ZAc 116,770</td></tr><tr><td colspan="3">Christopher Nicholson</td></tr><tr><td>AngloGold Ashanti Ltd (ANGJ.J)</td><td>E (10/18/2023)</td><td>ZAc 138,564</td></tr><tr><td>Gold Fields Limited (GFIJ.J)</td><td>E (04/16/2026)</td><td>ZAc 59,341</td></tr><tr><td>Harmony Gold Mining Company Ltd (HARJ.J)</td><td>O (04/16/2026)</td><td>ZAc 25,500</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.  
\* Historical prices are not split adjusted.

INDUSTRY COVERAGE: Carbon Steel

<table><tr><td>COMPANY (TICKER)</td><td>RATING (AS OF)</td><td>PRICE* (06/08/2026)</td></tr><tr><td colspan="3">Alain Gabriel, CFA</td></tr><tr><td>ArcelorMittal SA (MT.AS)</td><td>O (01/06/2026)</td><td>€58.74</td></tr><tr><td>Salzgitter AG (SZGG.DE)</td><td>O (06/01/2026)</td><td>€62.15</td></tr><tr><td>SSAB AB (SSABa.ST)</td><td>O (05/05/2026)</td><td>SKr 96.40</td></tr><tr><td>thyssenkrupp AG (TKAG.DE)</td><td>E (03/23/2026)</td><td>€11.36</td></tr></table>

voestalpine AG (VOES.VI)

E (06/01/2026)

€45.72

Stock Ratings are subject to change. Please see latest research for each company.

\* Historical prices are not split adjusted.

© 2026 MS
"""
