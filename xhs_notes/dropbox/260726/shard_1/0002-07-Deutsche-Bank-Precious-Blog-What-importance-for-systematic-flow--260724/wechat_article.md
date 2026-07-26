# DB：贵金属博客-系统性资金流对金价的影响

DB大宗商品团队在最新贵金属博客中提出一个值得关注的观察：今年4月至7月期间，黄金价格表现弱于央行与ETF资金流所暗示的水平，而规则驱动的趋势跟踪系统性资金可能是填补这一缺口的关键变量。

报告的核心判断建立在一个数据对比之上。该行构建了央行与ETF合并资金流占黄金矿产供应比例的月度序列，发现2026年1月这一比例曾高达48%，到3月骤降至-3%。此后该比例在0-29%之间波动。但单纯用这两类资金流来解释金价月度变化，在4月至7月之间出现了明显的负向残差——实际金价表现低于资金流模型预测值。

报告排除了CFTC期货持仓和亚洲黄金进口作为解释变量，因为这两者在同期均呈中性或净正面。真正可能填补这一缺口的，是规则化、趋势跟踪的系统性资金流。

![研报原图 1](assets/source_image_01.jpg)

## 1. 系统性资金流与RSI低于50形成对应关系

报告通过线性回归发现，4月以来金价相对于央行+ETF资金流的负向残差，与30天RSI低于50的时期高度吻合。截至7月24日，黄金30天RSI仍处于42.7，远低于50阈值。这意味着系统性账户在短期内几乎没有积累头寸的迹象。

> **KC评论：** 这里的关键不是RSI本身，而是报告将RSI作为系统性趋势跟踪策略的参考指标。当RSI低于50时，趋势跟踪模型倾向于持有空头或减仓，这种机械性卖盘可能放大了金价节奏变化，且与基本面资金流脱节。

![研报原图 2](assets/source_image_02.jpg)

## 2. 两类价格不敏感的需求构成核心支撑

报告重申了一个此前已论证过的框架：央行和ETF是黄金需求中最具价格刚性的两个板块，与珠宝需求形成鲜明对比。将两者合并分析，比单独考察任何一类资金流都更能解释金价行为。2026年1月两者合计消耗了近一半的矿产供应量，这种集中度本身就意味着，一旦这两类资金出现边际变化，对金价的冲击会被放大。

![研报原图 3](assets/source_image_03.jpg)

## 3. 价格与资金流的双向因果增加预测难度

报告引入“涌现”与“决定论”的概念框架来讨论价格形成机制。价格历史（趋势、RSI、MACD等技术指标）是读者集体行为的结果，反过来又影响读者行为，形成双向因果关系。这种涌现特性并不必然意味着非决定论，但由于宏观环境系统包含随机冲击，价格形成过程可能具有混沌性、计算不可约性或统计性特征，使得精确建模变得极为困难。

报告坦承，如果能够构建出系统性资金流的量化模型，很可能也会发现它在2025年12月至2026年2月期间（当时30天RSI远高于50）表现出强劲的积累行为。这反过来会提出一个新问题：系统性资金流可能在12-2月期间引入正向缺口，同时缩小4-7月的负向缺口。也就是说，系统性资金流可能同时解释两个方向的价格偏离，而非仅仅解释当前的节奏变化。

对于读者而言，这份报告的启示不在于给出一个确定性的金价预测，而在于提供了一个更完整的资金流分析框架。单纯跟踪央行购金和ETF持仓变化，可能遗漏系统性策略带来的短期价格冲击。当RSI持续低于50时，趋势跟踪卖盘的持续性值得关注——直到技术指标出现趋势反转信号之前，这类资金流可能继续影响金价表现。

<p style="color:#999999;font-size:12px;">For informational purposes only. Portions may be generated,translated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>

![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)

<p style="color:#999999;font-size:12px;">For informational purposes only. Portions may be generated,translated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>
