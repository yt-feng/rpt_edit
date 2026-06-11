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
## China Healthcare: May 2026 China hospital equipment bidding: Single-month bidding value marginally turned positive yoy

We continue to track bidding data for 9 types of medical equipment. After five consecutive months of yoy decline since last December, the total bidding value of these 9 equipment categories recorded a slight yoy increase of $+0.1\%$ in May. We believe this is in line with our previous expectation that the sector would move from a mild yoy decline to a mild yoy growth phase, and we still expect a more visible recovery in the industry to emerge in 2H26.

By equipment category, only CT, MRI, and LINAC recorded positive yoy growth in May. Patient monitors, which had previously sustained positive growth, failed to maintain their strong momentum. However, considering that many monitors procured during the Covid period are now entering the replacement cycle, we remain constructive on a potential improvement in patient monitor bidding data going forward.

Exhibit 1: Total bidding value of 9 main medical devices in China In Rmb, mn  
![](images/201b83a7235858115d444c0f3d3a3f26908037076c1eda1227f3fc20ca8dcafc.jpg)

<details>
<summary>stacked bar chart</summary>

| Month | Patient monitor | Ultrasound | Endoscope | CT | MRI | PET-CT | DR | LINAC | DSA (IGT) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Jan-23 | 500 | 3500 | 4000 | 1800 | 2500 | 1000 | 500 | 200 | 1500 |
| Mar-23 | 500 | 1800 | 2500 | 1800 | 1800 | 500 | 200 | 100 | 2500 |
| May-23 | 500 | 1800 | 2500 | 1800 | 1800 | 500 | 200 | 100 | 2500 |
| Jul-23 | 500 | 1800 | 2500 | 1800 | 1800 | 500 | 200 | 100 | 2500 |
| Sep-23 | 500 | 1800 | 2500 | 1800 | 1800 | 500 | 200 | 100 | 2500 |
| Nov-23 | 500 | 1800 | 2500 | 1800 | 1800 | 500 | 200 | 100 | 2500 |
| Jan-24 | 500 | 1800 | 2500 | 1800 | 1800 | 500 | 200 | 100 | 2500 |
| Mar-24 | 500 | 1800 | 2500 | 1800 | 1800 | 500 | 200 | 100 | 2500 |
| May-24 | 500 | 1800 | 2500 | 1800 | 1800 | 500 | 200 | 100 | 2500 |
| Jul-24 | 500 | 1800 | 2500 | 1800 | 1800 | 500 | 200 | 100 | 2500 |
| Sep-24 | 500 | 1800 | 2500 | 1800 | 1800 | 500 | 200 | 100 | 2500 |
| Nov-24 | 500 | 1800 | 2500 | 1800 | 1800 | 500 | 200 | 100 | 2500 |
</details>

Source: Joinchain

## Tianyi Yan

+86(21)2401-8609

tianyi.yan@goldmansachs.cn

GS (China) Securities

Company Limited

## Ziyi Chen

+852-2978-0526 | ziyi.chen@gs.com

GS (Asia) L.L.C.

## Michael Zheng

+86(21)2401-8928

michael.zheng@goldmansachs.cn

GS (China) Securities

Company Limited

GS does and seeks to do business with companies covered in its research reports. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of this report. Investors should consider this report as only a single factor in making their investment decision. For Reg AC certification and other important disclosures, see the Disclosure Appendix, or go to www.gs.com/research/hedge.html. Analysts employed by non-US affiliates are not registered/qualified as research analysts with FINRA in the U.S.

Exhibit 2: The YoY change rate of bidding value  
![](images/13cb60abbcd88406f85a655981de1726bde76c2568ea34ab88dbeb737e1b95ab.jpg)

<details>
<summary>bar chart</summary>

| Month | Value (%) |
|---|---|
| Jan-23 | 88 |
| Feb-23 | 106 |
| Mar-23 | 85 |
| Apr-23 | 43 |
| May-23 | 1 |
| Jun-23 | 20 |
| Jul-23 | -4 |
| Aug-23 | -29 |
| Sep-23 | -27 |
| Oct-23 | -26 |
| Nov-23 | -77 |
| Dec-23 | -55 |
| Jan-24 | -56 |
| Feb-24 | -57 |
| Mar-24 | -43 |
| Apr-24 | -30 |
| May-24 | -43 |
| Jun-24 | -30 |
| Jul-24 | -22 |
| Aug-24 | -2 |
| Sep-24 | -8 |
| Oct-24 | 7 |
| Nov-24 | 82 |
| Dec-24 | 49 |
| Jan-25 | 89 |
| Feb-25 | 131 |
| Mar-25 | 125 |
| Apr-25 | 74 |
| May-25 | 52 |
| Jun-25 | 29 |
| Jul-25 | 27 |
| Aug-25 | 16 |
| Sep-25 | 17 |
| Oct-25 | 15 |
| Nov-25 | -6 |
| Dec-25 | -17 |
| Jan-26 | -19 |
| Feb-26 | -19 |
| Mar-26 | -26 |
| Apr-26 | 0 |
</details>

Source: Joinchain

## Read across to Mindray and United Imaging

For United Imaging, its bidding value increased by +9% yoy in the first five months of this year, making it the only company among its major competitors – including GEHC, Siemens Healthineers, Philips, and Neusoft – to deliver positive growth. We believe this was mainly driven by the company’s stable market share in CT and MRI, as well as share gains in categories such as DSA and LINAC. The company’s recently announced new equity incentive plan calls for annual revenue growth of over 20% in each of 2026-28; otherwise, the plan would not be fully triggered. Considering that domestic tendering demand is still in the early stage of recovery, our current forecast remains slightly below the company’s implied guidance, at 19.3%. We expect the company’s overseas growth rate in 2026 will still be higher than its domestic growth rate, and its revenue contribution will exceed 25%.

Exhibit 3: Revenue breakdown by geography for United Imaging

<table><tr><td>In Rmb, mn</td><td>FY24</td><td>FY25</td><td>1Q26</td><td>FY26E</td></tr><tr><td>By geography</td><td></td><td></td><td></td><td></td></tr><tr><td>China domestic</td><td>8,034</td><td>10,369</td><td>2,198</td><td>11,717</td></tr><tr><td>yoy</td><td>-17.5%</td><td>29.1%</td><td>15.0%</td><td>13.0%</td></tr><tr><td>Overseas</td><td>2,266</td><td>3,431</td><td>710</td><td>4,752</td></tr><tr><td>yoy</td><td>35.0%</td><td>51.4%</td><td>25.2%</td><td>38.5%</td></tr><tr><td>Total revenue</td><td>10,300</td><td>13,800</td><td>2,908</td><td>16,469</td></tr><tr><td>yoy</td><td>-9.7%</td><td>34.0%</td><td>17.3%</td><td>19.3%</td></tr></table>

Source: Company data, GS Global Investment Research

For Mindray, in 1Q26 the company's revenue in China decreased by $-11\%$ yoy, while overseas revenue grew by $+16\%$ yoy (or $+20\%$ yoy when denominated in USD). Its emerging businesses achieved rapid growth both in China and overseas. However, its PMLS and medical imaging businesses in the Chinese market are still under the

destocking process (the company has now guided for the process to end in 2Q26), while the IVD business showed some improvement, especially with the coagulation and immunology businesses are both growing by approximately +10% yoy per the company. Furthermore, the company stated that the average market share of its three core IVD businesses—immunology, biochemistry, and coagulation—increased from 10% in 1H25 to 12% at YE25, and further rose to 13% in 1Q26. We expect the company’s China revenue to achieve positive growth in 2025 from a low base, while overseas markets will continue to maintain double-digit growth.

Exhibit 4: Revenue breakdown for Mindray

<table><tr><td rowspan="2"></td><td colspan="2">2025A</td><td colspan="2">1Q26A</td><td colspan="2">2026E</td></tr><tr><td>Revenue Rmb, mn</td><td>yoy %</td><td>Revenue Rmb, mn</td><td>yoy %</td><td>Revenue Rmb, mn</td><td>yoy %</td></tr><tr><td>Total revenue</td><td>33,282</td><td>-9%</td><td>8,352</td><td>1%</td><td>36,067</td><td>8%</td></tr><tr><td>China</td><td>15,632</td><td>-23%</td><td>3,903</td><td>-11%</td><td>16,169</td><td>3%</td></tr><tr><td>PMLS</td><td>2,522</td><td>-56%</td><td>475</td><td>-44%</td><td>2,404</td><td>-5%</td></tr><tr><td>Medical Imaging</td><td>2,029</td><td>-43%</td><td>461</td><td>-37%</td><td>2,027</td><td>0%</td></tr><tr><td>IVD</td><td>7,508</td><td>-17%</td><td>1,951</td><td>-3%</td><td>7,309</td><td>-3%</td></tr><tr><td>APT Medical</td><td>2,584</td><td>25%</td><td>704</td><td>25%</td><td>3,227</td><td>25%</td></tr><tr><td>Other Emerging Businesses</td><td>989</td><td>NA</td><td>312</td><td>31%</td><td>1,200</td><td>21%</td></tr><tr><td>Overseas</td><td>17,650</td><td>7%</td><td>4,449</td><td>16%</td><td>19,898</td><td>13%</td></tr><tr><td>PMLS</td><td>7,315</td><td>-6%</td><td>1,789</td><td>15%</td><td>7,916</td><td>8%</td></tr><tr><td>Medical Imaging</td><td>3,688</td><td>-6%</td><td>935</td><td>10%</td><td>4,113</td><td>12%</td></tr><tr><td>IVD</td><td>4,732</td><td>1%</td><td>1,242</td><td>20%</td><td>5,571</td><td>18%</td></tr><tr><td>Emerging Businesses</td><td>1,915</td><td>NA</td><td>483</td><td>19%</td><td>2,298</td><td>20%</td></tr><tr><td>Net profit</td><td>8,136</td><td>-30%</td><td>2,330</td><td>-11%</td><td>8,306</td><td>2%</td></tr></table>

Source: Company data, GS Global Investment Research

## Detailed bidding data in nine categories

Exhibit 5: Patient monitor procurement value since Jan-23  
![](images/f2914f78fa9ee2d834124032fe160ab34246d0d3dabf992d673634c9682f1122.jpg)

<details>
<summary>bar chart</summary>

Patient monitor
| Month | Value (Rmb mn) |
|---|---|
| Jan-23 | 530 |
| Mar-23 | 225 |
| May-23 | 185 |
| Jul-23 | 255 |
| Sep-23 | 185 |
| Nov-23 | 280 |
| Jan-24 | 310 |
| Mar-24 | 110 |
| May-24 | 90 |
| Jul-24 | 160 |
| Sep-24 | 250 |
| Nov-24 | 330 |
| Jan-25 | 470 |
| Mar-25 | 140 |
| May-25 | 170 |
| Jul-25 | 230 |
| Sep-25 | 190 |
| Nov-25 | 260 |
| Jan-26 | 305 |
| Mar-26 | 430 |
| May-26 | 245 |
| May-26 (light blue bar) | 190 |
</details>

Source: Joinchain

Exhibit 6: Patient monitor procurement value decreased by -23% yoy in May-26 vs. +25% in Apr-26  
![](images/afde914fd9bc83542196a46ed47ab713dcbab81710672df2ece72f71df65107a.jpg)

<details>
<summary>line chart</summary>

Patient monitor
| Month | Value (%) |
|---|---|
| Jan-25 | 53 |
| Feb-25 | 31 |
| Mar-25 | 104 |
| Apr-25 | 33 |
| May-25 | 50 |
| Jun-25 | 41 |
| Jul-25 | -33 |
| Aug-25 | -24 |
| Sep-25 | -20 |
| Oct-25 | -7 |
| Nov-25 | -11 |
| Dec-25 | -8 |
| Jan-26 | -13 |
| Feb-26 | -3 |
| Mar-26 | 24 |
| Apr-26 | 25 |
| May-26 | -23 |
</details>

Source: Joinchain

Exhibit 7: Endoscope procurement value since Jan-23  
![](images/48c5070b1068a9bc5213d0e9037ec5173812717f2ce9aabad7b0c68ce9400ed4.jpg)

<details>
<summary>bar chart</summary>

Endoscope
| Month | Endoscope (Rmb mn) |
|---|---|
| Jan-23 | 2750 |
| Feb-23 | 1650 |
| Mar-23 | 1600 |
| Apr-23 | 1550 |
| May-23 | 1300 |
| Jun-23 | 2050 |
| Jul-23 | 1850 |
| Aug-23 | 1950 |
| Sep-23 | 1700 |
| Oct-23 | 1900 |
| Nov-23 | 2450 |
| Dec-23 | 2450 |
| Jan-24 | 1450 |
| Feb-24 | 800 |
| Mar-24 | 600 |
| Apr-24 | 750 |
| May-24 | 850 |
| Jun-24 | 1100 |
| Jul-24 | 1550 |
| Aug-24 | 1450 |
| Sep-24 | 1750 |
| Oct-24 | 1550 |
| Nov-24 | 2300 |
| Dec-24 | 3250 |
| Jan-25 | 1900 |
| Feb-25 | 1250 |
| Mar-25 | 1450 |
| Apr-25 | 1450 |
| May-25 | 1350 |
| Jun-25 | 1350 |
| Jul-25 | 1450 |
| Aug-25 | 1400 |
| Sep-25 | 1700 |
| Oct-25 | 1700 |
| Nov-25 | 2250 |
| Dec-25 | 3100 |
| Jan-26 | 1750 |
| Feb-26 | 950 |
| Mar-26 | 1050 |
| Apr-26 | 1050 |
| May-26 | 1000 |
</details>

Source: Joinchain

Exhibit 8: Endoscope procurement value decreased by -25% yoy in May-26 vs. -25% in Apr-26  
![](images/12e3c76856ca4437b078e9dd7eeb0780319a31f111e7744b73974a7ae1274335.jpg)

<details>
<summary>line chart</summary>

Endoscope
| Month | Value (%) |
|---|---|
| Jan-25 | 30 |
| Feb-25 | 55 |
| Mar-25 | 126 |
| Apr-25 | 79 |
| May-25 | 49 |
| Jun-25 | 21 |
| Jul-25 | -6 |
| Aug-25 | -4 |
| Sep-25 | -2 |
| Oct-25 | 8 |
| Nov-25 | -3 |
| Dec-25 | -5 |
| Jan-26 | -7 |
| Feb-26 | -24 |
| Mar-26 | -28 |
| Apr-26 | -25 |
| May-26 | -25 |
</details>

Source: Joinchain

Exhibit 9: Ultrasound procurement value since Jan-23  
![](images/38272f59861388b310dbe15125efe9097e775d32bad704caaab3723094ebf536.jpg)

<details>
<summary>bar chart</summary>

Ultrasound
| Month | Value (Rmb mn) |
|---|---|
| Jan-23 | 2800 |
| Feb-23 | 1500 |
| Mar-23 | 1250 |
| Apr-23 | 1150 |
| May-23 | 1050 |
| Jun-23 | 1450 |
| Jul-23 | 1500 |
| Aug-23 | 1800 |
| Sep-23 | 1650 |
| Oct-23 | 1500 |
| Nov-23 | 1750 |
| Dec-23 | 1900 |
| Jan-24 | 1450 |
| Feb-24 | 650 |
| Mar-24 | 600 |
| Apr-24 | 800 |
| May-24 | 850 |
| Jun-24 | 900 |
| Jul-24 | 1050 |
| Aug-24 | 1150 |
| Sep-24 | 1200 |
| Oct-24 | 1050 |
| Nov-24 | 1950 |
| Dec-24 | 3300 |
| Jan-25 | 2200 |
| Feb-25 | 1450 |
| Mar-25 | 1500 |
| Apr-25 | 1350 |
| May-25 | 1450 |
| Jun-25 | 1500 |
| Jul-25 | 1400 |
| Aug-25 | 1550 |
| Sep-25 | 1750 |
| Oct-25 | 1600 |
| Nov-25 | 2250 |
| Dec-25 | 3350 |
| Jan-26 | 1350 |
| Feb-26 | 750 |
| Mar-26 | 950 |
| Apr-26 | 1150 |
| May-26 | 1150 |
</details>

Source: Joinchain

Exhibit 10: Ultrasound procurement value decreased by $-20\%$ in May-26 yoy vs. $-12\%$ in Apr-26  
![](images/0241e3fc5ea10ae60f54eba6c6ec886fa09e8155e2f536f7d645d8dfe34fc450.jpg)

<details>
<summary>line chart</summary>

Ultrasound
| Month | Value (%) |
|---|---|
| Jan-25 | 48 |
| Feb-25 | 117 |
| Mar-25 | 140 |
| Apr-25 | 63 |
| May-25 | 75 |
| Jun-25 | 64 |
| Jul-25 | 32 |
| Aug-25 | 35 |
| Sep-25 | 49 |
| Oct-25 | 54 |
| Nov-25 | 18 |
| Dec-25 | 1 |
| Jan-26 | -40 |
| Feb-26 | -49 |
| Mar-26 | -37 |
| Apr-26 | -12 |
| May-26 | -20 |
</details>

Source: Joinchain

Exhibit 11: CT scanner procurement value since Jan-23  
![](images/a93010052f8bcfc066303004b9d7db59b3a2a3cb9374c05991b4b6bcab20cd43.jpg)

<details>
<summary>bar chart</summary>

CT
| Month | Value (Rmb mn) |
|---|---|
| Jan-23 | 3100 |
| Feb-23 | 1550 |
| Mar-23 | 2000 |
| Apr-23 | 1500 |
| May-23 | 1200 |
| Jun-23 | 1900 |
| Jul-23 | 1850 |
| Aug-23 | 1650 |
| Sep-23 | 1400 |
| Oct-23 | 1700 |
| Nov-23 | 2250 |
| Dec-23 | 1950 |
| Jan-24 | 1300 |
| Feb-24 | 750 |
| Mar-24 | 850 |
| Apr-24 | 700 |
| May-24 | 850 |
| Jun-24 | 1150 |
| Jul-24 | 1050 |
| Aug-24 | 950 |
| Sep-24 | 1250 |
| Oct-24 | 1400 |
| Nov-24 | 1950 |
| Dec-24 | 3600 |
| Jan-25 | 1950 |
| Feb-25 | 1400 |
| Mar-25 | 2050 |
| Apr-25 | 2200 |
| May-25 | 1600 |
| Jun-25 | 1950 |
| Jul-25 | 1550 |
| Aug-25 | 1700 |
| Sep-25 | 1800 |
| Oct-25 | 2100 |
| Nov-25 | 2450 |
| Dec-25 | 3450 |
| Jan-26 | 1400 |
| Feb-26 | 1000 |
| Mar-26 | 1700 |
| Apr-26 | 1600 |
| May-26 | 1800 |
</details>

Source: Joinchain

Exhibit 12: CT scanner procurement value increased by +12% yoy in May-26 vs. -31% in Apr-26  
![](images/cd630e5894cafce7dde1c87b7485a6d6d1c19f771170ba00d44432a47b95daa7.jpg)

<details>
<summary>line chart</summary>

CT
| Month | Value (%) |
|---|---|
| Jan-25 | -51 |
| Feb-25 | 95 |
| Mar-25 | 145 |
| Apr-25 | 215 |
| May-25 | 90 |
| Jun-25 | 63 |
| Jul-25 | 48 |
| Aug-25 | 83 |
| Sep-25 | 42 |
| Oct-25 | 51 |
| Nov-25 | 23 |
| Dec-25 | -6 |
| Jan-26 | -29 |
| Feb-26 | -29 |
| Mar-26 | -16 |
| Apr-26 | -31 |
| May-26 | 12 |
</details>

Source: Joinchain

Exhibit 13: MRI procurement value since Jan-23  
![](images/dfdfdeba1188a85b819c109140ea6ebd543510e5453abeb5dd65c6949660e5d8.jpg)

<details>
<summary>bar chart</summary>

MRI
| Month | Value (Rmb mn) |
|---|---|
| Jan-23 | 3050 |
| Feb-23 | 1550 |
| Mar-23 | 1480 |
| Apr-23 | 1000 |
| May-23 | 1300 |
| Jun-23 | 1850 |
| Jul-23 | 1550 |
| Aug-23 | 1400 |
| Sep-23 | 1600 |
| Oct-23 | 1480 |
| Nov-23 | 1450 |
| Dec-23 | 1380 |
| Jan-24 | 1350 |
| Feb-24 | 600 |
| Mar-24 | 700 |
| Apr-24 | 780 |
| May-24 | 850 |
| Jun-24 | 950 |
| Jul-24 | 1050 |
| Aug-24 | 1600 |
| Sep-24 | 1550 |
| Oct-24 | 1950 |
| Nov-24 | 2300 |
| Dec-24 | 3600 |
| Jan-25 | 1800 |
| Feb-25 | 1250 |
| Mar-25 | 1650 |
| Apr-25 | 2300 |
| May-25 | 1550 |
| Jun-25 | 1650 |
| Jul-25 | 1650 |
| Aug-25 | 1650 |
| Sep-25 | 1700 |
| Oct-25 | 1850 |
| Nov-25 | 2450 |
| Dec-25 | 3200 |
| Jan-26 | 1350 |
| Feb-26 | 1250 |
| Mar-26 | 1350 |
| Apr-26 | 1150 |
| May-26 | 1800 |
</details>

Source: Joinchain

Exhibit 14: MRI procurement value increased by $+20\%$ yoy in May-26 vs. $-50\%$ in Apr-26  
![](images/ed3e790dd2332774382a0215fc368b6c564c7b10175b7dade80df8361c887602.jpg)

<details>
<summary>line chart</summary>

MRI
| Month | Value (%) |
|---|---|
| Jan-25 | 35 |
| Feb-25 | 119 |
| Mar-25 | 157 |
| Apr-25 | 194 |
| May-25 | 101 |
| Jun-25 | 67 |
| Jul-25 | 57 |
| Aug-25 | -0 |
| Sep-25 | 10 |
| Oct-25 | -3 |
| Nov-25 | 6 |
| Dec-25 | -11 |
| Jan-26 | -25 |
| Feb-26 | -2 |
| Mar-26 | -17 |
| Apr-26 | -50 |
| May-26 | 20 |
</details>

Source: Joinchain

Exhibit 15: PET-CT procurement value since Jan-23  
![](images/2fcc8f915a878486eac8fd4f8c8e353cc2308903f927c5cb199a9102b86507b8.jpg)

<details>
<summary>bar chart</summary>

PET-CT
| Month | Value (Rmb mn) |
|---|---|
| Jan-23 | 330 |
| Feb-23 | 245 |
| Mar-23 | 225 |
| Apr-23 | 75 |
| May-23 | 25 |
| Jun-23 | 300 |
| Jul-23 | 135 |
| Aug-23 | 95 |
| Sep-23 | 85 |
| Oct-23 | 315 |
| Nov-23 | 115 |
| Dec-23 | 140 |
| Jan-24 | 20 |
| Feb-24 | 125 |
| Mar-24 | 170 |
| Apr-24 | 45 |
| May-24 | 85 |
| Jun-24 | 55 |
| Jul-24 | 90 |
| Aug-24 | 50 |
| Sep-24 | 190 |
| Oct-24 | 290 |
| Nov-24 | 115 |
| Dec-24 | 375 |
| Jan-25 | 255 |
| Feb-25 | 50 |
| Mar-25 | 110 |
| Apr-25 | 280 |
| May-25 | 175 |
| Jun-25 | 65 |
| Jul-25 | 90 |
| Aug-25 | 250 |
| Sep-25 | 105 |
| Oct-25 | 105 |
| Nov-25 | 260 |
| Dec-25 | 340 |
| Jan-26 | 355 |
| Feb-26 | 260 |
| Mar-26 | 85 |
| Apr-26 | 195 |
| May-26 | 115 |
</details>

Source: Joinchain

Exhibit 16: PET-CT procurement value decreased by $-33\%$ yoy in May-26 vs. $-28\%$ in Apr-26  
![](images/902b1218d26201865d5a42b869374e1a4bf1267a616be7dc0539848e88e2f982.jpg)

<details>
<summary>line chart</summary>

PET-CT
| Month | Value (%) |
|---|---|
| Jan-25 | 1456 |
| Feb-25 | -57 |
| Mar-25 | -36 |
| Apr-25 | 479 |
| May-25 | 111 |
| Jun-25 | 17 |
| Jul-25 | -3 |
| Aug-25 | 401 |
| Sep-25 | -44 |
| Oct-25 | -64 |
| Nov-25 | 119 |
| Dec-25 | -9 |
| Jan-26 | 38 |
| Feb-26 | 388 |
| Mar-26 | -19 |
| Apr-26 | -28 |
| May-26 | -33 |
</details>

Source: Joinchain

Exhibit 17: DR procurement value since Jan-23  
![](images/f65df08b2e981ba8437d1ac3011b5ed8a2d83a924da02e684ae00c5b4d6c2735.jpg)

<details>
<summary>bar chart</summary>

| Month | DR (Rmb mn) |
|---|---|
| Jan-23 | 470 |
| Feb-23 | 255 |
| Mar-23 | 255 |
| Apr-23 | 235 |
| May-23 | 285 |
| Jun-23 | 305 |
| Jul-23 | 360 |
| Aug-23 | 315 |
| Sep-23 | 245 |
| Oct-23 | 335 |
| Nov-23 | 305 |
| Dec-23 | 160 |
| Jan-24 | 105 |
| Feb-24 | 90 |
| Mar-24 | 140 |
| Apr-24 | 115 |
| May-24 | 180 |
| Jun-24 | 210 |
| Jul-24 | 215 |
| Aug-24 | 270 |
| Sep-24 | 235 |
| Oct-24 | 305 |
| Nov-24 | 565 |
| Dec-24 | 415 |
| Jan-25 | 165 |
| Feb-25 | 215 |
| Mar-25 | 255 |
| Apr-25 | 305 |
| May-25 | 280 |
| Jun-25 | 250 |
| Jul-25 | 360 |
| Aug-25 | 390 |
| Sep-25 | 360 |
| Oct-25 | 445 |
| Nov-25 | 550 |
| Dec-25 | 270 |
| Jan-26 | 155 |
| Feb-26 | 305 |
| Mar-26 | 215 |
| Apr-26 | 230 |
</details>

Source: Joinchain

Exhibit 18: DR procurement value decreased by $-26\%$ yoy in May-26 vs. $-13\%$ in Apr-26  
![](images/159618413a504f7fad4bf863768bde12ba1eb03524c3385b63c7d474df20916b.jpg)

<details>
<summary>line chart</summary>

DR
| Month | Value (%) |
|---|---|
| Jan-25 | 152 |
| Feb-25 | 60 |
| Mar-25 | 131 |
| Apr-25 | 74 |
| May-25 | 156 |
| Jun-25 | 55 |
| Jul-25 | 20 |
| Aug-25 | 67 |
| Sep-25 | 43 |
| Oct-25 | 55 |
| Nov-25 | 45 |
| Dec-25 | 

[中间内容因长度限制已省略]

term impact on the market price of the equity securities discussed in this report, which impact may be directionally counter to the analyst's published price target expectations for such stocks. Any such trading strategies are distinct from and do not affect the analyst's fundamental equity rating for such stocks, which rating reflects a stock's return potential relative to its coverage universe as described herein.

We and our affiliates, officers, directors, and employees will from time to time have long or short positions in, act as principal in, and buy or sell, the securities or derivatives, if any, referred to in this research, unless otherwise prohibited by regulation or GS policy.

The views attributed to third party presenters at GS arranged conferences, including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

© 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
