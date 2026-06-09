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

Supported by stronger TV panel shipments, display fab utilization averaged \~80% in 4Q24 and 82% in 1Q25. It declined to 78% in 2Q25 as brands turned more conservative after earlier pull-ins tapered and the impact of China's trade-in program faded. Utilization rose to 80–85% in 3Q25 as restocking resumed for year-end promotions and remained at a similar level in 4Q25 despite seasonal softness, as well as into 1Q26. We think industry utilization can remain roughly flat QoQ at 80–85% in 2Q26, as output discipline remains in place.

In the medium to long term, we maintain our view that the display segment is undergoing structural change. Chinese panel makers have shifted strategically from top-line growth to profitability, with fewer government subsidies reinforcing supply discipline. We think more investors now believe the industry's “production to order” model can remain sustainable, especially as panel price cycles shortened to quarters in 2023–24 vs. multi-year cycles in the prior decade. Consolidation moves – including LG Display's sale of its Gen 8.5 Guangzhou fab to TCL and Sharp's shutdown of its Gen 10 Sakai fab – also support a healthier supply backdrop (for more information, see Display – Structural Changes on Supply Side Not Fairly Priced In, June 17, 2021).

Exhibit 5: Industry Average Utilization at Display Fabs  
![](images/02b27791b0ee70769db69815f4b1dbcf27b4b7579d4662666731d135c4ca6443.jpg)

<details>
<summary>line chart</summary>

| Quarter | Value (%) |
|---|---|
| 1Q18 | 90 |
| 2Q18 | 91 |
| 3Q18 | 93 |
| 4Q18 | 92 |
| 1Q19 | 85 |
| 2Q19 | 88 |
| 3Q19 | 87 |
| 4Q19 | 87 |
| 1Q20 | 87 |
| 2Q20 | 87 |
| 3Q20 | 93 |
| 4Q20 | 91 |
| 1Q21 | 89 |
| 2Q21 | 91 |
| 3Q21 | 90 |
| 4Q21 | 89 |
| 1Q22 | 89 |
| 2Q22 | 80 |
| 3Q22 | 65 |
| 4Q22 | 68 |
| 1Q23 | 68 |
| 2Q23 | 80 |
| 3Q23 | 81 |
| 4Q23 | 72 |
| 1Q24 | 77 |
| 2Q24 | 84 |
| 3Q24 | 82 |
| 4Q24 | 79 |
| 1Q25 | 82 |
| 2Q25 | 78 |
| 3Q25 | 84 |
| 4Q25 | 84 |
| 1Q26 | 83 |
| 2Q26E | 83 |
</details>

Source: WitsView, MS (E) estimates

## Risk/Reward Remains Less Attractive

We believe this round of panel price hikes is coming to an end, and thus risk/reward is less attractive, especially for Taiwanese names. Below are our current views:

- AUO (2409.TW, Derrick Yang): We are EW on AUO, with a PT of NT\$14.00, based on a 0.7x 2026e P/B multiple. Although TV panel price hikes are ongoing, we think the valuation of 1.4x 2026e P/B has priced in all favorable dynamics vs. its mid-cycle average of 0.8x since 2022.  
- BOE (000725.SZ, Derrick Yang): We have a relative preference for BOE, owing to its scale advantage, more diversified revenue mix across applications and technologies, and relatively cheap valuation vs. its Chinese peer TCL. Our PT of Rmb5.20 is based on 1.4x 2026e P/B vs. its mid-cycle average of 1.2x since 2022, and we think the premium is justified by its solid industry position.  
- Innolux (3481.TW, Derrick Yang): We are EW on Innolux, with a price target of NT \$19.5

[中间内容因长度限制已省略]

td>Gudeng Precision (3680.TWO)</td><td>O (11/25/2025)</td><td>NT$520.00</td></tr><tr><td>Hua Hong Semiconductor Ltd (1347.HK)</td><td>E (03/12/2026)</td><td>HK$145.30</td></tr><tr><td>Iluvatar CoreX Semiconductor Co., Ltd. (9903.HK)</td><td>O (04/27/2026)</td><td>HK$410.00</td></tr><tr><td>King Yuan Electronics Co Ltd (2449.TW)</td><td>O (03/03/2023)</td><td>NT$309.50</td></tr><tr><td>Maxscend Microelectronics Co Ltd (300782.SZ)</td><td>U (01/11/2021)</td><td>Rmb104.77</td></tr><tr><td>MediaTek (2454.TW)</td><td>O (11/28/2025)</td><td>NT$4,300.00</td></tr><tr><td>MetaX Integrated Circuits (688802.SS)</td><td>E (04/27/2026)</td><td>Rmb710.00</td></tr><tr><td>Nanya Technology Corp. (2408.TW)</td><td>O (05/28/2026)</td><td>NT$360.00</td></tr><tr><td>NAURA Technology Group Co Ltd (002371.SZ)</td><td>O (11/06/2023)</td><td>Rmb603.36</td></tr><tr><td>OmniVision Integrated Circuits Group Inc (603501.SS)</td><td>E (11/17/2025)</td><td>Rmb95.39</td></tr><tr><td>Phison Electronics Corp (8299.TWO)</td><td>E (02/25/2026)</td><td>NT$2,450.00</td></tr><tr><td>SG Micro Corp. (300661.SZ)</td><td>E (11/03/2025)</td><td>Rmb107.74</td></tr><tr><td>Silergy Corp. (6415.TW)</td><td>U (05/19/2026)</td><td>NT$582.00</td></tr><tr><td>SMIC (0981.HK)</td><td>O (10/21/2025)</td><td>HK$75.65</td></tr><tr><td>TSMC (2330.TW)</td><td>O (02/07/2022)</td><td>NT$2,365.00</td></tr><tr><td>UMC (2303.TW)</td><td>O (05/19/2026)</td><td>NT$131.50</td></tr><tr><td>Vanguard International Semiconductor (5347.TWO)</td><td>E (01/14/2026)</td><td>NT$161.50</td></tr><tr><td>WIN Semiconductors Corp (3105.TWO)</td><td>U (07/14/2025)</td><td>NT$483.50</td></tr><tr><td colspan="3">Daisy Dai, CFA</td></tr><tr><td>ASMPT Ltd (0522.HK)</td><td>O (07/24/2025)</td><td>HK$176.00</td></tr><tr><td>China Resources Microelectronics Limited (688396.SS)</td><td>U (03/02/2026)</td><td>Rmb66.58</td></tr><tr><td>Elan Microelectronics Corp (2458.TW)</td><td>O (10/03/2025)</td><td>NT$158.50</td></tr><tr><td>Empyrean Technology Co Ltd (301269.SZ)</td><td>E (01/17/2025)</td><td>Rmb98.73</td></tr><tr><td>Hangzhou Silan Microelectronics Co. Ltd. (600460.SS)</td><td>U (08/25/2025)</td><td>Rmb33.95</td></tr><tr><td>Innoscience (2577.HK)</td><td>E (10/13/2025)</td><td>HK$71.55</td></tr><tr><td>JCET Group Co Ltd (600584.SS)</td><td>E (01/16/2026)</td><td>Rmb75.65</td></tr><tr><td>Shanghai Fudan Microelectronics (1385.HK)</td><td>O (03/07/2025)</td><td>HK$28.80</td></tr><tr><td>SICC Co Ltd (688234.SS)</td><td>O (03/20/2026)</td><td>Rmb130.93</td></tr><tr><td>StarPower Semiconductor Ltd (603290.SS)</td><td>E (05/14/2026)</td><td>Rmb113.18</td></tr><tr><td>Unigroup Guoxin Microelectronics Co Ltd (002049.SZ)</td><td>U (01/10/2023)</td><td>Rmb75.14</td></tr><tr><td>Universal Scientific Ind. (Shanghai) (601231.SS)</td><td>O (11/05/2025)</td><td>Rmb42.66</td></tr><tr><td>Yangjie Technology (300373.SZ)</td><td>O (06/10/2022)</td><td>Rmb102.87</td></tr><tr><td colspan="3">Daniel Yen, CFA</td></tr><tr><td>AP Memory Technology Corp (6531.TW)</td><td>O (07/11/2025)</td><td>NT$1,010.00</td></tr><tr><td>ASMedia Technology Inc (5269.TW)</td><td>U (10/03/2025)</td><td>NT$1,525.00</td></tr><tr><td>Aspeed Technology (5274.TWO)</td><td>O (06/09/2025)</td><td>NT$17,505.00</td></tr><tr><td>Egis Technology Inc (6462.TWO)</td><td>E (01/28/2026)</td><td>NT$116.00</td></tr><tr><td>Espressif Systems (688018.SS)</td><td>O (05/15/2023)</td><td>Rmb120.25</td></tr><tr><td>GigaDevice Semiconductor Beijing Inc (603986.SS)</td><td>O (05/15/2025)</td><td>Rmb488.00</td></tr><tr><td>Macronix International Co Ltd (2337.TW)</td><td>O (09/18/2025)</td><td>NT$150.00</td></tr><tr><td>Montage Technology Co Ltd (6809.HK)</td><td>O (03/18/2026)</td><td>HK$368.80</td></tr><tr><td>Montage Technology Co Ltd (688008.SS)</td><td>O (03/18/2026)</td><td>Rmb239.39</td></tr><tr><td>Novatek (3034.TW)</td><td>U (02/04/2026)</td><td>NT$492.00</td></tr><tr><td>Nuvoton Technology Corporation (4919.TW)</td><td>U (11/10/2025)</td><td>NT$178.00</td></tr><tr><td>Parade Technologies Ltd (4966.TWO)</td><td>O (05/27/2026)</td><td>NT$736.00</td></tr><tr><td>Powerchip Semiconductor Manufacturing Co (6770.TW)</td><td>O (10/27/2025)</td><td>NT$74.60</td></tr><tr><td>Realtek Semiconductor (2379.TW)</td><td>E (01/30/2026)</td><td>NT$643.00</td></tr><tr><td>Shenzhen Goodix Technology Co Ltd (603160.SS)</td><td>U (07/14/2025)</td><td>Rmb55.32</td></tr><tr><td>Winbond Electronics Corp (2344.TW)</td><td>O (05/28/2026)</td><td>NT$162.00</td></tr><tr><td>WPG Holdings (3702.TW)</td><td>O (03/16/2026)</td><td>NT$114.50</td></tr><tr><td>WT Microelectronics Co. Ltd. (3036.TW)</td><td>O (01/27/2026)</td><td>NT$281.00</td></tr><tr><td colspan="3">Duan Liu</td></tr><tr><td>Dosilicon Co Ltd (688110.SS)</td><td>U (09/06/2024)</td><td>Rmb126.00</td></tr><tr><td>Shenzhen Longsys Electronics Co Ltd (301308.SZ)</td><td>E (02/25/2026)</td><td>Rmb520.01</td></tr><tr><td colspan="3">Tiffany Yeh</td></tr><tr><td>AllRing Tech Co. (6187.TWO)</td><td>O (09/23/2025)</td><td>NT$1,120.00</td></tr><tr><td>FOCI Fiber Optic Communications Inc (3363.TWO)</td><td>O (01/15/2025)</td><td>NT$908.00</td></tr><tr><td>Himax Technologies Inc (HIMX.O)</td><td>E (02/04/2026)</td><td>US$20.08</td></tr><tr><td>Hon Precision (7769.TW)</td><td>O (04/17/2026)</td><td>NT$7,275.00</td></tr><tr><td>MPI Corporation (6223.TWO)</td><td>O (04/17/2026)</td><td>NT$5,765.00</td></tr><tr><td>Silicon Motion (SIMO.O)</td><td>O (05/06/2024)</td><td>US$258.70</td></tr><tr><td>WinWay Technology Co Ltd (6515.TW)</td><td>O (04/17/2026)</td><td>NT$8,425.00</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.  
\* Historical prices are not split adjusted.

© 2026 MS
"""
