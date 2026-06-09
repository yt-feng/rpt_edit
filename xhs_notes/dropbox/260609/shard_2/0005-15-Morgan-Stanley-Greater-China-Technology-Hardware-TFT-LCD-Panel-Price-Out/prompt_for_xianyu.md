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
## Greater China Technology Hardware | Asia Pacific

# TFT-LCD Panel Price Outlook for June 2026: TVs Flat, Monitors +0.2%, NBs Flat MoM

We expect TV panel prices to start trending down from 3Q26 and IT panels from 4Q26. Moreover, emerging businesses will take time to deliver meaningful contribution. Maintain EW on TV panel names, with a relative preference for BOE.

TV panel prices to stay flat MoM in June: We expect mainstream 32", 43", 55", 65" and 75" TV panel pricing to stay flat MoM for the month of June. On the demand side, as earlier restocking since the start of the year tapers off, panel order momentum is slowing. On the supply side, panel makers continue to demonstrate good discipline in controlling output. We continue to believe that TV panel shipments could be below seasonal levels, given the strong 1H26, so panel makers' bargaining power is likely to weaken further in the coming months. Thus, our base-case assumption remains that TV panel prices should trend down from 3Q26, but the decline should not be significant, as supply-side discipline should provide downside support. On a quarterly average basis, we expect TV panel prices to increase by low single-digit % QoQ in 2Q26.

IT panel prices to stay largely stable in June: Monitor panel prices edged up 0.2% MoM, while NBs are expected to remain flat MoM. In general, we continue to expect IT panel prices to remain relatively stable vs. TV panels in the coming quarters.

Opportunities for glass in advanced packaging will take more time: We have been believers in the adoption of glass in advanced packaging architectures (see our deep dive report) as its larger dimensions could offer better cost efficiency. Moreover, it can provide better electrical performance with lower signal loss, reduced mismatch in coefficients of thermal expansion among different materials to mitigate warpage, and greater mechanical strength to resist distortion during manufacturing and operation. That said, the supply chain is still optimizing processes, so this remains less of a story for 2026–27.

Risk/reward less attractive: With panel prices likely to trend down from 3Q26, we view valuations as less attractive at this stage, especially for Taiwan names AUO (2409.TW; 1.4x P/B) and Innolux (3481.TW; 1.9x P/B). We acknowledge potential upside from emerging businesses, where glass could be used in advanced packaging, but meaningful contribution will take time. In addition, panel makers are not the only players seeking to penetrate this market. We therefore view the investment case for these names as less compelling on this angle, given valuations already exceed peak levels of the past few years. Within China, we prefer BOE (000725.SZ; 1.7x P/B) over TCL (000100.SZ; 1.7x P/B) due to its scale advantage and higher concentration in the display business.

MS TAIWAN LIMITED+

## Derrick Yang

Equity Analyst

Derrick.Yang@morganstanley.com +886 2 2730-2862

MS & CO. INTERNATIONAL PLC+

## Shawn Kim

Equity Analyst

Shawn.Kim@morganstanley.com +44 20 7677-1018

MS TAIWAN LIMITED+

## Vivi Huang

Research Associate

Vivi.Huang@morganstanley.com +886 2 2730-2860

## Sharon Shih

Equity Analyst

Sharon.Shih@morganstanley.com +886 2 2730-2865

## Asia Summer School 2026

![](images/519d15a3b31bd5a450a3d8abaed4cd91c52adb96467514766b633e69ff67aa90.jpg)

GREATER CHINA TECHNOLOGY HARDWARE

<table><tr><td>Asia Pacific Industry View</td><td>In-Line</td></tr></table>

S. KOREA TECHNOLOGY

<table><tr><td>Asia Pacific Industry View</td><td>Attractive</td></tr></table>

Exhibit 1: TFT-LCD TV Panel Price Trends  
![](images/fbb0f956ed3865c67a6f8ff4e6e57c208a21be4f44a3c2dc14cebcca5ee68e84.jpg)

<details>
<summary>line chart</summary>

| Date   | 75° 4K | 55° 4K | 55° FHD | 50° FHD | 43° FHD | 32° HD |
|--------|--------|--------|---------|---------|---------|--------|
| Jan-18 | 100%   | 100%   | 100%    | 100%    | 100%    | 100%   |
| Jul-18 | 90%    | 95%    | 90%     | 95%     | 90%     | 95%    |
| Jan-19 | 80%    | 85%    | 80%     | 85%     | 80%     | 85%    |
| Jul-19 | 70%    | 75%    | 70%     | 75%     | 70%     | 75%    |
| Jan-20 | 60%    | 65%    | 60%     | 65%     | 60%     | 65%    |
| Jul-20 | 50%    | 55%    | 50%     | 55%     | 50%     | 55%    |
| Jan-21 | 40%    | 45%    | 40%     | 45%     | 40%     | 45%    |
| Jul-21 | 30%    | 35%    | 30%     | 35%     | 30%     | 35%    |
| Jan-22 | 20%    | 25%    | 20%     | 25%     | 20%     | 25%    |
| Jul-22 | 30%    | 35%    | 30%     | 35%     | 30%     | 35%    |
| Jan-23 | 40%    | 45%    | 40%     | 45%     | 40%     | 45%    |
| Jul-23 | 50%    | 55%    | 50%     | 55%     | 50%     | 55%    |
| Jan-24 | 60%    | 65%    | 60%     | 65%     | 60%     | 65%    |
| Jul-24 | 70%    | 75%    | 70%     | 75%     | 70%     | 75%    |
| Jan-25 | 80%    | 85%    | 80%     | 85%     | 80%     | 85%    |
| Jul-25 | 90%    | 95%    | 90%     | 95%     | 90%     | 95%    |
| Jan-26 | 100%   | 100%   | 100%    | 100%    | 100%    | 100%   |
</details>

Source: Trendforce, MS

MS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.

## For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

+= Analysts employed by non-U.S. affiliates are not registered with FINRA, may not be associated persons of the member and may not be subject to FINRA restrictions on communications with a subject company, public appearances and trading securities held by a research analyst account.

## Pricing Chart

Exhibit 2: TFT-LCD Panel Prices – June 2026

<table><tr><td>Green Star</td><td>Format</td><td>Resolution</td><td>BU</td><td>1/1/2024</td><td>2/1/2024</td><td>3/1/2024</td><td>4/1/2024</td><td>5/1/2024</td><td>6/1/2024</td><td>7/1/2024</td><td>8/1/2024</td><td>9/1/2024</td><td>10/1/2024</td><td>11/1/2024</td><td>12/1/2024</td><td>1/1/2025</td><td>2/1/2025</td><td>3/1/2025</td><td>4/1/2025</td><td>5/1/2025</td><td>6/1/2025</td><td>7/1/2025</td><td>8/1/2025</td><td>9/1/2025</td><td>10/1/2025</td><td>11/1/2025</td><td>12/1/2025</td><td>1/1/2026</td><td>2/1/2026</td><td>3/1/2026</td><td>4/1/2026</td><td>5/1/2026</td><td>Jun-06</td></tr><tr><td>FF</td><td rowspan="2">XCLK</td><td rowspan="2">3840x2461/260 Open-Cell</td><td>241</td><td>243</td><td>248</td><td>253</td><td>255</td><td>255</td><td>253</td><td>250</td><td>248</td><td>248</td><td>248</td><td>250</td><td>253</td><td>256</td><td>257</td><td>257</td><td>257</td><td>256</td><td>253</td><td>253</td><td>253</td><td>251</td><td>248</td><td>245</td><td>245</td><td>247</td><td>250</td><td>251</td><td>251</td><td>251</td><td></td></tr><tr><td>Change (%)</td><td>0.0%</td><td>0.8%</td><td>2.1%</td><td>2.0%</td><td>0.8%</td><td>0.0%</td><td>-0.8%</td><td>-1.2%</td><td>-0.8%</td><td>0.0%</td><td>0.0%</td><td>0.0%</td><td>0.8%</td><td>1.2%</td><td>1.2%</td><td>0.4%</td><td>0.0%</td><td>0.0%</td><td>-0.4%</td><td>-1.2%</td><td>0.0%</td><td>0.0%</td><td>-0.8%</td><td>-1.2%</td><td>-1.2%</td><td>0.0%</td><td>0.8%</td><td>1.2%</td><td>0.4%</td><td>0.0%</td><td>0.0%</td></tr><tr><td>66°</td><td rowspan="2">XCLK</td><td rowspan="2">3840x2461/260 Open-Cell</td><td>173</td><td>176</td><td>181</td><td>186</td><td>188</td><td>188</td><td>186</td><td>183</td><td>181</td><td>181</td><td>181</td><td>182</td><td>184</td><td>186</td><td>187</td><td>187</td><td>187</td><td>186</td><td>183</td><td>183</td><td>183</td><td>181</td><td>178</td><td>178</td><td>178</td><td>178</td><td>182</td><td>185</td><td>187</td><td>187</td><td>187</td></tr><tr><td>Change (%)</td><td>0.0%</td><td>1.7%</td><td>2.8%</td><td>2.8%</td><td>1.1%</td><td>0.0%</td><td>-1.1%</td><td>-1.6%</td><td>-1.1%</td><td>0.0%</td><td>0.0%</td><td>0.0%</td><td>0.6%</td><td>1.1%</td><td>1.1%</td><td>0.5%</td><td>0.0%</td><td>0.0%</td><td>-0.5%</td><td>-1.6%</td><td>0.0%</td><td>0.0%</td><td>-1.1%</td><td>-1.7%</td><td>0.0%</td><td>0.6%</td><td>1.7%</td><td>1.6%</td><td>1.1%</td><td>0.0%</td><td>0.0%</td></tr><tr><td>FF</td><td rowspan="2">XCLK</td><td rowspan="2">3840x2461/260 Open-Cell</td><td>132</td><td>134</td><td>137</td><td>139</td><td>140</td><td>140</td><td>139</td><td>137</td><td>134</td><td>134</td><td>134</td><td>135</td><td>136</td><td>137</td><td>137</td><td>136</td><td>133</td><td>134</td><td>134</td><td>134</td><td>134</td><td>133</td><td>131</td><td>131</td><td>132</td><td>134</td><td>136</td><td>136</td><td>136</td><td>136</td><td>136</td></tr><tr><td>Change (%)</td><td>0.0%</td><td>1.5%</td><td>2.2%</td><td>2.5%</td><td>0.7%</td><td>0.0%</td><td>-0.7%</td><td>-1.4%</td><td>-2.2%</td><td>0.0%</td><td>0.0%</td><td>0.0%</td><td>0.7%</td><td>0.7%</td><td>0.7%</td><td>0.0%</td><td>0.0%</td><td>-0.7%</td><td>-1.5%</td><td>0.0%</td><td>0.0%</td><td>-0.7%</td><td>-1.5%</td><td>0.0%</td><td>0.8%</td><td>1.5%</td><td>0.5%</td><td>0.0%</td><td>0.0%</td><td>0.0%</td><td>0.0%</td></tr><tr><td>HD</td><td rowspan="2">1366x768</td><td rowspan="2">Open-Cell</td><td>34</td><td>35</td><td>36</td><td>37</td><td>37</td><td>37</td><td>36</td><td>35</td><td>34</td><td>34</td><td>34</td><td>34</td><td>35</td><td>35.5</td><td>36</td><td>36</td><td>36</td><td>36</td><td>35</td><td>35</td><td>35</td><td>35</td><td>34</td><td>34</td><td>35</td><td>35</td><td>36</td><td>37</td><td>37</td><td>37</td><td>37</td></tr><tr><td>Change (%)</td><td>3.0%</td><td>2.9%</td><td>2.9%</td><td>2.8%</td><td>0.0%</td><td>0.0%</td><td>-2.7%</td><td>-2.8%</td><td>-2.9%</td><td>0.0%</td><td>0.0%</td><td>0.0%</td><td>2.9%</td><td>1.4%</td><td>1.4%</td><td>0.0%</td><td>0.0%</td><td>-2.8%</td><td>0.0%</td><td>0.0%</td><td>0.0%</td><td>-2.9%</td><td>-2.9%</td><td>0.0%</td><td>2.9%</td><td>2.9%</td><td>2.8%</td><td>0.0%</td><td>0.0%</td><td>0.0%</td><td>0.0%</td></tr><tr><td>23.8&quot;</td><td rowspan="2">FHD</td><td rowspan="2">1920x1080</td><td>Flat-LED</td><td>47.9</td><td>47.9</td><td>48.3</td><td>48.8</td><td>49.4</td><td>49.7</td><td>49.7</td><td>49.7</td><td>49.6</td><td>49.4</td><td>49.2</td><td>49.2</td><td>49.2</td><td>49.4</td><td>49.7</td><td>49.9</td><td>49.9</td><td>49.9</td><td>49.9</td><td>49.9</td><td>49.9</td><td>49.9</td><td>49.9</td><td>49.9</td><td>50.1</td><td>50.4</td><td>50.7</td><td>50.9</td><td>51.1</td><td></td></tr><tr><td>Change (%)</td><td>0.0%</td><td>0.0%</td><td>0.8%</td><td>0.8%</td><td>1.0%</td><td>1.2%</td><td>0.6%</td><td>0.0%</td><td>0.0%</td><td>-0.2%</td><td>-0.4%</td><td>-0.4%</td><td>0.0%</td><td>0.0%</td><td>0.0%</td><td>0.4%</td><td>0.6%</td><td>0.4%</td><td>0.0%</td><td>0.0%</td><td>0.0%</td><td>0.0%</td><td>0.0%</td><td>0.0%</td><td>0.0%</td><td>0.4%</td><td>0.6%</td><td>0.6%</td><td>0.4%</td><td>0.4%</td><td></td></tr><tr><td>14.0&quot;</td><td rowspan="2">WUGXU</td><td rowspan="2">1920x1201/200</td><td>Flat-LED</td><td>42.50</td><td>42.30</td><td>42.10</td><td>42.10</td><td>42.10</td><td>42.10</td><td>42.10</td><td>42.10</td><td>42.10</td><td>42.10</td><td>42.10</td><td>42.10</td><td>42.10</td><td>42.10</td><td>42.10</td><td>42.10</td><td>42.10</td><td>42.10</td><td>42.10</td><td>41.90</td><td>42.10</td><td>42.00</td><td>41.90</td><td>41.70</td><td>41.50</td><td>41.50</td><td>41.50</td><td>41.50</td><td>41.50</td><td></td></tr><tr><td>Change (%)</td><td>-0.5%</td><td>-0.5%</td><td>-0.5%</td><td>0.0%</td><td>0.0%</td><td>0.0%</td><td>0.0%</td><td>0.0%</td><td>0.0%</td><td>0.0%</td><td>0.0%</td><td>0.0%</td><td>0.0%</td><td>0.0%</td><td>0.0%</td><td>0.0%</td><td>0.0%</td><td>0.0%</td><td>0.0%</td><td>0.0%</td><td>0.0%</td><td>-0.2%</td><td>-0.2%</td><td>-0.5%</td><td>-0.5%</td><td>0.0%</td><td>0.0%</td><td>0.0%</td><td>0.0%</td><td>0.0%</td><td></td></tr><tr><td>HD</td><td rowspan="2">1366x768</td><td rowspan="2">Flat-LED</td><td>24.75</td><td>24.75</td><td>24.75</td><td>24.85</td><td>24.95</td><td>25.05</td><td>25.05</td><td>25.05</td><td>25.05</td><td>25.05</td><td>25.05</td><td>25.05</td><td>25.05</td><td>25.05</td><td>25.05</td><td>25.05</td><td>25.05</td><td>25.05</td><td>25.05</td><td>25.05</td><td>25.05</td><td>25.05</td><td>24.95</td><td>24.95</td><td>24.95</td><td>24.95</td><td>24.95</td><td>24.95</td><td>24.95</td><td>24.95</td><td></td></tr><tr><td>Change (%)</td><td>0.0%</td><td>0.0%</td><td>0.0%</td><td>0.4%</td><td>0.4%</td><td>0.4%</td><td>0.4%</td><td>0.4%</td><td>0.4%</td><td>0.4%</td><td>0.4%</td><td>0.4%</td><td>0.4%</td><td>0.4%</td><td>0.4%</td><td>0.4%</td><td>0.4%</td><td>0.4%</td><td>0.4%</td><td>0.4%</td><td>0.4%</td><td>0.4%</td><td>0.4%</td><td>0.0%</td><td>-0.4%</td><td>-0.4%</td><td>0.0%</td><td>0.0%</td><td>0.0%</td><td>0.0%</td><td></td></tr></table>

Source: TrendForce, MS

Note: To be more consistent with the industry practice, WitsView changed the way it publishes panel price quotes in January 2025. It now only provides expectations of the full-month panel price outlook on the 5th of every month, instead of specific quotes for the first half of the month. It will then provide finalized prices for the month on the 20th of every month, which will be similar to the original 2H panel pricing quotes.

## TV Panel Prices To See Stabilizing in June

TV panel prices started to edge up at the beginning of this year, rising 1% MoM in January, 2% MoM in February and 2% MoM in March. April and May were largely flat, and we see prices stabilizing into June before order momentum potentially tapers from late 2Q26.

Exhibit 3: TV Panel Price Trend (QoQ)  
![](images/896cf83104eccc74b1a26a3d64de5c134baee5f3cb410cac32699c5281cd3abe.jpg)

<details>
<summary>bar chart</summary>

TV Panel Price QoQ
| Quarter | TV Panel Price QoQ (%) |
|---|---|
| 4Q20 | 21 |
| 1Q21 | 13 |
| 2Q21 | 15 |
| 3Q21 | 12 |
| 4Q21 | 30 |
| 1Q22 | 11 |
| 2Q22 | 8 |
| 3Q22 | 7 |
| 4Q22 | 6 |
| 1Q23 | 5 |
| 2Q23 | 14 |
| 3Q23 | 13 |
| 4Q23 | 6 |
| 1Q24 | 6 |
| 2Q24 | 6 |
| 3Q24 | 6 |
| 4Q24 | 6 |
| 1Q25 | 5 |
| 2Q25 | 5 |
| 3Q25 | 6 |
| 4Q25 | 6 |
| 1Q26 | 6 |
| 2Q26E | 6 |
</details>

Source: Trendforce, MS (E) estimates

Exhibit 4: IT Panel Price (QoQ)  
![](images/484c8c21f24e63f9dca135c57b92a1bafc4b89ad97807833762f82d34f134bcc.jpg)

<details>
<summary>bar chart</summary>

| Quarter | Monitor Panel Price QoQ (%) | NB Panel Price QoQ (%) |
| :--- | :--- | :--- |
| 4Q20 | 3.5 | 7.0 |
| 1Q21 | 10.5 | 11.5 |
| 2Q21 | 15.0 | 16.0 |
| 3Q21 | 8.0 | 9.0 |
| 4Q21 | -1.0 | -2.0 |
| 1Q22 | 3.0 | 10.5 |
| 2Q22 | 14.0 | 13.0 |
| 3Q22 | 13.0 | 8.5 |
| 4Q22 | 4.5 | 5.5 |
| 1Q23 | -1.0 | -1.0 |
| 2Q23 | -0.5 | -1.0 |
| 3Q23 | -0.5 | -1.0 |
| 4Q23 | -0.5 | -1.0 |
| 1Q24 | -0.5 | -1.0 |
| 2Q24 | 3.0 | -1.0 |
| 3Q24 | -0.5 | -1.0 |
| 4Q24 | -1.0 | -1.0 |
| 1Q25 | -0.5 | -1.0 |
| 2Q25 | -0.5 | -1.0 |
| 3Q25 | -0.5 | -1.0 |
| 4Q25 | -0.5 | -1.0 |
| 1Q26 | -0.5 | -1.0 |
| 2Q26E | -0.5 | -1.0 |
</details>

Source: Trendforce, MS (E) estimates

## Panel Shipments To Be Skewed Toward 1H26

Over the past decade, TV panel shipments have averaged a 49%/51% split between 1H/2H. In 2026, we expect the mix to skew toward 1H26, as TV brands have restocked ahead of major promotional events, including the Winter Olympics in February, the FIFA World Cup in June–July, and the China 618 campaign. While we see no clear evidence that these events will significantly boost global TV demand, shipment timing has consistently shifted between quarters around such promotions.

## Display Fab Utilization to Stay at 80-85% in 2Q26

Supported by stronger TV panel shipments, display fab utilization averaged \~80% in 4Q24 and 82% in 1Q25. It declined to 78% in 2Q25 as brands turned more conservative after earlier pull-ins tapered and the impact of China's trade-in program faded. Utilization rose to 80–85% in 3Q25 as restocking resumed for year-end promotion

[中间内容因长度限制已省略]

Integrated Circuits Group Inc (603501.SS)</td><td>E (11/17/2025)</td><td>Rmb95.39</td></tr><tr><td>Phison Electronics Corp (8299.TWO)</td><td>E (02/25/2026)</td><td>NT$2,450.00</td></tr><tr><td>SG Micro Corp. (300661.SZ)</td><td>E (11/03/2025)</td><td>Rmb107.74</td></tr><tr><td>Silergy Corp. (6415.TW)</td><td>U (05/19/2026)</td><td>NT$582.00</td></tr><tr><td>SMIC (0981.HK)</td><td>O (10/21/2025)</td><td>HK$75.65</td></tr><tr><td>TSMC (2330.TW)</td><td>O (02/07/2022)</td><td>NT$2,365.00</td></tr><tr><td>UMC (2303.TW)</td><td>O (05/19/2026)</td><td>NT$131.50</td></tr><tr><td>Vanguard International Semiconductor (5347.TWO)</td><td>E (01/14/2026)</td><td>NT$161.50</td></tr><tr><td>WIN Semiconductors Corp (3105.TWO)</td><td>U (07/14/2025)</td><td>NT$483.50</td></tr><tr><td colspan="3">Daisy Dai, CFA</td></tr><tr><td>ASMPT Ltd (0522.HK)</td><td>O (07/24/2025)</td><td>HK$176.00</td></tr><tr><td>China Resources Microelectronics Limited (688396.SS)</td><td>U (03/02/2026)</td><td>Rmb66.58</td></tr><tr><td>Elan Microelectronics Corp (2458.TW)</td><td>O (10/03/2025)</td><td>NT$158.50</td></tr><tr><td>Empyrean Technology Co Ltd (301269.SZ)</td><td>E (01/17/2025)</td><td>Rmb98.73</td></tr><tr><td>Hangzhou Silan Microelectronics Co. Ltd. (600460.SS)</td><td>U (08/25/2025)</td><td>Rmb33.95</td></tr><tr><td>Innoscience (2577.HK)</td><td>E (10/13/2025)</td><td>HK$71.55</td></tr><tr><td>JCET Group Co Ltd (600584.SS)</td><td>E (01/16/2026)</td><td>Rmb75.65</td></tr><tr><td>Shanghai Fudan Microelectronics (1385.HK)</td><td>O (03/07/2025)</td><td>HK$28.80</td></tr><tr><td>SICC Co Ltd (688234.SS)</td><td>O (03/20/2026)</td><td>Rmb130.93</td></tr><tr><td>StarPower Semiconductor Ltd (603290.SS)</td><td>E (05/14/2026)</td><td>Rmb113.18</td></tr><tr><td>Unigroup Guoxin Microelectronics Co Ltd (002049.SZ)</td><td>U (01/10/2023)</td><td>Rmb75.14</td></tr><tr><td>Universal Scientific Ind. (Shanghai) (601231.SS)</td><td>O (11/05/2025)</td><td>Rmb42.66</td></tr><tr><td>Yangjie Technology (300373.SZ)</td><td>O (06/10/2022)</td><td>Rmb102.87</td></tr><tr><td colspan="3">Daniel Yen, CFA</td></tr><tr><td>AP Memory Technology Corp (6531.TW)</td><td>O (07/11/2025)</td><td>NT$1,010.00</td></tr><tr><td>ASMedia Technology Inc (5269.TW)</td><td>U (10/03/2025)</td><td>NT$1,525.00</td></tr><tr><td>Aspeed Technology (5274.TWO)</td><td>O (06/09/2025)</td><td>NT$17,505.00</td></tr><tr><td>Egis Technology Inc (6462.TWO)</td><td>E (01/28/2026)</td><td>NT$116.00</td></tr><tr><td>Espressif Systems (688018.SS)</td><td>O (05/15/2023)</td><td>Rmb120.25</td></tr><tr><td>GigaDevice Semiconductor Beijing Inc (603986.SS)</td><td>O (05/15/2025)</td><td>Rmb488.00</td></tr><tr><td>Macronix International Co Ltd (2337.TW)</td><td>O (09/18/2025)</td><td>NT$150.00</td></tr><tr><td>Montage Technology Co Ltd (6809.HK)</td><td>O (03/18/2026)</td><td>HK$368.80</td></tr><tr><td>Montage Technology Co Ltd (688008.SS)</td><td>O (03/18/2026)</td><td>Rmb239.39</td></tr><tr><td>Novatek (3034.TW)</td><td>U (02/04/2026)</td><td>NT$492.00</td></tr><tr><td>Nuvoton Technology Corporation (4919.TW)</td><td>U (11/10/2025)</td><td>NT$178.00</td></tr><tr><td>Parade Technologies Ltd (4966.TWO)</td><td>O (05/27/2026)</td><td>NT$736.00</td></tr><tr><td>Powerchip Semiconductor Manufacturing Co (6770.TW)</td><td>O (10/27/2025)</td><td>NT$74.60</td></tr><tr><td>Realtek Semiconductor (2379.TW)</td><td>E (01/30/2026)</td><td>NT$643.00</td></tr><tr><td>Shenzhen Goodix Technology Co Ltd (603160.SS)</td><td>U (07/14/2025)</td><td>Rmb55.32</td></tr><tr><td>Winbond Electronics Corp (2344.TW)</td><td>O (05/28/2026)</td><td>NT$162.00</td></tr><tr><td>WPG Holdings (3702.TW)</td><td>O (03/16/2026)</td><td>NT$114.50</td></tr><tr><td>WT Microelectronics Co. Ltd. (3036.TW)</td><td>O (01/27/2026)</td><td>NT$281.00</td></tr><tr><td colspan="3">Duan Liu</td></tr><tr><td>Dosilicon Co Ltd (688110.SS)</td><td>U (09/06/2024)</td><td>Rmb126.00</td></tr><tr><td>Shenzhen Longsys Electronics Co Ltd (301308.SZ)</td><td>E (02/25/2026)</td><td>Rmb520.01</td></tr><tr><td colspan="3">Tiffany Yeh</td></tr><tr><td>AllRing Tech Co. (6187.TWO)</td><td>O (09/23/2025)</td><td>NT$1,120.00</td></tr><tr><td>FOCI Fiber Optic Communications Inc (3363.TWO)</td><td>O (01/15/2025)</td><td>NT$908.00</td></tr><tr><td>Himax Technologies Inc (HIMX.O)</td><td>E (02/04/2026)</td><td>US$20.08</td></tr><tr><td>Hon Precision (7769.TW)</td><td>O (04/17/2026)</td><td>NT$7,275.00</td></tr><tr><td>MPI Corporation (6223.TWO)</td><td>O (04/17/2026)</td><td>NT$5,765.00</td></tr><tr><td>Silicon Motion (SIMO.O)</td><td>O (05/06/2024)</td><td>US$258.70</td></tr><tr><td>WinWay Technology Co Ltd (6515.TW)</td><td>O (04/17/2026)</td><td>NT$8,425.00</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.  
\* Historical prices are not split adjusted.

© 2026 MS
"""
