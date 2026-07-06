你是财经类 AI Podcast 制作人，擅长把研报内容改写成中文、英文两条独立的访谈式播客脚本。

【目标】
- 基于下面研报解析内容，写两份 podcast 脚本：一份中文，一份英文。
- 每份目标时长约 5 分钟。
- 两份都要是“访谈聊天式”，不是单人念稿。
- 听感：像一位主持人和一位研究员围绕报告做深度但自然的讨论。
- 不要使用 emoji。
- 不要把全文讲完，要留下 1-2 个“完整报告里会继续展开”的悬念。

【输出格式必须严格遵守】
- 中文部分只能使用 `ZH_A:` 和 `ZH_B:` 开头。
- 英文部分只能使用 `EN_A:` 和 `EN_B:` 开头。
- 每一句独立成行。
- 不要输出 Markdown 标题。
- 不要输出舞台说明、音效说明或括号注释。
- 先输出完整中文脚本，再输出完整英文脚本。

【角色设定】
- A 是主持人：负责提问、转场、替听众追问“所以这意味着什么”。
- B 是研究员：负责解释报告逻辑、给出结构化判断和保留悬念。
- 两个角色必须频繁轮换，避免一个人连续说超过 3 句。
- 每句要适合 TTS 朗读：短句、自然、不要太书面。

【中文脚本结构】
1. 开场：A 用一个问题引出报告价值，B 给出主判断。
2. 第一部分：这份报告真正要回答的问题是什么。
3. 第二部分：2-3 个关键洞察，每个洞察都要有“这意味着什么”。
4. 第三部分：哪些问题仍然没有完全展开，为什么值得继续读完整报告。
5. 结尾：自然引导听众加入社群/阅读完整报告，不要硬广。

【英文脚本结构】
- 英文不是中文逐句翻译，而是面向英文听众重新组织。
- 保留同样的主线和洞察，但表达更口语、更 podcast。
- Use natural conversational English.
- Avoid long sentences and avoid reading like a research memo.

【内容边界】
- 可以基于研报内容做适度发散，但必须是从原文逻辑推出的判断。
- 不要编造具体数据、公司动作或引用。
- 对不确定内容要用“这里仍需要继续验证”或 “the report does not fully answer this yet” 表达。
- 默认避免出现具体投行品牌名，比如“GS”“GS”，统一写作“投行研报”或 “a global investment bank report”。

【研报解析内容】
"""
# Memory Semis Monthly July '26 Edition: Further pricing upside amidst LTA negotiations

## Upside to 2H26 memory pricing

Based upon our industry checks, we increase base-line DDR contract pricing to +32% QoQ in 3Q26 (was +17%) and +18% QoQ in 4Q26 (was +12%), after +67% QoQ in 2Q26. Depending upon pricing under longer term agreements (LTAs), as well as HBM pricing and mix, the QoQ ASP comparisons will vary though by memory vendor. We continue to forecast the DRAM industry to be undersupplied until at least 2Q28. The gap between bit demand growth in 2027 (+36.2% YoY) and supply (+19.3%) is too wide to close by then. If we assume no inventory digestion downstream in 2027 (i.e., no customers' inventory rebuild in 2H26), then the sufficiency ratio would actually deteriorate to -13.6% from -8.1% in 2026E. Both are unprecedented levels over the last 30 years. As for NAND flash, we now forecast +30% QoQ in 3Q26 (was +17%) and +12% QoQ (unchanged) in 4Q26 after +67% QoQ also in 2Q. We forecast the NAND upcycle to continue til at least 4Q27. Net net, this leaves us forecasting memory industry revenues to reach US\$992bn in 2026 and US\$1,763bn in 2027. The main risk to this unprecedented upcycle remains affordability by customers, notably hyperscalers which will have to continue to tap capital markets to finance this capex.

## LTA negotiations continue

Revised LTA negotiations, which incorporate more fixed terms for volumes and pricing, continue. We see some differences between Micron's SCAs, with price "floor" and "ceiling", and those of the Korean memory makers, which we believe have a portion of volumes fixed (c. 60-70% over a 5-year contract), at fixed pricing, to which a variable component (volume and pricing) is added. We believe Samsung is progressing in completing by 3Q more revised LTA agreements with another handful of large customers. The focus remains on DDR5, for which we would expect a target of 50-70% of volumes being tied up to LTAs. As for SK Hynix, we believe negotiations continue to focus on the larger hyperscale customers for both DDR5 and NAND flash.

## Slightly raising HBM demand forecasts, Meta not an issue

We tweak our HBM industry demand forecast to 33.1bn Gb in 2026 (+90% YoY) and 58.7bn Gb in 2027 (+77% YoY) from 32.9/58.0bn prior. We assume HBM procurement equivalent to 8.5mil Nvidia AI GPU units in 2026E, and 11.0mil in 2027E, consistent with our recent CoWoS estimate revision (link). We revise our estimates for HBM-equivalent Google TPU units to 4.2mil for 2026E and 9.1mil (up) for 2027E, also tweaking up HBM procurement for AMD and AWS for 2027. Meanwhile, recent press reports of Meta possibly selling compute to outside customers (link) negatively impacted memory stocks earlier this week. Still, this is likely monetisation of older assets prior to rolling out further Blackwell/Rubin, as well as MTIA capacity (see also note from Steven Ju: link). As such, we see no impact on HBM procurement.

## Pullback in memory semis stocks likely temporary

Memory stocks are on average down 17% from their June peak, after outperforming Semis, Tech, and GEM YTD. Some of this could be over-crowding. Yet, fundamentals remain strong, with the memory industry set to generate close to US\$1.2tn of FCF in 2027E. We believe this will ultimately lead to a step-up in returns to shareholders. We remain positive on the group, with Samsung Key Call Buy (PT Won550k), and Buy ratings on SK Hynix (PT 3.20m from 3.00m), MU (PT US\$1,625), Kioxia (PT ¥132,000) and Nanya Tech (PT NT\$495).

## Equities

Global Semiconductors

Nicolas Gaudois
Analyst
nicolas.gaudois@ubs.com
+65-6495 5148

Timothy Arcuri
Analyst
timothy.arcuri@ubs.com
+1-415-352 5676

Kenji Yasui
Analyst
kenji.yasui@ubs.com
+81-3-5208 6211

Jimmy Yoon
Analyst
jimmy.yoon@ubs.com
+65-6495 4617

Gianmarco Vella
Associate Analyst
gianmarco.vella@ubs.com
+1-415-352 4555

Atsuhiro Kinoshita
Analyst
atsuhiro.kinoshita@ubs.com
+81-3-5208 6768

Sunny Lin
Analyst
sunny.lin@ubs.com
+886-2-8722 7346

Jimmy Yu
Analyst
S1460517080002
jimmy.yu@ubs.com
+86-21-3866 8880

Randy Abrams
Analyst
randy.abrams@ubs.com
+886-2-8722 7338

Francois-Xavier Bouvignies
Analyst
francois.bouvignies@ubs.com
+44-20-7568 7105

## KEY CHARTS

Figure 1: AI server GPU/accelerator unit forecasts ('000 units)

<table><tr><td></td><td>HBM Gen.</td><td colspan="3">HBM Content (GB)</td><td>2025</td><td>1Q26</td><td>2Q26E</td><td>3Q26E</td><td>4Q26E</td><td>2026E</td><td>1Q27E</td><td>2Q27E</td><td>3Q27E</td><td>4Q27E</td><td>2027E</td></tr><tr><td>NVIDIA</td><td></td><td>2025E</td><td>2026E</td><td>2027E</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>L40S</td><td>GDDR6</td><td>48</td><td></td><td></td><td>38.1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>H200</td><td>HBM3E</td><td>141</td><td></td><td></td><td>592.7</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>H20 / H20E</td><td>HBM3 / 3E</td><td>96</td><td>96</td><td></td><td>441.0</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>B200 (8Hi)</td><td>HBM3E</td><td>192</td><td>192</td><td></td><td>1,440.9</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>GB200 (2x GPU - 8Hi)</td><td>HBM3E</td><td>384</td><td>384</td><td></td><td>1,080.4</td><td>102.9</td><td></td><td></td><td></td><td>102.9</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>B300 (12Hi)</td><td>HBM3E</td><td>288</td><td>288</td><td>288</td><td>587.4</td><td>267.0</td><td>300.0</td><td>250.0</td><td>170.0</td><td>987.0</td><td>100.0</td><td></td><td></td><td></td><td>100.0</td></tr><tr><td>GB300 (2x GPU - 12Hi)</td><td>HBM3E</td><td>576</td><td>576</td><td>576</td><td>778.2</td><td>658.0</td><td>670.0</td><td>600.0</td><td>520.0</td><td>2,448.0</td><td>280.0</td><td>180.0</td><td>110.0</td><td>60.0</td><td>630.0</td></tr><tr><td>R200 (12Hi)</td><td>HBM4</td><td>288</td><td>288</td><td>288</td><td></td><td></td><td>20.0</td><td>200.0</td><td>380.0</td><td>600.0</td><td>360.0</td><td>400.0</td><td>300.0</td><td>210.0</td><td>1,270.0</td></tr><tr><td>RV200 (2x GPU - 12Hi)</td><td>HBM4</td><td>576</td><td>576</td><td>576</td><td></td><td></td><td>40.0</td><td>250.0</td><td>480.0</td><td>770.0</td><td>570.0</td><td>700.0</td><td>670.0</td><td>520.0</td><td>2,460.0</td></tr><tr><td>R300 (12Hi)</td><td>HBM4E</td><td></td><td>384</td><td>384</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>130.0</td><td>270.0</td><td>400.0</td></tr><tr><td>RV300 (4x GPU - 12Hi)</td><td>HBM4E</td><td></td><td>768</td><td>768</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>200.0</td><td>500.0</td><td>700.0</td></tr><tr><td>*Other GPU/Accel</td><td>HBM3 / 3E</td><td>288</td><td>384</td><td>576</td><td>106.9</td><td>60.0</td><td>80.0</td><td>80.0</td><td>80.0</td><td>300.0</td><td>70.0</td><td>60.0</td><td>60.0</td><td>50.0</td><td>240.0</td></tr><tr><td>Total Units</td><td></td><td></td><td></td><td></td><td>5,065.6</td><td>1,087.9</td><td>1,110.0</td><td>1,380.0</td><td>1,630.0</td><td>5,207.9</td><td>1,380.0</td><td>1,340.0</td><td>1,470.0</td><td>1,610.0</td><td>5,800.0</td></tr><tr><td>% YoY</td><td></td><td></td><td></td><td></td><td>3.2%</td><td>-17.2%</td><td>0.0%</td><td>8.2%</td><td>19.4%</td><td>2.8%</td><td>26.9%</td><td>20.7%</td><td>6.5%</td><td>-1.2%</td><td>11.4%</td></tr><tr><td>% QoQ</td><td></td><td></td><td></td><td></td><td></td><td>-20.3%</td><td>2.0%</td><td>24.3%</td><td>18.1%</td><td></td><td>-15.3%</td><td>-2.9%</td><td>9.7%</td><td>9.5%</td><td></td></tr><tr><td>Total GPUs</td><td></td><td></td><td></td><td></td><td>6,924.3</td><td>1,848.8</td><td>1,820.0</td><td>2,230.0</td><td>2,630.0</td><td>8,528.8</td><td>2,230.0</td><td>2,220.0</td><td>2,850.0</td><td>3,690.0</td><td>10,990.0</td></tr><tr><td>% YoY</td><td></td><td></td><td></td><td></td><td>37.9%</td><td>27.2%</td><td>22.9%</td><td>19.6%</td><td>23.7%</td><td>23.2%</td><td>20.6%</td><td>22.0%</td><td>27.8%</td><td>40.3%</td><td>28.9%</td></tr><tr><td>% QoQ</td><td></td><td></td><td></td><td></td><td></td><td>-13.0%</td><td>-1.6%</td><td>22.5%</td><td>17.9%</td><td></td><td>-15.2%</td><td>-0.4%</td><td>28.4%</td><td>29.5%</td><td></td></tr><tr><td>AMD</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>MI300</td><td>HBM3</td><td>192</td><td>192</td><td></td><td>71.3</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>MI325X (12Hi)</td><td>HBM3E</td><td>256</td><td>256</td><td></td><td>223.8</td><td>18.0</td><td></td><td></td><td></td><td>18.0</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>MI355X (12Hi)</td><td>HBM3E</td><td>288</td><td>288</td><td>288</td><td>220.7</td><td>170.0</td><td>150.0</td><td>80.0</td><td>70.0</td><td>470.0</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>MI308X</td><td>HBM3</td><td>192</td><td>192</td><td>192</td><td>95.8</td><td>29.0</td><td>28.0</td><td>5.0</td><td></td><td>62.0</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>MI450 (12Hi)</td><td>HBM4</td><td></td><td>432</td><td>432</td><td></td><td></td><td></td><td>45.0</td><td>230.0</td><td>275.0</td><td>350.0</td><td>450.0</td><td>470.0</td><td>380.0</td><td>1,650.0</td></tr><tr><td>MI5XX (16Hi)</td><td>HBM4E</td><td></td><td></td><td>1024</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>60.0</td><td>160.0</td><td>220.0</td></tr><tr><td>*Other GPU/Accel</td><td>HBM3</td><td>192</td><td>192</td><td>288</td><td>4.2</td><td>1.4</td><td>1.5</td><td>1.5</td><td>1.5</td><td>5.8</td><td>2.0</td><td>2.0</td><td>2.0</td><td>2.0</td><td>8.0</td></tr><tr><td>Total Units</td><td></td><td></td><td></td><td></td><td>615.8</td><td>218.4</td><td>179.5</td><td>131.5</td><td>301.5</td><td>830.8</td><td>352.0</td><td>452.0</td><td>532.0</td><td>542.0</td><td>1,878.0</td></tr><tr><td>% YoY</td><td></td><td></td><td></td><td></td><td>41.1%</td><td>81.0%</td><td>86.4%</td><td>-26.5%</td><td>37.0%</td><td>34.9%</td><td>61.2%</td><td>151.8%</td><td>304.7%</td><td>79.8%</td><td>126.0%</td></tr><tr><td>% QoQ</td><td></td><td></td><td></td><td></td><td></td><td>-0.7%</td><td>-17.8%</td><td>-26.8%</td><td>129.3%</td><td></td><td>16.8%</td><td>28.4%</td><td>17.7%</td><td>1.9%</td><td></td></tr><tr><td>Google</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>TPU v5e</td><td>HBM2E</td><td>32</td><td>32</td><td></td><td>134</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>TPU v5p</td><td>HBM2E</td><td>96</td><td>96</td><td></td><td>1,916</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>TPU v6e</td><td>HBM3E</td><td>32</td><td>32</td><td>32</td><td>426</td><td>205</td><td>224</td><td>141</td><td>70</td><td>640</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>TPU v7</td><td>HBM3E</td><td>192</td><td>192</td><td>192</td><td>90</td><td>520</td><td>720</td><td>800</td><td>750</td><td>2,790</td><td>640</td><td>420</td><td>300</td><td>180</td><td>1,540</td></tr><tr><td>TPU v8 (Dual die AX)</td><td>HBM3E</td><td></td><td>288</td><td>288</td><td></td><td></td><td></td><td>25</td><td>225</td><td>250</td><td>740</td><td>940</td><td>980</td><td>840</td><td>3,500</td></tr><tr><td>TPU v8T (Single die X)</td><td>HBM3E</td><td></td><td>216</td><td>216</td><td></td><td></td><td></td><td>70</td><td>380</td><td>450</td><td>850</td><td>1,040</td><td>1,160</td><td>950</td><td>4,000</td></tr><tr><td>*Other TPU/Accel</td><td>HBM3</td><td>96</td><td>144</td><td>144</td><td>77</td><td>7</td><td>9</td><td>10</td><td>10</td><td>37</td><td>15</td><td>15</td><td>15</td><td>15</td><td>60</td></tr><tr><td>Total Units</td><td></td><td></td><td></td><td></td><td>2,642.5</td><td>732.0</td><td>953.4</td><td>1,046.2</td><td>1,435.4</td><td>4,167.0</td><td>2,245.0</td><td>2,415.0</td><td>2,455.0</td><td>1,985.0</td><td>9,100.0</td></tr><tr><td>% YoY</td><td></td><td></td><td></td><td></td><td>18.6%</td><td>14.3%</td><td>66.1%</td><td>82.4%</td><td>68.0%</td><td>57.7%</td><td>206.7%</td><td>153.3%</td><td>134.7%</td><td>38.3%</td><td>118.4%</td></tr><tr><td>% QoQ</td><td></td><td></td><td></td><td></td><td></td><td>-14.3%</td><td>30.2%</td><td>9.7%</td><td>37.2%</td><td></td><td>56.4%</td><td>7.6%</td><td>1.7%</td><td>-19.1%</td><td></td></tr><tr><td>Amazon</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Inferentia 2</td><td>HBM2E</td><td>32</td><td>32</td><td></td><td>88</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Trainium 2 / 2.5</td><td>HBM3E</td><td>96</td><td>144</td><td>144</td><td>496</td><td>130</td><td>220</td><td>140</td><td>100</td><td>590</td><td>50</td><td>10</td><td></td><td></td><td>60</td></tr><tr><td>Inferentia 3</td><td>HBM3E</td><td>96</td><td>96</td><td>96</td><td>162</td><td>30</td><td>28</td><td>20</td><td>18</td><td>96</td><td>15</td><td>10</td><td></td><td></td><td>25</td></tr><tr><td>Trainium 3</td><td>HBM3E</td><td>144</td><td>144</td><td>144</td><td></td><td></td><td>320</td><td>620</td><td>840</td><td>1,780</td><td>840</td><td>780</td><td>640</td><td>540</td><td>2,800</td></tr><tr><td>Trainium 4</td><td>HBM4</td><td></td><td>256</td><td>256</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>40</td><td>240</td><td>280</td></tr><tr><td>*Other Accel</td><td>HBM3</td><td>144</td><td>144</td><td>144</td><td>37</td><td>5</td><td>6</td><td>8</td><td>10</td><td>28</td><td>8</td><td>8</td><td>7</td><td>7</td><td>30</td></tr><tr><td>Total Units</td><td></td><td></td><td></td><td></td><td>783.2</td><td>164.8</td><td>573.7</td><td>787.8</td><td>967.6</td><td>2,493.9</td><td>913.0</td><td>808.0</td><td>687.0</td><td>787.0</td><td>3,195.0</td></tr><tr><td>% YoY</td><td></td><td></td><td></td><td></td><td>-7.7%</td><td>-16.5%</td><td>179.8%</td><td>301.7%</td><td>423.9%</td><td>218.4%</td><td>454.0%</td><td>40.8%</td><td>-12.8%</td><td>-18.7%</td><td>28.1%</td></tr><tr><td>% QoQ</td><td></td><td></td><td></td><td></td><td></td><td>-10.8%</td><td>248.1%</td><td>37.3%</td><td>22.8%</td><td></td><td>-5.6%</td><td>-11.5%</td><td>-15.0%</td><td>14.6%</td><td></td></tr><tr><td>Intel / Habana</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Gaudi 3</td><td>HBM2 / 3E</td><td>288</td><td>288</td><td>288</td><td>188</td><td>30</td><td>18</td><td>8</td><td>0</td><td>56</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Gaudi 4</td><td>HBM3E</td><td>288</td><td>288</td><td>288</td><td></td><td></td><td></td><td>10</td><td>25</td><td>35</td><td>25</td><td>20</td><td>15</td><td>10</td><td>70</td></tr><tr><td>*Others</td><td>HBM2 / 3E</td><td>192</td><td>192</td><td>192</td><td>25</td><td>6</td><td>4</td><td>4</td><td>5</td><td>18</td><td>4</td><td>4</td><td>4</td><td>4</td><td>16</td></tr><tr><td>Total Units</td><td></td><td></td><td></td><td></td><td>213.2</td><td>36.0</td><td>21.6</td><td>21.6</td><td>30.0</td><td>109.2</td><td>29.0</td><td>24.0</td><td>19.0</td><td>14.0</td><td>86.0</td></tr><tr><td>% YoY</td><td></td><td></td><td></td><td></td><td>-32.1%</td><td>-20.3%</td><td>-60.1%</td><td>-62.7%</td><td>-46.3%</td><td>-48.8%</td><td>-19.4%</td><td>11.1%</td><td>-12.0%</td><td>-53.3%</td><td>-21.2%</td></tr><tr><td>% QoQ</td><td></td><td></td><td></td><td></td><td></td><td>-35.6%</td><td>-40.0%</td><td>0.0%</td><td>38.9%</td><td></td><td>-3.3%</td><td>-17.2%</td><td>-20.8%</td><td>-26.3%</td><td></td></tr><tr><td>Microsoft</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Maia 100</td><td>HBM3</td><td>120</td><td>120</td><td>120</td><td>34</td><td>3</td><td>1</td><td></td><td></td><td>4</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Maia 200</td><td>HBM3E</td><td></td><td>288</td><td>288</td><td></td><td>2</td><td>6</td><td>10</td><td>14</td><td>33</td><td>14</td><td>10</td><td>7</td><td>4</td><td>35</td></tr><tr><td>Maia 300</td><td>HBM4</td><td></td><td></td><td>288</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>8</td><td>14</td><td>22</td></tr><tr><td>*Others</td><td>HBM3</td><td>120</td><td>192</td><td>192</td><td>8</td><td>2</td><td>2</td><td>2</td><td>2</td><td>8</td><td>2</td><td>2</td><td>2</td><td>2</td><td>8</td></tr><tr><td>Total Units</td><td></td><td></td><td></td><td></td><td>41.8</td><td>7.3</td><td>8.9</td><td>12.5</td><td>16.1</td><td>44.7</td><td>16.0</td><td>12.0</td><td>17.0</td><td>20.0</td><td>65.0</td></tr><tr><td>% YoY</td><td></td><td></td><td></td><td></td><td>22.3%</td><td>-27.1%</td><td>-19.2%</td><td>3.9%</td><td>83.6%</td><td>7.1%</td><td>119.5%</td><td>35.0%</td><td>36.3%</td><td>24.4%</td><td>45.3%</td></tr><tr><td>% QoQ</td><td></td><td></td><td></td><td></td><td></td><td>-16.7%</td><td>21.9%</td><td>40.3%</td><td>28.9%</td><td></td><td>-0.4%</td><td>-25.0%</td><td>41.7%</td><td>17.6%</td><td></td></tr><tr><td>Meta</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>MTIA v1</td><td>LPDDR5</td><td>64</td><td>64</td><td></td><td>421</td><td>20</td><td>5</td><td></td><td></td><td>25</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>MTIA v2</td><td>LPDDR5</td><td>128</td><td>128</td><td></td><td>30</td><td>20</td><td>8</td><td>2</td><td></td><td>30</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>MTIA v3</td><td>HBM3E</td><td>192</td><td>192</td><td>192</td><td>5</td><td>15</td><td>20</td><td>35</td><td>40</td><td>110</td><td>40</td><td>30</td><td>20</td><td>15</td><td>105</td></tr><tr><td>MTIA v4</td><td>HBM4</td><td></td><td>432</td><td>432</td><td></td><td></td><td></td><td></td><td></td><td></td><td>40</td><td>80</td><td>100</td><td>120</td><td>340</td></tr><tr><td>*Others</td><td>LPDDR5</td><td>64</td><td>128</td><td>128</td><td>28</td><td>3</td><td>1</td><td>1</td><td>1</td><td>6</td><td>5</td><td>5</td><td>5</td><td>5</td

[中间内容因长度限制已省略]

lated by the Financial Market Supervisory Authority in Switzerland. In the United Kingdom, UBS AG is authorised by the Prudential Regulation Authority and is subject to regulation by the Financial Conduct Authority and limited regulation by the Prudential Regulation Authority. Details about the extent of regulation by the Prudential Regulation Authority are available from us on request. A member of the London Stock Exchange. This publication is distributed to retail clients of UBS Wealth Management. Ukraine: UBS is a premier global financial services firm offering wealth management services to individual, corporate and institutional investors. UBS is established in Switzerland and operates under Swiss law and in over 50 countries and from all major financial centers. UBS is not registered and licensed as a bank/financial institution under Ukrainian legislation and does not provide banking and other financial services in Ukraine. UBS has not made, and will not make, any offer of the mentioned products to the public in Ukraine. No action has been taken to authorize an offer of the mentioned products to the public in Ukraine and the distribution of this document shall not constitute financial services for the purposes of the Law of Ukraine "On Financial Services and Financial Companies" dated 14 December 2021. Any offer of the mentioned products shall not constitute an investment advice, public offer, circulation, transfer, safekeeping, holding or custody of securities in the territory of Ukraine. Accordingly, nothing in this document or any other document, information or communication related to the mentioned products shall be interpreted as containing an offer, a public offer or invitation to offer or to a public offer, or solicitation of securities in the territory of Ukraine or investment advice under Ukrainian law. Electronic communication must not be considered as an offer to enter into an electronic agreement or other electronic instrument within the meaning of the Law of Ukraine "On Electronic Commerce" dated 3 September 2015. This document is strictly for private use by its holder and may not be passed on to third parties or otherwise publicly distributed. USA: Distributed to US persons only by UBS Financial Services Inc. or UBS LLC, subsidiaries of UBS AG. UBS Switzerland AG, UBS Europe SE, UBS Bank, S.A., UBS BB Corretora de Câmbio, Títulos e Valores Mobiliários S.A., UBS Asesores México, S.A.' de C.V., UBS SuMi TRUST Wealth Management Co., Ltd., UBS Wealth Management Israel Ltd. and UBS Menkul Degerler AS are affiliates of UBS AG. UBS Financial Services Inc. accepts responsibility for the content of a report prepared by a non-US affiliate when it distributes reports to US persons. All transactions by a US person in the securities mentioned in this report should be effected through a US-registered broker dealer affiliated with UBS, and not through a non-US affiliate. The contents of this report have not been and will not be approved by any securities or investment authority in the United States or elsewhere. UBS Financial Services Inc. is not acting as a municipal advisor to any municipal entity or obligated person within the meaning of Section 15B of the Securities Exchange Act (the "Municipal Advisor Rule") and the opinions or views contained herein are not intended to be, and do not constitute, advice within the meaning of the Municipal Advisor Rule. For information on the ways in which UBS LLC manages conflicts and maintains independence of its UBS Global Research product; historical performance information; certain additional disclosures concerning UBS Global Research recommendations; and terms and conditions for certain third party data used in research report, please visit https://www.ubs.com/disclosures.

© UBS 2026. The key symbol and UBS are among the registered and unregistered trademarks of UBS. All rights reserved.

## CS Wealth Management Disclaimer

This disclaimer must be read in conjunction with “Risk information” and “Important Information About Sustainable Investing Strategies” sections of the Global Wealth Management Disclaimer above. You receive this document in your capacity as a client of CS Wealth Management. Your personal data will be processed in accordance with the CS privacy statement accessible at your domicile through the official CS website https://www.credit-suisse.com. In order to provide you with marketing materials concerning our products and services, UBS Group AG and its subsidiaries may process your basic personal data (i.e. contact details such as name, e-mail address) until you notify us that you no longer wish to receive them. You can optout from receiving these materials at any time by informing your Relationship Manager.

Except as otherwise specified herein and/or depending on the local CS entity from which you are receiving this report, this report is distributed by UBS Switzerland AG, authorised and regulated by the Swiss Financial Market Supervisory Authority (FINMA). Saudi Arabia: This document is being distributed by CS Saudi Arabia I Part of UBS Group (CR Number 1010228645, NUN Number 7001515373), duly licensed and regulated by the Saudi Arabian Capital Market Authority pursuant to License Number 08104-37 dated 23/03/1429H corresponding to 21/03/2008AD. CS Saudi Arabia's principal place of business is at King Khaled Road, Laysen Valley, Building number 6, 12329-2376, Riyadh, Saudi Arabia. Website: https://www.credit-suisse.com/sa/en/cssa.html.

© UBS 2026. The key symbol and UBS are among the registered and unregistered trademarks of UBS. All rights reserved.
"""
