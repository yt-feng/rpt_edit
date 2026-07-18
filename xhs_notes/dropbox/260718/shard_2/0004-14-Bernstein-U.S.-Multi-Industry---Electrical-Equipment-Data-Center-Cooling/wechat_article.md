# Bernstein：美国多行业-电气设备数据中心冷却与供电-不同设备每兆瓦价值

AI基础设施的扩张正在改写数据中心设备供应商的竞争格局。Bernstein最新研报提供了一个此前市场缺乏的量化框架：不同冷却与供电架构下，每兆瓦（MW）的设备价值究竟如何分布。核心结论是，从风冷到液冷、从传统交流电到高压直流电，总设备价值并未大幅变化，但价值在组件之间发生了显著转移。对于读者而言，理解这个转移方向，比单纯关注“数据中心概念”更重要。

报告通过组件级拆解，给出了清晰的数字参考。在冷却侧，风冷数据中心每兆瓦设备价值约为110万至150万美元，液冷数据中心则提升至130万至180万美元。增量主要来自冷板、冷却液分配单元（CDU）和管路歧管，这些组件在风冷架构中完全不存在。而在供电侧，传统交流架构每兆瓦价值为180万至250万美元，混合800V直流架构为170万至250万美元，原生800V直流架构为140万至210万美元。价值下降并不剧烈，因为UPS虽然被取消，但电池储能系统（BESS）、整流器和电压调节模块（VRM）等新设备填补了空缺。

![研报原图 1](assets/source_image_01.jpg)

## 1. 液冷不是替代，而是重新分配冷却价值链

报告指出，液冷架构并非完全抛弃风冷设备。冷板、CDU和歧管成为新增价值中心，合计每兆瓦贡献约55万至75万美元。但与此同时，机房空调（CRAH）和背板热交换器（RDHx）的价值大幅变化，从风冷架构中的35万至55万美元降至液冷架构中的仅8万至10万美元。冷机（Chiller）作为冷却系统的“中央引擎”，价值基本保持不变，仍在45万至55万美元区间。

这意味着，液冷趋势下，受益者并非所有冷却设备厂商。那些在CRAH和RDHx领域份额较大的公司，面临单位价值被压缩的可能性；而CDU、冷板和歧管供应商则获得增量市场。报告特别强调，CDU的估值包含过滤、集成、安装等全周期成本，这进一步抬高了该组件的进入壁垒。

> **KC观察：** 液冷架构中冷机价值不变，但CRAH和RDHx价值变化明显，说明液冷并未消除数据中心对中央冷却的需求，只是改变了末端散热方式。读者需要区分哪些公司是“冷机+液冷组件”双受益，哪些公司可能因架构切换而面临收入结构变化。

![研报原图 2](assets/source_image_02.jpg)

## 2. 供电架构演进中，UPS被替代但总价值保持稳定

供电侧的变化更为复杂。传统交流架构中，UPS是最大的单一价值组件，每兆瓦贡献40万至50万美元。在混合800V直流架构中，UPS被取消，取而代之的是整流器（价值尚不明确）、电池储能系统（BESS）和备用电池单元（BBU），合计每兆瓦新增约20万至30万美元。原生800V直流架构则进一步取消了整流器和变压器，引入固态变压器（SST），但SST的价值同样处于技术演进中，报告未给出明确估值。

报告认为，尽管架构切换会淘汰部分传统设备，但总供电设备价值仅从180万至250万美元微降至140万至210万美元。柴油发电机作为备用电源，在三种架构中价值均保持在60万至80万美元，是最大的单一价值组件。这表明，即便数据中心向更高电压、更高效的方向演进，基础设施研究的总盘子并不会显著缩小，只是资金流向了不同的设备类别。

![研报原图 3](assets/source_image_03.jpg)

## 3. 一个可复用的观察框架：从“每兆瓦价值”判断供应商受益程度

这份报告最有价值的贡献，是提供了一个可量化的分析框架。读者可以将目标公司的产品组合，与不同架构下的组件价值表进行对照，从而判断其在AI数据中心建设浪潮中的受益程度。

具体而言，可以分三步操作：第一，确认目标公司的主要产品属于冷却还是供电环节；第二，判断这些产品在风冷/液冷、交流/直流架构中的价值占比是上升、持平还是下降；第三，结合行业对下一代架构的采用速度，估算收入弹性。例如，一家在CDU和冷板领域有布局的公司，在液冷渗透率从当前水平提升至50%的过程中，其每兆瓦收入可能增长30%以上；而一家主要依赖CRAH的公司，则可能面临单位价值被压缩的局面。

报告本身并未给出具体的公司收入弹性测算，但它提供的组件级价值数据，足以让读者自行完成这一推演。对于关注工业科技领域的决策者而言，这个框架比笼统的“数据中心受益方向”标签更具实操价值。

<p style="color:#999999;font-size:12px;">For informational purposes only. Portions may be generated,translated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>

![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)

<p style="color:#999999;font-size:12px;">For informational purposes only. Portions may be generated,translated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>
