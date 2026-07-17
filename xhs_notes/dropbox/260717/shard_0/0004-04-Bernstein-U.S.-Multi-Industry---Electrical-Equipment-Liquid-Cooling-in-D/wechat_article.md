# 数据中心冷却技术观察：单相DTC之后是什么

数据中心液冷领域正在发生一件值得关注的事。当整个行业都在为下一代GPU准备两相DTC或直接-to-die等更激进的冷却方案时，CoolIT拿出了一张15kW的单相冷板，在实验室条件下证明单相DTC可以处理6倍于当前公认极限的热负荷。如果这张冷板能实现规模化商用，行业过去两年围绕技术路线切换的讨论框架可能需要重新调整。

这份研究笔记的核心判断是：单相DTC的寿命可能比市场预期的长得多。当前市场共识认为，随着GPU TDP突破2.5kW，单相DTC将触及热力学极限，两相DTC或直接-to-die将成为必然选择。但CoolIT的15kW冷板在1.2升/分钟流速、45摄氏度入口温度、PG25冷却液的标准工况下，证明了单相方案仍有显著余量。报告认为这一产品可信，且CoolIT拥有底层专利。

> **KC评论：** 这里的关键不是15kW这个数字本身，而是它出现在单相DTC被认为“物理上不可能”的区间。如果单相方案能覆盖未来两代GPU的散热需求，整个冷却供应链的资本开支节奏和竞争格局都会不同。


![研报原图 1](assets/source_image_01.jpg)

## 1. 两相DTC的工程挑战尚未解决，商业化窗口可能被推迟

两相DTC利用冷却液蒸发相变吸收潜热，理论上热通量是单相方案的3倍以上。但报告明确指出，两相系统面临三个尚未解决的工程难题：气液两相在微通道内的逆向流动导致局部热点、GPU负载瞬态变化（0到100%功率只需毫秒级）对控制算法的极高要求、以及PFAS冷却液面临的监管不确定性。

目前最接近商业化的玩家是Vertiv和Accelsius，但产品仍处于早期试点阶段。ZutaCore刚完成1亿美元C轮融资，Accelsius完成6500万美元B轮。如果CoolIT的15kW冷板能先一步规模化，两相DTC的紧迫性将大幅降低——行业可能不需要在2027-2028年就完成技术切换。


![研报原图 2](assets/source_image_02.jpg)

## 2. 直接-to-die技术更远，2030年前不会规模部署

直接-to-die将微通道直接蚀刻在硅片上，省去冷板和热界面材料，理论上热通量最优。但报告认为这项技术“极其早期”，微软和台积电虽有研究信号，但尚未看到任何大规模采用的迹象。核心障碍包括去离子水对硅的腐蚀不确定性、以及制造良率的未知性。

即便CoolIT的冷板未能如期商用，直接-to-die也大概率要到2030年后才会成为主流。这意味着未来3-5年，数据中心冷却的核心竞争仍将围绕单相DTC的优化展开。


![研报原图 3](assets/source_image_03.jpg)

## 3. 对冷却设备供应商：短期无忧，长期格局可能被重塑

报告对冷却设备供应商的影响做了分层判断。短期看，需求远超供给，CoolIT的15kW冷板不会对Vertiv、nVent等厂商的收入和利润率产生实质性冲击。但长期看，如果单相DTC的寿命被延长，两相DTC和直接-to-die带来的“创新溢价”将消失，冷板和CDU可能加速走向商品化。

对冷板供应商而言，这反而消除了技术过时不确定性——既然单相方案还能用很多年，就不需要为直接-to-die的替代焦虑。但对那些押注两相DTC的厂商（如Carrier研究ZutaCore、JCI研究Accelsius），如果单相方案持续有效，这些研究的回报周期可能被拉长。

> **KC评论：** 读者需要区分“技术可行性”和“商业必要性”。CoolIT证明了单相DTC在实验室可行，但规模化后的成本、可靠性和维护便利性才是决定运营商是否切换的关键。报告没有给出明确答案，但提出了一个值得跟踪的问题：竞争对手能否快速复制CoolIT的专利方案。

## 4. 一个可复用的观察框架：技术路线切换的触发条件

这份报告提供了一个判断液冷技术路线的分析框架：关注三个变量——GPU TDP的实际演进速度、单相冷板的商用化进度、以及两相系统的工程突破节点。如果GPU TDP在2027-2028年仍维持在6kW以下，且CoolIT的15kW冷板能通过客户验证，那么两相DTC的部署时间表可能推迟到2030年后。反之，如果NVIDIA的Rubin Ultra TDP超出预期，或两相系统在12-18个月内解决逆向流动问题，技术切换的窗口将重新打开。

对于数据中心运营商和冷却设备采购方，当前最理性的策略可能是保持单相方案的灵活性，同时跟踪两相和直接-to-die的进展，而不是过早锁定某一条技术路线。


<p style="color:#999999;font-size:12px;">For informational purposes only. Portions may be generated,translated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>

![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)

<p style="color:#999999;font-size:12px;">For informational purposes only. Portions may be generated,translated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>
