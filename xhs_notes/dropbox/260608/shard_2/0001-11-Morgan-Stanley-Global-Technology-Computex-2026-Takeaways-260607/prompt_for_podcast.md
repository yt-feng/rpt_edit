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
# Global Technology

# Computex 2026 Takeaways

A full suite of racks in a Nvidia Vera Rubin POD was on full display at Computex, including the Vera rack, Storage rack, Groq 3 LPX rack, Spectrum-X CPO Switch, and Vera Rubin NVL72. Nvidia also introduced its Agentic PC chip RTX Spark chip, which is scheduled to launch in the fall.

# Key Takeaways

We don't think Kyber will be ready for mass deployment in Rubin Ultra.   
- Our checks suggest the 800V DC power rack is on track to ship in 4Q26.   
■ Networking and power/data interconnects will play a bigger role in AI cluster.   
■ Mechanical components should also benefit from AI device growth.

The number of people attending Computex continues to surprise on the upside, which we view as a positive indicator for AI demand as a whole, as investors from around the world are flying in to look at the supply chain's latest breakthroughs on AI servers, from components to rack-level designs. NVIDIA's Vera CPUs were on display in different form factors, such as the MGX board used in a Vera rack, or in the HGX board. For the standalone Vera CPU rack, it comes with 125/256 CPUs per air/liquid-cooled rack and MP is scheduled for 4Q26. Hon Hai also showcased the Groq 3 LPX compute tray, which is expected to enter production in 3Q26, while Wistron/Wiwynn's BlueField-4 STX storage rack highlights growing storage/networking attach. Based on Nvidia's Vera Rubin POD, every 8 Vera Rubin NVL72 will be accompanied by 1 Vera CPU standalone rack, 1 STX storage rack, and 5 Groq 3 LPX racks. See our Compute quick takes here, and Rubin Rack BOM Analysis here.

Power and cooling continue to be a key highlight at COMPUTEX this year as well, as rack density and chip TDP continue to rise. NVIDIA's 800V DC roadmap points to 800V DC standalone power rack readiness in 3Q26, a 1.6MW power center, and 4.8MW power blocks from 1Q28, while Delta highlighted SST and fuel-cell solutions. On cooling, vendors showcased liquid-to-air, liquid-to-liquid and in-row CDUs, including Delta's 3MW in-row CDU and planned 6.8MW version by year-end. FIT's busbars and QDs, Vera Rubin liquid-cooling readiness for 3Q26 mass production, and longer-term microchannel lids all point to a faster thermal-content upgrade cycle, though yield, leakage and reliability qualification remain key hurdles.

AI PC will take time to bear fruit: NVIDIA introduced RTX Spark, an Arm-based SoC combining Grace CPU, Blackwell GPU, AI acceleration and unified memory, with shipments to start from fall 2026. The highest-end spec notebook will likely exceed US\$3K, but it also comes in a desktop form factor. However, we expect limited near-term demand impact. AI power users will be the first to buy, but many have already bought Mac Minis earlier in the year. That said, we believe the DT form factor makes more sense as Jensen's vision is to have this running 24/7 in your home.

MS TAIWAN LIMITED+

# Howard Kao

Equity Analyst

Howard.Kao@morganstanley.com +886 2 2730-2989

# Sharon Shih

Equity Analyst

Sharon.Shih@morganstanley.com +886 2 2730-2865

# Derrick Yang

Equity Analyst

Derrick.Yang@morganstanley.com +886 2 2730-2862

# Samantha Chen

Research Associate

Samantha.Chen@morganstanley.com +886 2 2730-2876

# Irene Yen

Research Associate

Irene.Yen@morganstanley.com +886 2 2730-2869

# Vivi Huang

Research Associate

Vivi.Huang@morganstanley.com +886 2 2730-2860

# GREATER CHINA TECHNOLOGY HARDWARE

# Asia Pacific

Industry View

In-Line

MS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.

# For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

+= Analysts employed by non-U.S. affiliates are not registered with FINRA, may not be associated persons of the member and may not be subject to FINRA restrictions on communications with a subject company, public appearances and trading securities held by a research analyst account.

# Servers and PCs

# Vera CPU Compute Tray / Rack

There are 2 Vera CPUs on a NVIDIA MGX Vera CPU board (Exhibit 2), 4 Vera CPU board in a Vera CPU compute tray (Exhibit 1) and 16/32 Vera CPU compute trays in a Vera CPU rack (Exhibit 4), so 128/256 Vera CPUs per rack (air-cooled/liquid-cooled). Each Vera CPU has "up to" 1.5TB SOCAMM LPDDR5X memory. During our Spotlight on Computex 2026 meeting (report link), Brand Cheng, the chairman of Foxconn Industrial Internet, said he expects to kick off mass production of the Vera CPU rack (L11) in 4Q26. Based on Nvidia's Vera Rubin POD, there is 1 Vera CPU rack per 8 Vera Rubin NVL72 racks.

Exhibit 1: Vera CPU compute tray   
![](images/863adb0042bd8a500f950aa7026f468c7e3806c44276811d6b481a73b914724c.jpg)

<details>
<summary>natural_image</summary>

Interior view of a NVIDIA Vera CPU Compute Tray module showing internal components and mounting hardware (no text or symbols on the device itself)
</details>

Source: NVIDIA, MS.

Exhibit 2: MGX Vera CPU board   
![](images/23ae613fac49fd64ae502965e940a4c885e3d2602828a9a854ed8f63ff5cd370.jpg)

<details>
<summary>text_image</summary>

NVIDIA
NVIDIA MGX™ Vera CPU Platform
The CPU for the age of AI.
</details>

Source: Compal, MS.

Exhibit 3: HGX Vera CPU board   
![](images/35c7791d2a6c6a86ed3ac2af9f5ffea36fe353125470b85c79ca538b93723c53.jpg)

<details>
<summary>text_image</summary>

NVIDIA
NVIDIA HGXTM Vera CPU Platform
The CPU designed for AI factory scale.
</details>

Source: Compal, MS.

Exhibit 4: Air-cooled Vera CPU rack with 2U compute trays (right)   
![](images/100efb58c80c8fe81c78c7b566441edb827e70b71535cf05b48b617b13c249a1.jpg)

<details>
<summary>text_image</summary>

800 VDC
Power Rack
NVIDIA® BlueField®-4
STX Storage Rack
NVIDIA Vera
CPU Rack
</details>

Source: Wistron/Wiwynn, MS.

# Groq 3 LPX Compute Tray

Hon Hai showcased a Groq 3 LPX compute tray at its booth (but this one below was taken at NVIDIA GTC Taipei, not at Hon Hai's booth). Per our checks, each LPX compute tray houses 1 Intel CPU, 2 Altera FPGAs, 1 BF-4 module, 16 LPXs and 28 QDs (20 MQD04 + 4 MQDB + 4 UQD08), with a 52L (26+26) PCB. During our Spotlight on Computex 2026 meeting (report link), Brand Cheng, the chairman of Foxconn Industrial Internet, said he expects to kick off mass production of the LPX CPU rack (in L10 and L11) in 3Q26. Based on Nvidia's Vera Rubin POD, there are 5 Groq 3 LPX racks per 8 Vera Rubin NVL72 racks.

Exhibit 5: LPX compute tray   
![](images/abe2cbc9b6cd13e4d69fcadc3dca9f212a0f09ba3b45bf2d138bcc1339319c1d.jpg)

<details>
<summary>text_image</summary>

NVIDIA Groq 3 LPX Compute Tray
</details>

Source: NVIDIA, MS.

# NVIDIA BlueField $^{®}$ -4 Storage Processor / STX Storage Rack

Wistron/Wiwynn showcased a NVIDIA BlueField $^{®}$ -4 storage processor (Exhibit 6) and a NVIDIA BlueField $^{®}$ -4 STX storage rack (Exhibit 7) at their booth. Each 2U tray containing 2 Vera CPUs, 4 ConnectX-9 NICs and 24 SSDs consumes 1.2-1.3kW, and 16 such trays make a STX rack. Based on Nvidia's Vera Rubin POD, there is 1 STX rack per 8 Vera Rubin NVL72 racks.

Exhibit 6: BlueField®-4 storage processor   
![](images/59fe2cff3b2a37636cefcccb57a5f3540a7324552500e9b16da3067bd9aa3880.jpg)

<details>
<summary>text_image</summary>

NVIDIA® BlueField®-4 Storage Processor
• NVIDIA BlueField®-4 data processor powers the NVIDIA ETC Control Memory Storage Platform, a row (less of AI-market stocks blueberries enabling power efficient, go into generic AI)
• Key Features:
• Stabilized hardware for memory tools
• Fixed GPU efficiency in low-concentive hardware
• Single Power, 25GHz and 100V DC drive power (in FiND)
• Switch with Micro-TM3.3 drives and Quad Drive SSD
</details>

Source: Wistron/Wiwynn, MS.

Exhibit 7: BlueField®-4 STX storage rack (middle)   
![](images/ab5a71dd7f4ed83d0e63e608f5b3d56beeb9553469efb1d1934df40fd8acb8f5.jpg)

<details>
<summary>text_image</summary>

800 VDC
Power Rack
NVIDIA® BlueField®-4
STX Storage Rack
NVIDIA Ver
CPU Rack
</details>

Source: Wistron/Wiwynn, MS.

# FIT's Interconnect and Power Supply Solutions

At Hon Hai's booth, we got to see FIT's interconnect and power solutions for VR200 NVL racks as well. For the 44L midplane PCB (Exhibit 8), we believe primary suppliers are VGT, WUS and Kinwong, while Zhen Ding is trying for qualifications as well. For the Paladin HD2 connectors for VR200 NVL72 midplanes and cable cartridges (Exhibit 9), our latest checks indicate ASP could reach US\$70-90+ per set, which is much higher than our previous estimate. For the next-generation Kyber racks, our checks have indicated that a new midplane connector called "Voronoi" will be introduced (report link), and FIT is the key design partner for this new board-to-board connector. The Voronoi connector was not out for display at the booth, though, as the designs have yet to be finalized; we believe FIT is currently working on yield improvement and cost optimization with its supply chain partners for Voronoi, particularly around the pogo pin designs.

FIT also showcased its power solutions (primarily in-tray busbars, liquid-cooled rack busbars and power whips) for VR200 NVL72 at the booth (Exhibit 11). This is an area where we believe FIT will be able to gain meaningful shares, starting with the Rubin platform. For the VR200 liquid-cooled busbar show in Exhibit 12, our checks indicate FIT's ASP could be in the range of US\$3,000-4,000; pricing of the next-gen rack busbar will likely be finalized by EoY 2026.

Exhibit 14 shows FIT's quick disconnects (QDs) products. For the 2" FFQD used in CDUs, we believe there are only two primary suppliers – Danfoss and FIT, and the ASP is roughly

US\$400-700 per piece, though FIT's prices could be slightly lower than this. Additionally, our checks indicate that NVIDIA is looking to introduce a new QD design for Rubin Ultra server racks, in order to achieve higher water flow per area per second, as cooling requirements increase with the TDPs of chips. We believe FIT is the primary designer of this "new QD", which implies potential disruption to the competitive landscape of the QD market.

Last but not least, FIT's external laser small form-factor pluggable (ELSFP) was another key focus at the booth (Exhibit 13). Our checks indicate that the ASP of a 20dBm (decibel-milliwatts)/100mW (milliwatts) ELSFP could reach US\$400-500, primarily driven by the high cost of lasers in the module; the 23dBm/200mW ELSFP was still a prototype, so its price has not been determined. We believe ELSFP will be more of a growth driver to FIT from 2H27 onwards.

Exhibit 8: FIT's VR200 NVL72 midplane   
![](images/a68293b464f141a8e75bf9c2270fa4a530be1c0caa4a47e525f7350e7387e0e5.jpg)

<details>
<summary>natural_image</summary>

Close-up of hands assembling electronic circuit boards with visible components and connectors (no text or symbols)
</details>

Source: FIT, MS.

Exhibit 10: FIT's backplane connector   
![](images/74515b65758c0d5eefe7415060294592d4972d90d012e73f8fb2eff5cb4af325.jpg)

<details>
<summary>text_image</summary>

BP Connector
</details>

Source: FIT, MS.

Exhibit 9: FIT's VR200 NVL72 midplane   
![](images/aea8860758121b31ac784435fd8a6750a14e0210fbb338818bfb3bb20711a032.jpg)

<details>
<summary>text_image</summary>

Midplane for
MVRDA Vortex Modbus MVL72
</details>

Source: FIT, MS.

Exhibit 11: FIT's power solutions for Vera Rubin NVL72 and Rubin NVL8 (HGX)   
![](images/7f3a4ba173b6c401a3f02b3d795c34360d0683bc6de684a1a4dd3e411c06178d.jpg)

<details>
<summary>text_image</summary>

NVIDIA MGXTM Components
for Vera Rubin NVL72 & Rubin NVL8
WISA MGX™ Components for
Vera Rubin NVL72 and Rubin NVL8
Bustar Clip 600A
Bustar Clip 600A
Bustar Clip 600A
Bustar Clip 600A
Bustar Clip 600A
Bustar Clip 600A
Bustar Clip 600A
Bustar Clip 600A
Bustar Clip 600A
Bustar Clip 600A
Bustar Clip 600C
Bustar Clip 600A
Bustar Clip 600A
Bustar Clip 600A
Bustar Clip 600A
Bustar Clip 600A
Bustar Clip 600A
Bustar Clip 600A
Bustar Clip 600A
Bustar Clip 600A
Bustar Clip 600
</details>

Source: FIT, MS.

Exhibit 12: FIT's liquid-cooled busbar   
![](images/6288bb574e6550ae11431ed3e3f0a54014fef73c0c3c9573d8c030e311e9643e.jpg)

<details>
<summary>text_image</summary>

LC Busbar
</details>

Source: FIT, MS.

Exhibit 13: FIT's external laser small form-factor pluggables (ELSFP)   
![](images/a4a93d9febe0d845d74dd37af76462287d3774bb9ac385d257a14ec982263db8.jpg)

<details>
<summary>text_image</summary>

CPO VHP ELSFP (23dBm)
CPO UHP ELSFP (20dBm)
</details>

Source: FIT, MS.

Exhibit 14: FIT's quick disconnect (QDs)   
![](images/97702e39ddf769d568f22ab2d10aa7dd8aa300fb6ee069f98201b741ee529b29.jpg)

<details>
<summary>text_image</summary>

L278
L288W
Fainting
1" FFQD
2" FFQD
</details>

Source: FIT, MS.

# RTX Spark – redefining PC?

Another highlight is NVIDIA x MediaTek's RTX Spark for PCs: The Arm-based SoC, which combines a Grace CPU, Blackwell GPU, AI acceleration, and unified memory, was officially announced by NVIDIA CEO Jensen Huang at his 2026 Computex keynote speech. We got to see the RTX Spark notebooks from Lenovo, Asustek, MSI, Dell, HP and Microsoft at MediaTek's booth (Exhibit 15 and Exhibit 16); Asustek also showcased their RTX Spark PCs at its own booths (Exhibit 17 and Exhibit 18). During the financial analyst Q&A session, NVIDIA Jensen Huang also shared his vision on the future of PCs, where PCs don't simply work as "typewriters" but real agents that can complete tasks on the user's behalf, even when the user is not physically around.

While we don't argue against Jensen's vision on agentic PCs, we believe it's unlikely that RTX Spark will have a meaningful impact on PC end demand in the next 12 months. Our checks suggest the RTX Spark NBs target to ship from fall 2026 onwards, with price points likely reaching US\$3,000+ (on 128GB of DRAM) and combined shipments of only 5-10mn for the two variants (N1X, followed by N1) in the first 12 months. Our checks suggest a quarterly run rate of 200-250k units/quarter for the N1X chip, implying only \~1M units for the first 12 months. The higher prices will likely prevent the RTX Spark PCs from becoming mainstream, which implies that these PCs will hardly offset a "PC market rolling over", as we head into 2H with continued PC price hikes.

Initially, these "Agentic PCs" will only be bought by the real AI power users, but we have also seen a lot of these power users buying Mac Minis earlier in the same to run their AI workloads. As a result, we think volumes will likely come in below expectations. That said, between a laptop and a desktop form factor, we are of the view that the desktop form factor would make more sense as a PC that you keep at home running 24/7.

See also our report: Global PCs: Will RTX Spark Reinvigorate the PC Market? (3 Jun 2026)

# RTX Spark specs:

- Up to 128 GB unified memory   
- Up to 1 petaflop FP4 AI performance   
- Up to 20 core ultra-efficient CPU   
- Up to 6,144 core RTX GPU

- "All-day" battery life   
• Built for agents and AI

Exhibit 15: MSI, Dell and Lenovo's RTX Spark NBs   
![](images/39f502eb5c0de21d9080bc85c1f6480fd804d426d0bba32faaa2b9e86020d6c5.jpg)

<details>
<summary>text_image</summary>

Duo XPS 10
Lenovo
Lenovo Yoga Pro 9n
</details>

Source: MediaTek, MSI, Dell, Lenovo and MS.

Exhibit 16: Microsoft, ASUS and HP's RTX Spark NBs   
![](images/065b8cabfb000f959201349c37f15bc7adb5d5c48847b9c366acf8cbe60df9a9.jpg)

<details>
<summary>natural_image</summary>

Display of three laptops on a white shelf with colorful abstract graphics in the background (no visible text or symbols on main objects)
</details>

Source: MediaTek, Microsoft, ASUS, HP and MS.

Exhibit 17: ASUS ProArt Mini PC powered by NVIDIA RTX Spark   
![](images/3e6533554d80299864dd0515a6c70f78926c61e5d93e7def99a53fa569a9f881.jpg)

<details>
<summary>text_image</summary>

STARK OF AI
ASUS ProArt Mini PC
Powered by NVIDIA RTX Spark
</details>

Source: ASUS, MS.

Exhibit 18: ASUS ProArt P16 powered by NVIDIA RTX Spark   
![](images/513eecc422a72c529597922a878034b39d9d7a91ae9a55df8f7f9c62cffb92f7.jpg)

<details>
<summary>text_image</summary>

ProArt
ASUS ProArt P16
Powered by NVIDIA ProArt Spark
ProArt
Do Not Touch
Asus ProArt P16
Follow the Green to Win
</details>

Source: ASUS, MS.

# Power and Cooling

# 800 VDC Power Rack Aims for Mass Production in 3Q26

800 VDC deployment path throughout 2028: While 800V HVDC power solution remains in development, Nvidia at its GTC Taipei indicates the development will be separated in stages:

• 800 VDC power rack is ready for deployment in 3Q26   
• 800 VDC power center of 1.6MW will be ready in 2Q27   
- 800 VDC power block featured 4.8MW aims for ready for deployment In 1Q28

Exhibit 19: 800 VDC equipment readiness   
![](images/f0712da19f184471c74a9b8478172a41819818bbca3d8b4e19bb3a9bfa5a61eb.jpg)

<details>
<summary>text_image</summary>

800 VDC Equipment Readiness
2026
Q3 2026 Option 1A – Power Rack
(660 kW) Q2 2027 Option 1B – DC Power Center
(1.6 MW) Q1 2028 Option 1C – Power Block
(4.8 MW+)
✓ Deployment Ready ✓ Deployment Ready ✓ Deployment Ready
Focus Area Status Impact
Grounding & Protection ● Architecture converging with UL and OEMs Foundation for safe and reliable deployment
Equipment Certification ● Certification pathways established and progressing Accelerates deployment readiness
Collection Devices ● MCCB available; SSCB ecosystem maturing Enables fast fault isolation and higher availability
Highway, Connector & Whips ● Standardized 125A architecture under development Supports scalable rack deployment
Density Power
version ● Rectifiers available SST roadmap advancing Enables future 800 VDC Compute Product
</details>

Source: Nvidia, MS.

At Computex, we have seen quite a few power solution vendors showcase 800 VDC standalone power racks, such as Delta Electronics, Lite-On Tech, Vertiv, Schneider, FLEX, etc. Our check suggests there will be two design specs for 800 VDC standalone power racks in 2H26 – one is featured 660kW (without BBU) and the other is 900kW (with BBU). Nvidia is collaborating with Microsof

[中间内容因长度限制已省略]

 Fibre and Cable JSC Ltd (601869.SS)</td><td>U (10/13/2021)</td><td>Rmb441.67</td></tr><tr><td>Yangtze Optical Fibre and Cable JSC Ltd (6869.HK)</td><td>E (04/20/2023)</td><td>HK$239.20</td></tr><tr><td>Yongxin Optics Co Ltd (603297.SS)</td><td>E (11/15/2022)</td><td>Rmb123.83</td></tr><tr><td>Zhejiang Crystal-Optech Co Ltd (002273.SZ)</td><td>O (11/15/2022)</td><td>Rmb36.22</td></tr><tr><td>Zhongji Innolight Co Ltd (300308.SZ)</td><td>++</td><td>Rmb1,179.99</td></tr><tr><td>ZTE Corporation (0763.HK)</td><td>O (06/04/2026)</td><td>HK$29.66</td></tr><tr><td>ZTE Corporation (000063.SZ)</td><td>E (06/04/2026)</td><td>Rmb39.13</td></tr></table>

Derrick Yang 

<table><tr><td>Accton Technology Corporation (2345.TW)</td><td>O (06/06/2024)</td><td>NT$2,490.00</td></tr><tr><td>Advantech (2395.TW)</td><td>O (01/20/2021)</td><td>NT$496.00</td></tr><tr><td>AirTAC International (1590.TW)</td><td>O (04/16/2025)</td><td>NT$1,320.00</td></tr><tr><td>AU Optronics (2409.TW)</td><td>E (02/10/2026)</td><td>NT$27.10</td></tr><tr><td>Bizlink (3665.TW)</td><td>O (03/10/2025)</td><td>NT$2,200.00</td></tr><tr><td>BOE Technology (000725.SZ)</td><td>O (09/06/2019)</td><td>Rmb6.43</td></tr><tr><td>Chenbro (8210.TW)</td><td>O (07/23/2025)</td><td>NT$1,370.00</td></tr><tr><td>Chroma Ate Inc. (2360.TW)</td><td>O (10/05/2021)</td><td>NT$2,565.00</td></tr><tr><td>E Ink Holdings Inc. (8069.TWO)</td><td>O (05/11/2026)</td><td>NT$214.00</td></tr><tr><td>Ennostar Inc (3714.TW)</td><td>U (09/23/2022)</td><td>NT$70.20</td></tr><tr><td>Hiwin Technologies Corp. (2049.TW)</td><td>O (03/30/2026)</td><td>NT$345.00</td></tr><tr><td>Innolux (3481.TW)</td><td>E (04/07/2025)</td><td>NT$53.70</td></tr><tr><td>King Slide Works Co. Ltd. (2059.TW)</td><td>O (11/08/2023)</td><td>NT$5,620.00</td></tr><tr><td>Lens Technology (300433.SZ)</td><td>E (07/22/2020)</td><td>Rmb45.61</td></tr><tr><td>Radiant Opto-Electronics Corporation (6176.TW)</td><td>E (03/01/2024)</td><td>NT$101.00</td></tr><tr><td>Sanan Optoelectronics (600703.SS)</td><td>U (08/21/2023)</td><td>Rmb16.91</td></tr><tr><td>TCL Corp. (000100.SZ)</td><td>E (04/07/2025)</td><td>Rmb4.89</td></tr><tr><td>Tianma Microelectronics (000050.SZ)</td><td>U (01/24/2018)</td><td>Rmb8.61</td></tr><tr><td>Wuhan Jingce Electronic Group Co Ltd (300567.SZ)</td><td>E (11/26/2021)</td><td>Rmb189.23</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.   
\* Historical prices are not split adjusted.   
Howard Kao 

<table><tr><td>Acer Inc. (2353.TW)</td><td>U (04/23/2025)</td><td>NT$38.40</td></tr><tr><td>Asustek Computer Inc. (2357.TW)</td><td>U (11/16/2025)</td><td>NT$900.00</td></tr><tr><td>Compal Electronics (2324.TW)</td><td>U (04/23/2025)</td><td>NT$41.40</td></tr><tr><td>FIT Hon Teng Ltd (6088.HK)</td><td>O (11/03/2025)</td><td>HK$8.45</td></tr><tr><td>Giga-Byte Technology Co. Ltd. (2376.TW)</td><td>E (11/16/2025)</td><td>NT$369.00</td></tr><tr><td>Gold Circuit Electronics Ltd. (2368.TW)</td><td>O (10/06/2022)</td><td>NT$1,315.00</td></tr><tr><td>Inspur Electronic Information (000977.SZ)</td><td>E (08/28/2023)</td><td>Rmb62.14</td></tr><tr><td>Lenovo (0992.HK)</td><td>E (11/16/2025)</td><td>HK$24.88</td></tr><tr><td>Lotes Co. Ltd. (3533.TW)</td><td>E (05/12/2025)</td><td>NT$2,365.00</td></tr><tr><td>Nan Ya PCB (8046.TW)</td><td>O (02/23/2026)</td><td>NT$845.00</td></tr><tr><td>Pegatron Corporation (4938.TW)</td><td>E (03/25/2026)</td><td>NT$96.90</td></tr><tr><td>Quanta Computer Inc. (2382.TW)</td><td>O (05/01/2023)</td><td>NT$390.50</td></tr><tr><td>Shengyi Technology Co Ltd. (600183.SS)</td><td>E (05/26/2022)</td><td>Rmb137.36</td></tr><tr><td>Shennan Circuits Co Ltd (002916.SZ)</td><td>E (08/24/2023)</td><td>Rmb373.00</td></tr><tr><td>Unimicron (3037.TW)</td><td>O (02/23/2026)</td><td>NT$933.00</td></tr><tr><td>Wistron Corporation (3231.TW)</td><td>O (07/12/2023)</td><td>NT$171.00</td></tr><tr><td>Wiwynn Corp (6669.TW)</td><td>O (11/10/2025)</td><td>NT$5,660.00</td></tr><tr><td>Yageo Corp. (2327.TW)</td><td>O (10/28/2025)</td><td>NT$769.00</td></tr><tr><td>Zhen Ding (4958.TW)</td><td>O (05/18/2026)</td><td>NT$504.00</td></tr><tr><td colspan="3">Sharon Shih</td></tr><tr><td>Asia Vital Components Co. Ltd. (3017.TW)</td><td>O (07/30/2024)</td><td>NT$2,600.00</td></tr><tr><td>Auras Technology Co Ltd (3324.TWO)</td><td>E (05/04/2023)</td><td>NT$1,110.00</td></tr><tr><td>Catcher Technology (2474.TW)</td><td>U (11/17/2025)</td><td>NT$230.50</td></tr><tr><td>Delta Electronics Inc. (2308.TW)</td><td>O (07/13/2017)</td><td>NT$2,300.00</td></tr><tr><td>Fositek Corp (6805.TW)</td><td>O (06/25/2025)</td><td>NT$1,950.00</td></tr><tr><td>Foxconn Industrial Internet Co. Ltd. (601138.SS)</td><td>O (07/10/2019)</td><td>Rmb74.06</td></tr><tr><td>Foxconn Technology (2354.TW)</td><td>U (04/23/2025)</td><td>NT$60.60</td></tr><tr><td>GoerTek Inc (002241.SZ)</td><td>U (04/23/2025)</td><td>Rmb24.82</td></tr><tr><td>Hon Hai Precision (2317.TW)</td><td>O (03/15/2024)</td><td>NT$284.50</td></tr><tr><td>LandMark Optoelectronics Corporation (3081.TWO)</td><td>E (03/26/2026)</td><td>NT$2,655.00</td></tr><tr><td>Lingyi Itech Guangdong Co (002600.SZ)</td><td>U (04/23/2025)</td><td>Rmb15.08</td></tr><tr><td>Lite-On Technology (2301.TW)</td><td>E (01/15/2025)</td><td>NT$230.00</td></tr><tr><td>Luxshare Precision Industry Co., Ltd. (002475.SZ)</td><td>O (10/24/2016)</td><td>Rmb68.77</td></tr><tr><td>Sunonwealth Electric Machine Industry Co (2421.TW)</td><td>E (02/23/2024)</td><td>NT$161.50</td></tr><tr><td>Tong Hsing (6271.TW)</td><td>E (03/18/2019)</td><td>NT$236.50</td></tr><tr><td>Visual Photonics Epitaxy Co Ltd (2455.TW)</td><td>E (09/11/2023)</td><td>NT$399.00</td></tr></table>

© 2026 MS
"""
