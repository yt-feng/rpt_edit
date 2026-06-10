你是麦肯锡/投研风格的微信公众号财经文章主笔，擅长用金字塔原理把研报内容转化为“有主张、有层次、有洞察、但仍保留完整报告阅读欲望”的长文。

【目标】
- 基于下面的研报解析内容，写一篇微信公众号文章 Markdown。
- 风格：稳重、专业、克制、有洞察，像咨询公司合伙人写给高净值读者/产业决策者的研报导读。
- 长度：约 3000 字，允许上下浮动 15%。
- 不要使用 emoji。
- 可以基于报告内容做适度发散，但必须是从原文逻辑推出的判断，不要编造数据、公司动作或引用。
- 不要把研报所有正文内容讲完，要留下明确但自然的伏笔，让读者愿意加入社群阅读完整报告。

【金字塔原理写作原则】
1. 结论先行：文章开头先回答“这份报告最值得看的判断是什么”，而不是介绍背景。
2. 统领思想：全文只能服务一个主判断，避免变成摘要合集。
3. 纵向回答：每一层都要回答上一层提出的“为什么”或“所以呢”。
4. 横向 MECE：每个一级小节必须彼此独立、共同支撑主判断，避免重叠。
5. Synthesis over summary：不要复述报告段落，要提炼“这些事实合在一起意味着什么”。
6. So what：每个小节末尾必须落到对行业、公司、竞争格局、资产定价或读者观察框架的含义。
7. Action title：所有 `##` 小标题必须是“直接讲述洞察的完整句子”，不能是目录标签。

【标题与小标题硬性要求】
- `# 标题` 必须直接表达一个判断，例如“市场真正低估的不是需求，而是供给侧的再定价”。
- `# 标题` 必须包含报告机构的中文名称。已识别机构名：`JEF`。标题格式建议：`# JEF：一句主判断`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、摩根斯坦利、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
- 机构名只要求出现在 `# 标题` 中，正文可以克制提及，不要为了重复机构名牺牲可读性。
- 禁止使用以下机械标题：
  - 一、核心判断
  - 二、真正重要的是结构性变量
  - 三、报告没有说透
  - 四、对读者的启发
  - 关键变化
  - 投资启示
  - 总结
- 所有 `##` 标题都要像麦肯锡报告里的 action title：读完标题就知道这一节结论。
- 小标题可以带序号，但序号后必须是一句洞察，例如：`## 1. 这轮变化真正考验的是企业能否把规模转化为议价权`。

【建议结构，但不要机械照抄标题】
1. `# 标题`：机构中文名 + 一句主判断，不超过 40 字。
2. 开头 4-6 段：直接给出主判断、为什么现在重要、报告提供了什么新信号。
3. 4-6 个 `##` 小节：每个小节标题都是洞察句，不是栏目名。
4. 至少一个小节讨论“报告尚未完全回答的关键问题”，但标题也要是洞察句。
5. 至少一个小节给出读者的观察框架，但不要命名为“对读者的启发”。
6. 文末自然承接未解问题，引导读者加入社群/微信群继续讨论。不要照抄固定话术，请基于本文未解问题每次重新写一段自然 CTA；语义可以参考：欢迎来星球微信群里继续讨论。
7. 在免责声明前，单独插入这张图片链接：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`
8. 结尾只输出英文灰色免责声明：`<p style="color:#999999;font-size:12px;">Personal reading notes and learning share only. Not investment advice.</p>`

【hook 要求】
- 不要硬插“加入社群”。
- hook 应该来自正文自然出现的未解问题，比如：关键假设尚未验证、竞争优势仍需拆解、图表背后的二阶影响没有展开。
- 文末 CTA 要像“顺着这些未解问题继续读完整报告/继续讨论”，不是广告口吻。
- CTA 必须每篇重新写，不能固定输出“加入社群，领取完整研报解读与原始图表”。可以类似“欢迎来星球微信群里继续讨论”。

【图片要求】
- 不要主动生成 MinerU 图片 markdown；系统会在文章生成后自动插入 MinerU 原始图片。
- 但文末免责声明前必须保留知识星球图片：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`。

【内容边界】
- 只能基于研报原文和解析结果推导，不要编造数据、公司动作、引用。
- 遇到不确定内容，要用“这里仍需验证”“报告没有完全展开”等表达。
- 避免“震惊”“爆款”“一文看懂”等浮夸表达。
- 不要出现小红书话题标签。
- 不要出现 emoji。
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份JEF研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
## China AI Monthly - Excess Fear of AI Disruption in Software, Esp for China

We view AI's impact on SW as a "natural selection" event, rather than SaaS "apocalypse". Our extensive talks with 7 China SW players on AI reveal likelihood of more resilience to AI disruption than US peers, given China's project-based or module-based SaaS pricing. But IT budget pressure is the key headwind. China SW U/P US peers (7%) and CSI 300 (18%) YTD, driven by earnings D/G and multiple compression. Our top pick in China SW remains Kingdee (KD).

China Software underperforms (U/P) US on earnings downgrade and multiple compression. Since Oct 2025, the US software (SW) sector has sold off sharply on fears that AI will disrupt SaaS. Anthropic's release of Claude Cowork on Jan 12, 2026 intensified the downturn through Mar 31 (\~23% decline), before the market realized that disruption fears were overdone, driving \~21% recovery since then. Our US SW basket (14 stocks): has fallen 6.4% YTD purely due to multiple contraction. Cons 2026 rev profit has risen 2% since Jan 12, while EV/S is down 6.5% YTD from 6.1x to 5.7x. Our China (CN) SW basket (19 stocks): has fallen 13% YTD. Cons 2026 rev has fallen 5% since Jan 12, and EV/S is down 15% YTD from 5.0x to 4.3x, suggesting the sell-off was driven by earnings downgrade (D/G) and multiple contraction.

The rise of LLMs and AI agents is driving a structural shift in SW architecture and economics. We believe AI is NOT a SaaS "apocalypse", but a "natural selection mechanism", as players with defensible moats that proactively embrace AI can evolve into AI-native platforms, while those with weak moats and are slow to adopt AI risk displacement. Three key impacts: 1) Architectural shift. SW will transition from UI-centric, human-operated systems to API-first, agent-executable workflow platforms. Agents can automate tasks autonomously but still rely on SW APIs for workflows, business logic, and data. 2) Pressure on seat-based pricing. As agents replace human operators, per-seat pricing models face structural pressure, pushing vendors toward consumption- and outcome-based pricing. 3) Margin pressure. Unlike traditional SW's near-zero marginal cost, LLM inference is a big usage-based variable cost, which means SW players will have to pass such costs on to customers or be able to charge a healthy margin.

CN SW is less prone to AI disruption, but frail IT budgets remain the headwind. Many CN SW players operate on project-based models, serving large SOEs requiring heavy systems integration and customization. Data security concerns and asset-based mentality have limited public cloud SaaS penetration with SOEs. Moreover, Chinese SaaS players rarely use seat-based pricing; instead, they charge by module. This makes CN SW generally more resilient to AI disruption than its US peers. However, the primary headwind remains IT budget pressure for large enterprises in a weak macro environment.

KD still our top pick in China SW. We believe industrial SW, financial IT, and ERP are the most resilient to AI disruption given deep workflow integration, proprietary data, zero tolerance for hallucination, and strict vendor qualifications. We view KD's recent sell-off as a good entry point: 1) KD's ERP is deeply embedded in clients' workflows as a system of record, and is costly and risky to replace; 2) KD's proprietary data and industry know-how is difficult for AI vendors to replicate; 3) module-based pricing insulates rev from workforce reductions; 4) KD has launched its own AI-native ERP suite and Lingee AIOS, guiding Rmb1.0bn in AI rev for 2026; 5) SaaS now >50% of rev, drives teen rev growth, GPM expansion, and strong op leverage aided by internal AI-driven cost efficiencies; 6) valuation at 0.7x 2026E PEG is highly attractive. Cont on next page...

Exhibit 1 - SW Baskets' EV/S - US vs CN  
![](images/57ed897312c5f499c327308981b26fed2376ad9684bb731d645cde35d66e9bd6.jpg)

<details>
<summary>line chart</summary>

| Date | Chinese Software Companies EV/Sales | US Software Companies EV/Sales |
| --- | --- | --- |
| 5/1/2021 | 7.0 | 6.5 |
| 6/1/2021 | 6.5 | 6.0 |
| 7/1/2021 | 6.0 | 5.5 |
| 8/1/2021 | 5.5 | 5.0 |
| 9/1/2021 | 5.0 | 4.5 |
| 10/1/2021 | 4.5 | 4.0 |
| 11/1/2021 | 4.0 | 3.5 |
| 12/1/2021 | 3.5 | 3.0 |
| 1/1/2022 | 3.0 | 2.5 |
| 2/1/2022 | 2.5 | 2.0 |
| 3/1/2022 | 2.0 | 1.5 |
| 4/1/2022 | 1.5 | 1.0 |
| 5/1/2022 | 1.0 | 0.5 |
| 6/1/2022 | 0.5 | 0.0 |
| 7/1/2022 | 0.0 | -0.5 |
| 8/1/2022 | -0.5 | -1.0 |
| 9/1/2022 | -1.0 | -1.5 |
| 10/1/2022 | -1.5 | -2.0 |
| 11/1/2022 | -2.0 | -2.5 |
| 12/1/2022 | -2.5 | -3.0 |
| 1/1/2023 | -3.0 | -3.5 |
| 2/1/2023 | -3.5 | -4.0 |
| 3/1/2023 | -4.0 | -4.5 |
| 4/1/2023 | -4.5 | -5.0 |
| 5/1/2023 | -5.0 | -5.5 |
| 6/1/2023 | -5.5 | -6.0 |
| 7/1/2023 | -6.0 | -6.5 |
| 8/1/2023 | -6.5 | -7.0 |
| 9/1/2023 | -7.0 | -7.5 |
| 10/1/2023 | -7.5 | -8.0 |
| 11/1/2023 | -8.0 | -8.5 |
| 12/1/2023 | -8.5 | -9.0 |
| 1/1/2024 | -9.0 | -9.5 |
| 2/1/2024 | -9.5 | -10.0 |
| 3/1/2024 | -10.0 | -10.5 |
| 4/1/2024 | -10.5 | -11.0 |
| 5/1/2024 | -11.0 | -11.5 |
| 6/1/2024 | -11.5 | -12.0 |
| 7/1/2024 | -12.0 | -12.5 |
| 8/1/2024 | -12.5 | -13.0 |
| 9/1/2024 | -13.0 | -13.5 |
| 10/1/2024 | -13.5 | -14.0 |
| 11/1/2024 | -14.0 | -14.5 |
| 12/1/2024 | -14.5 | -15.0 |
| 1/1/2025 | -15.0 | -15.5 |
| 2/1/2025 | -15.5 | -16.0 |
| 3/1/2025 | -16.0 | -16.5 |
| 4/1/2025 | -16.5 | -17.0 |
| 5/1/2025 | -17.0 | -17.5 |
| 6/1/2025 | -17.5 | -18.0 |
| 7/1/2025 | -18.0 | -18.5 |
| 8/1/2025 | -18.5 | -19.0 |
| 9/1/2025 | -19.0 | -19.5 |
| 10/1/2025 | -19.5 | -20.0 |
| 11/1/2025 | -20.0 | -20.5 |
| 12/1/2025 | -20.5 | -21.0 |
| 1/1/2036 | -21.0 | -21.5 |
| 2/1/2036 | -21.5 | -22.0 |
| 3/1/2036 | -22.0 | -22.5 |
| 4/1/2036 | -22.5 | -23.0 |
| 5/1/2036 | -23.0 | -23.5 |
| 6/1/2036 | -23.5 | -24.0 |
| 7/1/2036 | -24.0 | -24.5 |
| 8/1/2036 | -24.5 | -25.0 |
| 9/1/2036 | -25.0 | -25.5 |
| 10/1/2036 | -25.5 | -26.0 |
| 11/1/2036 | -26.0 | -26.5 |
| 12/1/2036 | -26.5 | -27.0 |
| 1/1/2047 | -27.0 | -27.5 |
| 2/1/2047 | -27.5 | -28.0 |
| 3/1/2047 | -28.0 | -28.5 |
| 4/1/2047 | -28.5 | -29.0 |
| 5/1/2047 | -29.0 | -29.5 |
| 6/1/2047 | -29.5 | -30.0 |
| 7/1/2047 | -30.0 | -30.5 |
| 8/1/2047 | -30.5 | -31.0 |
| 9/1/2047 | -31.0 | -31.5 |
| 10/1/2047 | -31.5 | -32.0 |
| 11/1/2047 | -32.0 | -32.5 |
| 12/1/2047 | -32.5 | -33.0 |
| 1/1/48 | -33.0 | -33.5 |
| 2/1/48 | -33.5 | -34.0 |
| 3/1/48 | -34.0 | -34.5 |
| 4/1/48 | -34.5 | -35.0 |
| 5/1/48 | -35.0 | -35.5 |
| ... | +7 | +8 |
| ... | +8 | +9 |
| ... | +9 | +8 |
| ... | +8 | +7 |
| ... | +7 | +6 |
| ... | +6 | +5 |
| ... | +5 | +4 |
| ... | +4 | +3 |
| ... | +3 | +2 |
| ... | +2 | +1 |
| ... | +1 | +0 |
| ... | +0 | +-1 |
| ... | +-1 | +-3 |
| ... | +-3 | +-6 |
| ... | +-6 | +-9 |
| ... | +-9 | +-8 |
| ... | +-8 | +-7 |
| ... | +-7 | +-6 |
| ... | +-6 | +-6 |
| ... | +-6 | +-6 |
| ... | +-6 | +-6 |
| ... | +-6 | +-6 |
| ... | +-6 | +-6 |
| ... | +-6 | +-6 |
| ... | +-6 | +-6 |
</details>

Source: FactSet, Bloomberg, JEF Sector EV/S is equal weighted

Exhibit 2 - China SW EV/S Premium over China Internet  
![](images/143c98bdeb8dd259d786413ba6063d03a8c4c5a5feec6fa1c1ea93799e63a81b.jpg)

<details>
<summary>line chart</summary>

| Date       | Value |
| ---------- | ----- |
| 5/12/2023  | 300%  |
| 7/12/2023  | 250%  |
| 9/12/2023  | 200%  |
| 11/12/2023 | 150%  |
| 1/1/2024   | 100%  |
| 2/1/2024   | 50%   |
| 3/1/2024   | 100%  |
| 4/1/2024   | 150%  |
| 5/1/2024   | 200%  |
| 6/1/2024   | 250%  |
| 7/1/2024   | 300%  |
| 8/1/2024   | 250%  |
| 9/1/2024   | 200%  |
| 10/1/2024  | 150%  |
| 11/1/2024  | 100%  |
| 12/1/2024  | 50%   |
| 1/1/2025   | 100%  |
| 2/1/2025   | 150%  |
| 3/1/2025   | 200%  |
| 4/1/2025   | 250%  |
| 5/1/2025   | 300%  |
| 6/1/2025   | 250%  |
| 7/1/2025   | 200%  |
| 8/1/2025   | 150%  |
| 9/1/2025   | 100%  |
| 10/1/2025  | 50%   |
| 11/1/2025  | 100%  |
| 12/1/2025  | 150%  |
| 1/1/2026   | 200%  |
| 2/1/2026   | 250%  |
| 3/1/2026   | 300%  |
| 4/1/2026   | 250%  |
| 5/1/2026   | 200%  |
</details>

Source: FactSet, Bloomberg, JEF

Exhibit 3 - Ranking of China SW AI Defensibility  
![](images/16e0531110f9fed762f0f457cd093187068b3f4012392371010be31ca2f9b668.jpg)

<details>
<summary>bar chart</summary>

| Category | Value |
|---|---|
| Sunrose | 35 |
| Brought | 35 |
| Hamburg | 34 |
| Hambun | 34 |
| Foyou | 34 |
| Kingdee | 34 |
| JFOSO | 31 |
| Youn | 31 |
| Aluata | 30 |
| Chukon | 28 |
| VeroTech | 28 |
| Sangeor | 26 |
| Glodon | 26 |
| Sonset | 24 |
| Cianjin | 20 |
</details>

Source: JEF estimates (See Table 1 for details)
Score: Max 40, min 0. High score = less vulnerable to AI

Exhibit 4 - JEF SW coverage's AI moat and timeframe of AI transition  
![](images/8ee19b8325e75caf031195a9a820022175d33173d50882acf52d1f10a7446f2d.jpg)

<details>
<summary>scatter plot</summary>

| Entity | Timeframe of All Disruption | Means to find off of All Disruption |
| --- | --- | --- |
| Charest | 3 | 18 |
| Sincout | 4 | 22 |
| Godlar | 5 | 26 |
| Godlar | 6 | 28 |
| Kingdee | 7 | 30 |
| Kingdee | 8 | 32 |
| Hundon | 9 | 34 |
| Iodlon | 10 | 36 |
| Iodlon | 11 | 38 |
| Iodlon | 12 | 40 |
| Iodlon | 13 | 42 |
| Iodlon | 14 | 44 |
| Iodlon | 15 | 46 |
| Iodlon | 16 | 48 |
| Iodlon | 17 | 50 |
| Iodlon | 18 | 52 |
| Iodlon | 19 | 54 |
| Iodlon | 20 | 56 |
| Iodlon | 21 | 58 |
| Iodlon | 22 | 60 |
| Iodlon | 23 | 62 |
| Iodlon | 24 | 64 |
| Iodlon | 25 | 66 |
| Iodlon | 26 | 68 |
| Iodlon | 27 | 70 |
| Iodlon | 28 | 72 |
| Iodlon | 29 | 74 |
| Iodlon | 30 | 76 |
| Iodlon | 31 | 78 |
| Iodlon | 32 | 80 |
| Iodlon | 33 | 82 |
| Iodlon | 34 | 84 |
| Iodlon | 35 | 86 |
| Iodlon | 36 | 88 |
| Iodlon | 37 | 90 |
| Iodlon | 38 | 92 |
| Iodlon | 39 | 94 |
| Iodlon | 40 | 96 |
| Iodlon | 41 | 98 |
| Iodlon | 42 | 100 |
| Iodlon | 43 | 102 |
| Iodlon | 44 | 104 |
| Iodlon | 45 | 106 |
| Iodlon | 46 | 108 |
| Iodlon | 47 | 110 |
| Iodlon | 48 | 112 |
| Iodlon | 49 | 114 |
| Iodlon | 50 | 116 |
| Iodlon | 51 | 118 |
| Iodlon | 52 | 120 |
| Iodlon | 53 | 122 |
| Iodlon | 54 | 124 |
| Iodlon | 55 | 126 |
| Iodlon | 56 | 128 |
| Iodlon | 57 | 130 |
| Iodlon | 58 | 132 |
| Iodlon | 59 | 134 |
| Iodlon | 60 | 136 |
| Iodlon | 61 | 138 |
| Iodlon | 62 | 140 |
| Iodlon | 63 | 142 |
| Iodlon | 64 | 144 |
| Iodlon | 65 | 146 |
| Iodlon | 66 | 148 |
| Iodlon | 67 | 150 |
| Iodlon | 68 | 152 |
| Iodlon | 69 | 154 |
| Iodlon | 70 | 156 |
| Iodlon | 71 | 158 |
| Iodlon | 72 | 160 |
| Iodlon | 73 | 162 |
| Iodlon | 74 | 164 |
| Iodlon | 75 | 166 |
| Iodlon | 76 | 168 |
| Iodlon | 77 | 170 |
| Iodlon | 78 | 172 |
| Iodlon | 79 | 174 |
| Iodlon | 80 | 176 |
| Iodlon | 81 | 178 |
| Iodlon | 82 | 180 |
| Iodlon | 83 | 182 |
| Iodlon | 84 | 184 |
| Iodlon | 85 | 186 |
| Iodlon | 86 | 188 |
| Iodlon | 87 | 190 |
| Iodlon | 88 | 192 |
| Iodlon | 89 | 194 |
| Iodlon | 90 | 196 |
| Iodlon | 91 | 198 |
| Iodlon | 92 | 200 |
| Iodlon | 93 | 202 |
| Iodlon | 94 | 204 |
| Iodlon | 95 | 206 |
| Iodlon | 96 | 208 |
| Iodlon | 97 | 210 |
| Iodlon | 98 | 212 |
| Iodlon | 99 | 214 |
| Iodlon | 100 | 216 |
| JZWSH | - | - |
| Krigdee | - | - |
| Hundon | - | - |
| Bovnight | - | - |
| YZWSH | - | - |
| Krigdee | - | - |
| Hundon | - | - |
| Bovnight | - | - |
| YZWSH | - | - |
| Krigdee | - | - |
| Hundon | - | - |
| Bovnight | - | - |
| Krigdee | - | - |
| Hundon | - | - |
| Bovnight | - | - |
| Krigdee | - | - |
| Hundon | - | - |
| Bovnight | - | - |
| Krigdee | - | - |
</details>

Source: Company, JEF
Timeframe only shows relative window for AI transition

CN= China, HW= Hardware, KD=Kingdee, SW= Software, UI= User Interface

Edison Lee, CFA \* | Equity Analyst

852 3743 8009 | edison.lee@JEF.com

Matt Ma \* | Equity Analyst

852 3767 1109 | matt.ma@JEF.com

Annie Ping, CFA, FRM \* | Equity Associate

+852 3767 1273 | annie.ping@JEF.com

Nick Cheng \* | Equity Analyst

+852 3743 8750 | nick.cheng@JEF.com

Jacky He \* | Equity Analyst

+852 3743 8084 | jacky.he@JEF.com

China's AI models narrow the performance gap with the US, while aggressive price cuts intensify competition and could pressure margins. In May, Anthropic's Claude Opus 4.8, OpenAI's GPT 5.5, and Google's Gemini 3.1 Pro remain the top three globally on AA's intelligence ranking. In China, leadership keeps shifting, Qwen 3.7 Max surpassed Kimi K2.6 as the best Chinese model. The US-China performance gap has slightly narrowed, with Qwen 3.7 Max now $8\%$ below the top US model (vs. $10\%$ in April; $18\%$ in Dec 2025). Moreover, Chinese models continue to offer superior value for performance, their avg price as a percentage of US model price fell to $21\%$ in May ( $31\%$ in Apr), driven by Qwen/Xiaomi price cuts on their flagship models by $46\%/86\%$ . DeepSeek also announced the $75\%$ promotional discount on its DS V4 pro would be permanent. This likely signals intensifying competition as incumbents fight for market share. However, given sharply rising HW costs, aggressive API pricing could pressure ROI for Chinese model players.

## The 3-Minute Guide

US SW has Fallen 3% in One Year and 6% YTD; While CN SW Underperformed US SW and has Fallen All Along

Exhibit 5 - US SW Cohort's Mkt Cap Chg  
![](images/396a606aaa5f6da23e791045ed61f69f4f71891952ef459b4d5b0efcc10fe5c0.jpg)

<details>
<summary>bar chart</summary>

| Period | Value (%) |
|---|---|
| 3 Year | 38.7 |
| 1 Year | -3.1 |
| YTD | -6.4 |
| 3 Month | 15.4 |
</details>

Source: FactSet, JEF  
Performance is for our US SW basket; date as of May 31

Exhibit 6 - CN SW Cohort's Mkt Cap Chg  
![](images/94f2b70f56bfa9498237b2d4fdc37c864fc7a1c6f02ed5133242c90e71737dba.jpg)

<details>
<summary>bar chart</summary>

| Period | Value (%) |
|---|---|
| 3 Year | -39.3 |
| 1 Year | -9.5 |
| YTD | -13.1 |
| 3 Month | -19.3 |
</details>

Source: FactSet, JEF  
Performance is for our CN SW basket; date as of May 31

US SW Cohort's Rev Cons Ests were Upgraded Since January, while CN SW Cohort's Rev Cons Ests were Downgraded

Exhibit 7 - US SW Cohort's Cons Rev Ests  
![](images/919186377a4595279deedbc98e9aa35268562169774930c9859f75dd5c81853c.jpg)

<details>
<summary>bar chart</summary>

US SW Rev cons from Jan 12 - May 31: +2%
| Date | Revenue (US$ Mn) |
| :--- | :--- |
| Jan 12, 2026 | 656,853 |
| Mar 31, 2026 | 667,746 |
| May 31, 2026 | 673,052 |
</details>

Source: Bloomberg, JEF

Exhibit 8 - CN SW Cohort's Cons Rev Ests  
![](images/8ad4789944c46691cc01e56c7ca79645520865d4ad2c03f29f1a41567c3fd804.jpg)

<details>
<summary>bar chart</summary>

CN SW Rev cons from Jan 12 - May 31: -5%
| Date | Value (US$ Mn) |
| :--- | :--- |
| Jan 12, 2026 | 19,246 |
| Mar 31, 2026 | 18,808 |
| May 31, 2026 | 18,191 |
</details>

Source: Bloomberg, JEF

US SW EV/S premium over CN SW reached a 3-year low in Feb 2026 upon AI-driven sell-off, but has partially recovered since then

Exhibit 9 - SW Companies EV/S - US vs CN  
![](images/d0df46af52bf6e9337d7fd8455909d76839525d185957cbde628ad27b3950f6f.jpg)

<details>
<summary>line chart</summary>

| Date       | Chinese Software Companies EV/Sales | US Software Companies EV/Sales |
| ---------- | ----------------------------------- | ----------------------------- |
| 5/31/2023  | 6.5                                 | 6.0                           |
| 6/30/2023  | 6.0                                 | 6.5                           |
| 7/31/2023  | 5.5                                 | 6.0                           |
| 8/31/2023  | 5.0                                 | 6.5                           |
| 9/30/2023  | 4.5                                 | 6.0                           |
| 10/31/2023 | 4.0                                 | 6.5                           |
| 11/30/2023 | 3.5                                 | 7.0                           |
| 12/31/2023 | 3.0                                 | 6.5                           |
| 1/31/2024  | 2.5                                 | 6.0                           |
| 2/29/2024  | 3.0                                 | 6.5                           |
| 3/31/2024  | 3.5                                 | 6.0                           |
| 4/30/2024  | 4.0                                 | 6.5                           |
| 5/31/2024  | 4.5                                 | 7.0                           |
| 6/30/2024  | 5.0                                 | 6.5                           |
| 7/31/2024  | 5.5                                 | 6.0                           |
| 8/31/2024  | 6.0                                 | 6.5                           |
| 9/30/2024  | 6.5                                 | 7.0                           |
| 10/31/2024 | 7.0                                 | 7.5                           |
| 11/30/2024 | 7.5                                 | 7.0                           |
| 12/31/2024 | 7.0                                 | 6.5                           |
| 1/31/2025  | 6.5                                 | 6.0                           |
| 2/28/2025  | 6.0                                 | 5.5                           |
| 3/31/2025  | 5.5                                 | 5.0                           |
| 4/30/2025  | 5.0                                 | 4.5                           |
| 5/31/2025  | 4.5                                 | 4.0                           |
| 6/30/2025  | 4.0                                 | 3.5                           |
| 7/31/2025  | 3.5                                 | 3.0                           |
| 8/31/2025  | 3.0                                 | 2.5                           |
| 9/30/2025  | 2.5                                 | 2.0                           |
| 10/31/2025 | 2.0                                 | 1.5                           |
| 11/30/2025 | 1.5                                 | 1.0                           |
| 12/31/2025 | 1.0                                 | 0.5                           |
| 1/31/2026  | 0.5                                 | 0.0                           |
| 2/28/2026  | 0.0                                 | -0.5                          |
| 3/31/2026  | -0.5                                | -1.0                          |
| 4/30/2026  | -1.0                                | -1.5                          |
| 5/31/2026  | -1.5                                | -2.0                          |
</details>

Source: FactSet, Bloomberg, JEF

Exhibit 10 - China SW EV/S Premium over China Internet  
![](images/5e35b113956941f0516841053c54f6975ad93584d3f23940050f9bb234f677d9.jpg)

<details>
<summary>line chart</summary>

| Date       | Value |
| ---------- | ----- |
| 5/31/2023  | 350%  |
| 7/31/2023  | 300%  |
| 9/30/2023  | 250%  |
| 11/30/2023 | 200%  |
| 1/31/2024  | 150%  |
| 3/

[中间内容因长度限制已省略]

lar investment objectives, portfolio holdings, strategy, financial situation, or needs of any recipient. As such, any advice or recommendation in this report may not be suitable for a particular recipient. JEF assumes recipients of this report are capable of evaluating the information contained herein and of exercising independent judgment. A recipient of this report should not make any investment decision without first considering whether any advice or recommendation in this report is suitable for the recipient based on the recipient's particular circumstances and, if appropriate or otherwise needed, seeking professional advice, including tax advice. JEF does not perform any suitability or other analysis to check whether an investment decision made by the recipient based on this report is consistent with a recipient's investment objectives, portfolio holdings, strategy, financial situation, or needs.

By providing this report, neither JRS nor any other JEF entity accepts any authority, discretion, or control over the management of the recipient's assets. Any action taken by the recipient of this report, based on the information in the report, is at the recipient's sole judgment and risk. The recipient must perform his or her own independent review of any prospective investment. If the recipient uses the services of JEF LLC (or other affiliated broker-dealers), in connection with a purchase or sale of a security that is a subject of these materials, such broker-dealer may act as principal for its own accounts or as agent for another person. Only JRS is registered with the SEC as an investment adviser; and therefore neither JEF LLC nor any other JEF affiliate has any fiduciary duty in connection with distribution of these reports.

The price and value of the investments referred to herein and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

This report may contain forward looking statements that may be affected by inaccurate assumptions or by known or unknown risks, uncertainties, and other important factors. As a result, the actual results, events, performance or achievements of the financial product may be materially different from those expressed or implied in such statements.

This report has been prepared independently of any issuer of securities mentioned herein and not as agent of any issuer of securities. No Equity Research personnel have authority whatsoever to make any representations or warranty on behalf of the issuer(s). Any comments or statements made herein are those of the JEF entity producing this report and may differ from the views of other JEF entities.

This report may contain information obtained from third parties, including ratings from credit ratings agencies such as Standard & Poor's, and information derived from third-party or proprietary generative artificial intelligence (Gen AI) models. JEF does not guarantee the accuracy, completeness, timeliness or availability of this information, and is not responsible for any errors or omissions (negligent or otherwise), regardless of the cause, or for the results obtained from the use of such content. Neither JEF nor any third-party content providers, including providers of Gen AI models, give any express or implied warranties, including, but not limited to, any warranties of merchantability or fitness for a particular purpose or use. Neither JEF nor any third-party content provider shall be liable for any direct, indirect, incidental, exemplary, compensatory, punitive, special or consequential damages, costs, expenses, legal fees, or losses (including lost income or profits and opportunity costs) in connection with any use of their content, including ratings. Credit ratings are statements of opinions and are not statements of fact or recommendations to purchase, hold or sell securities. They do not address the suitability of securities or the suitability of securities for investment purposes, and should not be relied on as investment advice. Reproduction and distribution of third party content in any form is prohibited except with the prior written permission of the related third party.

JEF reports are disseminated and available electronically, and, in some cases, also in printed form. Electronic research is simultaneously made available to all clients. This report or any portion hereof may not be copied, reprinted, sold, or redistributed or disclosed by the recipient or any third party, by content scraping or extraction, automated processing, or any other form or means, without the prior written consent of JEF. Any unauthorized use is prohibited. Neither JEF nor any of its respective directors, officers or employees, is responsible for guaranteeing the financial success of any investment, or accepts any liability whatsoever for any direct, indirect or consequential damages or losses arising from any use of this report or its contents. Nothing herein shall be construed to waive any liability JEF has under applicable U.S. federal or state securities laws.

For Important Disclosure information relating to JRS, please see https://adviserinfo.sec.gov/IAPD/Content/Common/crd\_iapd\_Brochure.aspx?BRCHR\_VRSN\_ID=483878 and https://adviserinfo.sec.gov/Firm/292142 or visit our website at https://javatar.bluematrix.com/sellside/Disclosures.action, or www.JEF.com, or call 1.888.JEF.

© 2026 JEF
"""
