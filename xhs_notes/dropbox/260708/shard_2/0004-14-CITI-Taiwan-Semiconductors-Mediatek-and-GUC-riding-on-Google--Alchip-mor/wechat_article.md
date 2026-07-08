# Citi：AI ASIC产业从单点技术竞争转向系统级供应链协同

AI计算从GPU向ASIC迁移，已经是产业共识。但真正决定谁能在这场迁移中胜出的，不是芯片架构的先进性，而是谁能在先进制程、先进封装、HBM和ABF载板全线吃紧的情况下，把芯片按时交付出来。

Citi最新一份覆盖台湾半导体设计服务公司的报告，给出了一个清晰的排序逻辑：供应链管理能力，正在取代技术能力，成为AI ASIC设计服务公司未来两年的核心竞争壁垒。报告认为，联发科和世芯在AI ASIC增长动能上最为强劲，而创意电子的成长则更偏后端。

这份报告最有价值的部分，不是它对各家公司的营收预估，而是它揭示了AI ASIC产业正在发生的结构性变化——从单点技术竞争，转向系统级供应链协同的竞争。

![研报原图 1](assets/source_image_01.jpg)

## 1. 联发科的AI ASIC收入将超越现有核心业务，供应链管理是最大杠杆

Citi对联发科AI ASIC收入的预估大幅上调。2027年从136亿美元上调至180亿美元，2028年从180亿美元上调至400亿美元。上调的核心原因不是需求侧的超预期，而是联发科在供应链中的价值量在提升——它不再只做I/O die，还开始切入compute die，甚至参与客户chiplet设计的多个芯片tile。

报告给出的出货量数据值得留意：2026年50万颗，2027年400万颗，2028年400万颗。2027到2028年出货量持平，但收入从180亿美元提升至400亿美元，意味着单颗价值量在提升。这背后是联发科在I/O、顶die、光学和内存定制die上的价值延伸。

> **KC评论：** 联发科AI ASIC收入将在两年内超过其现有手机芯片业务，这个判断本身就有很强的信号意义。但更值得思考的是，为什么是联发科？Citi的逻辑是“better supply chain management capability”。在先进封装和HBM供给极度紧张的环境下，能够协调台积电、日月光、多家HBM供应商和ABF载板厂的玩家，才能拿到订单。技术能力是门票，供应链管理才是决胜局。

![研报原图 2](assets/source_image_02.jpg)

## 2. 世芯的CPU项目能见度到2028年，但客户分散化带来新的不确定性

世芯的AI ASIC业务确定性相对更高。Citi指出，其美国CSP客户的CPU ASIC需求强劲，能见度明确到2028年。此外，面向美国客户的机器人和汽车项目预计在2027年底到2028年初开始贡献收入。

但报告也点出了一个潜在不确定性：世芯的客户正在寻求台积电以外的代工厂支持。虽然Citi认为世芯与台积电的紧密合作仍是汽车和机器人项目的主要来源，但客户分散化策略本身就是一把双刃剑——它降低了单一供应链不确定性，但也意味着世芯可能失去作为台积电“嫡系”的产能优先权。

这家公司还有一个值得关注的增长点：消费电子ASIC项目，以及互联IP和CPO技术的积累。Citi认为这些业务使其ASIC增长趋势保持完整。

![研报原图 3](assets/source_image_03.jpg)

## 3. 创意电子的成长偏后端，产能分配是2026年的关键变量

在三家公司中，创意电子的成长节奏最靠后。Citi预计其客户N3 AI加速器将在2026年第三季度开始放量，但近期的动能可能受限于产能约束、客户的COT商业模式和分散化策略。

报告没有完全展开的一个判断是：当产能成为稀缺资源时，客户的商业模式选择会直接影响设计服务公司的收入节奏。COT（客户自有工具）模式意味着客户自己掌握更多设计环节，设计服务公司的附加值和收入确认节奏都会受到影响。

> **KC评论：** 创意电子的毛利率可能有上行空间，因为它在后端设计上参与了更复杂的芯片设计。但“back-end loaded”这个表述本身就是一个提醒——读者需要等到2026年下半年才能验证其增长故事。报告建议等待2026年预期重置后再重新评估，这个建议本身就说明近期的能见度不够清晰。

## 4. 报告未完全回答的关键问题：产能分配的逻辑是什么？

Citi的报告给出了明确的排序偏好：联发科 > 世芯 > 创意电子。但有一个问题报告没有完全展开：在先进封装和HBM供给极度紧张的情况下，台积电和封装厂会如何分配产能？是按客户规模、历史合作深度，还是按利润率？

这个问题直接关系到三家公司的相对竞争力。如果台积电倾向于优先保障长期深度合作的客户，世芯和联发科的优势会更明显。如果按照利润率分配，创意电子的后端设计贡献可能为其争取到更多产能。这个变量需要持续跟踪台积电的产能分配公告和各家公司的订单能见度。

另一个未解问题是：当AI ASIC从单芯片走向chiplet架构后，设计服务公司的价值量会发生怎样的变化？联发科已经证明了它可以参与多个chiplet tile的设计，但这是否会成为行业常态？如果chiplet架构普及，设计服务公司的价值量可能从单芯片的“设计服务费”转向多tile的“系统集成费”，商业模式本身也会发生变化。

对于关注AI基础设施的读者，它揭示了一个正在发生的产业趋势：AI ASIC的竞争正在从技术竞赛转向供应链管理竞赛。谁能把台积电、日月光、HBM供应商和ABF载板厂协调得更好，谁就能在接下来两年的AI ASIC扩张中拿到最大份额。

<p style="color:#999999;font-size:12px;">For informational purposes only. Portions may be generated, translated, summarized, or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment, legal, tax, accounting, or other professional advice.</p>

![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)

<p style="color:#999999;font-size:12px;">For informational purposes only. Portions may be generated, translated, summarized, or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment, legal, tax, accounting, or other professional advice.</p>
