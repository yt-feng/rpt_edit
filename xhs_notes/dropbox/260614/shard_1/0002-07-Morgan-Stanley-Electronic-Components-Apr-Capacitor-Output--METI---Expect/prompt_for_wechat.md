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
June 12, 2026 08:22 AM GMT

## Electronic Components | Japan

# Apr Capacitor Output (METI): Expect Continuing Expansion of Demand for Small, Large-capacity MLCCs

METI production stats show Japan MLCC output value converted into US\$ -10.4% YoY and +11.8% MoM in Apr. MLCC shipment value in US\$ according to MoF trade stats was +16.0% YoY and +9.1% MoM.

## Key Takeaways

It is unclear why MLCC production stats show domestic output value in US\$ falling YoY while trade stats show export value increasing.  
We raise our forecast for MLCC shipment value in 2026 from \$16.48bn (+12.4% YoY) to \$17.43bn (+18.8% YoY).  
Demand for small, large-capacity MLCCs for AI/DC use seems likely to continue expanding.

Ceramic capacitors (MLCCs): Apr output ¥70.9bn (-1.1% YoY, +12.0% MoM), with average selling price (ASP) of ¥0.63 (-20.0% YoY, +1.4% MoM). In US\$ terms, production value of \$445.50mn was -10.4% YoY from \$497.25mn and +11.8% MoM from \$398.56mn, while ASP of 0.399¢ was -27.5% YoY from 0.550¢ and +1.2% MoM from 0.394¢.

AECs: Apr production ¥16.5bn (+3.2% YoY, -3.1% MoM), with ASP of ¥19.1 (+0.3% YoY, -1.1% MoM). In US\$, production value of \$103.77mn was -6.4% YoY from \$110.91mn and -3.3% MoM from \$107.35mn, while ASP of 12.03¢ was -9.1% YoY from 13.24¢ and -1.3% MoM from 12.19¢.

Trade stats show MLCC export value in US\$ +16.0% YoY, +9.1% MoM: Trade stats published by MOF on May 28 showed Apr MLCC export value at ¥74.2bn (+28.0% YoY, +9.3% MoM), export volume at 93.1bn units (+10.4%, +6.5%), and ASP at ¥0.797 (+15.9%, +2.6%). In US\$, export value of \$466.23mn was +16.0% YoY from \$402.05mn and +9.1% MoM from \$427.52mn, while ASP of 0.501¢ rose 5.0% YoY from 0.477¢ and 2.4% MoM from 0.489¢.

We raise our global MLCC shipment value forecasts: We estimate that global MLCC shipment value was \$14.67bn in 2025 (+10.3% YoY) and raise our forecasts from \$16.48bn (+12.4% YoY) to \$17.43bn (+18.8%) for 2026, \$18.34bn (+11.2%) to \$20.89bn (+19.9%) for 2027, and \$20.30bn (+10.7%) to \$24.25bn (+16.1%) for 2028. We expect AI/data center-related demand for value-added products to continue expanding in and after 2026.

MS MUFG SECURITIES CO., LTD.+

## Shoji Sato

Equity Analyst

Shoji.Sato@morganstanleymufg.com +81 3 6836-8404

## Sota Harashima

Equity Analyst

Sota.Harashima@morganstanleymufg.com +81 3 6836-8897

![](images/8a1cebffa41b1005ef4dccab644401df16a2dc89b1bda918dad5bb4798ce878a.jpg)

<details>
<summary>text_image</summary>

Japan Summer School 2026
</details>

## ELECTRONIC COMPONENTS

## Japan

Industry View

In-Line

Domestic production of ceramic capacitors  
![](images/09e0ed3df85d464cdacc1e9f1fb1d4ff5dc4d387da425c16a12fb6948f5bd005.jpg)

<details>
<summary>line chart</summary>

| Date   | Ceramic Capacitor ASP (LS) | YoY % Change of Production Amount(RS) |
|--------|----------------------------|----------------------------------------|
| 04/41  | ~0.5                       | ~0%                                    |
| 05/31  | ~0.5                       | ~0%                                    |
| 06/31  | ~0.5                       | ~0%                                    |
| 07/31  | ~0.5                       | ~0%                                    |
| 08/31  | ~0.5                       | ~0%                                    |
| 09/31  | ~0.2                       | ~-50%                                  |
| 10/31  | ~0.8                       | ~100%                                  |
| 11/31  | ~0.4                       | ~0%                                    |
| 12/31  | ~0.4                       | ~0%                                    |
| 1/31   | ~0.4                       | ~0%                                    |
| 2/31   | ~0.4                       | ~0%                                    |
| 3/31   | ~0.4                       | ~0%                                    |
| 4/31   | ~0.4                       | ~0%                                    |
| 5/31   | ~0.4                       | ~0%                                    |
| 6/31   | ~0.4                       | ~0%                                    |
| 7/31   | ~0.4                       | ~0%                                    |
| 8/31   | ~0.4                       | ~0%                                    |
| 9/31   | ~0.4                       | ~0%                                    |
| 10/31  | ~0.4                       | ~0%                                    |
| 11/31  | ~0.4                       | ~0%                                    |
| 12/31  | ~0.4                       | ~0%                                    |
| 1/31   | ~0.4                       | ~0%                                    |
| 2/31   | ~0.4                       | ~0%                                    |
| 3/31   | ~0.4                       | ~0%                                    |
| ...    | ...                        | ...                                    |
| 26/61  | ~0.4                       | ~0%                                    |
</details>

Domestic production of AECs  
![](images/22c0aa7f542e1ed2da836a7f807f371d6e40720542ee78d8f2283190163381d2.jpg)

<details>
<summary>line chart</summary>

| Date   | Aluminum Capacitor ASP (LS) | YoY % Change of Production Amount (RS) |
|--------|-----------------------------|----------------------------------------|
| 04/1   | ~13.5                       | ~0%                                    |
| 05/1   | ~12.5                       | ~-5%                                   |
| 06/1   | ~13.0                       | ~0%                                    |
| 07/1   | ~12.0                       | ~5%                                    |
| 08/1   | ~11.5                       | ~-10%                                  |
| 09/1   | ~6.0                        | ~-50%                                  |
| 10/1   | ~21.0                       | ~100%                                  |
| 11/1   | ~12.0                       | ~50%                                   |
| 12/1   | ~9.0                        | ~-50%                                  |
| 1/1    | ~13.0                       | ~0%                                    |
| 2/1    | ~12.5                       | ~5%                                    |
| 3/1    | ~13.0                       | ~10%                                   |
| 4/1    | ~12.5                       | ~5%                                    |
| 5/1    | ~13.0                       | ~10%                                   |
| 6/1    | ~12.5                       | ~5%                                    |
| 7/1    | ~13.0                       | ~10%                                   |
| 8/1    | ~12.5                       | ~5%                                    |
| 9/1    | ~13.0                       | ~10%                                   |
| 10/1   | ~12.5                       | ~5%                                    |
| 11/1   | ~13.0                       | ~10%                                   |
| 12/1   | ~12.5                       | ~5%                                    |
| 1/1    | ~13.0                       | ~10%                                   |
| 2/1    | ~12.5                       | ~5%                                    |
| 3/1    | ~13.0                       | ~10%                                   |
| 4/1    | ~12.5                       | ~5%                                    |
| 5/1    | ~13.0                       | ~10%                                   |
| 6/1    | ~12.5                       | ~5%                                    |
</details>

Source: METI, MS

MS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.

## For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

+= Analysts employed by non-U.S. affiliates are not registered with FINRA, may not be associated persons of the member and may not be subject to FINRA restrictions on communications with a subject company, public appearances and trading securities held by a research analyst account.

## Raise global MLCC shipment value forecast

As Exhibit 1 shows, global MLCC shipment value declined for two consecutive years, from \$17.47bn in 2021 (+26.0% YoY) to \$14.32bn in 2022 (-18.1%) and \$12.64bn in 2023 (-11.7%), before rising again to \$13.30bn in 2024 (+5.2%) and \$14.67bn in 2025 (+10.3%). We increase our forecasts for shipment value from \$16.48bn (+12.4% YoY) to \$17.43bn (+18.8% YoY) for 2026, from \$18.34bn (+11.2%) to \$20.89bn (+19.9%) for 2027, and from \$20.30bn (+10.7%) to \$24.25bn (+16.1%) for 2028.

We foresee ongoing expansion in demand for value-added products for AI/DC use from 2026. This application and the shift to a new generation of GPUs will require large quantities of MLCCs with large capacity owing to space constraints for chip-use ABF package substrates and AI accelerator boards. (1) Murata is a frontrunner in miniaturization and increased capacity; (2) although MLCCs generally experience a reduction in capacitance when a DC voltage is applied, Murata's MLCCs maintain a large effective capacitance with minimal change; (3) Murata's MLCCs also have the characteristic of maintaining stable capacitance during high-frequency operation, where currents in electronic circuits switch rapidly. We think these features are likely to create more opportunities for customers to pay premium prices for Murata's high-quality and highly reliable products. Some market participants expect MLCC unit prices to rise for similar products, but we forecast that unit prices for comparable products will continue to decline mildly. In contrast, as miniaturization and increased capacity progress, we think it likely that Murata will increase sales with differentiated high value-added products, and see a clearer difference in profit margins compared to other MLCC companies. We think a key risk for Murata would be if it were unable to ramp up production to meet surging demand in computing areas, such as AI servers/data centers, and it lost share as a result of sacrificing supply capacity of MLCCs for other applications in order to respond to rising demand. However, our view is that it will be able to increase production in line with rising demand.

Exhibit 1: Global MLCC market forecasts

<table><tr><td>Base Case</td><td>2007</td><td>2008</td><td>2009</td><td>2010</td><td>2011</td><td>2012</td><td>2013</td><td>2014</td><td>2015</td><td>2016</td><td>2017</td><td>2018</td><td>2019</td><td>2020</td><td>2021</td><td>2022</td><td>2023</td><td>2024</td><td>2025</td><td>2026e</td><td>2027e</td><td>2028e</td><td>2029e</td><td>2030e</td><td>2031e</td></tr><tr><td>Total worldwide shipment quantity (Bil pcs)</td><td>1,504</td><td>1,480</td><td>1,640</td><td>2,050</td><td>2,029</td><td>2,167</td><td>2,293</td><td>2,605</td><td>2,735</td><td>3,080</td><td>3,480</td><td>3,828</td><td>3,254</td><td>3,695</td><td>4,446</td><td>3,572</td><td>3,187</td><td>3,386</td><td>3,773</td><td>4,037</td><td>4,360</td><td>4,709</td><td>5,086</td><td>5,493</td><td>5,932</td></tr><tr><td>YoY (%)</td><td>14.9%</td><td>-1.6%</td><td>10.8%</td><td>24.9%</td><td>-1.0%</td><td>6.8%</td><td>5.8%</td><td>13.6%</td><td>5.0%</td><td>12.6%</td><td>13.0%</td><td>10.0%</td><td>-15.0%</td><td>13.5%</td><td>20.3%</td><td>-19.7%</td><td>-10.8%</td><td>6.2%</td><td>11.4%</td><td>7.0%</td><td>8.0%</td><td>8.0%</td><td>8.0%</td><td>8.0%</td><td>8.0%</td></tr><tr><td>CAGR (1991~)</td><td>14.9%</td><td>13.8%</td><td>13.7%</td><td>14.2%</td><td>13.4%</td><td>13.1%</td><td>12.8%</td><td>12.8%</td><td>12.5%</td><td>12.5%</td><td>12.5%</td><td>12.4%</td><td>11.3%</td><td>11.4%</td><td>11.6%</td><td>10.5%</td><td>9.7%</td><td>9.6%</td><td>9.7%</td><td>9.6%</td><td>9.6%</td><td>9.5%</td><td>9.5%</td><td>9.4%</td><td>9.4%</td></tr><tr><td>ASP in worldwide shipment (Cent)</td><td>0.47</td><td>0.42</td><td>0.36</td><td>0.38</td><td>0.39</td><td>0.36</td><td>0.33</td><td>0.30</td><td>0.29</td><td>0.26</td><td>0.27</td><td>0.37</td><td>0.39</td><td>0.38</td><td>0.39</td><td>0.40</td><td>0.40</td><td>0.39</td><td>0.39</td><td>0.43</td><td>0.48</td><td>0.52</td><td>0.54</td><td>0.55</td><td>0.57</td></tr><tr><td>YoY (%)</td><td>-0.2%</td><td>-10.1%</td><td>-14.0%</td><td>6.8%</td><td>1.2%</td><td>-7.7%</td><td>-7.2%</td><td>-10.6%</td><td>-4.1%</td><td>-7.2%</td><td>3.8%</td><td>34.3%</td><td>4.6%</td><td>-2.8%</td><td>4.7%</td><td>2.0%</td><td>-1.0%</td><td>-1.0%</td><td>-1.0%</td><td>11.0%</td><td>11.0%</td><td>7.5%</td><td>4.0%</td><td>3.0%</td><td>3.0%</td></tr><tr><td>CAGR (1991~)</td><td>-8.6%</td><td>-8.7%</td><td>-9.0%</td><td>-8.2%</td><td>-7.8%</td><td>-7.8%</td><td>-7.7%</td><td>-7.9%</td><td>-7.7%</td><td>-7.7%</td><td>-7.3%</td><td>-6.0%</td><td>-5.6%</td><td>-5.5%</td><td>-5.2%</td><td>-5.0%</td><td>-4.9%</td><td>-4.8%</td><td>-4.6%</td><td>-4.2%</td><td>-3.8%</td><td>-3.5%</td><td>-3.4%</td><td>-3.2%</td><td>-3.0%</td></tr><tr><td>Total worldwide shipment value (Bil $)</td><td>7.00</td><td>6.19</td><td>5.90</td><td>7.87</td><td>7.89</td><td>7.77</td><td>7.63</td><td>7.75</td><td>7.80</td><td>8.15</td><td>9.56</td><td>14.13</td><td>12.56</td><td>13.86</td><td>17.47</td><td>14.32</td><td>12.64</td><td>13.30</td><td>14.67</td><td>17.43</td><td>20.89</td><td>24.25</td><td>27.24</td><td>30.30</td><td>33.71</td></tr><tr><td>YoY (%)</td><td>14.6%</td><td>-11.6%</td><td>-4.7%</td><td>33.4%</td><td>0.2%</td><td>-1.5%</td><td>-1.8%</td><td>1.6%</td><td>0.7%</td><td>4.5%</td><td>17.3%</td><td>47.7%</td><td>-11.1%</td><td>10.3%</td><td>26.0%</td><td>-18.1%</td><td>-11.7%</td><td>5.2%</td><td>10.3%</td><td>18.8%</td><td>19.9%</td><td>16.1%</td><td>12.3%</td><td>11.2%</td><td>11.2%</td></tr><tr><td>CAGR (1991~)</td><td>5.0%</td><td>4.0%</td><td>3.5%</td><td>4.8%</td><td>4.6%</td><td>4.3%</td><td>4.0%</td><td>3.9%</td><td>3.8%</td><td>3.8%</td><td>4.3%</td><td>5.7%</td><td>5.0%</td><td>5.2%</td><td>5.8%</td><td>5.0%</td><td>4.4%</td><td>4.4%</td><td>4.6%</td><td>5.0%</td><td>5.3%</td><td>5.6%</td><td>5.8%</td><td>5.9%</td><td>6.1%</td></tr></table>

Note: e=MS estimates  
Source: MS

## US\$ MLCC export value in trade stats +16.0% YoY, +9.1% MoM

Trade stats published by MOF on May 28 show April MLCC export value at ¥74.2bn (+28.0% YoY, +9.3% MoM), export volume at 93.1bn units (+10.4%, +6.5%), and ASP at ¥0.797 (+15.9%, +2.6%). In US\$ terms, export value of \$466.23mn was up 16.0% YoY from \$402.05mn and up 9.1% MoM from \$427.52mn, while ASP of 0.501¢ rose 5.0% YoY from 0.477¢ and rose 2.4% MoM from 0.489¢. The trade stats data do not provide a fully accurate picture of how ASP has changed on a same-product basis, but from export values, volumes, and ASP by destination region and customs post, on a same-product basis, we believe price declines have moderated, while ASPs have risen both YoY and MoM due to an improved product mix. For Greater China (China, Taiwan, and Hong Kong), which accounted for 57.7% of exports in April, volumes increased 0.1% MoM, US\$ export value increased 7.5%, and US\$ ASP rose 7.4%.

At major customs points, values were \$92.33mn at Narita (+26.9% YoY, +4.1% MoM) with ASP at 1.18¢ (+1.5%, -1.7%), \$152.30mn at Osaka (+0.8%, +13.7%) with ASP at 0.50¢ (-5.1%, +4.9%), and \$64.06mn at Kansai International (+34.0%, -6.8%) with ASP at 0.25¢ (-12.0%, +9.3%).

Exhibit 2: MLCC export value and ASP  
![](images/5974626aae8aa7fa0208795d22f27949f74ccabf9e42ae6f4c178f48056f6201.jpg)

<details>
<summary>bar-line hybrid chart</summary>

| Month | Narita (mn USD) | Osaka (mn USD) | Kansai airport (mn USD) | Kansai Airport ASP (cent) | Other (mn USD) | Narita ASP (mn USD) |
| --- | --- | --- | --- | --- | --- | --- |
| Jan 2019 | 300 | 250 | 100 | 0.4 | 300 | 1.2 |
| Apr 2019 | 320 | 260 | 110 | 0.45 | 320 | 1.25 |
| Jul 2019 | 340 | 270 | 120 | 0.5 | 340 | 1.3 |
| Oct 2019 | 360 | 280 | 130 | 0.55 | 360 | 1.35 |
| Jan 2020 | 380 | 290 | 140 | 0.6 | 380 | 1.4 |
| Apr 2020 | 400 | 300 | 150 | 0.65 | 400 | 1.45 |
| Jul 2020 | 420 | 310 | 160 | 0.7 | 420 | 1.5 |
| Oct 2020 | 440 | 320 | 170 | 0.75 | 440 | 1.55 |
| Jan 2021 | 460 | 330 | 180 | 0.8 | 460 | 1.6 |
| Apr 2021 | 480 | 340 | 190 | 0.85 | 480 | 1.65 |
| Jul 2021 | 500 | 350 | 200 | 0.9 | 500 | 1.7 |
| Oct 2021 | 520 | 360 | 210 | 0.95 | 520 | 1.75 |
| Jan 2022 | 540 | 370 | 220 | 1.0 | 540 | 1.8 |
| Apr 2022 | 560 | 380 | 230 | 1.05 | 560 | 1.85 |
| Jul 2022 | 580 | 390 | 240 | 1.1 | 580 | 1.9 |
| Oct 2022 | 600 | 400 | 250 | 1.15 | 600 | 1.95 |
| Jan 2023 | 620 | 410 | 260 | 1.2 | 620 | 2.0 |
| Apr 2023 | 640 | 420 | 270 | 1.25 | 640 | 2.05 |
| Jul 2023 | 660 | 430 | 280 | 1.3 | 660 | 2.1 |
| Oct 2023 | 680 | 440 | 290 | 1.35 | 680 | 2.15 |
| Jan 2024 | 700 | 450 | 300 | 1.4 | 700 | 2.2 |
| Apr 2024 | 720 | 460 | 310 | 1.45 | 720 | 2.25 |
| Jul 2024 | 740 | 470 | 320 | 1.5 | 740 | 2.3 |
| Oct 2024 | 760 | 480 | 330 | 1.55 | 760 | 2.35 |
</details>

Source: MoF trade data, MS

Exhibit 3: MLCC export value and ASP (Narita)  
![](images/b21e1c3d5bbc9279576fe59c3dcd449f78d0aa13d07408c14245d219c342373f.jpg)

<details>
<summary>bar-line hybrid chart</summary>

| Month | Narita shipment value (mn USD) | Narita ASP (cent) |
| --- | --- | --- |
| Jan | ~65 | ~1.1 |
| Apr | ~70 | ~1.1 |
| Jul | ~75 | ~1.1 |
| Oct | ~70 | ~1.1 |
| Jan | ~65 | ~1.1 |
| Apr | ~70 | ~1.1 |
| Jul | ~75 | ~1.1 |
| Oct | ~80 | ~1.1 |
| Jan | ~75 | ~1.1 |
| Apr | ~80 | ~1.1 |
| Jul | ~85 | ~1.1 |
| Oct | ~90 | ~1.1 |
| Jan | ~85 | ~1.1 |
| Apr | ~90 | ~1.1 |
| Jul | ~95 | ~1.1 |
| Oct | ~90 | ~1.1 |
| Jan | ~85 | ~1.1 |
| Apr | ~90 | ~1.1 |
| Jul | ~95 | ~1.1 |
| Oct | ~90 | ~1.1 |
| Jan | ~85 | ~1.1 |
</details>

Source: MoF trade data, MS

Exhibit 4: MLCC export value and ASP (Osaka)  
![](images/ce0f35e0036a4eee0ed3b415bbb51ea9fd77f0df0a8984a39ab8f1a5424d7914.jpg)

<details>
<summary>bar-line hybrid chart</summary>

| Month-Year | Osaka shipment value (mn USD) | Osaka ASP (cent) |
|------------|--------------------------------|------------------|
| Jan 2019   | ~190                           | ~0.60            |
| Apr 2019   | ~230                           | ~0.55            |
| Jul 2019   | ~250                           | ~0.50            |
| Oct 2019   | ~240                           | ~0.48            |
| Jan 2020   | ~230                           | ~0.47         

[中间内容因长度限制已省略]

 owned equally by MS International Holdings Inc. and RMB Investment Advisory (Proprietary) Limited, which is wholly owned by FirstRand Limited. The information in MS is being disseminated by MS Saudi Arabia, regulated by the Capital Market Authority in the Kingdom of Saudi Arabia, and is directed at Sophisticated investors only.

The information in MS is being communicated by MS & Co. International plc (DIFC Branch), regulated by the Dubai Financial Services Authority (the DFSA) or by MS & Co. International plc (ADGM Branch), regulated by the Financial Services Regulatory Authority Abu Dhabi (the FSRA), and is directed at Professional Clients only, as defined by the DFSA or the FSRA, respectively. The financial products or financial services to which this research relates will only be made available to a customer who we are satisfied meets the regulatory criteria of a Professional Client. A distribution of the different MS Research ratings or recommendations, in percentage terms for Investments in each sector covered, is available upon request from your sales representative.

The information in MS is being communicated by MS & Co. International plc (QFC Branch), regulated by the Qatar Financial Centre Regulatory Authority (the QFCRA), and is directed at business customers and market counterparties only and is not intended for Retail Customers as defined by the QFCRA.

As required by the Capital Markets Board of Turkey, investment information, comments and recommendations stated here, are not within the scope of investment advisory activity. Investment advisory service is provided exclusively to persons based on their risk and income preferences by the authorized firms. Comments and recommendations stated here are general in nature. These opinions may not fit to your financial status, risk and return preferences. For this reason, to make an investment decision by relying solely to this information stated here may not bring about outcomes that fit your expectations.

The trademarks and service marks contained in MS are the property of their respective owners. Third-party data providers make no warranties or representations relating to the accuracy, completeness, or timeliness of the data they provide and shall not have liability for any damages relating to such data. The Global Industry Classification Standard (GICS) was developed by and is the exclusive property of MSCI and S&P.

MS, or any portion thereof may not be reprinted, sold or redistributed without the written consent of MS.

Indicators and trackers referenced in MS may not be used as, or treated as, a benchmark under Regulation EU 2016/1011, or any other similar framework.

The issuers and/or fixed income products recommended or discussed in certain fixed income research reports may not be continuously followed. Accordingly, investors should regard those fixed income research reports as providing stand-alone analysis and should not expect continuing analysis or additional reports relating to such issuers and/or individual fixed income products. MS may hold, from time to time, material financial and commercial interests regarding the company subject to the Research report.

Registration granted by SEBI and certification from the National Institute of Securities Markets (NISM) in no way guarantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.

INDUSTRY COVERAGE: Electronic Components

<table><tr><td>COMPANY (TICKER)</td><td>RATING (AS OF)</td><td>PRICE* (06/12/2026)</td></tr><tr><td>Shoji Sato</td><td></td><td></td></tr><tr><td>ALPS ALPINE (6770.T)</td><td>O (03/17/2026)</td><td>¥2,017</td></tr><tr><td>Hamamatsu Photonics (6965.T)</td><td>U (09/17/2025)</td><td>¥2,496</td></tr><tr><td>Ibiden (4062.T)</td><td>U (02/04/2026)</td><td>¥19,105</td></tr><tr><td>Kyocera (6971.T)</td><td>E (06/25/2020)</td><td>¥3,671</td></tr><tr><td>Mabuchi Motor (6592.T)</td><td>E (11/03/2022)</td><td>¥1,524</td></tr><tr><td>Minebea Mitsumi (6479.T)</td><td>E (10/23/2025)</td><td>¥4,233</td></tr><tr><td>Murata Manufacturing (6981.T)</td><td>O (11/26/2025)</td><td>¥8,556</td></tr><tr><td>Nidec (6594.T)</td><td>NR (09/05/2025)</td><td>¥2,627</td></tr><tr><td>Niterra (5334.T)</td><td>O (01/17/2024)</td><td>¥9,967</td></tr><tr><td>Taiyo Yuden (6976.T)</td><td>E (10/19/2023)</td><td>¥15,725</td></tr><tr><td>TDK (6762.T)</td><td>O (08/02/2022)</td><td>¥3,504</td></tr><tr><td>Sota Harashima</td><td></td><td></td></tr><tr><td>CMK (6958.T)</td><td>E (02/28/2025)</td><td>¥721</td></tr><tr><td>Daishinku (6962.T)</td><td>E (03/07/2024)</td><td>¥1,006</td></tr><tr><td>Hirose Electric (6806.T)</td><td>O (07/10/2024)</td><td>¥27,420</td></tr><tr><td>IRISO Electronics (6908.T)</td><td>E (08/02/2022)</td><td>¥2,920</td></tr><tr><td>Japan Aviation Electronics Industry (6807.T)</td><td>E (01/17/2024)</td><td>¥2,300</td></tr><tr><td>KOA (6999.T)</td><td>U (11/04/2025)</td><td>¥2,515</td></tr><tr><td>Meiko Electronics (6787.T)</td><td>E (04/03/2026)</td><td>¥30,850</td></tr><tr><td>Nichicon (6996.T)</td><td>E (11/10/2021)</td><td>¥3,895</td></tr><tr><td>Nihon Dempa Kogyo (6779.T)</td><td>E (03/07/2024)</td><td>¥3,815</td></tr><tr><td>Nippon Chemi-Con (6997.T)</td><td>U (09/20/2024)</td><td>¥4,175</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.  
\* Historical prices are not split adjusted.
"""
