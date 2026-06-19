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
June 18, 2026 08:29 AM GMT

# Investor Presentation | Japan

## Pharmaceuticals

l Top Pick: Daiichi Sankyo  
l OW (Preference order): Daiichi Sankyo, Takeda, Otsuka, Chugai  
L OW (Mid-cap and generic): Kaken, Towa  
l Industry View: In-Line

MS MUFG SECURITIES CO., LTD.+

## Shinichiro Muraoka

Equity Analyst

Shinichiro.Muraoka@morganstanleymufg.com +81 3 6836-5424

## Jaeheon Lee

Equity Analyst

Jaeheon.Lee@morganstanleymufg.com +81 3 6836-8443

![](images/ec899d602bf98df2598a5f03fd01922838b7ac58ebe03070ae0f6e8b556e4d7c.jpg)

<details>
<summary>text_image</summary>

Japan Summer School 2026
</details>

## PHARMACEUTICALS

Japan

Industry View In-Line

MS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.

## For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

+= Analysts employed by non-U.S. affiliates are not registered with FINRA, may not be associated persons of the member and may not be subject to FINRA restrictions on communications with a subject company, public appearances and trading securities held by a research analyst account.

## Table of Contents

Coverage Overview 3

Valuation/Performance 4-9

Pharmaceutical Industry Structure 10-12

FX sensitivity 13

Appendix: Pharma industry overview 14-19

Summary for Each Company 20-37

Daiichi Sankyo 20

Takeda Pharmaceutical 21

Otsuka HD 22

Chugai Pharmaceutical 23

Kaken Pharmaceutical 24

Towa Pharmaceutical 25

Astellas Pharma 26

Eisai 27

Shionogi 28

Santen Pharmaceutical 29

Tsumura 30

Sumitomo Pharma 31

SanBio 32

JCR 33

Sawai Group Holdings 34

Ono Pharmaceutical 35

Nippon Shinyaku 36

Kyowa Kirin 37

## Our Coverage Stocks

Shinichiro Muraoka

<table><tr><td>Company</td><td>Ticker</td><td>Rating</td><td>Price Target</td><td>Current Price (2026/6/16)</td><td>Upside/Downside</td><td>YTD (%)</td><td>Market cap (bn)</td></tr><tr><td>Daiichi Sankyo</td><td>4568.T</td><td>Overweight</td><td>4,650</td><td>¥2,520</td><td>85%</td><td>-25%</td><td>¥4,694</td></tr><tr><td>Takeda</td><td>4502.T</td><td>Overweight</td><td>6,300</td><td>¥5,020</td><td>25%</td><td>4%</td><td>¥7,988</td></tr><tr><td>Otsuka HD</td><td>4578.T</td><td>Overweight</td><td>14,100</td><td>¥10,360</td><td>36%</td><td>16%</td><td>¥5,625</td></tr><tr><td>Chugai</td><td>4519.T</td><td>Overweight</td><td>10,700</td><td>¥7,523</td><td>42%</td><td>-8%</td><td>¥12,632</td></tr><tr><td>Shionogi</td><td>4507.T</td><td>Equal-Weight</td><td>2,950</td><td>¥2,809</td><td>5%</td><td>-1%</td><td>¥2,499</td></tr><tr><td>Eisai</td><td>4523.T</td><td>Equal-Weight</td><td>3,800</td><td>¥3,750</td><td>1%</td><td>-19%</td><td>¥1,094</td></tr><tr><td>Astellas</td><td>4503.T</td><td>Equal-Weight</td><td>2,050</td><td>¥2,144</td><td>-4%</td><td>3%</td><td>¥3,880</td></tr><tr><td>SanBio</td><td>4592.T</td><td>Equal-Weight</td><td>1,500</td><td>¥1,175</td><td>28%</td><td>-25%</td><td>¥92</td></tr><tr><td>JCR</td><td>4552.T</td><td>Equal-Weight</td><td>500</td><td>¥448</td><td>12%</td><td>-36%</td><td>¥58</td></tr><tr><td>Ono</td><td>4528.T</td><td>Underweight</td><td>1,950</td><td>¥2,259</td><td>-14%</td><td>5%</td><td>¥1,127</td></tr><tr><td>Kyowa Kirin</td><td>4151.T</td><td>Underweight</td><td>1,800</td><td>¥2,402</td><td>-25%</td><td>-5%</td><td>¥1,262</td></tr></table>

Jaeheon Lee

<table><tr><td>Company</td><td>Ticker</td><td>Rating</td><td>Price Target</td><td>Current Price (2026/6/16)</td><td>Upside/Downside</td><td>YTD (%)</td><td>Market cap (bn)</td></tr><tr><td>Kaken</td><td>4521.T</td><td>Overweight</td><td>5,300</td><td>¥3,770</td><td>41%</td><td>-6%</td><td>¥166</td></tr><tr><td>Towa</td><td>4553.T</td><td>Overweight</td><td>5,600</td><td>¥3,875</td><td>45%</td><td>7%</td><td>¥200</td></tr><tr><td>Sumitomo Pharma</td><td>4506.T</td><td>Equal-Weight</td><td>2,200</td><td>¥1,487</td><td>48%</td><td>-35%</td><td>¥668</td></tr><tr><td>Santen</td><td>4536.T</td><td>Equal-Weight</td><td>1,900</td><td>¥1,920</td><td>-1%</td><td>19%</td><td>¥619</td></tr><tr><td>Tsumura</td><td>4540.T</td><td>Equal-Weight</td><td>4,100</td><td>¥3,761</td><td>9%</td><td>-8%</td><td>¥289</td></tr><tr><td>Sawai GHD</td><td>4887.T</td><td>Equal-Weight</td><td>2,000</td><td>¥1,651</td><td>21%</td><td>-29%</td><td>¥191</td></tr><tr><td>Nippon Shinyaku</td><td>4516.T</td><td>Underweight</td><td>2,600</td><td>¥3,986</td><td>-35%</td><td>-30%</td><td>¥280</td></tr></table>

Source: FactSet, Company, MS

Valuations for Our Coverage Stocks (1)

<table><tr><td rowspan="2">Company</td><td rowspan="2">Rating</td><td rowspan="2">PT</td><td rowspan="2">Share Price 2026/06/16</td><td rowspan="2">YTD (%)</td><td rowspan="2">Last 4 wks</td><td rowspan="2">Mkt Cap (bn)</td><td colspan="8">EPS (Adj)</td><td colspan="4">P/E*</td><td rowspan="2">EPS Growth 2025-30e</td><td rowspan="2">PEG Ratio</td></tr><tr><td>2025</td><td>2026e</td><td>2027e</td><td>2028e</td><td>2029e</td><td>2030e</td><td>2025</td><td>2026e</td><td>2027e</td><td>2028e</td><td>2029e</td><td>2030e</td></tr><tr><td>Takeda</td><td>OW</td><td>¥6,300</td><td>¥5,020</td><td>2.1%</td><td>-6.4%</td><td>¥7,988</td><td>516.8</td><td>475.5</td><td>518.1</td><td>579.2</td><td>612.8</td><td>619.1</td><td>9.7x</td><td>10.6x</td><td>9.7x</td><td>8.7x</td><td>8.2x</td><td>8.1x</td><td>4%</td><td>2.9</td></tr><tr><td>Astellas</td><td>EW</td><td>¥2,050</td><td>¥2,144</td><td>1.9%</td><td>-8.3%</td><td>¥3,880</td><td>237.0</td><td>277.1</td><td>244.1</td><td>190.7</td><td>185.5</td><td>210.6</td><td>9.0x</td><td>7.7x</td><td>8.8x</td><td>11.2x</td><td>11.6x</td><td>10.2x</td><td>-2%</td><td>(3.3)</td></tr><tr><td>Daiichi Sankyo</td><td>OW</td><td>¥4,650</td><td>¥2,520</td><td>-22.5%</td><td>0.8%</td><td>¥4,694</td><td>210.2</td><td>163.8</td><td>126.4</td><td>176.7</td><td>218.4</td><td>276.2</td><td>12.0x</td><td>15.4x</td><td>19.9x</td><td>14.3x</td><td>11.5x</td><td>9.1x</td><td>6%</td><td>2.7</td></tr><tr><td>Eisai</td><td>EW</td><td>¥3,800</td><td>¥3,750</td><td>-17.8%</td><td>-18.9%</td><td>¥1,094</td><td>136.8</td><td>182.2</td><td>247.8</td><td>253.8</td><td>261.2</td><td>236.1</td><td>27.4x</td><td>20.6x</td><td>15.1x</td><td>14.8x</td><td>14.4x</td><td>15.9x</td><td>12%</td><td>1.8</td></tr><tr><td>Otsuka</td><td>OW</td><td>¥14,100</td><td>¥10,360</td><td>19.1%</td><td>-5.9%</td><td>¥5,625</td><td>685.1</td><td>623.1</td><td>715.5</td><td>794.4</td><td>883.0</td><td>648.4</td><td>15.1x</td><td>16.6x</td><td>14.5x</td><td>13.0x</td><td>11.7x</td><td>16.0x</td><td>-1%</td><td>(15.2)</td></tr><tr><td>Chugai</td><td>OW</td><td>¥10,700</td><td>¥7,523</td><td>-7.2%</td><td>-3.6%</td><td>¥12,632</td><td>274.1</td><td>311.3</td><td>350.5</td><td>390.3</td><td>424.0</td><td>484.8</td><td>27.5x</td><td>24.2x</td><td>21.5x</td><td>19.3x</td><td>17.7x</td><td>15.5x</td><td>12%</td><td>2.0</td></tr><tr><td>Kyowa Kirin</td><td>UW</td><td>¥1,800</td><td>¥2,402</td><td>-3.2%</td><td>3.2%</td><td>¥1,262</td><td>161.3</td><td>193.7</td><td>199.6</td><td>175.2</td><td>173.7</td><td>173.7</td><td>14.9x</td><td>12.4x</td><td>12.0x</td><td>13.7x</td><td>13.8x</td><td>13.8x</td><td>1%</td><td>8.3</td></tr><tr><td>Sumitomo Pharma</td><td>EW</td><td>¥2,200</td><td>¥1,487</td><td>-35.4%</td><td>-12.4%</td><td>¥668</td><td>236.2</td><td>213.4</td><td>270.7</td><td>164.9</td><td>304.0</td><td>193.1</td><td>6.3x</td><td>7.0x</td><td>5.5x</td><td>9.0x</td><td>4.9x</td><td>7.7x</td><td>-4%</td><td>(1.8)</td></tr><tr><td>Shionogi</td><td>EW</td><td>¥2,950</td><td>¥2,809</td><td>-0.3%</td><td>-8.0%</td><td>¥2,499</td><td>248.2</td><td>349.0</td><td>327.6</td><td>331.6</td><td>277.5</td><td>250.7</td><td>11.3x</td><td>8.0x</td><td>8.6x</td><td>8.5x</td><td>10.1x</td><td>11.2x</td><td>0%</td><td>39.5</td></tr><tr><td>Nippon Shinyaku</td><td>UW</td><td>¥2,600</td><td>¥3,986</td><td>-29.7%</td><td>-6.3%</td><td>¥280</td><td>441.2</td><td>440.6</td><td>259.6</td><td>47.5</td><td>54.9</td><td>54.9</td><td>9.0x</td><td>9.0x</td><td>15.4x</td><td>84.0x</td><td>72.6x</td><td>72.6x</td><td>-34%</td><td>(0.3)</td></tr><tr><td>Kaken</td><td>OW</td><td>¥5,300</td><td>¥3,770</td><td>-5.0%</td><td>-8.1%</td><td>¥166</td><td>56.6</td><td>174.1</td><td>218.9</td><td>84.4</td><td>153.0</td><td>255.9</td><td>66.7x</td><td>21.7x</td><td>17.2x</td><td>44.7x</td><td>24.6x</td><td>14.7x</td><td>35%</td><td>0.6</td></tr><tr><td>Ono</td><td>UW</td><td>¥1,950</td><td>¥2,259</td><td>3.5%</td><td>-11.2%</td><td>¥1,127</td><td>220.3</td><td>191.7</td><td>151.3</td><td>186.4</td><td>186.2</td><td>175.6</td><td>10.3x</td><td>11.8x</td><td>14.9x</td><td>12.1x</td><td>12.1x</td><td>12.9x</td><td>-4%</td><td>(2.7)</td></tr><tr><td>Santen</td><td>EW</td><td>¥1,900</td><td>¥1,920</td><td>15.7%</td><td>1.1%</td><td>¥619</td><td>133.3</td><td>139.3</td><td>151.4</td><td>168.8</td><td>186.8</td><td>214.8</td><td>14.4x</td><td>13.8x</td><td>12.7x</td><td>11.4x</td><td>10.3x</td><td>8.9x</td><td>10%</td><td>1.4</td></tr><tr><td>Tsumura</td><td>EW</td><td>¥4,100</td><td>¥3,761</td><td>-9.1%</td><td>-2.0%</td><td>¥289</td><td>376.3</td><td>404.2</td><td>432.3</td><td>428.2</td><td>460.4</td><td>481.8</td><td>10.0x</td><td>9.3x</td><td>8.7x</td><td>8.8x</td><td>8.2x</td><td>7.8x</td><td>5%</td><td>1.8</td></tr><tr><td>JCR</td><td>EW</td><td>¥500</td><td>¥448</td><td>-34.6%</td><td>-10.7%</td><td>¥58</td><td>17.9</td><td>5.7</td><td>13.9</td><td>5.7</td><td>18.9</td><td>29.5</td><td>25.1x</td><td>78.0x</td><td>32.1x</td><td>78.0x</td><td>23.8x</td><td>15.2x</td><td>11%</td><td>7.4</td></tr><tr><td>SanBio</td><td>EW</td><td>¥1,500</td><td>¥1,175</td><td>-33.4%</td><td>-37.9%</td><td>¥92</td><td>(52.6)</td><td>(65.9)</td><td>(40.2)</td><td>(19.7)</td><td>2.1</td><td>59.7</td><td>-</td><td>-</td><td>-</td><td>-</td><td>573.1x</td><td>19.7x</td><td>-</td><td>-</td></tr><tr><td>Sawai</td><td>EW</td><td>¥2,000</td><td>¥1,651</td><td>-28.9%</td><td>-17.5%</td><td>¥191</td><td>162.1</td><td>172.7</td><td>182.2</td><td>196.9</td><td>208.2</td><td>220.4</td><td>10.2x</td><td>9.6x</td><td>9.1x</td><td>8.4x</td><td>7.9x</td><td>7.5x</td><td>6%</td><td>1.5</td></tr><tr><td>Towa</td><td>OW</td><td>¥5,600</td><td>¥3,875</td><td>3.6%</td><td>-0.3%</td><td>¥200</td><td>106.7</td><td>513.9</td><td>505.8</td><td>550.5</td><td>578.9</td><td>595.2</td><td>36.3x</td><td>7.5x</td><td>7.7x</td><td>7.0x</td><td>6.7x</td><td>6.5x</td><td>41%</td><td>0.2</td></tr><tr><td colspan="13">Pharma Avg. (Weighted)</td><td>16.8x</td><td>15.8x</td><td>15.1x</td><td>14.3x</td><td>14.3x</td><td>12.7x</td><td>5%</td><td>3.4</td></tr><tr><td colspan="21">US Pharma (covered by Terence Flynn)</td></tr><tr><td>Abbvie</td><td>OW</td><td>$278.0</td><td>$222.47</td><td>-3.2%</td><td>5.2%</td><td>$393.1</td><td>$10.0</td><td>$14.8</td><td>$17.4</td><td>$19.5</td><td>$20.7</td><td>$21.2</td><td>22.3x</td><td>15.0x</td><td>12.8x</td><td>11.4x</td><td>10.7x</td><td>10.5x</td><td>16%</td><td>1.4</td></tr><tr><td>BMY</td><td>UW</td><td>$40.0</td><td>$55.92</td><td>2.5%</td><td>-3.0%</td><td>$114.2</td><td>$6.1</td><td>$6.5</td><td>$5.9</td><td>$5.0</td><td>$4.3</td><td>$4.9</td><td>9.1x</td><td>8.6x</td><td>9.5x</td><td>11.2x</td><td>12.9x</td><td>11.4x</td><td>-4%</td><td>(2.1)</td></tr><tr><td>JNJ</td><td>OW</td><td>$283.0</td><td>$235.18</td><td>13.2%</td><td>3.9%</td><td>$566.1</td><td>$10.8</td><td>$11.8</td><td>$13.5</td><td>$15.3</td><td>$17.3</td><td>$18.9</td><td>21.8x</td><td>19.9x</td><td>17.5x</td><td>15.3x</td><td>13.6x</td><td>12.4x</td><td>12%</td><td>1.8</td></tr><tr><td>Eli Lilly</td><td>OW</td><td>$1,344.0</td><td>$1,122.50</td><td>3.5%</td><td>10.7%</td><td>$1,057.1</td><td>$24.2</td><td>$39.9</td><td>$47.1</td><td>$57.8</td><td>$64.0</td><td>$73.8</td><td>46.4x</td><td>28.1x</td><td>23.8x</td><td>19.4x</td><td>17.5x</td><td>15.2x</td><td>25%</td><td>1.9</td></tr><tr><td>Merck</td><td>EW</td><td>$112.0</td><td>$115.17</td><td>9.7%</td><td>4.4%</td><td>$284.4</td><td>$9.0</td><td>$5.3</td><td>$9.9</td><td>$11.0</td><td>$8.9</td><td>$9.5</td><td>12.8x</td><td>21.8x</td><td>11.6x</td><td>10.5x</td><td>12.9x</td><td>12.2x</td><td>1%</td><td>11.6</td></tr><tr><td>Pfizer</td><td>EW</td><td>$28.0</td><td>$26.04</td><td>4.1%</td><td>2.3%</td><td>$148.4</td><td>$3.2</td><td>$3.1</td><td>$3.0</td><td>$2.3</td><td>$2.2</td><td>$2.3</td><td>8.1x</td><td>8.5x</td><td>8.6x</td><td>11.3x</td><td>12.0x</td><td>11.5x</td><td>-7%</td><td>(1.2)</td></tr><tr><td colspan="13">US Pharma Avg. (Weighted)</td><td>29.6x</td><td>21.6x</td><td>17.9x</td><td>15.5x</td><td>14.6x</td><td>13.1x</td><td>15%</td><td>2.0</td></tr><tr><td colspan="21">EU Pharma (covered by Sarita Kapila and Thibault Boutherin)</td></tr><tr><td>AZN</td><td>OW</td><td>GBp 16,500</td><td>GBp 13,284</td><td>-2.3%</td><td>-1.2%</td><td>$276.7</td><td>$9.2</td><td>$10.1</td><td>$11.6</td><td>$12.3</td><td>$14.0</td><td>$16.4</td><td>19.5x</td><td>17.6x</td><td>15.4x</td><td>14.5x</td><td>12.8x</td><td>10.9x</td><td>12%</td><td>1.6</td></tr><tr><td>GSK</td><td>UW</td><td>GBp 1,750</td><td>GBp 1,950</td><td>-2.3%</td><td>5.9%</td><td>$106.0</td><td>GBp 172.0</td><td>GBp 182.2</td><td>GBp 199.9</td><td>GBp 199.1</td><td>GBp 197.5</td><td>GBp 190.3</td><td>11.3x</td><td>10.7x</td><td>9.8x</td><td>9.8x</td><td>9.9x</td><td>10.2x</td><td>2%</td><td>5.6</td></tr><tr><td>Novartis</td><td>OW</td><td>CHF 135</td><td>CHF 120</td><td>10.4%</td><td>3.7%</td><td>$307.1</td><td>$9.0</td><td>$8.7</td><td>$9.8</td><td>$11.1</td><td>$12.5</td><td>$13.2</td><td>16.8x</td><td>17.3x</td><td>15.4x</td><td>13.6x</td><td>12.1x</td><td>11.4x</td><td>8%</td><td>2.1</td></tr><tr><td>Novo Nordisk</td><td>EW</td><td>DKK 250</td><td>DKK 280</td><td>-12.2%</td><td>-4.6%</td><td>$147.6</td><td>DKK 26.2</td><td>DKK 21.4</td><td>DKK 20.9</td><td>DKK 21.7</td><td>DKK 22.9</td><td>DKK 25.2</td><td>10.7x</td><td>13.1x</td><td>13.4x</td><td>12.9x</td><td>12.3x</td><td>11.1x</td><td>-1%</td><td>(14.2)</td></tr><tr><td>Roche</td><td>EW</td><td>CHF 295</td><td>CHF 330</td><td>-0.7%</td><td>0.4%</td><td>$331.3</td><td>CHF 19.6</td><td>CHF 20.5</td><td>CHF 21.9</td><td>CHF 22.7</td><td>CHF 24.7</td><td>CHF 25.0</td><td>16.8x</td><td>16.1x</td><td>15.1x</td><td>14.5x</td><td>13.3x</td><td>13.2x</td><td>5%</td><td>3.4</td></tr><tr><td>Sanofi</td><td>EW</td><td>€ 90</td><td>€ 76</td><td>-9.5%</td><td>1.2%</td><td>$106.6</td><td>€ 7.8</td><td>€ 8.6</td><td>€ 9.1</td><td>€ 10.0</td><td>€ 11.0</td><td>€ 11.9</td><td>9.7x</td><td>8.8x</td><td>8.4x</td><td>7.6x</td><td>6.9x</td><td>6.3x</td><td>9%</td><td>1.1</td></tr><tr><td colspan="13">EU Pharma Avg. (Weighted)</td><td>15.6x</td><td>15.3x</td><td>14.0x</td><td>13.1x</td><td>12.0x</td><td>11.2x</td><td>7%</td><td>2.3</td></tr><tr><td colspan="21">Biotech (covered by Terence Flynn)</td></tr><tr><td>Amgen</td><td>EW</td><td>$340.0</td><td>$222.0</td><td>4.4%</td><td>4.7%</td><td>$187.7</td><td>$21.8</td><td>$22.6</td><td>$23.0</td><td>$25.8</td><td>$28.8</td><td>$32.1</td><td>10.2x</td><td>9.8x</td><td>9.7x</td><td>8.6x</td><td>7.7x</td><td>6.9x</td><td>8%</td><td>1.3</td></tr><tr><td>Gilead</td><td>OW</td><td>$168.0</td><td>$127.2</td><td>2.2%</td><td>-2.5%</td><td>$158.0</td><td>$8.1</td><td>$0.7</td><td>$9.8</td><td>$10.6</td><td>$12.1</td><td>$13.8</td><td>15.6x</td><td>-186.0x</td><td>12.9x</td><td>12.0x</td><td>10.5x</td><td>9.2x</td><td>11%</td><td>1.4</td></tr><tr><td>Biogen</td><td>EW</td><td>$206.0</td><td>$195.6</td><td>12.9%</td><td>3.0%</td><td>$28.9</td><td>$15.3</td><td>$15.8</td><td>$15.2</td><td>$14.9</td><td>$10.7</td><td>$11.2</td><td>12.8x</td><td>12.4x</td><td>12.9x</td><td>13.2x</td><td>18.2x</td><td>17.4x</td><td>-6%</td><td>(2.1)</td></tr><tr><td>Vertex</td><td>OW</td><td>$616.0</td><td>$453.2</td><td>1.2%</td><td>5.0%</td><td>$115.0</td><td>$18.4</td><td>$18.7</td><td>$20.1</td><td>$22.4</td><td>$27.2</td><td>$33.1</td><td>24.6x</td><td>24.2x</td><td>22.5x</td><td>20.2x</td><td>16.7x</td><td>13.7x</td><td>12%</td><td>2.0</td></tr><tr><td>Regeneron</td><td>EW</td><td>$788.0</td><td>$614.7</td><td>-21.2%</td><td>-12.8%</td><td>$63.3</td><td>$44.2</td><td>$46.4</td><td>$54.2</td><td>$62.5</td><td>$70.0</td><td>$75.1</td><td>13.9x</td><td>13.3x</td><td>11.3x</td><td>9.8x</td><td>8.8x</td><td>8.2x</td><td>11%</td><td>1.2</td></tr><tr><td colspan="13">Biotech Avg. (Weighted)</td><td>15.3x</td><td>-42.6x</td><td>13.6x</td><td>12.4x</td><td>11.0x</td><td>9.7x</td><td>9%</td><td>1.6</td></tr></table>

Note 1: For Japanese companies, Note 3: e = MS Estimates, Chugai, Kiyawa Kirin and Otsuka (Dec FY-end). Note 2: EPS estimates for Kaken, Eisuk, JCR, and SanBio are on a reported basis, and EPS estimates for other companies exclude one-off factors and goodwill amortization. Note 3: e = MS Estimates, Chugai, Kiyawa Kirin and Otsuka (Dec FY-end).

Valuations for Our Coverage Stocks (2)

<table><tr><td>Company</td><td>Rating</td><td>PT</td><td>Share Price 2026/06/16</td><td>YTD (%)</td><td>Last 4 wks</td><td>Mkt Cap (bn)</td><td>EV (25) (bn)</td><td>2025</td><td>2026e</td><td>2027e</td><td>2028e</td><td>2029e</td><td>2030e</td><td>2025</td><td>2026e</td><td>2027e</td><td>2028e</td><td>2029e</td><td>2030e</td><td>P/B 2025</td><td>DY (%)</td></tr><tr><td>Takeda</td><td>OW</td><td>¥6,300</td><td>¥5,020</td><td>2.1%</td><td>-6.4%</td><td>¥7,988</td><td>¥12,275</td><td>7.7x</td><td>8.6x</td><td>8.6x</td><td>7.9x</td><td>7.6x</td><td>7.6x</td><td>2.7x</td><td>2.8x</td><td>2.4x</td><td>2.0x</td><td>1.5x</td><td>1.2x</td><td>1.0x</td><td>4.0%</td></tr><tr><td>Astellas</td><td>EW</td><td>¥2,050</td><td>¥2,144</td><td>1.9%</td><td>-8.3%</td><td>¥3,880</td><td>¥4,155</td><td>7.1x</td><td>6.3x</td><td>7.3x</td><td>9.0x</td><td>9.3x</td><td>8.2x</td><td>0.5x</td><td>0.0x</td><td>-0.7x</td><td>-1.5x</td><td>-2.0x</td><td>-2.2x</td><td>2.1x</td><td>3.6%</td></tr><tr><td>Daiichi Sankyo</td><td>OW</td><td>¥4,650</td><td>¥2,520</td><td>-22.5%</td><td>0.8%</td><td>¥4,694</td><td>¥4,439</td><td>14.1x</td><td>10.0x</td><td>8.8x</td><td>9.4x</td><td>7.8x</td><td>6.3x</td><td>-0.8x</td><td>-0.6x</td><td>-0.8x</td><td>-0.9x</td><td>-0.8x</td><td>-0.9x</td><td>2.8x</td><td>3.1%</td></tr><tr><td>Eisai</td><td>EW</td><td>¥3,800</td><td>¥3,750</td><td>-17.8%</td><td>-18.9%</td><td>¥1,094</td><td>¥1,033</td><td>12.3x</td><td>9.4x</td><td>7.7x</td><td>7.6x</td><td>7.6x</td><td>8.2x</td><td>-0.7x</td><td>-0.2x</td><td>0.1x</td><td>0.1x</td><td>0.1x</td><td>-0.1x</td><

[中间内容因长度限制已省略]

 RMB Investment Advisory (Proprietary) Limited, which is wholly owned by FirstRand Limited. The information in MS is being disseminated by MS Saudi Arabia, regulated by the Capital Market Authority in the Kingdom of Saudi Arabia, and is directed at Sophisticated investors only.

MS Hong Kong Securities Limited is the liquidity provider/market maker for securities of Otsuka Holdings listed on the Stock Exchange of Hong Kong Limited. An updated list can be found on HKEx website: http://www.hkex.com.hk.

The information in MS is being communicated by MS & Co. International plc (DIFC Branch), regulated by the Dubai Financial Services Authority (the DFSA) or by MS & Co. International plc (ADGM Branch), regulated by the Financial Services Regulatory Authority Abu Dhabi (the FSRA), and is directed at Professional Clients only, as defined by the DFSA or the FSRA, respectively. The financial products or financial services to which this research relates will only be made available to a customer who we are satisfied meets the regulatory criteria of a Professional Client. A distribution of the different MS Research ratings or recommendations, in percentage terms for Investments in each sector covered, is available upon request from your sales representative.

The information in MS is being communicated by MS & Co. International plc (QFC Branch), regulated by the Qatar Financial Centre Regulatory Authority (the QFCRA), and is directed at business customers and market counterparties only and is not intended for Retail Customers as defined by the QFCRA.

As required by the Capital Markets Board of Turkey, investment information, comments and recommendations stated here, are not within the scope of investment advisory activity. Investment advisory service is provided exclusively to persons based on their risk and income preferences by the authorized firms. Comments and recommendations stated here are general in nature. These opinions may not fit to your financial status, risk and return preferences. For this reason, to make an investment decision by relying solely to this information stated here may not bring about outcomes that fit your expectations.

The trademarks and service marks contained in MS are the property of their respective owners. Third-party data providers make no warranties or representations relating to the accuracy, completeness, or timeliness of the data they provide and shall not have liability for any damages relating to such data. The Global Industry Classification Standard (GICS) was developed by and is the exclusive property of MSCI and S&P.

MS, or any portion thereof may not be reprinted, sold or redistributed without the written consent of MS.

Indicators and trackers referenced in MS may not be used as, or treated as, a benchmark under Regulation EU 2016/1011, or any other similar framework.

The issuers and/or fixed income products recommended or discussed in certain fixed income research reports may not be continuously followed. Accordingly, investors should regard those fixed income research reports as providing stand-alone analysis and should not expect continuing analysis or additional reports relating to such issuers and/or individual fixed income products.

MS may hold, from time to time, material financial and commercial interests regarding the company subject to the Research report.

Registration granted by SEBI and certification from the National Institute of Securities Markets (NISM) in no way guarantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.

INDUSTRY COVERAGE: Pharmaceuticals

<table><tr><td>COMPANY (TICKER)</td><td>RATING (AS OF)</td><td>PRICE* (06/18/2026)</td></tr><tr><td>Jaeheon Lee</td><td></td><td></td></tr><tr><td>Kaken Pharmaceutical (4521.T)</td><td>O (11/18/2024)</td><td>¥3,800</td></tr><tr><td>Nippon Shinyaku (4516.T)</td><td>U (08/27/2025)</td><td>¥4,023</td></tr><tr><td>Santen Pharmaceutical (4536.T)</td><td>E (09/03/2025)</td><td>¥1,889</td></tr><tr><td>Sawai Group Holdings (4887.T)</td><td>E (06/12/2026)</td><td>¥1,653</td></tr><tr><td>Sumitomo Pharma (4506.T)</td><td>E (08/22/2025)</td><td>¥1,525</td></tr><tr><td>Towa Pharmaceutical (4553.T)</td><td>O (06/12/2026)</td><td>¥3,670</td></tr><tr><td>Tsumura (4540.T)</td><td>E (06/25/2025)</td><td>¥3,722</td></tr></table>

Shinichiro Muraoka

<table><tr><td>Astellas Pharma (4503.T)</td><td>E (03/06/2024)</td><td>¥2,175</td></tr><tr><td>Chugai Pharmaceutical (4519.T)</td><td>O (04/24/2023)</td><td>¥7,566</td></tr><tr><td>Daiichi Sankyo (4568.T)</td><td>O (03/30/2019)</td><td>¥2,706</td></tr><tr><td>Eisai (4523.T)</td><td>E (09/28/2022)</td><td>¥3,969</td></tr><tr><td>JCR Pharmaceuticals (4552.T)</td><td>E (06/06/2024)</td><td>¥475</td></tr><tr><td>Kyowa Kirin (4151.T)</td><td>U (03/06/2026)</td><td>¥2,505</td></tr><tr><td>Ono Pharmaceutical (4528.T)</td><td>U (02/22/2023)</td><td>¥2,277</td></tr><tr><td>Otsuka Holdings (4578.T)</td><td>O (01/23/2026)</td><td>¥10,830</td></tr><tr><td>SanBio (4592.T)</td><td>E (03/28/2024)</td><td>¥1,103</td></tr><tr><td>Shionogi (4507.T)</td><td>E (03/03/2016)</td><td>¥2,833</td></tr><tr><td>Takeda Pharmaceutical (4502.T)</td><td>O (01/13/2026)</td><td>¥5,037</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.  
\* Historical prices are not split adjusted.

© 2026 MS MUFG
"""
