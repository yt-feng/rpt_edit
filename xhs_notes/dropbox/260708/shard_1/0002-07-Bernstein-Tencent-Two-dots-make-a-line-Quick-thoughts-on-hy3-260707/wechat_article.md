# Bernstein：从Hy3看腾讯AI务实路径，不是堆参数，而是打通数据孤岛

腾讯Hy3模型正式发布，距离预览版仅10周。参数规模未变——2950亿参数、210亿活跃参数——但关键性能指标有明显改善。幻觉率从12.5%降至5.4%，多轮对话保留率从42.9%提升至75.1%。Bernstein这份报告的核心判断是：Hy3不是前沿模型，但它在腾讯需要构建智能体服务的核心能力上，达到了可用的水平。

这份报告真正值得注意的，不是模型参数或基准分数，而是它揭示了一个结构性问题：腾讯的AI团队和微信团队之间，存在数据访问的断层。


![研报原图 1](assets/source_image_01.jpg)


![研报原图 2](assets/source_image_02.jpg)


![研报原图 3](assets/source_image_03.jpg)


**1. 模型进步可验证，但方向选择更值得关注**

Hy3的发布节奏和性能提升，验证了Bernstein两个月前的一个判断：对于腾讯而言，拥有一个可信的预训练、强化学习和评估栈，比堆参数更重要。Hy3在工具调用稳定性、幻觉控制、多轮对话保持等维度上的改进，指向一个清晰的产品意图——腾讯在优先构建智能体服务所需的能力，而不是追逐通用推理或代码生成的最高分。

报告提到，Hy3使用了GQA（分组查询注意力），这意味着在KV缓存压缩技术（如MLA或DSA）上仍有改进空间。这是一个技术细节，但指向一个更实际的判断：腾讯的模型迭代路径是务实的，不是激进的。

> **KC评论：** Bernstein认为Hy3的能力水平接近GLM-5.1，而GLM-5.1是国内主流可用模型之一。这意味着腾讯在智能体服务上的模型基础已经建立，但距离“领先”还有距离。完整报告里对GQA与MLA的技术对比，值得技术背景的读者细看。

**2. 资本开支争议的另一面：token消耗的担忧被放大了**

市场对腾讯AI投入的担忧，主要集中在资本开支上升和折旧摊销增加。但Bernstein提出了一个不同的视角：token消耗量不会无节制增长。

逻辑很简单。聊天机器人对话消耗几百个token，而智能体交易需要数万个token。只有当智能体交易量和GMV真正起飞时，腾讯的token消耗才会进入指数级增长。而历史经验表明，从用户参与到商业化之间，存在时间差，但商业化落地只是时间问题，不是方向问题。

这意味着，当前市场对腾讯AI投入的“资产变重”担忧，可能忽略了商业化路径本身的结构性特征。

> **KC评论：** 报告没有完全展开的是，腾讯的智能体商业化更可能走“向商家收费”的路径，而不是向消费者收费。这与美国市场完全不同——美国消费者需要被教育才能点击购物链接，而国内互联网平台上的交易意图已经存在。这对理解腾讯AI的变现逻辑很关键。

**3. 报告没有完全回答的问题：微信数据访问的僵局如何打破**

这是Bernstein整份报告中最有洞察力、也最坦诚的部分。报告指出，腾讯AI团队经过大量投入重新调整了模型训练基础设施，并取得了实际进展，但“似乎无法访问微信数据”。与此同时，即将推出的微信AI智能体，是由微信团队独立构建的，与前者无关。

这意味着腾讯内部存在一个结构性的数据孤岛。AI团队拥有模型能力，但没有微信数据；微信团队拥有数据和场景，但模型能力可能不是最优的。Bernstein认为，这个问题最终会通过管理层决策解决，但报告也直言：“为什么这件事还没有发生，可能是一个值得向管理层提出的问题。”

对读者而言，这是一个重要的观察框架：腾讯AI的真正拐点，可能不是模型参数突破，而是内部数据壁垒的打通。如果这个僵局被打破，腾讯AI的商业化路径将显著加速。

Bernstein对，而在于它提供了一个更细致的分析框架：不是看模型有多强，而是看模型在生态里能拿到什么数据、能做什么事。


<p style="color:#999999;font-size:12px;">For informational purposes only. Portions may be generated,translated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>

![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)

<p style="color:#999999;font-size:12px;">For informational purposes only. Portions may be generated,translated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>
