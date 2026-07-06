# Bernstein：半导体光刻强度升至26%，ASML份额持续扩大而非被蚕食

市场对ASML的观察，很大程度上集中在High-NA EUV（高数值孔径极紫外光刻）的采用时间表上。台积电曾公开表达过对成本的顾虑，这让不少观察者认为High-NA的推广会显著滞后。但Bernstein这份最新深度报告给出了一个反直觉的判断：High-NA的采用路径比市场想象的更清晰，而且第一个大规模落地的场景，可能不在逻辑芯片，而在DRAM。

这份报告的核心价值，在于它拆解了High-NA成本结构中最容易被忽视的变量——掩模拼接。它解释了为什么对DRAM而言，High-NA的宏观环境账更容易算通，以及为什么整个半导体制造的光刻强度（litho intensity）正在进入一个上升周期。

![研报原图 1](assets/source_image_01.jpg)

## 1. DRAM的“小芯片”优势让High-NA成本更低

市场普遍认为High-NA太贵，但Bernstein指出，这个判断忽略了芯片尺寸带来的巨大差异。High-NA EUV的光学系统采用4倍和8倍的非等比缩小设计，导致其曝光场只有传统Low-NA EUV的一半。这意味着，对于尺寸较大的逻辑芯片（如GPU），需要将一个大芯片拆分到两个掩模上并进行拼接，这个过程会降低约23%的吞吐量。

而对于DRAM，其芯片尺寸天生较小，可以完整地放在一个曝光场内，无需拼接。因此，DRAM使用High-NA的单次曝光成本显著低于逻辑芯片。报告测算显示，即使考虑设备成熟度，到2027年，当Low-NA EUV需要双重曝光时，DRAM转向High-NA在宏观环境上是合理的。这预示着三星、SK海力士和美光将在1d制程节点率先引入High-NA。

> **KC评论：** 这一判断改变了市场的叙事焦点。过去大家只盯着台积电的表态，但忽略了存储芯片厂在先进制程上的竞争同样激烈，且它们的工艺特点更适合High-NA的早期导入。这为ASML的EUV出货量提供了一个新的、更确定的增长引擎。

![研报原图 2](assets/source_image_02.jpg)

## 2. 光刻强度从24%升至26%，ASML将获得更大份额

High-NA带来的不仅是设备本身的升级，更是整个制造流程的重构。当High-NA取代Low-NA的多重曝光时，它可以大幅减少后续的刻蚀、沉积、清洗等环节。这意味着，在芯片总制造成本中，光刻环节的占比（即光刻强度）将上升。

报告预测，全球光刻强度将从2025年的24%提升至2028年的26%。其中，DRAM的光刻强度将从1z节点的约20%跃升至1d节点的约30%。逻辑芯片的光刻强度在N2和A14节点将保持稳定，但会在A10节点后开始上升。这个趋势意味着，在整个半导体设备市场中，ASML的份额将持续扩大，而不是被其他工艺设备所蚕食。

![研报原图 3](assets/source_image_03.jpg)

## 3. ASML的增长尚未见顶，2030年营收有望达到800亿欧元

基于AI驱动的先进逻辑和DRAM产能扩张，Bernstein大幅上调了ASML的营收预测。报告将2027年的EUV（含High-NA）出货量从86台上调至91台，2028年从87台上调至113台。更重要的是，随着吞吐量的提升，设备平均售价也在强劲增长。

报告预计，到2030年，ASML的EUV业务营收将以30%的年复合增长率增长，达到427亿欧元，比市场普遍预期高出30%以上。同时，DUV业务在2026年至2030年间也将从130亿欧元增长至200亿欧元。综合来看，ASML的营收有望在2030年达到800亿欧元（20%的年复合增长率），每股收益达到97欧元（31%的年复合增长率）。

> **KC评论：** 市场对半导体周期的顶部总有担忧，但这份报告的核心论点是，ASML的增长驱动力已经从单纯的资本开支周期，转变为“资本开支周期”叠加“光刻强度结构性上升”的双重引擎。后者是更持久、更确定的结构性变量。

## 4. 报告尚未完全回答的关键问题：High-NA的成本下降曲线能否如期兑现

尽管论证逻辑严密，但报告本身也指出了几个关键的未解问题。High-NA设备当前的可用性（availability）仅为80-85%，远低于Low-NA的95%。虽然报告给出了到2030年提升至95%的路径，但这依赖于ASML对供应链和系统集成的持续优化。任何一个环节的延迟，都会影响成本下降的速度，进而影响客户的采用决策。

此外，报告假设的客户采用时间表——英特尔在2028年率先采用High-NA，台积电在2030年跟进——也面临不确定性。台积电的技术路线选择、客户对芯片尺寸和性能的要求，都可能改变这个时间表。

这些问题，正是值得去完整阅读Bernstein这份报告，并持续追踪后续数据点的地方。完整的报告、中文摘要、KC评论和图表合集，可以放回当天的全球半导体主线中继续观察。

<p style="color:#999999;font-size:12px;">For informational purposes only. Portions may be generated,translated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>

![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)

<p style="color:#999999;font-size:12px;">For informational purposes only. Portions may be generated,translated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>
