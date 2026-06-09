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


# Sharon Shih


# Derrick Yang


# Samantha Chen


# Irene Yen


# Vivi Huang


# GREATER CHINA TECHNOLOGY HARDWARE

# Asia Pacific


In-Line

MS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.

# For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.


# Servers and PCs

# Vera CPU Compute Tray / Rack

There are 2 Vera CPUs on a NVIDIA MGX Vera CPU board (Exhibit 2), 4 Vera CPU board in a Vera CPU compute tray (Exhibit 1) and 16/32 Vera CPU compute trays in a Vera CPU rack (Exhibit 4), so 128/256 Vera CPUs per rack (air-cooled/liquid-cooled). Each Vera CPU has "up to" 1.5TB SOCAMM LPDDR5X memory. During our Spotlight on Computex 2026 meeting (report link), Brand Cheng, the chairman of Foxconn Industrial Internet, said he expects to kick off mass production of the Vera CPU rack (L11) in 4Q26. Based on Nvidia's Vera Rubin POD, there is 1 Vera CPU rack per 8 Vera Rubin NVL72 racks.

Exhibit 1: Vera CPU compute tray

[[KC_IMAGE_001]]


Source: NVIDIA, MS.

Exhibit 2: MGX Vera CPU board

[[KC_IMAGE_002]]


Source: Compal, MS.

Exhibit 3: HGX Vera CPU board

[[KC_IMAGE_003]]


Source: Compal, MS.

Exhibit 4: Air-cooled Vera CPU rack with 2U compute trays (right)

[[KC_IMAGE_004]]


Source: Wistron/Wiwynn, MS.

# Groq 3 LPX Compute Tray

Hon Hai showcased a Groq 3 LPX compute tray at its booth (but this one below was taken at NVIDIA GTC Taipei, not at Hon Hai's booth). Per our checks, each LPX compute tray houses 1 Intel CPU, 2 Altera FPGAs, 1 BF-4 module, 16 LPXs and 28 QDs (20 MQD04 + 4 MQDB + 4 UQD08), with a 52L (26+26) PCB. During our Spotlight on Computex 2026 meeting (report link), Brand Cheng, the chairman of Foxconn Industrial Internet, said he expects to kick off mass production of the LPX CPU rack (in L10 and L11) in 3Q26. Based on Nvidia's Vera Rubin POD, there are 5 Groq 3 LPX racks per 8 Vera Rubin NVL72 racks.

Exhibit 5: LPX compute tray

[[KC_IMAGE_005]]


Source: NVIDIA, MS.

# NVIDIA BlueField $^{®}$ -4 Storage Processor / STX Storage Rack

Wistron/Wiwynn showcased a NVIDIA BlueField $^{®}$ -4 storage processor (Exhibit 6) and a NVIDIA BlueField $^{®}$ -4 STX storage rack (Exhibit 7) at their booth. Each 2U tray containing 2 Vera CPUs, 4 ConnectX-9 NICs and 24 SSDs consumes 1.2-1.3kW, and 16 such trays make a STX rack. Based on Nvidia's Vera Rubin POD, there is 1 STX rack per 8 Vera Rubin NVL72 racks.

Exhibit 6: BlueField®-4 storage processor

[[KC_IMAGE_006]]


Source: Wistron/Wiwynn, MS.

Exhibit 7: BlueField®-4 STX storage rack (middle)

[[KC_IMAGE_007]]


Source: Wistron/Wiwynn, MS.

# FIT's Interconnect and Power Supply Solutions

At Hon Hai's booth, we got to see FIT's interconnect and power solutions for VR200 NVL racks as well. For the 44L midplane PCB (Exhibit 8), we believe primary suppliers are VGT, WUS and Kinwong, while Zhen Ding is trying for qualifications as well. For the Paladin HD2 connectors for VR200 NVL72 midplanes and cable cartridges (Exhibit 9), our latest checks indicate ASP could reach US\$70-90+ per set, which is much higher than our previous estimate. For the next-generation Kyber racks, our checks have indicated that a new midplane connector called "Voronoi" will be introduced (report link), and FIT is the key design partner for this new board-to-board connector. The Voronoi connector was not out for display at the booth, though, as the designs have yet to be finalized; we believe FIT is currently working on yield improvement and cost optimization with its supply chain partners for Voronoi, particularly around the pogo pin designs.

FIT also showcased its power solutions (primarily in-tray busbars, liquid-cooled rack busbars and power whips) for VR200 NVL72 at the booth (Exhibit 11). This is an area where we believe FIT will be able to gain meaningful shares, starting with the Rubin platform. For the VR200 liquid-cooled busbar show in Exhibit 12, our checks indicate FIT's ASP could be in the range of US\$3,000-4,000; pricing of the next-gen rack busbar will likely be finalized by EoY 2026.

Exhibit 14 shows FIT's quick disconnects (QDs) products. For the 2" FFQD used in CDUs, we believe there are only two primary suppliers – Danfoss and FIT, and the ASP is roughly

US\$400-700 per piece, though FIT's prices could be slightly lower than this. Additionally, our checks indicate that NVIDIA is looking to introduce a new QD design for Rubin Ultra server racks, in order to achieve higher water flow per area per second, as cooling requirements increase with the TDPs of chips. We believe FIT is the primary designer of this "new QD", which implies potential disruption to the competitive landscape of the QD market.

Last but not least, FIT's external laser small form-factor pluggable (ELSFP) was another key focus at the booth (Exhibit 13). Our checks indicate that the ASP of a 20dBm (decibel-milliwatts)/100mW (milliwatts) ELSFP could reach US\$400-500, primarily driven by the high cost of lasers in the module; the 23dBm/200mW ELSFP was still a prototype, so its price has not been determined. We believe ELSFP will be more of a growth driver to FIT from 2H27 onwards.

Exhibit 8: FIT's VR200 NVL72 midplane

[[KC_IMAGE_008]]


Source: FIT, MS.

Exhibit 10: FIT's backplane connector

[[KC_IMAGE_009]]


Source: FIT, MS.

Exhibit 9: FIT's VR200 NVL72 midplane

[[KC_IMAGE_010]]


Source: FIT, MS.

Exhibit 11: FIT's power solutions for Vera Rubin NVL72 and Rubin NVL8 (HGX)

[[KC_IMAGE_011]]


Source: FIT, MS.

Exhibit 12: FIT's liquid-cooled busbar

[[KC_IMAGE_012]]


Source: FIT, MS.

Exhibit 13: FIT's external laser small form-factor pluggables (ELSFP)

[[KC_IMAGE_013]]


Source: FIT, MS.

Exhibit 14: FIT's quick disconnect (QDs)

[[KC_IMAGE_014]]


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

[[KC_IMAGE_015]]


Source: MediaTek, MSI, Dell, Lenovo and MS.

Exhibit 16: Microsoft, ASUS and HP's RTX Spark NBs

[[KC_IMAGE_016]]


Source: MediaTek, Microsoft, ASUS, HP and MS.

Exhibit 17: ASUS ProArt Mini PC powered by NVIDIA RTX Spark

[[KC_IMAGE_017]]


Source: ASUS, MS.

Exhibit 18: ASUS ProArt P16 powered by NVIDIA RTX Spark

[[KC_IMAGE_018]]


Source: ASUS, MS.

# Power and Cooling

# 800 VDC Power Rack Aims for Mass Production in 3Q26

800 VDC deployment path throughout 2028: While 800V HVDC power solution remains in development, Nvidia at its GTC Taipei indicates the development will be separated in stages:

• 800 VDC power rack is ready for deployment in 3Q26
• 800 VDC power center of 1.6MW will be ready in 2Q27
- 800 VDC power block featured 4.8MW aims for ready for deployment In 1Q28

Exhibit 19: 800 VDC equipment readiness

[[KC_IMAGE_019]]


Source: Nvidia, MS.

At Computex, we have seen quite a few power solution vendors showcase 800 VDC standalone power racks, such as Delta Electronics, Lite-On Tech, Vertiv, Schneider, FLEX, etc. Our check suggests there will be two design specs for 800 VDC standalone power racks in 2H26 – one is featured 660kW (without BBU) and the other is 900kW (with BBU). Nvidia is collaborating with Microsoft and Google on OCP power distribution standards, meaning no +-400V transitional solution. The supply chain is currently working with UL, IEEE and NFPA for new DC regulatory standards to AI data centers. It is also important to work on grounding and protection system alignment across the industry.

The development of solid-state transformer (SST) technology will also continue for higher power density applications. Our checks suggest Delta also showcased models for SST and fuel cell. Our checks suggest Delta's fuel cell pilot run production is on track to start from 2H26 and targeted for mass production in Taoyuan plant with targeted capacity of 300MW. SST comes in the size of 10' container and features 98.5% conversion efficiency

with output power of 1-2MW.

Exhibit 20: Solid Oxide Fuel Cell

[[KC_IMAGE_020]]


Source: Delta, MS.

Exhibit 21: Solid State Transformer

[[KC_IMAGE_021]]


Source: Delta, MS.

# TDP increases boost liquid cooling design upgrade

Various related vendors showcased liquid-to-air, liquid-to-liquid CDU and in-row CDU, signaling that future adoption will grow fast along with the Vera Rubin rack shipment ramp. General commentary suggests that a total solution offering and product reliability are key to winning. Delta showcased new 3MW liquid-to-liquid In-ROW CDU and targets to launch 6.8MW liquid-to-liquid In-ROW CDU by end of this year.

Exhibit 22: Delta's 3MW LTL In-ROW CDU

[[KC_IMAGE_022]]


Source: Delta, MS.

# Liquid cooling design for Vera Rubin

Vera Rubin liquid cooling with Bianca board design is indicated to be ready for mass production in 3Q26. Our checks suggest the content value of cold plate modules, inner manifold and NVQD per GPU tray is \~ US\$2,500. As mentioned in our takeaways, our checks suggest NVIDIA is looking to introduce a new design for QDs used in the Rubin Ultra rack systems.

Exhibit 23: Nvidia Vera Rubin NVL72 GPU Tray and Switch Tray

[[KC_IMAGE_023]]


Source: Nvidia, MS.

# Microchannel lid the next to come

A microchannel lid is an advanced thermal lid in which a network of micro-scale channels is fabricated within a metal cap and coolant is actively circulated through these channels. Comparing to the traditional multi-layer structure of liquid cooling (die, TIM1, lid, TIM2, and cold plate), MCL eliminates multiple thermal interfaces, directly attached to TIM 1, and significantly increasing heat transfer efficiency. Thus, its thermal capabilities surpasses that of existing cold-plate solutions. We believe microchannel lids could be a potential thermal design for upcoming chip platforms because TDP for chips continues to increase and exceed the thermal capabilities of existing solutions.

However, our checks suggest the adoption of MCL will take time – manufacturing yield, leakage detection and long-term reliability requirements remain challenges. OSATs will need to introduce additional process steps and upgrade equipment to enable coolant-injection testing, pressure validation, and post-test cleaning prior to shipment to customers and downstream module assemblers. As MCL becomes an integral component of the silicon packaging flow, its qualification cycle is extended and demands extensive reliability testing to meet datacenter deployment standards

Exhibit 24: Jentech's Microchannel lid

[[KC_IMAGE_024]]


Source: Jentech, MS

Exhibit 25: Delta's Micro Channel Lid

[[KC_IMAGE_025]]


Source: Delta, MS.

# Networking, Interconnects and Mechanical Components

# Accton

Accton showcased an optical wavelength selection (OWS) switch, based on the optical engine from its subsidiary InLC. OWS can be used in the scale up and scale across network for the AI cluster. Moreover, it has another CPO based switch in its booth. We believe that these demonstrate that Accton has the capability design and manufacture network switches based on different technologies and protocols. Our checks indicate that Accton has been engaging with potential customers for the optical switches and there might be some revenue contribution from 2027.

Besides the network switches, Accton also showcased its rack level solution, Edgecore Open Fabric, which is designed as an open platform that can integrate compute, networking, storage, and other complementary sub modules. We believe that end customers are increasingly request their supply chain partners to provide the rack level solutions, instead of individual components and modules, so Accton is also moving toward this direction. That said, it's understandable that there are some concerns regarding the margin-dilutive rack business, but we believe that Accton will try to mitigate that through more internally developed content, including the network switch, compute tray/server module assembly, optical transceivers, liquid cooling system, etc. Through more valued added in the process, instead of just assembly the rack, Accton should have the chance to generate margins comparable to its corporate average from this rack level business. We believe there might be some revenue contribution from 2027.

Exhibit 26: Accton - OWS Switch

[[KC_IMAGE_026]]


Source: Accton, MS.

Exhibit 27: Accton - Open Platform Rack Solution

[[KC_IMAGE_027]]


Source: Accton, MS.

# Micro LED in optical communications

MediaTek (2454.TW, covered by Charlie Chan) showcased a prototype of micro LED based active optical cable during Computex this year. The basic concept is to replace the mainstream laser diode with micro LED chips as the light source in the optical communication modules.

Compared to the current laser-diode based optical modules, micro LED based ones can offer power savings (30-50%), copper level reliability, scalability, monolithic CMOS integration, etc.

This new optical module could be used in optical transceivers first and could also be adopted by the CPO architecture in the longer term.

We note that Credo (CRDO.US, not covered) have been talking about its active LED cables (ALC) for several quarters, which are based on the similar technology as mentioned above. Bizlink will be the assembly partner for Credo, which expects the revenue contribution from start from its GY2028 (starting May 2027)

Other supply chain players include Ennostar (3714.TW) for micro LED chips, Tyntek (2426.TW) for photodiodes and AUO (2409.TW) for glass based packaging.

Exhibit 28: Mediatek - Micro LED Optical Engine Prototype

[[KC_IMAGE_028]]


Source: MediaTek, MS

Exhibit 29: Mediatek - Micro LED Optical Engine Prototype Spec

Source: MediaTek, MS

# Bizlink

# Power interconnects

Power whips and busbars are one of the major offerings at Bizlink. it showcased a variety of products with different specs that can fit into different customer demand. It has been one of the major suppliers in both the AI server and general server space, and we believe that it will stay competitive and even gain shares in some projects.

Exhibit 30: Power whips

Source: Bizlink, MS

Exhibit 31: Busbars

Source: Bizlink, MS

Exhibit 32: Busbar connectors

Source: Bizlink, MS

Exhibit 33: Powerwhips and busbar cables

Source: Bizlink, MS

# Data interconnect

Bizlink has a comprehensive portfolio of data interconnects, including DAC, AEC, AOC, etc. Those cables can support up to 1.6T of data rate now and could further evolve along with the industry spec upgrades

Through the acquisition of XFS, it also strengthened its capability in the optical fiber assembly and shuffle box. We expect the shuffle box shipment for CPO switch should start from 2027 and more meaningful shipment from 2028.

Exhibit 34: Bizlink - Shuffle Box

Source: Bizlink, MS

Exhibit 35: Bizlink - High Speed Data Cables

Source: Bizlink, MS

# Emerging businesses

Bizink have their data interconnect and power interconnect offerings designed for the low earth orbit (LEO), drone, autonomous driving and robotic dog applications. There offerings need special design and materials to meet the specific requirement in their stringent operating environments.

The revenue contribution from these applications are not significant yet, but it could represent good opportunities in the longer term

Exhibit 36: Bizlink - Offerings for LEO Satellite

Source: Bizlink, MS

Exhibit 37: Bizlink - Offerings for Drone

Source: Bizlink, MS

Exhibit 38: Bizlink - Offerings for Autonomous Driving

Source: Bizlink, MS

Exhibit 39: Bizlink - Offerings for Robotic Dog

Source: Bizlink, MS

# Mechanical Components

# Chenbro

Chenbro showcased its 1U NVIDIA MGX Vera Rubin server chassis solution, along with a full series of AI chassis products—including 1U, 2U, 4U, and 6U models—developed based on NVIDIA MGX architecture, as well as the AMD Helios compute tray chassis.

The company also unveiled several full rack solutions compatible with Nvidia's VR NVL72. Chenbro has turned more aggressive on tapping into the rack business, as it has been engaging with multiple new projects. We believe the development of more AI-related racks, including IT racks, CPU racks, switch racks, power racks, CDU racks, etc should be a positive trend for Chenbro on more project opportunities

Additionally, Chenbro exhibited a model blueprint of its Malaysia factory, showing their diversified global footprint to stay resilient amid geopolitical risks and be more responsive to customer demand. The new capacity will start mass production in Malaysia in 3Q26, with more to come in the US in 4Q27.

# King Slide

For King slide (2059.TW), it has no booth in the Computex exhibition this time, but its rail kits are widely integrated into various racks showcased by different supply chain players. We are seeing the trend of more AI related devices adopting rail kits for the ease of maintenance and repair, which presents a bigger addressable market for King Slide.

Exhibit 40: Nvidia MGX chassis for Vera CPU

Source: Chenbro, MS

Exhibit 41: Nvidia MGX 2U chassis for Vera CPU - a closer look

Source: Chenbro, MS
