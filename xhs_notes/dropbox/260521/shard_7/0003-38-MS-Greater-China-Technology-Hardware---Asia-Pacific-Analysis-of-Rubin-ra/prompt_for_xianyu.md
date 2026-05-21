你是闲鱼资料类商品文案编辑，擅长把一份投研/行业/公司研报改写成适合闲鱼发布的商品说明。

【目标】
- 基于下面研报解析内容，生成一份可以复制到闲鱼商品详情里的中文文案。
- 风格参考用户提供的闲鱼对标笔记：标题直给、信息密度高、用途明确、适合人群明确、交付方式清楚。
- 语言要自然，像真实卖家发布，不要像公众号文章、小红书笔记或 AI 摘要。
- 不要使用太夸张的营销词，不要承诺收益，不要说“稳赚”“内幕”“必涨”。
- 可以适度口语化，但不要低俗。

【必须输出结构】
1. `闲鱼标题：` 一行，控制在 30 字以内，适合商品标题。
2. `商品描述：` 正文，适合直接粘贴到闲鱼详情页。
3. `Hashtag：` 一行，给 6-10 个平台可用标签，用 `#` 开头，空格分隔。

【严禁输出】
- 不要输出 `建议价格：`。
- 不要输出 `搜索关键词：`。
- 不要输出“搜索词”“关键词”“搜索关键词”等栏目。
- 不要给具体价格区间、成交承诺或价格建议。

【商品描述写法】
- 第一段：直接说明这是什么报告，页数/语言/主题/公司或行业。如果页数、日期、语言不确定，就不要编。
- 第二段：说明适合谁，比如投研、券商面试、PE/VC、行业研究、学习参考、写报告等。
- 第三段：用 3-5 个亮点 bullet，风格参考：
  ✅ 三大情景框架：DCF、P/ARR、EV/Sales
  ✅ 关键变量分析
  ✅ 估值逻辑、假设、终值占比等核心内容覆盖
  ✅ 适合准备 AI 相关面试、研究 AI 估值的同学
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
# Greater China Technology Hardware | Asia Pacific Analysis of Rubin rack BOM, component content, and ODM value-added

Rubin rack ASP is at \~US\$7.8M buying from ODMs; price point is higher buying from OEMs. Biggest downstream content increase comes from PCB (+233%), MLCC (+182%), ABF (+82%), Power (+32%), and Cooling (+12%). But ODM value-added will also increase 35-40%, contrary to market view.

The Rubin rack will cost \~US\$7.8M: This is the price hyperscalers will be paying for a Rubin rack from ODMs; the price of a Rubin rack will be even higher if bought from OEMs (i.e., Lenovo, Asustek, Giga-Byte, Dell, etc). Most components will enjoy a rise in content, driven by increased complexity, computing density, and power density, among other things. Within the downstream components made by companies we cover, we estimate that PCB content will increase the most vs. Blackwell (+233%), followed by MLCC (+182%), ABF substrates (+82%), power (+32%), and cooling (+12%).

Rubin ODM value-added will also increase 35-40%: Our bottom-up analysis aligns with what Wistron's management said on its 4Q earnings call: that ODM value-added in dollar terms would increase for Rubin. The 35-40% increase is spread throughout the rack, with increased complexity across the computing board, computing tray, switch board, switch tray, cooling components, and rack-level assembly, as well as new boards to assemble/test. But there are other things ODMs can do that are not captured in our numbers. That said, based on the numbers that our analysis captures, the implied GM for a Rubin rack is \~1.9% (vs. \~2.7% for GB300). Again, however, we think investors should focus on the increase in absolute dollar profitability and not the decline in margins.

More ODMs are talking about the consignment business model: Hon Hai was the first to mention it, during its 4Q25 call. And at its 1Q26 earnings call, Quanta also mentioned that it expects some projects to shift over to a consignment business model in 2H26. It looks like this shift is slowly happening, and more customers are willing to help share the increased working capital burden. It remains unclear what percentage of projects will shift to consignment, but we do view this trend positively over the long-term.

Our post-earnings ODM preference: Wiwynn is our Top Pick in ODMs, followed by Wistron > Quanta > Hon Hai, based on upside to our price targets. Risk-reward for the ODM cohort still looks attractive at only \~13x CY27e P/E on average vs. the \~11.5x average over the past \~20 years. For component suppliers, we like Delta, AVC, Unimicron, ZDT, and FIT.

MS TAIWAN LIMITED+

# Howard Kao

Equity Analyst

Howard.Kao@morganstanley.com +886 2 2730-2989

# Irene Yen

Research Associate

Irene.Yen@morganstanley.com +886 2 2730-2869

# Sharon Shih

Equity Analyst

Sharon.Shih@morganstanley.com +886 2 2730-2865

# GREATER CHINA TECHNOLOGY HARDWARE

Asia Pacific

Industry View

In-Line

MS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.

# For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

+= Analysts employed by non-U.S. affiliates are not registered with FINRA, may not be associated persons of the member and may not be subject to FINRA restrictions on communications with a subject company, public appearances and trading securities held by a research analyst account.

# Bottom-Up Analysis of VR200 Rack BOM

We estimate that a Rubin rack will cost \~US\$7.8M, if bought from the ODMs: A big portion of the increase in rack cost is from memory prices, which have increased materially since Nvidia first launched GB200 NVL72. With the old memory prices, memory was only 5-10% of GB200 NVL72 rack bill of materials – but with the increased memory content and significantly higher pricing now, we estimate that memory is now 25-30% of the VR200 rack bill of materials. This drives the GPU content down from \~65% in GB200 to \~51% for VR200. This rack ASP is our estimate for what the ODMs will charge/receive from the cloud customers, but the pricing from the OEMs (i.e., Lenovo, Asustek, Giga-Byte, Dell, etc.) will be even higher, after including brand profit and other charges, which will vary by company.

Hyperscalers could be buying the SOCAMM themselves: Our base case is that Nvidia will buy the SOCAMM that goes onto the Rubin compute board, and resell at a 70% GM. In this base case scenario, the Rubin rack ASP would be \~US\$7.8M, as mentioned above and throughout the note. However, in the scenario where the SOCAMMs are acquired by the hyperscalers directly, the rack ASP would drop to \~US\$6.7M for a Rubin rack.

Exhibit 1: Owing to recent increase in memory prices, memory will become 25%+ of the rack BOM for Rubin   
![](images/2bc6cc102c22614c147a8624483c031f7547adc7663a2ab3a3181b8c8378b563.jpg)  
Source: MS estimates.

Exhibit 2: We estimate the new upcoming VR200 rack ASP to be \~US\$7.8mn   
Nvidia NVL72 Rack ASP (US\$)   
![](images/01357eea32a66ed9d1901cc914f145a5e09843a2f631c8adbe1ee13d0d7cfc5a.jpg)

<details>
<summary>bar</summary>

| Category | Value |
|---|---|
| GB200 | 3,329,523 |
| GB300 | 3,994,551 |
| VR200 | 7,803,148 |
</details>

Source: MS estimates.

Memory is not the only component showing a content increase: In our coverage, cooling components, power supply, PCB, ABF substrates, and MLCC, among others, are also all showing content increases. Other than a meaningful increase in memory content for the Rubin, for downstream components made by companies under our coverage, we see the biggest content increase for PCB (+233%), followed by MLCCs (+182%), ABF substrates (+82%), power supply (+32%), and cooling (+12%). And we believe the pure rack assembly value-added will also increase, \~30%, driven by increased complexity of the rack design.

Exhibit 3: We estimate that a single VR200 NVL72 rack will cost \~US\$7.8M 

<table><tr><td>Nvidia NVL72 Bill of Materials</td><td>GB300</td><td>VR200</td></tr><tr><td>GPU</td><td>$2,520,000</td><td>$3,960,000</td></tr><tr><td>CPU</td><td>$180,000</td><td>$180,000</td></tr><tr><td>NVLink Switch chip</td><td>$64,800</td><td>$144,000</td></tr><tr><td>Other networking chips</td><td>$261,000</td><td>$576,000</td></tr><tr><td>Memory</td><td>$373,939</td><td>$2,001,600</td></tr><tr><td>Cooling</td><td>$64,610</td><td>$72,080</td></tr><tr><td>Power supply</td><td>$57,600</td><td>$76,000</td></tr><tr><td>PCB</td><td>$35,100</td><td>$116,730</td></tr><tr><td>ABF Substrate</td><td>$11,160</td><td>$20,340</td></tr><tr><td>MLCC</td><td>$1,530</td><td>$4,320</td></tr><tr><td>Others</td><td>$402,412</td><td>$623,278</td></tr><tr><td>Rack assembly value add</td><td>$22,400</td><td>$28,800</td></tr><tr><td>Total</td><td>$3,994,551</td><td>$7,803,148</td></tr></table>

<table><tr><td>Diff.</td></tr><tr><td>57%</td></tr><tr><td>0%</td></tr><tr><td>122%</td></tr><tr><td>121%</td></tr><tr><td>435%</td></tr><tr><td>12%</td></tr><tr><td>32%</td></tr><tr><td>233%</td></tr><tr><td>82%</td></tr><tr><td>182%</td></tr><tr><td>55%</td></tr><tr><td>29%</td></tr><tr><td>95%</td></tr></table>

Source: MS estimates.

# Rubin PCB content is rising meaningfully

Rubin PCB content is showing the biggest increase amongst downstream components: Based on our supply chain checks, we see PCB content increasing massively, 233%+, for Rubin v. GB300. This would bring total PCB content up to \~US\$117K, vs only just \~US\$35K in GB300, which would be a big tailwind for the PCB suppliers, including Unimicron and ZDT in our coverage.

This meaningful jump in content is driven by an increase in PCBs, with the introduction of new modules like the ConnectX module and the midplane PCB, but there is an increase in layer count and CCL-grade for PCBs as well. For example, the computing board for Rubin is now a 26L board vs a 22L HDI PCB in GB300, and the CCL-grade is upgraded to M8 vs. M7 for Blackwell.

In addition, the dimensions of the computing board are also slightly larger in Rubin vs. Blackwell. Moreover, the switch tray PCB for Rubin is now a 32L PCB vs a 24L PCB for Blackwell.

All of this adds to the meaningful increase in PCB content. There is also a new midplane PCB in the computing tray (44L) that was previously not found in the GB300 rack, which also adds to the content growth.

Exhibit 4: VR200 PCB Content is 200%+ higher than that of GB300 

<table><tr><td>PCB ASP per board (US$)</td><td>GB300</td><td>VR200</td></tr><tr><td>Compute PCB</td><td>$650</td><td>$1,400</td></tr><tr><td>Switch PCB</td><td>$800</td><td>$1,450</td></tr><tr><td>Midplane PCB</td><td>$0</td><td>$1,500</td></tr><tr><td>BlueField PCB</td><td>$0</td><td>$255</td></tr><tr><td>ConnectX PCB</td><td>$0</td><td>$270</td></tr><tr><td>Other peripheral PCB</td><td>$50</td><td>$50</td></tr><tr><td>PCB Units per rack</td><td>GB300</td><td>VR200</td></tr><tr><td>Compute PCB</td><td>36x</td><td>36x</td></tr><tr><td>Switch PCB</td><td>9x</td><td>9x</td></tr><tr><td>Midplane PCB</td><td>0x</td><td>18x</td></tr><tr><td>BlueField PCB</td><td>18x</td><td>18x</td></tr><tr><td>ConnectX PCB</td><td>0x</td><td>72x</td></tr><tr><td>Other peripheral PCB</td><td>90x</td><td>45x</td></tr><tr><td>Total PCB Content per rack</td><td>GB300</td><td>VR200</td></tr><tr><td>Compute PCB</td><td>$23,400</td><td>$50,400</td></tr><tr><td>Switch PCB</td><td>$7,200</td><td>$13,050</td></tr><tr><td>Midplane PCB</td><td>$0</td><td>$27,000</td></tr><tr><td>BlueField PCB</td><td>$0</td><td>$4,590</td></tr><tr><td>ConnectX PCB</td><td>$0</td><td>$19,440</td></tr><tr><td>Other peripheral PCB</td><td>$4,500</td><td>$2,250</td></tr><tr><td>Total PCB Content per rack</td><td>$35,100</td><td>$116,730</td></tr></table>

Source: MS estimates.

# MLCC is showing a significant content increase

Based on our latest estimates, we estimate MLCC content for VR200 to be \~US\$4.3K:

This would present a quite meaningful increase vs. GB300 at only \~US\$1.5K, and could explain why high-end AI server MLCC demand is currently so strong and causing all the ODMs to aggressively trying to secure and build as much inventory as possible, ahead of the Rubin rack ramp from 2H26 on wards.

Our checks indicate that the MLCC content per computing board and switch board is increasing quite meaningfully, with the computing board MLCC content showing a larger content increase. In addition, the newly introduced BlueField and ConnectX modules will also contribute to more MLCC content per rack.

Exhibit 5: VR200 MLCC content is 180%+ higher compared to GB300 

<table><tr><td>MLCC content per board (US$)</td><td>GB300</td><td>VR200</td></tr><tr><td>Compute PCB</td><td>$25</td><td>$90</td></tr><tr><td>Switch PCB</td><td>$20</td><td>$45</td></tr><tr><td>BlueField DPU Module</td><td>$5</td><td>$5</td></tr><tr><td>ConnectX Orchid Module</td><td>$5</td><td>$5</td></tr><tr><td>Other peripheral PCB</td><td>$5</td><td>$5</td></tr><tr><td>Units per rack</td><td>GB300</td><td>VR200</td></tr><tr><td>Compute PCB</td><td>36x</td><td>36x</td></tr><tr><td>Switch PCB</td><td>9x</td><td>9x</td></tr><tr><td>BlueField DPU Module</td><td>0x</td><td>18x</td></tr><tr><td>ConnectX Orchid Module</td><td>0x</td><td>72x</td></tr><tr><td>Other peripheral PCB</td><td>90x</td><td>45x</td></tr><tr><td>Total MLCC Content per rack</td><td>GB300</td><td>VR200</td></tr><tr><td>Compute PCB</td><td>$900</td><td>$3,240</td></tr><tr><td>Switch PCB</td><td>$180</td><td>$405</td></tr><tr><td>BlueField DPU Module</td><td>$0</td><td>$90</td></tr><tr><td>ConnectX Orchid Module</td><td>$0</td><td>$360</td></tr><tr><td>Other peripheral PCB</td><td>$450</td><td>$225</td></tr><tr><td>Total MLCC Content per rack</td><td>$1,530</td><td>$4,320</td></tr></table>

Source: MS estimates.

# We estimate that ABF substrate content is also growing, driven by higher ASP per substrate and increased number of substrates

# We estimate that ABF substrate content for VR200 will increase $\sim 82\%$ vs. GB300:

Aside from content increases for the substrates themselves per chip, such as for the Rubin GPU and Vera CPU vs. its predecessor, there is also an increased number of substrates used per Rubin rack. This is because there are 2x more NVLink and ConnectX chips in the Rubin system vs. the Blackwell system. According to MS analyst Shoji Sato, the Rubin GPU ABF substrate ASP will rise to \~US\$200 per chip. which is up 100% vs. Blackwell at \~US\$100 of substrate content per chip.

Exhibit 6: VR200 ABF Substrate content is 80%+ higher compared to GB300 

<table><tr><td>ABF Substrate ASP per chip (US$)</td><td>GB300</td><td>VR200</td></tr><tr><td>GPU</td><td>$100</td><td>$200</td></tr><tr><td>CPU</td><td>$50</td><td>$60</td></tr><tr><td>NVSwitch ASIC</td><td>$30</td><td>$30</td></tr><tr><td>BlueField DPU</td><td>$30</td><td>$30</td></tr><tr><td>ConnectX chip</td><td>$30</td><td>$30</td></tr><tr><td>ABF Units per rack</td><td>GB300</td><td>VR200</td></tr><tr><td>GPU</td><td>72x</td><td>72x</td></tr><tr><td>CPU</td><td>36x</td><td>36x</td></tr><tr><td>NVSwitch ASIC</td><td>18x</td><td>36x</td></tr><tr><td>BlueField DPU</td><td>18x</td><td>18x</td></tr><tr><td>ConnectX chip</td><td>36x</td><td>72x</td></tr><tr><td>Total ABF Content per rack</td><td>GB300</td><td>VR200</td></tr><tr><td>GPU</td><td>$7,200</td><td>$14,400</td></tr><tr><td>CPU</td><td>$1,800</td><td>$2,160</td></tr><tr><td>NVSwitch ASIC</td><td>$540</td><td>$1,080</td></tr><tr><td>BlueField DPU</td><td>$540</td><td>$540</td></tr><tr><td>ConnectX chip</td><td>$1,080</td><td>$2,160</td></tr><tr><td>Total ABF Content per rack</td><td>$11,160</td><td>$20,340</td></tr></table>

Source: MS estimates.

# Clear AI server power upgrade path

Our latest supply chain checks suggest that besides the standard 110kW power shelf to be featured in the Vera Rubin platform, one US CSP is adopting HVDC standalone power rack in the Vera Rubin platform. For large-scale adoption, we expect 800V DC to be adopted in Nvidia's Rubin Ultra platform, scheduled for 2H27. Delta is also working with at least three US CSP customers on HVDC platform adoption in ASIC power rack projects, with initial rollout expected starting 2H26.

Exhibit 7: AI server power solution roadmap to 800 VDC architecture 

<table><tr><td>Server power supply design</td><td colspan="4">Power shelf</td><td colspan="2">HVDC Standalone power rack</td></tr><tr><td>AC-DC conversion</td><td>400V AC &gt;&gt; 50V DC</td><td>400V AC &gt;&gt; 50V DC</td><td>400V AC &gt;&gt; 50V DC</td><td>400V AC &gt;&gt; 50V DC</td><td>400V AC &gt;&gt; 800V DC</td><td>400V AC &gt;&gt; 800V DC</td></tr><tr><td>Nvidia AI GPU generation</td><td>GB200</td><td>GB300</td><td>GB300</td><td>Vera Rubin</td><td>Vera Rubin CPX version</td><td>Vera Rubin Ultra</td></tr><tr><td>Nvidia AI server rack architecture</td><td>Oberon</td><td>Oberon</td><td>Oberon</td><td>Oberon</td><td>Oberon</td><td>Kyber</td></tr><tr><td>Power wattage per server rack</td><td>120kW</td><td>140kW</td><td>140kW</td><td>200kW+</td><td>380kW+</td><td>600kW</td></tr><tr><td>Power wattage per PSU</td><td>5.5kW</td><td>8kW</td><td>12kW</td><td>18.3kW</td><td>18.3kW</td><td>30kW</td></tr><tr><td>Power value per AI server rack</td><td>US$36,000 (x)</td><td>US$57,600</td><td>US$69,120</td><td>US$76,000</td><td>US$398,160</td><td>&gt;10x</td></tr><tr><td>Power value per watt</td><td>US$0.3</td><td>US$0.41</td><td>US$0.49</td><td>US$0.38</td><td>US$1.05</td><td>...</td></tr></table>

Source: MS

# Liquid cooling content value growth

Vera Rubin server racks will be fully liquid-cooled: the fan-less design would increase the offering value per tray via i

[中间内容因长度限制已省略]

nternational (1590.TW)</td><td>O (04/16/2025)</td><td>NT$1,405.00</td></tr><tr><td>AU Optronics (2409.TW)</td><td>E (02/10/2026)</td><td>NT$18.75</td></tr><tr><td>Bizlink (3665.TW)</td><td>O (03/10/2025)</td><td>NT$1,965.00</td></tr><tr><td>BOE Technology (000725.SZ)</td><td>O (09/06/2019)</td><td>Rmb4.31</td></tr><tr><td>Chenbro (8210.TW)</td><td>O (07/23/2025)</td><td>NT$1,285.00</td></tr><tr><td>Chroma Ate Inc. (2360.TW)</td><td>O (10/05/2021)</td><td>NT$2,065.00</td></tr><tr><td>E Ink Holdings Inc. (8069.TWO)</td><td>O (05/11/2026)</td><td>NT$222.00</td></tr><tr><td>Ennostar Inc (3714.TW)</td><td>U (09/23/2022)</td><td>NT$67.40</td></tr><tr><td>Hiwin Technologies Corp. (2049.TW)</td><td>O (03/30/2026)</td><td>NT$359.50</td></tr><tr><td>Innolux (3481.TW)</td><td>E (04/07/2025)</td><td>NT$36.95</td></tr><tr><td>King Slide Works Co. Ltd. (2059.TW)</td><td>O (11/08/2023)</td><td>NT$4,500.00</td></tr><tr><td>Lens Technology (300433.SZ)</td><td>E (07/22/2020)</td><td>Rmb37.96</td></tr><tr><td>Radiant Opto-Electronics Corporation (6176.TW)</td><td>E (03/01/2024)</td><td>NT$104.50</td></tr><tr><td>Sanan Optoelectronics (600703.SS)</td><td>U (08/21/2023)</td><td>Rmb16.85</td></tr><tr><td>TCL Corp. (000100.SZ)</td><td>E (04/07/2025)</td><td>Rmb4.30</td></tr><tr><td>Tianma Microelectronics (000050.SZ)</td><td>U (01/24/2018)</td><td>Rmb7.52</td></tr><tr><td>Wuhan Jingce Electronic Group Co Ltd (300567.SZ)</td><td>E (11/26/2021)</td><td>Rmb187.50</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.   
\* Historical prices are not split adjusted.   
Howard Kao 

<table><tr><td>Acer Inc. (2353.TW)</td><td>U (04/23/2025)</td><td>NT$27.45</td></tr><tr><td>Asustek Computer Inc. (2357.TW)</td><td>U (11/16/2025)</td><td>NT$640.00</td></tr><tr><td>Compal Electronics (2324.TW)</td><td>U (04/23/2025)</td><td>NT$27.60</td></tr><tr><td>FIT Hon Teng Ltd (6088.HK)</td><td>O (11/03/2025)</td><td>HK$8.80</td></tr><tr><td>Giga-Byte Technology Co. Ltd. (2376.TW)</td><td>E (11/16/2025)</td><td>NT$302.00</td></tr><tr><td>Gold Circuit Electronics Ltd. (2368.TW)</td><td>O (10/06/2022)</td><td>NT$1,235.00</td></tr><tr><td>Inspur Electronic Information (000977.SZ)</td><td>E (08/28/2023)</td><td>Rmb72.23</td></tr><tr><td>Lenovo (0992.HK)</td><td>E (11/16/2025)</td><td>HK$12.71</td></tr><tr><td>Lotes Co. Ltd. (3533.TW)</td><td>E (05/12/2025)</td><td>NT$2,360.00</td></tr><tr><td>Nan Ya PCB (8046.TW)</td><td>O (02/23/2026)</td><td>NT$829.00</td></tr><tr><td>Pegatron Corporation (4938.TW)</td><td>E (03/25/2026)</td><td>NT$77.20</td></tr><tr><td>Quanta Computer Inc. (2382.TW)</td><td>O (05/01/2023)</td><td>NT$290.00</td></tr><tr><td>Shengyi Technology Co Ltd. (600183.SS)</td><td>E (05/26/2022)</td><td>Rmb100.78</td></tr><tr><td>Shennan Circuits Co Ltd (002916.SZ)</td><td>E (08/24/2023)</td><td>Rmb332.30</td></tr><tr><td>Unimicron (3037.TW)</td><td>O (02/23/2026)</td><td>NT$823.00</td></tr><tr><td>Wistron Corporation (3231.TW)</td><td>O (07/12/2023)</td><td>NT$132.50</td></tr><tr><td>Wiwynn Corp (6669.TW)</td><td>O (11/10/2025)</td><td>NT$4,910.00</td></tr><tr><td>Yageo Corp. (2327.TW)</td><td>O (10/28/2025)</td><td>NT$520.00</td></tr><tr><td>Zhen Ding (4958.TW)</td><td>O (05/18/2026)</td><td>NT$439.00</td></tr><tr><td colspan="3">Sharon Shih</td></tr><tr><td>Asia Vital Components Co. Ltd. (3017.TW)</td><td>O (07/30/2024)</td><td>NT$2,340.00</td></tr><tr><td>Auras Technology Co Ltd (3324.TWO)</td><td>E (05/04/2023)</td><td>NT$966.00</td></tr><tr><td>Catcher Technology (2474.TW)</td><td>U (11/17/2025)</td><td>NT$183.00</td></tr><tr><td>Delta Electronics Inc. (2308.TW)</td><td>O (07/13/2017)</td><td>NT$1,915.00</td></tr><tr><td>Fositek Corp (6805.TW)</td><td>O (06/25/2025)</td><td>NT$1,720.00</td></tr><tr><td>Foxconn Industrial Internet Co. Ltd. (601138.SS)</td><td>O (07/10/2019)</td><td>Rmb68.56</td></tr><tr><td>Foxconn Technology (2354.TW)</td><td>U (04/23/2025)</td><td>NT$57.50</td></tr><tr><td>GoerTek Inc (002241.SZ)</td><td>U (04/23/2025)</td><td>Rmb25.72</td></tr><tr><td>Hon Hai Precision (2317.TW)</td><td>O (03/15/2024)</td><td>NT$240.00</td></tr><tr><td>LandMark Optoelectronics Corporation (3081.TWO)</td><td>E (03/26/2026)</td><td>NT$2,490.00</td></tr><tr><td>Lingyi Itech Guangdong Co (002600.SZ)</td><td>U (04/23/2025)</td><td>Rmb16.91</td></tr><tr><td>Lite-On Technology (2301.TW)</td><td>E (01/15/2025)</td><td>NT$204.00</td></tr><tr><td>Luxshare Precision Industry Co., Ltd. (002475.SZ)</td><td>O (10/24/2016)</td><td>Rmb72.40</td></tr><tr><td>Sunonwealth Electric Machine Industry Co (2421.TW)</td><td>E (02/23/2024)</td><td>NT$143.00</td></tr><tr><td>Tong Hsing (6271.TW)</td><td>E (03/18/2019)</td><td>NT$187.50</td></tr><tr><td>Visual Photonics Epitaxy Co Ltd (2455.TW)</td><td>E (09/11/2023)</td><td>NT$400.50</td></tr></table>

© 2026 MS
"""
