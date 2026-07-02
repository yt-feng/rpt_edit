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
- `# 标题` 必须短、锐利、可转发，优先 18-30 个中文字符，最长不超过 36 个中文字符。
- `# 标题` 必须直接表达一个判断或悬念，例如“黄金缺的不是央行，是ETF”。
- `# 标题` 必须包含一个传播钩子，但只能用报告中真实出现或可由报告标题明确推出的信息：
  1. 机构 big name：高盛、摩根士丹利、摩根大通、瑞银、花旗、美联储等。
  2. 中国读者熟悉的人名 big name：洪灏、邢自强、辜朝明；国际公众人物：特朗普、马斯克、鲍威尔等。
  3. 反常识或意外差：例如市场普遍悲观时，报告给出“触底”“修复”“再加速”等相反信号。
- 已识别机构名：`IMF`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如高盛、摩根士丹利、汇丰、摩根大通、瑞银、花旗、美国银行、巴克莱、德意志银行、野村。
- 标题里不要同时写中文机构名和英文缩写，禁止“摩根大通：JPM：……”“高盛：GS：……”这类重复；写“摩根大通：……”或“高盛：……”即可。
- 标题可以用问句或对比句，但不要标题党到超出原报告证据。避免“震惊”“爆了”“彻底反转”“一夜变天”等廉价词。
- 标题不要晦涩抽象。少用“结构性分化”“二阶影响”“再定价框架”这类泛化词；如果必须使用，要落到一个具体对象。
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
1. `# 标题`：机构中文名或报告中的 big name + 一句主判断，不超过 36 字。
2. 开头 4-6 段：直接给出主判断、为什么现在重要、报告提供了什么新信号。
3. 4-6 个 `##` 小节：每个小节标题都是洞察句，不是栏目名。
4. 在正文中穿插 2-4 个 `> **KC评论：** ...` 引用块，每个 1-3 句，用更平白的话解释“这张图/这个判断对读者意味着什么”，并自然引出读完整报告的必要性。
5. 至少一个小节讨论“报告尚未完全回答的关键问题”，但标题也要是洞察句。
6. 至少一个小节给出读者的观察框架，但不要命名为“对读者的启发”。
7. 文末自然承接未解问题，引导读者加入社群/微信群继续讨论。不要照抄固定话术，请基于本文未解问题每次重新写一段自然 CTA；语义可以参考：加入社群，领取完整研报解读与原始图表。。
8. 在免责声明前，单独插入这张图片链接：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`
9. 结尾只输出英文灰色免责声明：`<p style="color:#999999;font-size:12px;">Personal reading notes and learning share only. Not investment advice.</p>`

【hook 要求】
- 不要硬插“加入社群”。
- hook 应该来自正文自然出现的未解问题，比如：关键假设尚未验证、竞争优势仍需拆解、图表背后的二阶影响没有展开。
- 文末 CTA 要像“顺着这些未解问题继续读完整报告/继续讨论”，不是广告口吻。
- CTA 必须每篇重新写，不能固定输出“加入社群，领取完整研报解读与原始图表”。它需要自然提到：每天会由 AI agent + 人工 review 生成国际投行中文摘要与 KC评论，daily 更新，约 10-40 页，也包含当天最新数据图表合集，既方便喂给 AI，也方便人工快速把握 market dynamics。

【KC评论要求】
- `KC评论` 不是复述原文，而是读者友好的解释、提醒或追问。
- 每条 `KC评论` 先说白话结论，再点出完整报告里值得继续看的图表、假设或细分拆解。
- 语气可以有判断力，但不要编造报告没有的数据或结论。

【图片要求】
- 不要主动生成 MinerU 图片 markdown；系统会在文章生成后自动插入 MinerU 原始图片。
- 但文末免责声明前必须保留知识星球图片：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`。

【内容边界】
- 只能基于研报原文和解析结果推导，不要编造数据、公司动作、引用。
- 遇到不确定内容，要用“这里仍需验证”“报告没有完全展开”等表达。
- 避免“震惊”“爆款”“一文看懂”等浮夸表达。
- 不要出现小红书话题标签。
- 不要出现 emoji。
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份IMF研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
## IMF POLICY PAPER

June 2026

THE CASE FOR A GENERAL ALLOCATION OF SDRs
DURING THE THIRTEENTH BASIC PERIOD

IMF staff regularly produces papers proposing new IMF policies, exploring options for reform, or reviewing existing IMF policies and operations. The following documents have been released and are included in this package:

\- The Report of the Managing Director to the Board of Governors, transmitted to the Board of Governors on June 26, 2026.

\- The Staff Report, prepared by IMF staff and completed on June 15, 2026 for the Executive Board's Information.

The IMF's transparency policy allows for the deletion of market-sensitive information and premature disclosure of the authorities' policy intentions in published staff reports and other documents.

Electronic copies of IMF Policy Papers are available to the public from http://www.imf.org/external/pp/ppindex.aspx

International Monetary Fund
Washington, D.C.

# INTERNATIONAL MONETARY FUND

Report of the Managing Director to the Board of Governors Pursuant to Article XVIII, Section 4(c) for the Thirteenth Basic Period

## June 26, 2026

The Twelfth Basic Period began on January 1, 2022 and is scheduled to end on December 31, 2026. The Thirteenth Basic Period will commence on January 1, 2027. The Articles of Agreement require the Managing Director to determine whether there is a case for a proposal regarding a general allocation or cancellation of Special Drawing Rights (SDR) in the next Basic Period to the Board of Governors no later than six months before the end of each Basic Period (Article XVIII, Section 4(c).

The Managing Director must be satisfied that a proposal for a general allocation or cancellation of SDRs, in her view: (i) is consistent with meeting the long-term global need to supplement existing reserve assets as set out in Article XVIII, Section 1(a); and (ii) would have broad support among participants in accordance with Section 4(b) of the same Article. Executive Board concurrence is required under Article XVIII, Section 4(a) for the proposal. Pursuant to Article XVIII, Section 4(d), a decision of the Board of Governors approving such a proposal of the Managing Director would require an 85 percent majority of the total voting power of members representing participants in the SDR Department, which currently encompasses all members of the Fund. If the Managing Director ascertains that there is no proposal consistent with Article XVIII, Section 1(a) that has broad support among participants, she must so report to the Board of Governors and to the Executive Board. The present report is submitted in accordance with these provisions.

In forming my view as to whether there is currently a basis for a new proposal, I have taken the following into consideration:

\- The case for a new allocation is not clear at this time. Since the 2021 General SDR allocation—the largest in Fund history—that took place during the last Basic Period, global developments have been characterized by resilient economic growth, high levels of international reserve assets, ample global liquidity, and improved access of emerging market economies to international capital markets. Despite the wars in Ukraine and the Middle East, since 2021, reserve assets have increased by over 21 percent globally, and by over 22 percent for emerging and developing countries (excluding China). The stock of SDRs relative to global reserves, capital flows, and international trade remain elevated, well above the levels before the 2021 Allocation as well as historical averages. While the war in the Middle East has already had major impacts on many members, its impact across members is asymmetric, along with its duration being unknown. As such, there is no strong evidence of a long-term

need to supplement global reserve assets at the current juncture. Staff will continue to closely monitor the situation in case the effects of the war become more persistent and widespread.

\- A new general SDR allocation would not receive the necessary support in terms of voting majority at this stage that is required for any proposal to succeed. In recent bilateral consultations, while a few Executive Directors saw merit in an allocation, Directors representing a majority of participants in terms of their voting power indicated that they would not support a new allocation in the current context. For reference, the last two SDR general allocations took place in the context of major global economic developments; the 2021 General SDR Allocation (SDR 456.5 billion) in the context of the COVID-19 Crisis, and the 2009 General Allocation (SDR 161.2 billion, in addition to the special allocation of SDR 21.5 billion to implement the Fourth Amendment to the Articles of Agreement) during the Global Financial Crisis. Prior to 2009, no general allocation had been approved since 1981.

On the basis of these considerations, I informed the Executive Board in my report of June 15, 2026 of my view at this stage that I would not be in a position to make, by June 30 of this year, a proposal for the Thirteenth Basic Period consistent with the provisions of the Articles that would have the broad support among participants.

In accordance with Article XVIII, Section 4(c), this does not preclude me during the Thirteenth Basic Period from making proposals on my own initiative, nor the Board of Governors or the Executive Board from requesting that I make a proposal, including in the event of unexpected major developments.

June 15, 2026

## THE CASE FOR A GENERAL ALLOCATION OF SDRs DURING THE THIRTEENTH BASIC PERIOD

## EXECUTIVE SUMMARY

This report sets out the basis for consideration of a new allocation or cancelation of Special Drawing Rights (SDRs) for the next (Thirteenth) Basic Period, scheduled to begin on January 1, 2027. The Articles of Agreement require that the Managing Director determine whether there is a case for general SDR allocation or cancellation to the Board of Governors no later than six months before the end of each five-year Basic Period. The case to make a proposal is based on two requirements: (i) consistency with meeting the long-term global need to supplement existing reserve assets; and (ii) broad support among participants for the proposal

This paper does not present a proposal for a new allocation of SDRs. There is neither a clear economic case nor the necessary support for a new allocation at present. Since the 2021 General SDR Allocation, global developments have been characterized by resilient economic growth, high levels of international reserve assets, ample global liquidity, and improved access of emerging market economies to international capital markets. Moreover, there are clear indications that a new general SDR allocation would not receive the necessary support to proceed.

Based on these considerations, the Managing Director does not plan to make a proposal by June 30, 2026. This does not preclude the Managing Director to make a proposal, at her initiative or at the request of the Board of Governors or the Executive Board, at any time during the Thirteenth Basic Period. Management and staff will continue to carefully monitor the evolving global situation, and remain in close contact with the membership to see how the Fund can best meet their needs.

## Approved By

Bernard Lauwers (FIN)

Yan Liu (LEG)

Christian Mumssen (SPR)

Prepared by the Finance (FIN), Legal (LEG), and Strategy, Policy, and Review (SPR) Departments. The team was led by J. Gijón (FIN), C. Delong (LEG), and A. Shahmoradi (SPR); and comprised Q. Chen and N. Magud (FIN). J. Thornton provided overall guidance under the supervision of C. Oner (FIN), B. Steinki (LEG), and G. Chabert (SPR). G. Pais Marden (FIN) provided research assistance. M. DeGuzman and R. Avila (both FIN) helped prepare the report.

## CONTENTS

BACKGROUND 3

CASE FOR AN ALLOCATION \_\_\_\_ 3

CONCLUSION 4

## FIGURES

1. Reserve Assets and Sovereign Issuances \_\_\_\_ 5

2. Long-term Perspective of SDR Holdings, 1980–2025 \_\_\_\_ 6

## BACKGROUND

1. The Articles of Agreement require the Managing Director to determine whether there is a case for a proposal regarding a general SDR allocation or cancellation to the Board of Governors no later than six months before the end of each five-year Basic Period. The Twelfth Basic Period began on January 1, 2022, and is scheduled to end on December 31, 2026. The Thirteenth Basic Period will commence on January 1, 2027, and based on Article XVIII, Section 4(c) the Managing Director has to make a proposal regarding a general allocation or cancellation to the Board of Governors by June 30, 2026.

2. Before making any proposal, the Managing Director must be satisfied that a proposal for a general allocation or cancellation of SDRs, in her view: (i) is consistent with meeting the long-term global need to supplement existing reserve assets as set out in Article XVIII, Section 1(a); and (ii) that there is broad support among participants for the proposal in accordance with Section 4(b) of the same Article. Executive Board concurrence is required under Article XVIII, Section 4(a) for the proposal. Under Article XVIII, Section 4(d), a decision of the Board of Governors approving such a proposal of the Managing Director requires an 85 percent majority of the total voting power of participants in the SDR Department, which currently encompasses all members of the Fund (Article XVIII, Section 4(d)). If the Managing Director ascertains that there is no proposal which she considers consistent with Article XVIII, Section 1(a) that has broad support among participants, she must so report to the Board of Governors and to the Executive Board (Article XVIII, Section 4(c)). The present report is submitted in accordance with these provisions.

## CASE FOR AN ALLOCATION

## 3. In determining whether to make a proposal, the following issues were considered:

\- The lack of a clear case for a new allocation. The case for a new allocation in accordance with Article XVII, Section 1(a) is not clear at this time. Since the 2021 General SDR allocation—the largest in Fund history—that took place during the last Basic Period, global developments have been characterized by resilient economic growth, high levels of international reserve assets, ample global liquidity, and improved access of emerging market economies to international capital markets (Figure 1). Notwithstanding the wars in Ukraine and the Middle East, reserve assets have increased by over 21 percent globally since 2021, and by over 22 percent for emerging and developing countries (excluding China). The stock of SDRs relative to global reserves, capital flows, and international trade remain elevated, well above the levels before the 2021 Allocation as well as historical averages (Figure 2). While the war in the Middle East has already had major impacts on many members, its impact across members is asymmetric, and its duration unknown. In view of the above-mentioned factors, staff does not see a case for new

allocation. Staff will continue to monitor the situation closely in case the effects of the war become more persistent and widespread.

\- The lack of broad support of participants for a new allocation. There are clear indications that a new general SDR allocation would not receive the necessary 85 percent majority of the total voting power in the Board of Governors at present. In recent bilateral consultations, while a few Executive Directors saw merit in an allocation, Executive Directors representing a majority of the participants in terms of voting power indicated that they would not support a new allocation in the current context. For reference, the last two SDR general allocations took place in the context of major global economic developments; the 2021 General SDR Allocation (SDR 456.5 billion) in the context of the COVID-19 Crisis, and the 2009 General Allocation (SDR 161.2 billion, in addition to a special allocation of SDR 21.5 billion to implement the Fourth Amendment to the Articles of Agreement) during the Global Financial Crisis. Prior to 2009, no general allocation had been approved since 1981.

## CONCLUSION

4. In light of the considerations above, the Managing Director does not plan to make a proposal by June 30 of this year. This conclusion is based on Article XVIII, Section 4, which requires that the Managing Director make a proposal only if, in her view, such a proposal would be consistent with meeting the long-term global need to supplement existing reserve assets, and would also have broad support among participants. In view of this requirement, the considerations above, and the Executive Board's interest in streamlining, the Managing Director does not plan to propose a Board discussion of the issue on this occasion.

5. This conclusion does not preclude the Managing Director from making a proposal during the Thirteenth Basic Period. In accordance with Article XVIII, Section 4(c), the Managing Director can propose an allocation or cancellation, at her own initiative or at the request of the Board of Governors or the Executive Board, at any time during the remainder of the Thirteenth Basic Period, such as in the case of unexpected major developments that could motivate such a proposal.

Figure 1. Reserve Assets and Sovereign Issuances  
Global Reserve Assets, 1995–2025 (In trillions of SDRs)  
![](images/2c355c76c7b30daee83e882dd567bc3957df960f6365890811fe110218f5a127.jpg)

Sovereign Issuances, 2005–2025
(In billions of USD)  
![](images/b48aa9d523b84d2c1e16e4c2eda09522c36dc8294ca593a9641be65774461ba4.jpg)  
Source: IMF; World Economic Outlook; and Fund staff calculations.

Figure 2. Long-term Perspective of SDR Holdings, 1980–2025 (In percent of)  
Global Reserves 1/  
![](images/7e348ed0148400e2cb5c97525cc48075cdb9f92f38e5fae7d4ccb5f966494f2c.jpg)  
Global Gross Capital Flows

![](images/e0a35d9f69f9ea17a507ebf949e20e3deb470f381b2da1500514a8260f535447.jpg)  
Global Trade 3/

![](images/8a5d5f257ae9a775547d50b1c2b76cc2a41b630a313d668f9969a60af137cf8e.jpg)  
Source: IMF; World Economic Outlook; and Fund staff calculations.  
1/ Including gold.  
2/ Excluding China.  
3/ Goods and services.
"""
