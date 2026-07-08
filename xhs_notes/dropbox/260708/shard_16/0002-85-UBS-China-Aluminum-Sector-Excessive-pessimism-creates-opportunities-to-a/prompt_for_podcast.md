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
# China Aluminum Sector Excessive pessimism creates opportunities to accumulate

## China: aluminium capacity limit intact; valuation reset creates opportunities

China's 2017 supply-side reforms capped approved nameplate aluminium capacity at 45.43mt. While record margins have driven modest overproduction via potline upgrades, deferred maintenance and parallel production, we expect output to rise to 45.6mt in 2026E and 46.0mt in 2027E (vs. 44.5mt in 2025), slightly above nameplate capacity. However, we do not expect China to abandon the capacity cap and revert to the unconstrained smelter expansion of 2009-17. Reflecting our moderately softer aluminium price outlook and a less tight market, we cut our sector earnings forecasts 10-30% for 2026-27 and our PTs c20%, based on unchanged target PE and dividend yield assumptions. However, we think valuations remain compelling with our new PTs implying 60-80% upside. Upside catalysts include ongoing inspections of overproduction and potential closures of non-compliant capacity, Indonesian policy uncertainty and limits to further nickel power diversion, and delayed Middle East restarts. These could support aluminium prices and earnings.

## Ex China: more supply and less tightness, but no material surplus

We forecast a 1.1mt global aluminium deficit in 2026 before the market returns to balance in 2027E, supported by >3mt supply growth. In Indonesia, we expect output growth of 1.0mt in 2026E and 1.7mt in 2027E. We flag c3.0mt of supply has been affected by Middle East tensions and supported the 2026E deficit, but gradual restarts and the release of 0.3-0.4mt of trapped inventory should ease tightness in Europe and the US. However, we do not expect a material surplus over the next two to three years. Indonesian policy uncertainty, recovering traditional demand and a supportive copper-aluminium ratio (>4x) should help aluminium prices rebase above the cost curve even as market tightness eases.

## China demand looks weak in 2026E, but supported by exports

China's property/construction activities and solar are weighing heavily on aluminum demand in 2026, offset by robust aluminium net exports of c40% YoY in the first five months. Earlier price hikes amid the Middle East disruption have pressured downstream demand. In 2027E, property and solar should be less of a drag. Structural demand from vehicle lightweighting, resilient machinery sales and electrical transmission growth, supported by some copper to aluminium substitution, suggest total China demand should stay flat in 2026E and increase 2% in 2027E. Recent price moderation may support some demand improvement/restocking.

## Excessive pessimism creates attractive valuations; maintain Buy ratings

UBS now forecasts global aluminium prices of US\$1.50/lb in 2026 and US\$1.42/lb in 2027. Factoring in a 9%/5% SHFE/LME discount, we lower our China aluminium price forecasts to Rmb23,000/t/Rmb22,500/t for 2026/27, and cut 2026E/27E earnings for Tianshan, Chalco and Hongqiao 9-15%/24-33%, respectively. We roll forward to 2027E and maintain our target valuations (10x PE for Tianshan and Chalco; 6.5% dividend yield for Hongqiao), and cut our PTs 19-21%.

Equities

China
Aluminum

Sharon Ding
Analyst
sharon.ding@ubs.com
+852-2971 6284

Elvis Liu
Associate Analyst
elvis.liu@ubs.com
+852-3712 3052

Daniel Major
Analyst
daniel.major@ubs.com
+44-20-7568 3472

Timothy Handerson
Analyst
timothy.handerson@ubs.com
+62-21-2554 5000

Figure 1: Summary of our price target changes

<table><tr><td rowspan="2">Sector</td><td rowspan="2">Ticker</td><td>Rating</td><td colspan="5">Price Target</td><td colspan="3">26E Net Profit (Rmb mn)</td><td colspan="3">27E Net Profit (Rmb mn)</td><td colspan="3">26E Implied Div.Yield</td><td colspan="3">27E Implied Div.Yield</td></tr><tr><td>New</td><td>New</td><td>Old</td><td>Chg.</td><td>LC</td><td>Upside</td><td>New</td><td>Old</td><td>Chg.</td><td>New</td><td>Old</td><td>Chg.</td><td>New</td><td>Old</td><td>Chg.</td><td>New</td><td>Old</td><td>Chg.</td></tr><tr><td colspan="20">Aluminium</td></tr><tr><td>Hongqiao</td><td>1378.HK</td><td>Buy</td><td>36.80</td><td>46.10</td><td>-20%</td><td>20.88</td><td>76%</td><td>30,405</td><td>35,054</td><td>-13%</td><td>30,192</td><td>39,501</td><td>-24%</td><td>11%</td><td>12%</td><td>-2%</td><td>11%</td><td>14%</td><td>-3%</td></tr><tr><td>Chalco-H</td><td>2600.hk</td><td>Buy</td><td>14.20</td><td>17.50</td><td>-19%</td><td>7.70</td><td>84%</td><td>21,612</td><td>25,326</td><td>-15%</td><td>21,130</td><td>30,591</td><td>-31%</td><td>8%</td><td>9%</td><td>-1%</td><td>7%</td><td>11%</td><td>-3%</td></tr><tr><td>Chalco-A</td><td>601600.SS</td><td>Buy</td><td>13.50</td><td>17.10</td><td>-21%</td><td>8.33</td><td>62%</td><td>21,612</td><td>25,326</td><td>-15%</td><td>21,130</td><td>30,591</td><td>-31%</td><td>6%</td><td>7%</td><td>-1%</td><td>6%</td><td>9%</td><td>-3%</td></tr><tr><td>Tianshan</td><td>002532.SZ</td><td>Buy</td><td>18.10</td><td>23.00</td><td>-21%</td><td>11.37</td><td>59%</td><td>8,279</td><td>9,053</td><td>-9%</td><td>8,358</td><td>12,405</td><td>-33%</td><td>8%</td><td>9%</td><td>-1%</td><td>8%</td><td>12%</td><td>-4%</td></tr></table>

Source: UBS estimate; Note: Priced as of 3 July 2026

## Supply

China: run at 45.6mt capacity by May 2026, 46/46.1mt capacity and 45.6/46mt output in 2026/27E

We forecast China's installed aluminium capacity to reach \~46.0mt by end-2026, with output rising 2.5% YoY to 45.6mt. As of May 2026, commissioned capacity stood at 45.6mt. We expect an additional \~0.4mt in 2H26 (Zhalv Phase II +0.21mt; Tianshan +0.12mt, Zhaofeng +0.07mt), taking total capacity to \~46.0mt by year-end.

Figure 2: China aluminium supply in 2026-27E  
![](images/43938fa795173302c31ad283fe6fe3eddd62236a5fcb72b8cfcf9f1f31238efb.jpg)

<table><tr><td>Unit: mt</td><td>5M26</td><td>2026</td><td>2027</td></tr><tr><td>Total Installed Capacity</td><td>45.6</td><td>46.0</td><td>46.1</td></tr><tr><td>Net addition</td><td>0.3</td><td>0.4</td><td>0.1</td></tr><tr><td>Replacement</td><td>0.7</td><td>1.9</td><td>2.3</td></tr><tr><td>Legacy</td><td>0.7</td><td>0.7</td><td>0.7</td></tr><tr><td>Operating</td><td>0.5</td><td>0.5</td><td>0.5</td></tr><tr><td>Suspended</td><td>0.2</td><td>0.2</td><td>0.2</td></tr><tr><td>Unchanged</td><td>44.0</td><td>43.1</td><td>43.1</td></tr><tr><td>Annuzalized Output</td><td>45.2</td><td>45.6</td><td>46.0</td></tr><tr><td>Utilization%</td><td>99.1%</td><td>99.1%</td><td>99.7%</td></tr></table>

Source: Aladdiny, Mysteel, UBS estimates

Figure 3: China capacity additions and replacement in 2026-27E (kt)

<table><tr><td>Region</td><td>Company</td><td>New 26E</td><td>Replacement 26E</td><td>Remark</td></tr><tr><td>Shanxi</td><td>Zhaofeng</td><td>69</td><td>225</td><td>69kt in 3Q26; 225kt in 4Q26; replace 240–300kA pots with 600kA pots</td></tr><tr><td>Inner Mongolia</td><td>Zhalv Phase II</td><td>350</td><td></td><td>140kt in 1Q26; 210kt in 2Q26</td></tr><tr><td>Xinjiang</td><td>Tianshan</td><td>240</td><td></td><td>Phase I commissioned by end-25; Phase II to complete by mid-July 26</td></tr><tr><td>Yunnan</td><td>Yunnan Hongtai Yunnan Honghe</td><td></td><td>300</td><td>Hongqiao relocation from Shandong to Yunnan; 5M26 completed 100kt, potentially 200-300kt depending on market conditions</td></tr><tr><td>Yunnan</td><td>Yunnan Qiya</td><td></td><td>210</td><td>Qiya relocation from Yunnan to Xinjiang; completion expected in 4Q26</td></tr><tr><td>Inner Mongolia</td><td>Dongshan</td><td></td><td>240</td><td>Yidian relocation from Henan to Inner Mongolia</td></tr><tr><td>Guizhou</td><td>Shuangyuan</td><td></td><td>100</td><td>Nanshan 100kt quota to Guizhou Shuangyuan; commissioned in 1Q26</td></tr><tr><td>Qinghai</td><td>Qiaotou Power</td><td></td><td>500</td><td>Upgrade of 312 units of 600kA potlines</td></tr><tr><td>Inner Mongolia</td><td>Jinlian</td><td></td><td>24</td><td>Upgrade from 400kA to 500kA</td></tr><tr><td>Xinjiang</td><td>Xinfa</td><td></td><td>270</td><td>270kt transfer in 2H26; replace 400kA with 600kA pots</td></tr><tr><td>Xinjiang</td><td>Xiwang</td><td></td><td>160</td><td>Xiwang 500kA upgrade; commissioning in 1H26</td></tr><tr><td>Xinjiang</td><td>Qiya</td><td></td><td>400</td><td>400kt Phase II capacity retrofit; 100kt in 2Q26 and 300kt in 3Q26</td></tr><tr><td>Chongqing</td><td>Bofeng</td><td></td><td>180</td><td>Upgrade from 240/300kA to 400kA; commissioning in 4Q26</td></tr><tr><td>Liaoning</td><td>Xiangyu</td><td></td><td>300</td><td>300kt restart already included in 26 capacity, nearly finish by 5M26</td></tr><tr><td>China</td><td>Total</td><td>659</td><td>2,609</td><td></td></tr></table>

<table><tr><td>Region</td><td>Company</td><td>New 27E</td><td>Replacement 27E</td><td>Remark</td></tr><tr><td>Qinghai</td><td>Hongsen</td><td>110</td><td></td><td>Originally planned for 26; likely delayed to 27</td></tr><tr><td>Qinghai</td><td>Baihe</td><td></td><td>500</td><td>Upgrade 600kA potlines</td></tr><tr><td>Shanxi</td><td>Zhaofeng</td><td></td><td>100</td><td>Zhaofeng Phase II capacity replacement</td></tr><tr><td>Shanxi</td><td>Senze</td><td></td><td>500</td><td>Under feasibility review; commissioning timing uncertain</td></tr><tr><td>Xinjiang</td><td>Wanji</td><td></td><td>580</td><td>360 units of 600kA pots; capacity transfer from Xin&#x27;an&#x27;s existing base</td></tr><tr><td>Xinjiang</td><td>Huazhang</td><td></td><td>500</td><td>Upgrade from 300kA to 600kA; commissioning in 2027</td></tr><tr><td>Sichuan</td><td>Hongchangsheng</td><td></td><td>115</td><td>Upgrade from 200kA to 400kA; commissioning in 4Q27</td></tr><tr><td>China</td><td>Total</td><td>110</td><td>2,295</td><td></td></tr></table>

Source: Aladdiny, company data, UBS estimates

Figure 4: c2% annualized upside theoretically, but limited by operational constraints

<table><tr><td rowspan="2">PotKa</td><td rowspan="2">Capacitymt</td><td rowspan="2">Total%</td><td rowspan="2">Efficiency%</td><td rowspan="2">Unit Outputt, annually</td><td colspan="2">Current Efficiency +0.2%</td><td colspan="3">Current Intensity +1~3%</td><td colspan="2">CE +0.2%; CI +1~3%</td></tr><tr><td>Unit Output</td><td>Est. Capacity</td><td>Assumption</td><td>Unit Output</td><td>Est. Capacity</td><td>Unit Output</td><td>Est. Capacity</td></tr><tr><td>200</td><td>0.9</td><td>2%</td><td>92%</td><td>541</td><td>542</td><td>0.9</td><td>1%</td><td>546</td><td>0.9</td><td>548</td><td>0.9</td></tr><tr><td>230</td><td>0.2</td><td>0%</td><td>92%</td><td>622</td><td>623</td><td>0.2</td><td>1%</td><td>628</td><td>0.2</td><td>630</td><td>0.2</td></tr><tr><td>240</td><td>3.0</td><td>7%</td><td>92%</td><td>649</td><td>650</td><td>3.0</td><td>1%</td><td>656</td><td>3.0</td><td>657</td><td>3.0</td></tr><tr><td>245</td><td>0.1</td><td>0%</td><td>92%</td><td>663</td><td>664</td><td>0.1</td><td>1%</td><td>669</td><td>0.1</td><td>671</td><td>0.1</td></tr><tr><td>280</td><td>0.4</td><td>1%</td><td>92%</td><td>757</td><td>759</td><td>0.4</td><td>1%</td><td>765</td><td>0.4</td><td>767</td><td>0.4</td></tr><tr><td>300</td><td>2.6</td><td>6%</td><td>93%</td><td>820</td><td>822</td><td>2.6</td><td>1%</td><td>828</td><td>2.6</td><td>830</td><td>2.6</td></tr><tr><td>320</td><td>0.6</td><td>1%</td><td>93%</td><td>875</td><td>877</td><td>0.6</td><td>2%</td><td>892</td><td>0.6</td><td>894</td><td>0.6</td></tr><tr><td>330</td><td>0.9</td><td>2%</td><td>93%</td><td>902</td><td>904</td><td>0.9</td><td>2%</td><td>920</td><td>0.9</td><td>922</td><td>0.9</td></tr><tr><td>350</td><td>1.6</td><td>3%</td><td>93%</td><td>957</td><td>959</td><td>1.6</td><td>2%</td><td>976</td><td>1.6</td><td>978</td><td>1.6</td></tr><tr><td>360</td><td>0.2</td><td>0%</td><td>93%</td><td>984</td><td>986</td><td>0.2</td><td>2%</td><td>1,004</td><td>0.2</td><td>1,006</td><td>0.2</td></tr><tr><td>400</td><td>10.2</td><td>22%</td><td>94%</td><td>1,105</td><td>1,108</td><td>10.2</td><td>2%</td><td>1,127</td><td>10.4</td><td>1,130</td><td>10.4</td></tr><tr><td>420</td><td>2.1</td><td>5%</td><td>94%</td><td>1,161</td><td>1,163</td><td>2.1</td><td>2%</td><td>1,184</td><td>2.2</td><td>1,186</td><td>2.2</td></tr><tr><td>440</td><td>0.6</td><td>1%</td><td>94%</td><td>1,216</td><td>1,218</td><td>0.6</td><td>2%</td><td>1,240</td><td>0.6</td><td>1,243</td><td>0.6</td></tr><tr><td>460</td><td>1.3</td><td>3%</td><td>94%</td><td>1,271</td><td>1,274</td><td>1.3</td><td>2%</td><td>1,297</td><td>1.4</td><td>1,299</td><td>1.4</td></tr><tr><td>500</td><td>14.2</td><td>31%</td><td>95%</td><td>1,396</td><td>1,399</td><td>14.2</td><td>3%</td><td>1,438</td><td>14.6</td><td>1,441</td><td>14.7</td></tr><tr><td>530</td><td>0.5</td><td>1%</td><td>95%</td><td>1,480</td><td>1,483</td><td>0.5</td><td>3%</td><td>1,525</td><td>0.5</td><td>1,528</td><td>0.5</td></tr><tr><td>600</td><td>6.3</td><td>14%</td><td>95%</td><td>1,676</td><td>1,679</td><td>6.3</td><td>3%</td><td>1,726</td><td>6.5</td><td>1,730</td><td>6.5</td></tr><tr><td>Total</td><td>45.6</td><td>100%</td><td></td><td></td><td></td><td>45.7</td><td></td><td></td><td>46.7</td><td></td><td>46.8</td></tr></table>

Source: Aladdiny, UBS estimates. Note: (1) China by-pot capacity distribution based on Aladdiny data as of May 2026; (2) Unit output estimated by UBS, assuming ideal conditions in which a 1kA DC current at 100% current efficiency yields 0.008054t of aluminium per day. 3) Current Intensity assumption by cross-check with Aladdiny, SMM, and aluminium smelters

We think market concerns around overproduction appear overstated.

\- Capacity replacement may temporarily allow parallel production. In 2026, total capacity swaps are \~2.6mt, including \~0.85mt cross-province relocations and \~1.76mt upgrades. While overlapping operations during transitions can in theory lift output above nameplate capacity, the impact is limited at the aggregate monthly level.

\- Non-compliant legacy capacity (c.\~0.6-0.8mt) is already captured in installed capacity. Its potential formalisation therefore does not represent net additions and has no incremental impact on supply. However, permanent shutdown would lead to a net reduction in both nameplate capacity and production.

\- Potline upgrades can lift effective output via gains in efficiency or amperage. For example, according to Aladdiny, a 1ppt improvement in current efficiency (e.g. from 93% to 94%) lifts annual output by \~1.1% (c.147kt for a 500ka potline), while a 10ka increase (500ka to 510ka) raises output by \~2.0% (c.73.5kt at 94% efficiency). In practice, current efficiency gains are slow and incremental. Aladdiny estimates annual improvement of \~0.5ppt, and only \~30% of capacity may achieve this in the near term. Amperage increases offer more headroom (theoretically up to \~10%), but technical constraints mean even a sustained 5% uplift takes time and is not nationally feasible. If we assume an idealised scenario of 100% utilisation, with nationwide efficiency improving by 0.2ppt and amperage rising 1\~3%, effective annualised capacity could reach \~46.8mt. However, producers remain reluctant to maximise short-term output, given concerns over profit sustainability and potline lifespan. Meanwhile, rotating maintenance cycles (requiring overhaul every 4-8 years) leave a structural utilisation buffer of \~2%.

In reality, despite theoretical and anecdotal instances of parallel operations and output gains from pot upgrades, China's nationwide monthly installed-capacity utilisation has not exceeded 100% from 2021 through YTD26. Effective utilisation has remained tightly anchored around 100% ( $\pm2\%$ ), with a peak of +1.6% in Feb-23. Even at margin peaks of >Rmb8,000/t, operational constraints continue to cap supply, with 5M26 effective utilisation staying within +1%. Notably, while some market participants use annualized April 2026 NBS output (>47mt) as a baseline proxy for 26E production, we continue to track and base our estimates on Aladdiny and Mysteel operating data.

Overall, we do not expect the speculated overproduction to materially lift utilisation or supply, and continue to view the market as well balanced rather than structurally oversupplied.

Figure 5: Cross comparison of annualized aluminium output: NBS vs. Aladdiny vs. Mysteel (Unit: mt)  
![](images/9a12a7a71ad19f1d310624814bdfec9474887aa20f42847fc063265952c43120.jpg)  
Source: Wind, Aladdin, Mysteel, UBS. Note: NBS reports Jan-Feb production on a combined basis. Jan-Feb annualized output is derived by annualizing cumulative output over the total Jan-Feb calendar days

Figure 6: China aluminium utilization: Aladdiny  
![](images/b40d930beee677d8b60c2c517082243b10c4a99597f331961f623085a0e8d172.jpg)  
Source: Aladdiny, UBS

Figure 7: China aluminium utilization: Mysteel  
![](images/a2e8ec442d1385172d144483ac88ea41535f0641019e9a224e168635b854b330.jpg)  
Source: Mysteel, UBS

## Indonesia: to add 1.5/1.9mt capacity and 1.0/1.7mt output in 2026/27E

We raise our Indonesia aluminium output outlook for 2026-27, driven by both new projects and accelerated ramp-ups. Key additions include Tsingshan's Taiyun Morowali project (600kt, 27E) and Weda Bay expansion (800kt; 400kt in 26E, 400kt in 27E). Several projects are also tracking ahead of schedule: Harita's 100kt has been brought forward from 2028–29 to 2027–28; Bosai's 600kt similarly moves forward; and ramp-up is accelerating across Tsingshan's projects (Juwan, Taijing, Xianfeng; 1.2mt capacity).

Figure 8: Capacity and output estimates for Indonesian aluminium smelter progress  
Capacity: Indonesia aluminium smelter progress estimate (unit: kt)

<table><tr><td>Group</td><td>Project</td><td>Venue</td><td>2025</td><td>2026E</td><td>2027E</td><td>2028E</td><td>2029E+</td><td>Remarks</td></tr><tr><td>Tsingshan / Huafeng</td><td>Huaqing (Morowali)</td><td>Sulawesi</td><td>500</td><td>500</td><td>500</td><td>500</td><td>500</td><td>ALD: Planned 1.0mt; second 0.5mt deferred (no land/power)</td></tr><tr><td>Tsingshan / Xinfa</td><td>Taijing/HF (Morowali)</td><td>Sulawesi</td><td></td><td>600</td><td>600</td><td>600</td><td>600</td><td>ALD/ UBS Indo: Started May26; ~0.6mt by end-26</td></tr><tr><td>Tsingshan / Xinfa</td><td>Taiyun (Morowali)</td><td>Sulawesi</td><td></td><td></td><td>600</td><td>600</td><td>600</td><td>ALD: pots full ramp by late-26/early-27; captive power by Q428/ 29 UBS Indo: Limited extra NPI &amp; matte power support in 26-27</td></tr><tr><td>Tsingshan / Xinfa</td><td>Juwan (Weda Bay)</td><td>Maluku</td><td>200</td><td>270</td><td>270</td><td>270</td><td>270</td><td>ALD: Full ramp delayed from Dec-25 to mid-Feb 2026</td></tr><tr><td>Tsingshan / Xinfa</td><td>Xianfeng (Weda Bay)</td><td>Maluku</td><td></td><td>330</td><td>330</td><td>330</td><td>330</td><td>ALD: Starts early Jun-26; full

[中间内容因长度限制已省略]

lated by the Financial Market Supervisory Authority in Switzerland. In the United Kingdom, UBS AG is authorised by the Prudential Regulation Authority and is subject to regulation by the Financial Conduct Authority and limited regulation by the Prudential Regulation Authority. Details about the extent of regulation by the Prudential Regulation Authority are available from us on request. A member of the London Stock Exchange. This publication is distributed to retail clients of UBS Wealth Management. Ukraine: UBS is a premier global financial services firm offering wealth management services to individual, corporate and institutional investors. UBS is established in Switzerland and operates under Swiss law and in over 50 countries and from all major financial centers. UBS is not registered and licensed as a bank/financial institution under Ukrainian legislation and does not provide banking and other financial services in Ukraine. UBS has not made, and will not make, any offer of the mentioned products to the public in Ukraine. No action has been taken to authorize an offer of the mentioned products to the public in Ukraine and the distribution of this document shall not constitute financial services for the purposes of the Law of Ukraine "On Financial Services and Financial Companies" dated 14 December 2021. Any offer of the mentioned products shall not constitute an investment advice, public offer, circulation, transfer, safekeeping, holding or custody of securities in the territory of Ukraine. Accordingly, nothing in this document or any other document, information or communication related to the mentioned products shall be interpreted as containing an offer, a public offer or invitation to offer or to a public offer, or solicitation of securities in the territory of Ukraine or investment advice under Ukrainian law. Electronic communication must not be considered as an offer to enter into an electronic agreement or other electronic instrument within the meaning of the Law of Ukraine "On Electronic Commerce" dated 3 September 2015. This document is strictly for private use by its holder and may not be passed on to third parties or otherwise publicly distributed. USA: Distributed to US persons only by UBS Financial Services Inc. or UBS LLC, subsidiaries of UBS AG. UBS Switzerland AG, UBS Europe SE, UBS Bank, S.A., UBS BB Corretora de Câmbio, Títulos e Valores Mobiliários S.A., UBS Asesores México, S.A.' de C.V., UBS SuMi TRUST Wealth Management Co., Ltd., UBS Wealth Management Israel Ltd. and UBS Menkul Degerler AS are affiliates of UBS AG. UBS Financial Services Inc. accepts responsibility for the content of a report prepared by a non-US affiliate when it distributes reports to US persons. All transactions by a US person in the securities mentioned in this report should be effected through a US-registered broker dealer affiliated with UBS, and not through a non-US affiliate. The contents of this report have not been and will not be approved by any securities or investment authority in the United States or elsewhere. UBS Financial Services Inc. is not acting as a municipal advisor to any municipal entity or obligated person within the meaning of Section 15B of the Securities Exchange Act (the "Municipal Advisor Rule") and the opinions or views contained herein are not intended to be, and do not constitute, advice within the meaning of the Municipal Advisor Rule. For information on the ways in which UBS LLC manages conflicts and maintains independence of its UBS Global Research product; historical performance information; certain additional disclosures concerning UBS Global Research recommendations; and terms and conditions for certain third party data used in research report, please visit https://www.ubs.com/disclosures.

© UBS 2026. The key symbol and UBS are among the registered and unregistered trademarks of UBS. All rights reserved.

## CS Wealth Management Disclaimer

This disclaimer must be read in conjunction with “Risk information” and “Important Information About Sustainable Investing Strategies” sections of the Global Wealth Management Disclaimer above. You receive this document in your capacity as a client of CS Wealth Management. Your personal data will be processed in accordance with the CS privacy statement accessible at your domicile through the official CS website https://www.credit-suisse.com. In order to provide you with marketing materials concerning our products and services, UBS Group AG and its subsidiaries may process your basic personal data (i.e. contact details such as name, e-mail address) until you notify us that you no longer wish to receive them. You can optout from receiving these materials at any time by informing your Relationship Manager.

Except as otherwise specified herein and/or depending on the local CS entity from which you are receiving this report, this report is distributed by UBS Switzerland AG, authorised and regulated by the Swiss Financial Market Supervisory Authority (FINMA). Saudi Arabia: This document is being distributed by CS Saudi Arabia I Part of UBS Group (CR Number 1010228645, NUN Number 7001515373), duly licensed and regulated by the Saudi Arabian Capital Market Authority pursuant to License Number 08104-37 dated 23/03/1429H corresponding to 21/03/2008AD. CS Saudi Arabia's principal place of business is at King Khaled Road, Laysen Valley, Building number 6, 12329-2376, Riyadh, Saudi Arabia. Website: https://www.credit-suisse.com/sa/en/cssa.html.

© UBS 2026. The key symbol and UBS are among the registered and unregistered trademarks of UBS. All rights reserved.
"""
