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
- `# 标题` 必须包含报告机构的中文名称。已识别机构名：`摩根斯坦利`。标题格式建议：`# 摩根斯坦利：一句主判断`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、摩根斯坦利、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份摩根斯坦利研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
## India Materials | Asia Pacific

# Steel: Looking beyond seasonality

Localization of the Indian steel industry and the medium-term anti-involution theme in China provide structural support for steel spreads beyond seasonality. Steel stocks have performed well, and we expect select names to continue to outperform, supported by strong earnings growth potential.

Steel stocks have performed well: Higher steel prices and limited impact from the Middle East conflict have kept earnings cuts risk low, in our view, supporting continued outperformance this year following a strong 2025. Steel stocks in our coverage rose \~12% YTD (market cap-weighted), while the Sensex declined \~13% (vs. +27% for steel and \~9% for the Sensex in 2025).

We believe this strong performance cycle is not yet over and expect steel stocks to remain well supported over the medium term:

- Barring seasonality, spreads are supported: Domestic HRC prices have risen \~26% from mid-December lows, supported by the extension of safeguard duties. Some recent pullback reflects seasonally weaker demand, with domestic HRC now trading at an \~8% discount to import parity (per our estimates). Against this backdrop, spreads have declined \~11% from their April peak and may remain under pressure through the monsoon period, in line with historical trends. However, as demand improves post-monsoon, we expect domestic prices to find support and spreads to expand.  
- Limited Middle East conflict impact: While higher explosives and logistics costs and currency depreciation have driven some cost inflation, most raw material sourcing remains independent of the Middle East, limiting direct impact. However, a prolonged conflict could affect downstream industries, potentially weighing on domestic demand.  
- China medium-term story intact: Chinese exports have softened amid the Middle East conflict and seasonally weak domestic demand, which could pressure near-term spreads. However, the medium-term anti-involution theme should support domestic margins.

Raise estimates: We raise our India HRC price assumptions to reflect currency depreciation and higher raw material costs. As a result, we increase F27 steel spread estimates by \~2%, while F28 remains largely unchanged. We revise earnings estimates and roll forward our valuation base, leading to higher price targets. We expect select steel stocks to continue to perform well over the next 12 months. Maintain OW on JSW Steel, Jindal Steel, and Tata Steel, and UW on SAIL.

MS INDIA COMPANY PRIVATE LIMITED+

## Rahul Gupta

Equity Analyst

Rahul.Gupta1@morganstanley.com

+91 22 6118-2233

## Ruchika A Dhanuka

Research Associate

Ruchika.Dhanuka@morganstanley.com

+91 22 6118-2112

![](images/afaa3154914ab3bb0d70120fc4e9a14c1e366cb0e79cd55112f4390528ef705b.jpg)

<details>
<summary>text_image</summary>

Asia Summer School 2026
</details>

![](images/fcba12564ee9a77ff3a72c72277c7a5271f1f79457269fcfd0f37d8b01b414d7.jpg)

<details>
<summary>text_image</summary>

India Investment Forum 2026
</details>

## INDIA MATERIALS

Asia Pacific

Industry View

In-Line

Exhibit 1: India – Steel: What's changed

<table><tr><td rowspan="2">Company Name</td><td rowspan="2">Tickers</td><td rowspan="2">Rating Unchanged</td><td rowspan="2">Current Price (Rs)</td><td colspan="2">Price Target (Rs)</td><td rowspan="2">Upside/ (Downside)</td><td colspan="2">EBITDA Change (%)</td></tr><tr><td>OLD</td><td>NEW</td><td>F2027e</td><td>F2028e</td></tr><tr><td colspan="9">Steel</td></tr><tr><td>Jindal Steel</td><td>JINT.NS</td><td>OW</td><td>1149</td><td>1250</td><td>1340</td><td>17%</td><td>5%</td><td>-1%</td></tr><tr><td>JSW Steel</td><td>JSTL.NS</td><td>OW</td><td>1259</td><td>1330</td><td>1470</td><td>17%</td><td>-11%</td><td>-11%</td></tr><tr><td>Tata Steel</td><td>TISC.NS</td><td>OW</td><td>203</td><td>215</td><td>235</td><td>16%</td><td>-4%</td><td>3%</td></tr><tr><td>SAIL</td><td>SAIL.NS</td><td>UW</td><td>186</td><td>140</td><td>160</td><td>-14%</td><td>10%</td><td>6%</td></tr></table>

Source: MS (e) estimates. Prices as of June 9, 2026.

MS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.

## For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

+= Analysts employed by non-U.S. affiliates are not registered with FINRA, may not be associated persons of the member and may not be subject to FINRA restrictions on communications with a subject company, public appearances and trading securities held by a research analyst account.

## India Materials: Order of Preference

We prefer global commodities over domestic commodities. Within this, we favor

Aluminum, as a tight medium-term demand–supply outlook should support prices at elevated levels for longer.

We also like Steel, supported by policy measures such as safeguard duties and the medium-term China anti-involution theme, which should help balance global demand–supply and support prices. This should translate into improved spreads and margins for steel stocks in our coverage. However, we believe rerating potential is largely priced in, given rich valuations, and expect stock performance to be driven primarily by earnings growth.

Coal, while a global commodity, is perceived as more domestic in India, with Coal India acting as a proxy for thermal power demand. Weak thermal power demand trends, along with elevated inventories at power plants, continue to constrain CIL's volume growth. Higher global thermal coal prices have supported e-auction volumes and pricing, but we believe current valuations already reflect this.

For Cement, recent price hikes should offset upcoming cost pressures (driven by the Middle East conflict). However, risks remain from potential cost slippage amid a slowing demand environment. At the same time, supply remains strong, which could pressure pricing power. As a result, we see potential downside risks to F27 margins.

## Key Exhibits

## Demand/supply

Exhibit 2: India: Expect domestic production growth to pick up as new capacities ramp up through the year; demand likely to remain good  
![](images/7a0decd838544480c8837c3fd530d6e7c1a79134b7f65540550d2366e8eefebe.jpg)

<details>
<summary>line chart</summary>

| Month   | Production | Consumption/Demand |
|---------|------------|--------------------|
| May-23  | 13.0%      | 10.0%              |
| Aug-23  | 23.0%      | 18.0%              |
| Nov-23  | 16.0%      | 15.0%              |
| Feb-24  | 8.0%       | 10.0%              |
| May-24  | 3.0%       | 18.0%              |
| Aug-24  | -1.0%      | 10.0%              |
| Nov-24  | 2.0%       | 7.0%               |
| Feb-25  | 6.0%       | 13.0%              |
| May-25  | 11.0%      | 12.0%              |
| Aug-25  | 14.0%      | 11.0%              |
| Nov-25  | 5.0%       | 6.0%               |
| Feb-26  | 7.0%       | 10.0%              |
| May-26  | 7.0%       | 8.0%               |
</details>

Source: JPC, Ministry of Steel, MS. Above data for non-alloy finished steel.

Exhibit 3: Gross exports of finished steel picked up recently, but should normalize as demand picks up beyond monsoons (million tons)  
![](images/d4d5747706d4d2e6aad70d1b2a2430bd4d36be5dd8d48603f296012e949ddbe3.jpg)

<details>
<summary>area chart</summary>

| Month | 10Y Range | Current F2027 | Average |
|-------|-----------|---------------|---------|
| Apr   | ~1.1      | 0.4           | 0.5     |
| May   | ~1.6      | 0.4           | 0.55    |
| Jun   | ~1.7      | -             | 0.55    |
| Jul   | ~1.5      | -             | 0.55    |
| Aug   | ~1.3      | -             | 0.6     |
| Sep   | ~1.3      | -             | 0.6     |
| Oct   | ~1.0      | -             | 0.5     |
| Nov   | ~1.0      | -             | 0.5     |
| Dec   | ~1.2      | -             | 0.5     |
| Jan   | ~1.0      | -             | 0.5     |
| Feb   | ~1.3      | -             | 0.6     |
| Mar   | ~1.8      | -             | 0.75    |
</details>

Source: JPC, Ministry of Steel, MS. Note: 10-year range reflects F16 to F26. Above data is for non-alloy steel.

Exhibit 4: Gross imports of finished steel rose April-May, but should moderate given unfavourable pricing (million tons)  
![](images/e42486b24439ab91457ce1f15b49c377b29f3bca12d0f26605ac47029fdc8463.jpg)

<details>
<summary>line chart</summary>

| Month | 10Y Range | Current F2027 | Average |
|-------|-----------|---------------|---------|
| Apr   | ~0.8      | 0.4           | ~0.35   |
| May   | ~1.0      | 0.4           | ~0.35   |
| Jun   | ~0.9      | -             | ~0.35   |
| Jul   | ~1.0      | -             | ~0.4    |
| Aug   | ~0.9      | -             | ~0.45   |
| Sep   | ~1.0      | -             | ~0.45   |
| Oct   | ~1.0      | -             | ~0.45   |
| Nov   | ~1.0      | -             | ~0.45   |
| Dec   | ~1.0      | -             | ~0.45   |
| Jan   | ~1.0      | -             | ~0.45   |
| Feb   | ~1.0      | -             | ~0.45   |
| Mar   | ~1.0      | -             | ~0.45   |
</details>

Source: JPC, Ministry of Steel, MS. Note: 10-year range includes F16 to F26. Above data is for non-alloy steel.

Exhibit 5:  
Finished steel inventory (non-alloy) on an absolute basis has come off (mnt)...  
![](images/390e76ee52ab79c33c126bdfdbbb5e2a53efeee44b0bfe17b8b45a3b55cc79a2.jpg)

<details>
<summary>line chart</summary>

| Month | F2024 | F2025 | F2026 | F2023 | F2021 | F2022 |
|-------|-------|-------|-------|-------|-------|-------|
| Apr   | 14.0  | 14.0  | 14.0  | 11.0  | 13.8  | 8.5   |
| May   | 14.2  | 14.1  | 13.9  | 11.1  | 13.7  | 8.3   |
| Jun   | 14.1  | 14.0  | 13.7  | 11.5  | 13.5  | 8.0   |
| Jul   | 14.0  | 13.9  | 13.5  | 12.0  | 13.3  | 7.7   |
| Aug   | 13.9  | 13.8  | 13.3  | 12.5  | 13.1  | 7.6   |
| Sep   | 13.8  | 13.7  | 13.1  | 13.0  | 12.9  | 7.5   |
| Oct   | 13.7  | 13.6  | 12.9  | 13.5  | 12.7  | 7.5   |
| Nov   | 13.6  | 14.2  | 12.7  | 14.0  | 12.5  | 7.6   |
| Dec   | 13.5  | 13.9  | 12.5  | 13.8  | 12.3  | 7.8   |
| Jan   | 13.4  | 13.8  | 12.3  | 13.7  | 12.1  | 7.7   |
| Feb   | 13.3  | 13.7  | 12.1  | 13.6  | 11.9  | 7.6   |
| Mar   | 13.2  | 13.6  | 11.0  | 13.5  | 9.0   | 7.7   |
</details>

Source: JPC, Ministry of Steel, MS.

Exhibit 6: ...and looks even more attractive on an inventory days outstanding basis  
![](images/571660d92365c7447e92af1ca27a0fc8699988ac65d49ffac52b5997bcf9ff91.jpg)

<details>
<summary>line chart</summary>

| Month | F2024 | F2021 | F2025 | F2023 | F2022 | F2026 |
|-------|-------|-------|-------|-------|-------|-------|
| Apr   | 57    | 38    | 30    | 34    | 29    | 25    |
| May   | 56    | 38    | 31    | 33    | 28    | 24    |
| Jun   | 54    | 38    | 33    | 33    | 27    | 25    |
| Jul   | 52    | 38    | 34    | 33    | 26    | 26    |
| Aug   | 50    | 38    | 35    | 33    | 26    | 27    |
| Sep   | 48    | 38    | 36    | 33    | 26    | 28    |
| Oct   | 46    | 38    | 37    | 31    | 26    | 29    |
| Nov   | 44    | 38    | 40    | 31    | 27    | 30    |
| Dec   | 42    | 37    | 37    | 31    | 28    | 31    |
| Jan   | 40    | 37    | 37    | 31    | 28    | 32    |
| Feb   | 38    | 37    | 38    | 30    | 27    | 33    |
| Mar   | 36    | 36    | 35    | 27    | 26    | 26    |
</details>

Source: JPC, Ministry of Steel, MS

## Prices and spreads

Exhibit 7: International iron ore prices have remained elevated in recent months; we expect some pullback from here  
![](images/a25c6b5eff5e8bb13ea24668a28a14661b32c2e6aa62c3309d8dde6d8e8c5a93.jpg)

<details>
<summary>line chart</summary>

| Date    | Price (US$/t) |
|---------|---------------|
| Jun-19  | 115           |
| Sep-19  | 85            |
| Dec-19  | 80            |
| Mar-20  | 85            |
| Jun-20  | 100           |
| Sep-20  | 120           |
| Dec-20  | 160           |
| Mar-21  | 230           |
| Jun-21  | 210           |
| Sep-21  | 100           |
| Dec-21  | 160           |
| Mar-22  | 140           |
| Jun-22  | 100           |
| Sep-22  | 95            |
| Dec-22  | 110           |
| Mar-23  | 120           |
| Jun-23  | 105           |
| Sep-23  | 130           |
| Dec-23  | 140           |
| Mar-24  | 110           |
| Jun-24  | 105           |
| Sep-24  | 100           |
| Dec-24  | 105           |
| Mar-25  | 100           |
| Jun-25  | 95            |
| Sep-25  | 105           |
| Dec-25  | 105           |
| Mar-26  | 110           |
| Jun-26  | 105           |
</details>

Source: Platts, MS

Exhibit 78: Domestic iron ore prices (NMDC) have also seen some expansion  
![](images/b759dc59f57161e770179c45554503c942fec325a4ffa30fa89b66918737ba84.jpg)

<details>
<summary>line chart</summary>

| Date    | Price (Rs/t) |
|---------|--------------|
| Jun-19  | 3200         |
| Sep-19  | 3000         |
| Dec-19  | 3100         |
| Mar-20  | 2800         |
| Jun-20  | 3500         |
| Sep-20  | 4500         |
| Dec-20  | 6000         |
| Mar-21  | 8500         |
| Jun-21  | 7800         |
| Sep-21  | 6500         |
| Dec-21  | 5500         |
| Mar-22  | 6200         |
| Jun-22  | 3200         |
| Sep-22  | 3100         |
| Dec-22  | 4500         |
| Mar-23  | 5500         |
| Jun-23  | 4500         |
| Sep-23  | 4800         |
| Dec-23  | 5500         |
| Mar-24  | 5800         |
| Jun-24  | 5500         |
| Sep-24  | 5800         |
| Dec-24  | 5500         |
| Mar-25  | 5800         |
| Jun-25  | 5500         |
| Sep-25  | 5800         |
| Dec-25  | 5500         |
| Mar-26  | 5800         |
| Jun-26  | 6000         |
</details>

Source: Company data (NMDC), MS.

Exhibit 9: Domestic iron ore prices discount vs. import parity has narrowed (%)  
![](images/c6efec21ee77875fdff2ea60eee198d8f3ef7c7922d63bb2cfbf83579a514e75.jpg)

<details>
<summary>line chart</summary>

| Date   | Iron Ore Fines Prices (NMDC) |
|--------|------------------------------|
| Jun-21 | -50%                         |
| Sep-21 | -45%                         |
| Dec-21 | -30%                         |
| Mar-22 | -50%                         |
| Jun-22 | -70%                         |
| Sep-22 | -60%                         |
| Dec-22 | -65%                         |
| Mar-23 | -55%                         |
| Jun-23 | -50%                         |
| Sep-23 | -60%                         |
| Dec-23 | -65%                         |
| Mar-24 | -50%                         |
| Jun-24 | -55%                         |
| Sep-24 | -60%                         |
| Dec-24 | -50%                         |
| Mar-25 | -55%                         |
| Jun-25 | -40%                         |
| Sep-25 | -50%                         |
| Dec-25 | -55%                         |
| Mar-26 | -60%                         |
| Jun-26 | -50%                         |
</details>

Source: NMDC, IBM, MS. Note: NMDC 64% Fe Fine prices vs. import parity prices. For imported iron ore, we have taken 65% Fe CFR North China and import duty of 2.5%.

Exhibit 11: Domestic steel prices have seen some rollbacks to account for upcoming weak demand season  
![](images/c2ce90871549b90236ef84ffdd0cd9ec40fc8ca60594ad1298d0a8801b81ef27.jpg)

<details>
<summary>line chart</summary>

| Date   | India HRC (US$/t) | Imported Price (US$/t), incl. Safeguard duty |
|--------|-------------------|---------------------------------------------|
| Jun-22 | 850               | 875                                         |
| Sep-22 | 700               | 680                                         |
| Dec-22 | 650               | 600                                         |
| Mar-23 | 750               | 775                                         |
| Jun-23 | 700               | 650                                         |
| Sep-23 | 680               | 630                                         |
| Dec-23 | 650               | 600                                         |
| Mar-24 | 630               | 580                                         |
| Jun-24 | 600               | 550                                         |
| Sep-24 | 580               | 520                                         |
| Dec-24 | 550               | 530                                         |
| Mar-25 | 600               | 550                                         |
| Jun-25 | 620               | 580                                         |
| Sep-25 | 580               | 600                                         |
| Dec-25 | 550               | 530                                         |
| Mar-26 | 600               | 620                                         |
| Jun-26 | 650               | 675                                         |
</details>

Source: Platts, MS. Note: Import parity prices arrived at using China HRC export prices, import duty of 7.5%, surcharge of 10% on import duty, freight charges, etc.

Exhibit 13: India's HRC spreads: We expect support over medium term  
![](images/897226cb818a2000d701a717cdf5cc8d6118673dab4c62bbcd1f07f49d0cd816.jpg)

<details>
<summary>line chart</summary>

| Date    | Domestic Spreads (Rs/t) |
|---------|--------------------------|
| Jun-16  | ~30,000                  |
| Dec-16  | ~35,000                  |
| Jun-17  | ~38,000                  |
| Dec-17  | ~34,000                  |
| Jun-18  | ~37,000                  |
| Dec-18  | ~35,000                  |
| Jun-19  | ~32,000                  |
| Dec-19  | ~30,000                  |
| Jun-20  | ~35,000                  |
| Dec-20  | ~45,000                  |
| Jun-21  | ~62,000                  |
| Dec-21  | ~55,000                  |
| Jun-22  | ~60,000                  |
| Dec-22  | ~45,000                  |
| Jun-23  | ~35,000                  |
| Dec-23  | ~38,000                  |
| Jun-24  | ~35,000                  |
| Dec-24  | ~32,000                  |
| Jun-25  | ~35,000                  |
| Dec-25  | ~38,000                  |
| Jun-26  | ~35,000                  |
</details>

Source: Platts, NMDC, MS. Note: HRC Spreads = Spot HRC Price - (1.6 x NMDC Iron Ore price) - (0.6 x Global HCC prices).

Exhibit 10: Coking coal prices too have stayed higher over recent months  
![](images/9c87526fd6f12468e2cac3d745c0a32eb862521166c0be48e77a313f0a4ae4ed.jpg)

<details>
<summary>line chart</summary>

| Date    | Value (US$/t

[中间内容因长度限制已省略]

le 19(5) of the Financial Services and Markets Act 2000 (Financial Promotion) Order 2005 (as amended, the "Order"); (ii) are persons who are high net worth entities falling within Article 49(2)(a) to (d) of the Order; or (iii) are persons to whom an invitation or inducement to engage in investment activity (within the meaning of section 21 of the Financial Services and Markets Act 2000, as amended) may otherwise lawfully be communicated or caused to be communicated. RMB MS Proprietary Limited is a member of the JSE Limited and A2X (Pty) Ltd. RMB MS Proprietary Limited is a joint venture owned equally by MS International Holdings Inc. and RMB Investment Advisory (Proprietary) Limited, which is wholly owned by FirstRand Limited. The information in MS is being disseminated by MS Saudi Arabia, regulated by the Capital Market Authority in the Kingdom of Saudi Arabia, and is directed at Sophisticated investors only.

The information in MS is being communicated by MS & Co. International plc (DIFC Branch), regulated by the Dubai Financial Services Authority (the DFSA) or by MS & Co. International plc (ADGM Branch), regulated by the Financial Services Regulatory Authority Abu Dhabi (the FSRA), and is directed at Professional Clients only, as defined by the DFSA or the FSRA, respectively. The financial products or financial services to which this research relates will only be made available to a customer who we are satisfied meets the regulatory criteria of a Professional Client. A distribution of the different MS Research ratings or recommendations, in percentage terms for Investments in each sector covered, is available upon request from your sales representative.

The information in MS is being communicated by MS & Co. International plc (QFC Branch), regulated by the Qatar Financial Centre Regulatory Authority (the QFCRA), and is directed at business customers and market counterparties only and is not intended for Retail Customers as defined by the QFCRA.

As required by the Capital Markets Board of Turkey, investment information, comments and recommendations stated here, are not within the scope of investment advisory activity. Investment advisory service is provided exclusively to persons based on their risk and income preferences by the authorized firms. Comments and recommendations stated here are general in nature. These opinions may not fit to your financial status, risk and return preferences. For this reason, to make an investment decision by relying solely to this information stated here may not bring about outcomes that fit your expectations.

The trademarks and service marks contained in MS are the property of their respective owners. Third-party data providers make no warranties or representations relating to the accuracy, completeness, or timeliness of the data they provide and shall not have liability for any damages relating to such data. The Global Industry Classification Standard (GICS) was developed by and is the exclusive property of MSCI and S&P.

MS, or any portion thereof may not be reprinted, sold or redistributed without the written consent of MS.

Indicators and trackers referenced in MS may not be used as, or treated as, a benchmark under Regulation EU 2016/1011, or any other similar framework.

The issuers and/or fixed income products recommended or discussed in certain fixed income research reports may not be continuously followed. Accordingly, investors should regard those fixed income research reports as providing stand-alone analysis and should not expect continuing analysis or additional reports relating to such issuers and/or individual fixed income products. MS may hold, from time to time, material financial and commercial interests regarding the company subject to the Research report.

Registration granted by SEBI and certification from the National Institute of Securities Markets (NISM) in no way guarantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.

INDUSTRY COVERAGE: India Materials

<table><tr><td>COMPANY (TICKER)</td><td>RATING (AS OF)</td><td>PRICE* (06/10/2026)</td></tr><tr><td colspan="3">Rahul Gupta</td></tr><tr><td>ACC Ltd. (ACC.NS)</td><td>U (02/17/2025)</td><td>Rs1,316.20</td></tr><tr><td>Ambuja Cements Ltd (ABUJ.NS)</td><td>E (02/12/2026)</td><td>Rs409.80</td></tr><tr><td>Coal India Limited (COAL.NS)</td><td>E (04/17/2025)</td><td>Rs451.00</td></tr><tr><td>Dalmia Bharat Ltd (DALB.NS)</td><td>U (07/19/2024)</td><td>Rs1,637.90</td></tr><tr><td>Grasim Industries Ltd (GRAS.NS)</td><td>O (06/09/2025)</td><td>Rs3,071.20</td></tr><tr><td>Hindalco Industries Ltd (HALC.NS)</td><td>O (05/26/2026)</td><td>Rs1,039.30</td></tr><tr><td>Jindal Steel Ltd (JINT.NS)</td><td>O (01/21/2026)</td><td>Rs1,121.10</td></tr><tr><td>JSW Steel Ltd. (JSTL.NS)</td><td>O (09/05/2025)</td><td>Rs1,269.80</td></tr><tr><td>Shree Cement Ltd (SHCM.NS)</td><td>U (02/12/2026)</td><td>Rs23,850.00</td></tr><tr><td>Steel Authority of India Limited (SAIL.NS)</td><td>U (01/21/2026)</td><td>Rs181.72</td></tr><tr><td>Tata Steel (TISC.NS)</td><td>O (09/05/2025)</td><td>Rs199.31</td></tr><tr><td>Ultratech Cement Ltd (ULTC.NS)</td><td>O (06/02/2022)</td><td>Rs10,866.00</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.  
\* Historical prices are not split adjusted.

© 2026 MS
"""
