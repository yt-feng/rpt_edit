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
# Asia Tech Hardware

# Asia Tech Hardware & Semi: key takeaways from the 2026 Taipei Computex

![](images/3412057fffe06f951ca2fc7f9328efdc41dd99a01d22cd09663dcef3c800b6bd.jpg)

Alex Wang, CFA

+852 2123 2613

alex.wang@bernsteinsg.com

![](images/dded695e51be7976ed0e61750335e4f845b2fa81207b072c2b9d301d0338228c.jpg)

Mark Li

+852 2123 2645

mark.li@bernsteinsg.com

![](images/97bd5ec3a6d97231363af52cbf342279d99a5c8edffb3652e028344a64a0c8a9.jpg)

Shirley Yang, CFA

+852 2123 2660

shirley.yang@bernsteinsg.com

![](images/09b439f395c98e2d9a9999791ab8fe35cb4f4474df259f46db8dd5406194db36.jpg)

Ethan Xu

+852 2123 2634

ethan.xu@bernsteinsg.com

![](images/48de9b88439227d590a1c9b9b0196e653a8b8343949cb02a14afa5f06878a365.jpg)

Yipin Cai, CFA

+852 2123 2669

yipin.cai@bernsteinsg.com

![](images/162329195a6057ee42fdab39a0eb3958ea7f61f4dae7e852b23051a542f35b6d.jpg)

Edward Hou, CFA

+852 2123 2623

edward.hou@bernsteinsg.com

We joined Taipei Computex from $2^{nd}$ June to $4^{th}$ June, including guided tours of Delta (OP), MediaTek (OP), Foxconn (2317 TT), Bizlink (3665 TT), Auras (3324 TT) and Lite-on (2301 TT), and IR meetings with Hon Precision (2317 TT), FOCI (8210 TT), ASE (3711 TT), Lotes (3533 TT), Winway (6515 TT), and Zhending (4958 TT; all not covered)

800V HVDC racks took center stage at Computex. Multiple suppliers including Delta, Lite-on, Vertiv, Flex, etc. showcased 800VDC power racks aligned with Nvidia's reference design, with Delta highlighting flexibility for customized configurations (e.g., optional PDU integration). Supercapacitor adoption is gaining traction but remains constrained by raw material supply. We expect Delta to maintain leadership in the power rack transition, with initial shipments starting in 2H26, while solid-state transformers (SST) and fuel cells become more relevant from 2028. As power rack deployments scale, connectivity players like Bizlink should benefit via upgraded power whips and connectors.

Liquid-to-air will likely continue to dominate the market next year, but there are more product samples of liquid-to-liquid (L2L) CDUs available across vendors. Vendors including Delta, Auras and Vertiv are sampling >1MW L2L CDUs for next-gen data centers, with commercialization likely in 2H27. On the components side, Jentech showcased its micro-channel-lid (under sample testing), and Auras highlighted its liquid cooling DIMM (mass production) and two-phase liquid cooling cold plate (developing). Delta and Vertiv also introduced integrated, modular solutions combining power, cooling, and connectivity, cutting CSP deployment time by roughly 50%.

CPO/NPO switch is coming for scale out architectures. For scale-up, while Nvidia prefers copper, there are companies testing CPO on early stage. Our channel check suggests that there are multiple CPO/NPO projects are undergoing among different end customers. 3.2T NPO (optical engine (OE) attached on PCB) for scale-out will be the mainstream next year, but the industry is also developing 6.4T CPO (OE on substrate) likely for 2028. As Jensen put in Taipei Computex “use copper when you can...we’ve made copper sexy again”, Nvidia view that copper still has runway in scale-up systems, and will likely introduce CPO for rack-to-rack (“further scale-up”) interconnects in Feynman era.

However, Wiwynn & Ayar Labs showcased scale-up CPO tray in Computex, likely entering customer testing in 2027. Meanwhile, Amphenol, Foxconn and Arista demonstrated XPO (eXtra-dense Pluggable Optics), delivering 4× OSFP density and enabling 204.8T switching. Combined with CPC (co-packaged copper), this could further extend copper's lifecycle within the rack. Despite the emergence of CPO/NPO, pluggable transceivers will likely continue to dominate the scale-out in the next two years, benefiting PCB companies like ZhenDing.

MediaTek showcased CPO & MicroLED for CPO. No specific updates on its ASIC business but we find the CPO shown with EIC & PIC designed by MediaTek impressive. MediaTek is working with MSFT on MicroLED which possibly allow light source packaged inside CPO too. Overall we reiterate Outperform on the stock.

BERNSTEIN TICKER TABLE 

<table><tr><td rowspan="2">Ticker</td><td rowspan="2">Rating</td><td colspan="3">4 Jun 2026</td><td rowspan="2">TTMRel.</td><td colspan="4">Reported EPS</td><td colspan="3">Reported P/E (x)</td></tr><tr><td>ClosingPrice</td><td>PriceTarget</td><td>Cur</td><td>2025A</td><td>2026E</td><td>2027E</td><td>2025A</td><td>2026E</td><td>2027E</td><td></td></tr><tr><td>2382.TT (Quanta)</td><td>U</td><td>TWD</td><td>404.00</td><td>250.00</td><td>(5.0)%</td><td>TWD</td><td>18.91</td><td>21.07</td><td>23.08</td><td>21.4</td><td>19.2</td><td>17.5</td></tr><tr><td>2360.TT (Chroma ATE)</td><td>O</td><td>TWD</td><td>2,620.00</td><td>1,660.00</td><td>601.4%</td><td>TWD</td><td>27.50</td><td>33.22</td><td>43.66</td><td>95.3</td><td>78.9</td><td>60.0</td></tr><tr><td>2308.TT (Delta)</td><td>O</td><td>TWD</td><td>2,425.00</td><td>2,620.00</td><td>474.1%</td><td>TWD</td><td>23.09</td><td>37.09</td><td>58.40</td><td>105.0</td><td>65.4</td><td>41.5</td></tr><tr><td>3037.TT (Unimicron)</td><td>O</td><td>TWD</td><td>971.00</td><td>990.00</td><td>800.8%</td><td>TWD</td><td>4.36</td><td>14.06</td><td>25.10</td><td>222.7</td><td>69.1</td><td>38.7</td></tr><tr><td>002475.CH ( Luxshare )</td><td>O</td><td>CNY</td><td>74.59</td><td>86.00</td><td>92.9%</td><td>CNY</td><td>2.26</td><td>2.66</td><td>3.45</td><td>33.0</td><td>28.0</td><td>21.6</td></tr><tr><td>2454.TT (MediaTek)</td><td>O</td><td>TWD</td><td>4,430.00</td><td>4,380.00</td><td>198.2%</td><td>TWD</td><td>66.17</td><td>69.52</td><td>170.50</td><td>67.0</td><td>63.7</td><td>26.0</td></tr><tr><td>ASIAX</td><td></td><td></td><td>2,057.41</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

O - Outperform, M - Market-Perform, U - Underperform, NR - Not Rated, CS - Coverage Suspended   
Source: Bloomberg, Bernstein estimates and analysis.

# INVESTMENT IMPLICATIONS

We rate Quanta Underperform, PT=NT\$250.00.

We rate Chroma Outperform, PT=NT\$1,660.00.

We rate Delta Outperform, PT=NT\$2,620.00.

We rate Unimicron Outperform, PT=NT\$990.00.

We rate Luxshare Outperform, PT = RMB86.00.

We rate MediaTek Outperform, PT=NT\$4,380.00

# DETAILS

# EXHIBIT 1: Computex remained popular throughout the week this year

2025 Computex   
![](images/e4fb84db502e354d37ed02a583a99ca83f12d76ebacc532d120779b36e45dca3.jpg)

<details>
<summary>text_image</summary>

台北南港展覽館1館
客滿 請稍候 100% 90% 80%
容留人數管制量 42069人
目前館內人數為 26036人
</details>

Taipei Nangang Exhibition Hall 1   
Visitor # limit: 42,069   
Current visitor #: 26,036   
Photo taken at 2:51PM, Tue, 20 May 2025

![](images/db0ebb5b67bcb029a820697937c7fdd3670ecae155afeadcf90a5decff77d648.jpg)

<details>
<summary>text_image</summary>

台北南港展覽館1館
客滿 篇務候 100% 90% 80%
容留人數管制量 42069人
目前館內人數為 33437人
</details>

Taipei Nangang Exhibition Hall 1   
Visitor # limit: 42,069   
Current visitor #: 33,437   
Photo taken at 3:59PM, Thur, 22 May 2025

2026 Computex   
![](images/3cc5473854d7374bf13fd22b855032e2b72bddce04826ee48f1b83a55be87f9f.jpg)

<details>
<summary>text_image</summary>

台北南港展覽館1館
客滿 編碼候 100% 90% 80%
容留人數管制量 42069人
目前館內人數為 23360人
</details>

Taipei Nangang Exhibition Hall 1   
Visitor # limit: 42,069   
Current visitor #: 23,360   
Photo taken at 11:00AM, Wed, 3 June 2026

![](images/d67c178e1bd57bcc57188eb8b7ffb3702501e69ed183a653bca678bf976f6d9e.jpg)

<details>
<summary>text_image</summary>

台北南港展覽館1館
客滿 訓瑞侯 100% 90% 80%
容留人數管制量 42069人
目前館內人數為 27112人
</details>

Taipei Nangang Exhibition Hall 1   
Visitor # limit: 42,069   
Current visitor #: 27,112   
Photo taken at 3:00PM, Thur, 4 June 2026   
Source: Bernstein photo

# POWER COMPONENT/SYSTEM

EXHIBIT 2: Power rack from Delta and Vertiv   
Delta's 800 VDC In-Row Power Rack   
![](images/0f85a89bf35f09f8d339b3e26d97c3f7741184c84dcba076580ef2aff2d09537.jpg)

<details>
<summary>text_image</summary>

NVIDIA MGX™ 模组方案
NVIDIA MGX® Power Solution
800 VDC 列图电源系统
2.4MW
列图电源
MDC
</details>

Vertiv's 800 VDC Side Car   
![](images/3d804ce6b472d497e05c47246a6bb977f60d6bc63128740085baf4ff47e4cc68.jpg)

<details>
<summary>natural_image</summary>

Exterior view of a 800VDC side car with green-labeled rack-mounted units and display screens (no readable text or symbols on the main structure)
</details>

Source: Bernstein photo

EXHIBIT 3: Delta's Solid Oxide Fuel Cell   
![](images/cc45665c5a0492e29f6d5f86b427d3fdb82a3042965e891367db8e79490748d4.jpg)

<details>
<summary>text_image</summary>

Solid Oxide Fuel Cell
3.3MW Power Station
Optimal On-site Power Generation
</details>

Source: Bernstein photo

EXHIBIT 4: Delta's Solid State Transformer (SST)   
![](images/c0d7a5bcbc17b570f4b05880eaedb9262d187bc94ef57747ab4a48f7fdbaa282.jpg)

<details>
<summary>text_image</summary>

MV Side
中壓系統
MV to LV
AC/DC Converter
交直流中壓低壓變流器
MV Fuse
壓流電器
Control Box
控制器
Power Module
半導體功率元件
Solid State Transformer 固態變壓器
BI-Directional AC/DC at MV & LV 中低壓交直流雙向轉換
High Power Density 高功率密度 | High Efficiency and Reliability 高效可靠
</details>

Source: Bernstein photo

# LIQUID COOLING

EXHIBIT 5: Liquid-to-liquid CDU from Auras and Delta   
![](images/7ba9598c9c5da9d633ccd5796cdb280c93f36515b9ebadb9a08a62939f4c2804.jpg)

<details>
<summary>natural_image</summary>

Exterior view of a dual-chamber industrial machine (CDU) with visible pipes, valves, and control panels (no text or symbols on main body)
</details>

![](images/99394de9018d584b6e4bd6a7bce4e71108768373a2e59e76d83f431ac644e3ab.jpg)

<details>
<summary>text_image</summary>

Delta's 3MW LTL In-Row CDU
3 MW 清置控制器
列間冷卻流動器
8 MPV LTL In-Row
PROFESSIONAL POWER
POWER: IN-ROW
POWER: IN-ROW
POWER: IN-ROW
POWER: IN-ROW
POWER: IN-ROW
POWER: IN-ROW
POWER: IN-ROW
POWER: IN-ROW
POWER: IN-ROW
POWER: IN-ROW
POWER: IN-ROW
POWER: IN-ROW
POWER: IN-ROW
</details>

EXHIBIT 6: Jentech's Micro-Channel Lid   
![](images/eafe2cc3278109c70b34aac01a4978093ac269bcc60547e00545ddf4b2059bcb.jpg)

<details>
<summary>text_image</summary>

Jentech Thermal Technology Evolution Roadmap
Micro-Channel Lid
- Thermal Design Power : Support > 2~3kw TDP
Requirement (High TDP)
- Production Stage : Sample Testing
- Hot Spot Spreading : Excellent Performance On
Active Hot Spot Heat Dissipation
- Cooling System Requirement : Liquid Cooling
System Integration
VC+MC Lid
- Thermal Design Power : Support > 4kw TDP
Requirement (High TDP)
- Production Stage : Developing
- Hot Spot Spreading : Provide Best Performance
On Hot Spot Heat Dissipation
- Cooling System Requirement : Full Liquid Cooling
System Integration
</details>

Source: Bernstein photo   
Source: Bernstein photo

# OPTICAL SOLUTIONS

EXHIBIT 7: CPO/NPO solutions   
Wiwynn & Ayar Labs scale-up CPO tray   
![](images/d1b4a485a5a9f9a056f3d366d2c9429be7340fc45a695973d144cefb59e7d946.jpg)

<details>
<summary>natural_image</summary>

Interior view of a server rack with GUC and AyarLabs branding (no readable text or symbols beyond branding)
</details>

Nvidia Spectrum CPO switch   
![](images/ef419c75a5f379a7d774b7b2890675ee816d58f7eee19335967587cb16c17d86.jpg)

<details>
<summary>natural_image</summary>

Interior view of a NVIDIA server rack with exposed circuit board and drive bays (no text or symbols visible)
</details>

MediaTek's CPO solution   
![](images/81d186561e65315c18c0f08ecbf83c037d6ecbec19d9cfc559560bccf8cd4db9.jpg)

<details>
<summary>text_image</summary>

EIC + PIC
400Gb
per Fiber
</details>

Source: Bernstein photo

EXHIBIT 8: Amphenol's XPO (eXtra-dense Pluggable Optics) + CPC (Co-packaged copper; left) and XPO + NPC (Near-packaged copper)   
![](images/c2a109b911845952365659664ae68f5e165b62f5b4cf92cc09ac6df991d3396e.jpg)

<details>
<summary>natural_image</summary>

Exterior view of an XPO I/O cage with yellow fiber optic cables and a central microchip (no readable text or symbols)
</details>

Source: Bernstein photo

# I. REQUIRED DISCLOSURES

References to "Bernstein" or the "Firm" in these disclosures relate to the following entities: Bernstein Institutional Services LLC (April 1, 2024 onwards), Bernstein & Co., LLC (pre April 1, 2024), Bernstein Autonomous LLP, BSG France S.A. (April 1, 2024 onwards), Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited, Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社) and analysts employed by SG Africa Technologies & Services to produce Bernstein under a Global Services Agreement in place between Bernstein and SG.

Bernstein is part of a joint venture between SG (SG) and AllianceBernstein, L.P. (AB). Unless specifically noted otherwise, for purposes of these disclosures, references to Bernstein's “affiliates” relate to both SG and AB and their respective affiliates.

# VALUATION METHODOLOGY

# Quanta Computer Inc

We set a NT\$250 price target using a P/E multiple of 11X against our 2027 EPS estimate of NT\$23.1.

# Chroma ATE Inc

We set a NT\$1,660 target price using a P/E multiple of 38x against our 2027 EPS estimate of NT\$43.7.

# Delta Electronics Inc

We set a NT\$2,620 target price using a P/E multiple of 37x against our 2027-28 average EPS estimate of NT\$70.8.

# Unimicron Technology Corp

We set a NT\$990 target price using a P/E multiple of 32X against our 2027-28 avg. EPS of NT\$30.8.

# Luxshare Precision Industry Co Ltd

We set a RMB86 target price using a P/E multiple of 25x against our 2027 EPS of RMB3.5.

# MediaTek Inc

We set a NT\$4,380 1-year price target using a P/E multiple of 22x against our forward Q5-Q8 EPS estimate of NT\$199.

# RISKS

# Quanta Computer Inc

Upside risks to our price target for Quanta include:

- Higher-than-expected demand for AI server from hyperscalers in 2026-27   
• Less-than-expected gross margin drag from AI server   
• Higher-than-expected PC shipment, especially from consumer PCs

# Chroma ATE Inc

Downside risks to our price target for Chroma ATE include:

- Lower-than-expected demand for AI chips from hyperscalers, AI startups and enterprises   
- Increasing competition in the AI chip SLT market

\- Slower-than-expected EV penetration pace

# Delta Electronics Inc

Downside risks to our price target for Delta Electronics include:

- Stronger-than-expected competition in AI server power components and thermal management solutions or delayed adoption of HVDC technology may slow down the power electronics segment's growth   
- A delayed or milder recovery of China automation market and global infrastructure market may postpone the profitability recovery in these two segments   
- Worse-than-expected U.S. tariffs policies on China/Thailand and other countries where Delta production sites locate in

# Unimicron Technology Corp

Downside risks to our price target for Unimicron include:

- Aggressive ABF capacity expansion among competitors that slow down the ABF market recovery   
- Slower-than-expected recovery of HDI yield and gross margin

\- Macroeconomic pressure and tariff issue could delay the recovery of smartphones and PCs, impacting the utilization of multiple products at Unimicron

# Luxshare Precision Industry Co Ltd

Downside risks to our price target for Luxshare include:

- Weaker-than-expected iPhone 18 replacement cycle   
- Slower-than-expected share gains for key products in AI server   
• Stronger-than-expected margin pressure due to new product ramp or competition   
• Higher-than-expected memory price impact

# MediaTek Inc

There are a number of downside risks to our MediaTek price target: (1) Stronger competitive pressure from Qualcomm in 5G market (2) Slower 5G adoption increase, especially in China (3) Weaker smartphone demand globally (4) Slower diversification beyond smartphone (5) Downcycle in the broad semiconductor market

# RATINGS DEFINITIONS, BENCHMARKS AND DISTRIBUTION

# EQUITY RATINGS DEFINITIONS

# Bernstein brand

The Bernstein brand rates stocks based on forecasts of relative performance for the next 12 months versus the S&P 500 for stocks listed on the U.S. and Canadian exchanges, versus the Bloomberg Europe Developed Markets Large and Mid Cap Price Return Index EUR (EDME) for stocks listed on the European exchanges and emerging markets exchanges outside of the Asia Pacific region, versus the Bloomberg Japan Large and Mid Cap Price Return Index USD (JPL) for stocks listed on the Japanese exchanges, and versus the Bloomberg Asia ex-Japan Large and Mid Cap Price Return Index (ASIAX) for stocks listed on the Asian (ex-Japan) exchanges -unless otherwise specified.

The Bernstein brand has three categories of ratings:

\- Outperform: Stock will outpace the market index by more than 15 pp

• Market-Perform: Stock will perform in line with the market index to within +/-15 pp   
• Underperform: Stock will trail the performance of the market index by more than 15 pp

Coverage Suspended: Coverage of a company under the Bernstein brand has been suspended. Ratings and price targets are suspended temporarily, are no longer current, and should therefore not be relied upon.

Not Rated: A rating assigned when the stock cannot be accurately valued, or the performance of the company accurately predicted, at the present time. The covering analyst may continue to publish research reports on the company to update investors on events and developments.

Not Covered (NC) denotes companies that are not under coverage.

Bernstein brand stock ratings are based on a 12-month time horizon.

# Autonomous brand – common stocks

The Autonomous brand rates common stocks as indicated below. As our benchmarks we use the Bloomberg Europe 500 Banks And Financial Services Index (BEBANKS) and Bloomberg Europe Dev Mkt Financials Large and Mid Cap Price Ret Index EUR (EDMFI) index for developed European banks and Payments, the Bloomberg Europe 500 Insurance Index (BEINSUR) for European insurers, the S&P 500 and S&P Financials for US banks and Payments coverage, S5LIFE for US Insurance, the S&P Insurance Select Industry (SPSIINS) for US Non-Life Insurers coverage, and the Bloomberg Emerging Markets Financials Large, Mid and Small Cap Price Return Index (EMLSF) for emerging market banks and insurers and Payments. Ratings are stated relative to the sector (not the market).

The Autonomous brand has three categories of common stock ratings:

- Outperform (OP): Stock will outpace the relevant index by more than 10 pp   
- Neutral (N): Stock will perform in line with the market index to within +/-10 pp   
• Underperform (UP): Stock will trail the perf

[中间内容因长度限制已省略]

 learning or artificial intelligence system, or as a prompt or input into any such system. You also may not, without Bernstein's express written consent, do any of the foregoing in connection with your own internal machine learning or artificial intelligence system.

Bernstein may use artificial intelligence tools in the preparation of its materials. Any such materials are reviewed by Bernstein's research analysts prior to publication.

This report has been prepared for information purposes only and is based on current public information that we consider reliable, but the entities noted herein do not warrant or represent (express or implied) as to the sources of information or data contained herein are accurate, complete, not misleading or as to its fitness for the purpose intended even though the entities noted herein rely on reputable or trustworthy data providers, it should not be relied upon as such. Opinions expressed are the author(s)' current opinions as of the date appearing on the material only and we do not undertake to advise you of any change in the reported information or in the opinions herein.

This publication was prepared and issued by the entity referred to herein for distribution to eligible counterparties or professional clients. The information in this report is intended for general circulation and does not constitute an offer to buy or sell any security, investment, legal or tax advice nor a personal recommendation, as defined by any of the aforementioned regulators. It does not take into account the particular investment objectives, financial situations, or needs of individual investors. The report has not been reviewed by any of the aforementioned regulators and does not represent any official recommendation from the aforementioned regulators. The investments referred to herein may not be suitable for you. Investors must make their own investment decisions in consultation with advice sought from a financial adviser regarding the suitability of the investment product, taking into account the specific investment objectives, financial situation or particular needs of any recipient of the recommendation, before the recipient makes a commitment to purchase the investment product.

The analysis contained herein is based on numerous assumptions. Different assumptions could result in materially different results. The information in this report does not constitute, or form part of, any offer to sell or issue, or any offer to purchase or subscribe for shares, or to induce engage in any other investment activity. The value of any securities or financial instruments mentioned in this report may fluctuate subject to market conditions. Information about past performance of an investment is not necessarily a guide to, indicative of, or assurance of future performance. Estimates of future performance mentioned by the research analyst in this report are based on assumptions that may not be realized due to unforeseen factors like market volatility/fluctuation. In relation to securities or financial instruments denominated in a foreign currency other than the clients' home currency, movements in exchange rates will have an effect on the value, either favorable or unfavorable. Before acting on any recommendations in this report, recipients should consider the appropriateness of investing in the subject securities or financial instruments mentioned in this report and, if necessary, seek for independent professional advice.

The securities described herein may not be eligible for sale in all jurisdictions or to certain categories of investors where that permission profile is not consistent with the licenses held by the entities noted herein. This document is for distribution only as may be permitted by law. It is not directed to, or intended for distribution to or use by, any person or entity who is a citizen or resident of or located in any locality, state, country or other jurisdiction where such distribution, publication, availability or use would be contrary to law or regulation or would subject the entities noted herein to any regulation or licensing requirement within such jurisdiction.

Source: Bloomberg Index Services Limited. BLOOMBERG® is a trademark and service mark of Bloomberg Finance L.P. and its affiliates (collectively “Bloomberg”). Bloomberg or Bloomberg’s licensors own all proprietary rights in the Bloomberg Indices. Neither Bloomberg nor Bloomberg’s licensors approves or endorses this material, or guarantees the accuracy or completeness of any information herein, or makes any warranty, express or implied, as to the results to be obtained therefrom and, to the maximum extent allowed by law, neither shall have any liability or responsibility for injury or damages arising in connection therewith.

No part of this material may be reproduced, distributed or transmitted or otherwise made available without prior consent of the entities noted herein. Copyright Bernstein Institutional Services LLC Bernstein Autonomous LLP, BSG France S.A., Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited and Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社). All rights reserved. The trademarks and service marks contained herein are the property of their respective owners. Any unauthorized use or disclosure is strictly prohibited. The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands.
"""
