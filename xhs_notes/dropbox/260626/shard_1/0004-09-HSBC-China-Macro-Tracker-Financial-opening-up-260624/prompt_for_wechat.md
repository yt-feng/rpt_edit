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
  1. 机构 big name：GS、MS、JPM、UBS、Citi、美联储等。
  2. 中国读者熟悉的人名 big name：洪灏、邢自强、辜朝明；国际公众人物：特朗普、马斯克、鲍威尔等。
  3. 反常识或意外差：例如市场普遍悲观时，报告给出“触底”“修复”“再加速”等相反信号。
- 已识别机构名：`HSBC`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、MS、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
- 标题里不要同时写中文机构名和英文缩写，禁止“JPM：JPM：……”“GS：GS：……”这类重复；写“JPM：……”或“GS：……”即可。
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
7. 文末自然承接未解问题，引导读者加入社群/微信群继续讨论。不要照抄固定话术，请基于本文未解问题每次重新写一段自然 CTA；语义可以参考：每天由 AI agent + 人工 review 生成国际投行中文摘要与 KC评论，daily 更新约 10-40 页，并整理当天最新数据图表合集，方便喂给 AI，也方便人工快速把握 market dynamics。欢迎来星球微信群里继续讨论。。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份HSBC研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
Financial opening-up

\- The Lujiazui Forum focused on RMB internationalisation, further opening-up, and enhancing the monetary toolkit

\- China unveiled an action plan to better utilise foreign investment, increase market access, and encourage R&D

◆ Muted consumption during the Dragon Boat festival and “6.18”, fiscal spending slowed in May, and SLGB needs a lift

## Lujiazui Forum: RMB internationalisation and monetary reforms in focus

The 2026 Lujiazui Financial Forum was held on 17-18 June, with China's top financial regulators (including leaders from the PBOC, NFRA, CSRC and SAFE) participating. The commitment to high-level opening-up, capital market reforms, and monetary policy reform was evident in their speeches, while a slew of measures was also unveiled (see Table 1).

The Forum sent a clear signal of support for high-level financial opening-up. Authorities will pilot offshore financial activities, covering areas such as offshore trade finance, free trade zone offshore bonds, and offshore reinsurance. Offshore FX trading in the Shanghai FTZ by six large domestic commercial banks and a new RMB Repo Facility for central banks were also introduced (Foreign and International Monetary Authorities (FIMA) RMB Repo). The moves could support liquidity and aligns with the $15^{\text{th}}$ FYP's incentive to promote RMB internationalisation, high-level opening-up, and support Chinese companies' global strategy.

On the monetary policy front, the PBOC announced adjustments and enhanced use of the temporary overnight repo and reverse repo operation tools (which were introduced in July 2024). The rates will be set at 25bp below and above the policy rate (seven-day reverse repo rate), meaning a narrower and symmetrical rate corridor of 50bp versus 70bp previously. This should help control volatility of front-end interbank borrowing costs, which typically shows seasonal spikes towards quarter-end (Chart 31). This may also pave the way for eventual use of the overnight rate as the key policy rate, as used in many DM central banks including the Fed. While we think the PBOC is likely to keep the policy rate on hold this year (see Global Economics Quarterly, 22 June), the adjustment to monetary tools adds more options to the PBOC's toolkit.

FDI: A new action plan to better utilise foreign investment and open-up access Part of China's high-level opening-up plan involves expanding domestic access for foreign activities. On 22 June, China's Ministry of Commerce, together with other government departments, released an action plan to optimise the utilisation of foreign investment. The plan includes expanding market access in sectors such as services, finance, and pharmaceuticals; streamlining processes for cross-border mergers and acquisitions, data flows, and reinvestment by foreign invested enterprises in China; and strengthening policy support measures for foreign funded R&D centres.

## Disclosures & Disclaimer

This report must be read with the disclosures and the analyst certifications in the Disclosure appendix, and with the Disclaimer, which forms part of it.

## Erin Xin

Senior Economist, Greater China  
The Hongkong and Shanghai Banking Corporation Limited  
erin.y.xin@hsbc.com.hk  
+852 2996 6975

## Taylor Wang

Economist, China  
The Hongkong and Shanghai Banking Corporation Limited  
taylor.t.l.wang@hsbc.com.hk  
+852 2288 8650

## Jing Liu

Chief Economist, Greater China  
The Hongkong and Shanghai Banking Corporation Limited  
jing.econ.liu@hsbc.com.hk  
+852 3941 0063

## Heidi Li

Associate Guangzhou

Issuer of report: The Hongkong and Shanghai Banking Corporation Limited

View HSBC Global Investment Research at: https://www.research.hsbc.com

We see more MNCs looking to tap into China's innovation capabilities by establishing R&D centres and increase investment in China, and we are seeing a revival in FDI flows (Chart 1). The World Intellectual Property Organization (WIPO) has ranked China among the world's top-10 most innovative economies. In the first five months of this year, nearly 4,000 foreign enterprises expanded their investments in China. In 2025, R&D spending accounted for $14.3\%$ of MNCs' global R&D in their greenfield investment in China, with pharmaceuticals attracting the largest share ( $70.8\%$ of total R&D investment) (CAITEC, 16 June). The action plan will encourage FDI inflows and channel capital into high-tech industries and modern services, supporting industrial upgrading and long-term development.

Meanwhile, a relatively stable China-US economic and trade relationship may also support stronger US investment appetite (Chart 2). China and the US have agreed to set up a Board of Investment Board to identify and clarify non-strategic sectors where they can strengthen bilateral investment cooperation. From January to May, US FDI in China increased by $17.3\%$ y-o-y. Meanwhile, China's resilience amid the Middle East conflict has further strengthened its relative appeal, reflected in a $285.5\%$ increase in Saudi investment. The recent easing of Middle East tensions between the US and Iran may also help sentiment to improve trade and investment flows (CNBC, 22 June).

Consumption: Dragon Boat festival sees per capita spending down; “6.18” sales muted China’s consumers remain cautious (see China’s cautious consumer, 22 May). China recently held the annual Dragon Boat festival (19-21 June), which saw the number of domestic trips rise 4.4% y-o-y (124m), while total spending increased 4% (RMB44.5bn). While each hit new records, the per capita spending remained below pre-pandemic levels (down 14% vs 2019) (Chart 3). Ongoing caution for consumers has been evident in labour market pressures and continued drag in the property sector.

Such lukewarm consumer sentiment follows the annual online shopping holiday "6.18", which lasted from 13 May to 18 June (the same period as in 2025), which showed goods demand lagging. Gross merchandise value in e-commerce was generally flat, reaching RMB864bn vs RMB856bn last year, according to data from Syntun. This mimics the soft May retail sales, which declined $0.6\%$ y-o-y.

We believe the services sector could take the lead given its greater potential to expand growth in new areas such as digital and AI services, as well as basic services including childcare and healthcare. A new combined goods and services series was released by NBS in May 2026, 2.8% ytd y-o-y, which showed services (5.4%) leading goods (1.4%) growth (Chart 4).

## Fiscal data: another month of expenditure slowdown

Fiscal expenditure continued to slow in May, echoing the disappointing FAI data. The major drag still came from government-managed funds, where expenditure fell 11% y-o-y due to softer land sales and the slowdown in special local government bond issuance (only 3.7% of annual quota in May 2026 versus 10% in May 2025). On the general public budget side, revenue growth held up well (up 6.6% y-o-y), helped by the ongoing recovery in VAT and corporate income taxes amidst PPI improvement (see China inflation, 10 June). However, expenditure recorded another decline (-1.6%). Together, the broad-based fiscal deficit reached RMB590bn in Apr-May this year versus RMB982bn over the same period last year.

Structurally, a smaller share of the general public expenditures was allocated to infrastructure (i.e., environment protection, community affairs, agriculture, and transportation) and more funding was given to livelihood-related areas since the start of this year (Chart 5). This aligns with the policy tone that the long-term push to build a strong domestic market will be achieved via “investing in people” (human capital, healthcare, education, skills). That said, with recent FAI weakness intensifying, we expect the balance to re-emphasise investment. To support this, we expect re-acceleration of bond issuance and faster deployment of funds to projects (Chart 6).

Table 1: Major financial measures announced at the 2026 Lujiazui Financial Forum

<table><tr><td>Department</td><td>Measures</td></tr><tr><td>PboC</td><td>◆ Improve short-term interest rate control framework◆ Establish a repo facility for overseas central bank-type institutions◆ Study a macroprudential tool to provide liquidity support to non-banks under specific scenarios◆ Authorise six banks to conduct offshore RMB FX trading in the Shanghai FTZ via the China Foreign Exchange Trade System (CFETS) platform◆ Promote greater investment by medium- and long-term funds in equities and bonds</td></tr><tr><td>NFRA</td><td>◆ Accelerate revisions to the Banking Supervision Law and the Insurance Law◆ Support pilot programmes for new financial business models in Shanghai; jointly roll out measures to speed up Shanghai&#x27;s development as an international reinsurance centre◆ Support efforts to mitigate risks in the property sector and local government debt</td></tr><tr><td>CSRC</td><td>◆ Work with the PBOC to advance a pilot for RMB FX futures◆ Strongly support M&amp;A and refinancing by listed companies; support eligible Hong Kong-listed companies to list onshore◆ Expand STAR Market &quot;Fifth Set&quot; listing criteria to cover AI foundation model companies◆ Release guidance in due course on the regulated development of AI in capital markets◆ Encourage licenced foreign institutions to participate in the fund investment advisory pilot and expand the programme</td></tr><tr><td>SAFE</td><td>◆ Launch a package of incremental policies soon to facilitate cross-border investment and financing◆ Fully reform cross-border policies for foreign direct investment (FDI)◆ Further streamline FX administration for outbound direct investment (ODI) and external debt; optimise rules for FX loans and cross-border equity incentives; issue a new batch of QDII quotas</td></tr><tr><td>Shanghai International Financial Centre – Offshore Finance Action Plan</td><td>◆ Expand the pilot for integrated reform of offshore trade finance services in the Lingang New Area of the Shanghai FTZ; support global quality traders to set up dedicated offshore trade companies◆ Set a dedicated quota for Free Trade Account (FTA) units in the Shanghai FTZ to invest in offshore bonds◆ Support Shanghai&#x27;s pilot for multinational treasury centres; encourage MNCs to establish international treasury centres◆ Support eligible commercial banks to conduct offshore RMB FX trading in the Shanghai FTZ◆ Facilitate financial services for non-resident individuals</td></tr></table>

Source: CLS, HSBC

## Charts of the week

1. China's rising innovation capabilities attract FDI  
![](images/bc258bbce6e181f4f1733b5bb3e9db3097d75d57428fd32f642524876e7bb670.jpg)  
Source: SAFE HSBC; Note: We use the method discussed in FDI Myths and Truths (11 Dec 2023) to compute "real FDI" inflows, which strip out 'phantom' investments into special purpose entities, for the sake of masking the funding source but not for actual use.

2. Investment from the US may increase as China-US relations stabilise  
![](images/2052062626c33c6dd71e056a197bc38f5a60ec6d9703250b39cdfec8644f448a.jpg)  
Source: Wind, HSBC

3. Holiday travel increased, but per capita spending remained subdued  
![](images/fb37e5d43b1448b15ebc3dc272d35fa86cb870d1e6af47d537ee11e18bf59948.jpg)  
Source: Xinhua, HSBC

4. NBS released a new time series combining goods and services  
![](images/1fa60b2e5036b7a69493bf3fefd9db683768ec50658a1dd7ec75c38f16c4fb3a.jpg)  
Source: Wind, HSBC

5. More fiscal funding was given to livelihood-related areas  
![](images/96af66575974781fb2097b94915da1a790fc022cbfe7efb0ae6febed247452fc.jpg)  
Source: CEIC, HSBC

6. LGSB issuance can be stepped up to support infrastructure investment  
![](images/7a8a860f20a489a36258f4761d32e3df15c240fc0c4bb9e9bdf48766ba17a7f3.jpg)  
Source: Wind, HSBC; Note: Data as of 23 June.

## Economic activity

7. National box office revenues edged up  
![](images/900bad6b4463c3868ce8d473778c3137e83e278e629495414e401f4f760c3a88.jpg)  
Source: Wind, HSBC

8. Housing prices in tier-1 cities edged up  
![](images/6742b88983670420a83d7e9f7bb4323257f8e338cbe9c6d18d3e7f18dc95465c.jpg)  
Source: Bloomberg, HSBC; Note: as of 23 June.

9. New home sales edged up seasonally  
![](images/f4fb4a01603cfc94bdfd193ee4c4aa96b460ab340e1ac724d0395eb5eb34dc24.jpg)  
Source: Wind, HSBC

10. New home sales in Tier-1 cities dipped during the holiday  
![](images/dc39917d84e156e7042a6fb765b633fd60a52f3edd06ac4ef4bef046d44381fa.jpg)  
Source: Wind, HSBC

11. Second-hand home sales in 18 major cities eased due to the holiday  
![](images/9e8e672a64727f0fd555fcd62f72d3a9f64ef5600ca06c29624257c623b0b19c.jpg)  
Source: Wind, HSBC

12. Transactions in second-hand homes in Tier-2 cities remained higher y-o-y  
![](images/30c9d14d540ced41dccce251f80ae42d75611823669ef95bba852f74b3c55947.jpg)  
Source: Wind, HSBC

13. Land sales edged down  
![](images/74c56ba4a15ed4a0e50c6e8acea2d119a52b1c38e9878245e9198cf0b17393a1.jpg)

14. Planned construction area of land sold edged down  
![](images/cdcfef73dc7d21a564bab9eb26d0c5385f40bee4716b8c1fa6e899026911413a.jpg)

15. The semi-steel tyre operating rate edged down  
![](images/3b2c85eb9be7d5829b98e4158de51d50296a887cd06a40388d7c42cde3c38335.jpg)  
Source: Wind, HSBC  
Source: Wind, HSBC

16. The production rate in the chemical sector picked up  
![](images/fd26eafa28ae97f3b8b58271dffcecb8ec2540fdcd90f5451410cef0abac1be9.jpg)

17. The blast furnace operating rate remained above historical levels  
![](images/21fe2197076bfff55fe2761be135b1f62e36392ae16e685ae0592a7fc91df315.jpg)  
19. The cement shipping rate steadied  
Source: Wind, HSBC

18. The petroleum asphalt operating rate ticked up  
![](images/61a5f81ae547eb961c7be9019869e1049f1e1c1ed8d8d5723de96496e4d300ed.jpg)  
Source: Wind, HSBC

![](images/33434967d78bf14bc3b989300d92a570bd24890e266854fc7de0450461ea0573.jpg)  
Source: Wind, HSBC

20. Coal consumption for eight major provinces edged down  
![](images/537485513e4edef9ea8f9ebba7caf36766c5131f8c7cb1f90a1508f7d3d02d92.jpg)  
Source: Wind, HSBC

21. The operating rate of polyester filaments eased further  
![](images/7295a32bcd35499203121d064d9397ff60875bbc0ecbc20b3889249b261be2e3.jpg)  
Source: Wind, HSBC

22. The Baltic Dry Index edged down  
![](images/2ca449f96ec2c29d03bfa441e8331666a57af72ef914c0f2e6e064418f7e509f.jpg)  
Source: Wind, HSBC

## Travel and logistics

23. Metro volumes in large cities steadied  
![](images/919d75f872f01c191dd44494e17e3989a6dcdbcbaa1cb237765a5710d809be64.jpg)  
Source: Wind, HSBC; note: six cities include Beijing, Shanghai, Guangzhou, Shenzhen, Chengdu and Tianjin.

24. Postal delivery volumes edged down  
![](images/388463480068d379e6f83420b5f340651791f21c3f737144603b0d0e64d03628.jpg)  
Source: Wind, HSBC

25. Container exports from China to the US edged down  
![](images/699f93fcecb7ec47394ccbeec8df874913fb4de544a4ddf5c9ac590cd4f51615.jpg)  
Source: Bloomberg, HSBC

26. China's major ports' freight throughput edged down  
![](images/8868cf1b8a9535851c9ebe174dfc4a5d958ab2d625c24b132c86633f9549b782.jpg)  
Source: CEIC, HSBC; Note: Weekly beginning at Monday

## Inflation and policies

27. Crude oil prices fell as the US and Iran reached a deal  
![](images/6195910d590d5342750cc2416c3d30a0b8daa60db464bc58f514f3ae6443b75e.jpg)  
Source: Wind, HSBC

28. Cement prices and glass prices both edged down  
![](images/2a7eade82e39187fa3e74744e9abbe94f2326f7228a6284d969aab120a0a8059.jpg)  
Source: Wind, HSBC

29. Agricultural product prices eased seasonally  
![](images/681d98e719c1fd8933f6f5c2e4ccbb4d14ed3800bb19e2cc60ec28f6af524d8f.jpg)  
Source: Wind, HSBC

30. Container shipping costs on China-Southeast Asia route edged up  
![](images/cfcdce69ffab96b801ed93b96be55c8f0af87f7562de7294a1f69fe86d855294.jpg)  
Source: Wind, HSBC

31. Interbank rates edged up  
![](images/77626177fd05fe174c5373df96216169174a4a22059af9e3b4f227839ec7f951.jpg)  
Source: Wind, HSBC

32. The PBOC made net injections through OMOs last week  
![](images/2124c38fc906f3f159f8b54f818a1632a007f95cfd950b8471f96978eb223b86.jpg)  
Source: Wind, HSBC

## Links to recent reports in the China Macro Tracker series

What the US-Iran deal could mean for China, 17 June 2026

Blueprints for employment strategy, 10 June 2026

Home sweet home, 3 June 2026

Structural measures move up the agenda, 27 May 2026

Stable relations, but domestic pressures, 20 May 2026

First Presidential summit of the year arrives, 13 May 2026

Future focused, 6 May 2026

Tougher investment security reviews, 29 April 2026

More reserve policies are in the pipeline, 22 April 2026

Focus on "doing o's own thing well", 15 April 2026

Better coordination of development and security, 9 April 2026

Resilience and stability could pay off, 1 April 2026

Expanding opening-up and FDI, 25 March 2026

A good start, more moves to follow, 18 March 2026

NPC press conferences, global oil volatility, 11 March 2026

China's Two Sessions in a volatile world, 4 March 2026

US tariff changes, record breaking CNY holiday, 25 February 2026

Boosting investment and innovation, 11 February 2026

Chinese New Year migration begins, China-UK reset, 4 February 2026

A more conservative approach to the GDP target, 28 January 2026

Domestic pressures may prompt more urgency, 21 January 2026

Domestic demand needs an investment lift, 14 January 2026

Starting the new year with policy support, 7 January 2026

Demand-led rebalancing, 17 December 2025

Politburo, Pandas and Provincial Five-Year Plans, 10 December 2025

Last policy meetings for the year approaching, 3 December 2025

Phone a friend, 26 November 2025

Not yet at the finishing line, 19 November 2025

A balanced approach, 12 November 2025

A new tenuous equilibrium, 5 November 2025

Potential trade breakthroughs, 29 October 2025

Deal or no deal, 22 October 2025

On pins and needles, 15 October 2025

New measures before the Golden Week, 1 October 2025

Talking points, 24 September 2025

US-China talks see progress in Madrid, 17 September 2025

Anti-involution to help longer-term development, 10 September 2025

Domestic reforms accelerating, 3 September 2025

# Disclosure appendix

## Analyst Certification

The following analyst(s), economist(s), or strategist(s) who is(are) primarily responsible for this report, including any analyst(s) whose name(s) appear(s) as author of an individual section or sections of the report and any analyst(s) named as the covering analyst(s) of a subsidiary company in a sum-of-the-parts valuation certifies(y) that the opinion(s) on the subject security(ies) or issuer(s), any views or forecasts expressed in the section(s) of which such individual(s) is(are) named as author(s), and any other views or forecasts e

[中间内容因长度限制已省略]

imited (ABN 48 006 434 162, AFSL No. 232595). These respective entities make no representations that the products or services mentioned in this document are available to persons in Australia or are necessarily suitable for any particular person or appropriate in accordance with local law. No consideration has been given to the particular investment objectives, financial situation or particular needs of any recipient.

HSBC Securities (USA) Inc. accepts responsibility for the content of this research report prepared by its non-US foreign affiliate. The information contained herein is under no circumstances to be construed as investment advice and is not tailored to the needs of the recipient. All US persons receiving and/or accessing this report and intending to effect transactions in any security discussed herein should do so with HSBC Securities (USA) Inc. in the United States and not with its non-US foreign affiliate, the issuer of this report. HSBC México, SA, Institución de Banca Múltiple, Grupo Financiero HSBC is authorized and regulated by Secretaría de Hacienda y Crédito Público and Comisión Nacional Bancaria y de Valores (CNBV). In Brazil, this document has been distributed by Banco HSBC SA ("HSBC Brazil"), and/or its affiliates. As required by Resolution No. 20/2021 of the Securities and Exchange Commission of Brazil (Comissão de Valores Mobiliários), potential conflicts of interest concerning (i) HSBC Brazil and/or its affiliates; and (ii) the analyst(s) responsible for authoring this report are stated on the chart above labelled "HSBC & Analyst Disclosures".

If you are a customer of HSBC International Wealth & Premier Banking ("IWPB"), including HSBC Private Bank, you are eligible to receive this publication only if: (i) you have been approved to receive relevant research publications by an applicable HSBC legal entity; (ii) you have agreed to the applicable HSBC entity's terms and conditions and/or customer declaration for accessing research; and (iii) you have agreed to the terms and conditions of any other internet banking, online banking, mobile banking and/or investment services offered by that HSBC entity, through which you will access research publications (collectively with (ii), the "Terms"). If you do not meet the above eligibility requirements, please disregard this publication and, if you are a IWPB customer, please notify your Relationship Manager or call the relevant customer hotline. Distribution of this publication is the sole responsibility of the HSBC entity with whom you have agreed the Terms. Receipt of research publications is strictly subject to the Terms and any other conditions or disclaimers applicable to the provision of the publications that may be advised by IWPB. © Copyright 2026, The Hongkong and Shanghai Banking Corporation Limited, ALL RIGHTS RESERVED. No part of this publication may be reproduced, stored in a retrieval system, or transmitted, on any form or by any means, electronic, mechanical, photocopying, recording, or otherwise, without the prior written permission of The Hongkong and Shanghai Banking Corporation Limited.

# Global Economics Research Team

## Global

Global Chief Economist
Janet Henry +44 20 7991 6711
janet.henry@hsbcib.com

Global Economist  
James Pomeroy +44 20 7991 6714  
james.pomeroy@hsbc.com

Global Economist  
Bethan Ellis +44 20 7991 6714  
bethan.ellis@hsbc.com

Trade Economist  
Shanella Rajanayagam +44 20 3268 4118  
shanella.l.ajanayagam@hsbc.com

## Europe

Chief European Economist
Simon Wells +44 20 7991 6718
simon.wells@hsbcib.com

Senior Economist  
Chris Hare +44 20 7991 2995  
chris.hare@hsbc.com

## United Kingdom

Senior Economist, UK
Elizabeth Martins +44 20 7991 2170
liz.martins@hsbc.com

UK Economist Emma Wilks +442032685948 emma.wilks@hsbc.com

## Germany

Stefan Schilbe +49 211 910 3137
stefan.schilbe@hsbc.de

Anja Sabine Heimann +44 738 724 7457
anja.sabine.heimann@hsbc.com

## France

Chantana Sam +33 1 4070 7795
chantana.sam@hsbc.fr

## North America

## US

Ryan Wang +1 212 525 3181
ryan.wang@us.hsbc.com

## Asia Pacific

Co-Head of Global Research, Asia-Pacific and Co-Head of Asian Economics Research
Frederic Neumann +852 2822 4556
fredericneumann@hsbc.com.hk

Chief Economist, Australia, New Zealand and Global Commodities
Paul Bloxham +612 9255 2635
paulbloxham@hsbc.com.au

Chief Economist, India and Indonesia
Pranjul Bhandari +65 6658 4976
pranjul.bhandari@hsbc.com.sg

Jamie Culling +612 9006 5042
jamie.culling@hsbc.com.au

Jing Liu +852 3941 0063
jing.econ.liu@hsbc.com.hk

Ines Lam +852 2288 7131
ines.y.k.lam@hsbc.com.hk

Yun Liu +852 2822 4297
yun.liu@hsbc.com.hk

Aayushi Chaudhary +91 22 2268 5543
aayushi.b.chaudhary@hsbc.co.in

Maitreyi Das +91 80 6737 3155
maitreyi.das@hsbc.co.in

Erin Xin +852 2996 6975
erin.y.xin@hsbc.com.hk

Aris Dacanay +852 3945 1247
aris.dacanay@hsbc.com.hk

Jin Choi +852 2996 6597
jin.h.j.choi@hsbc.com.hk

Akiko Kitamura +852 2996 6676
akiko.kitamura@hsbc.com.hk

Justin Feng +852 2288 7108
justin.feng@hsbc.com.hk

Taylor Wang +852 2288 8650
taylor.t.l.wang@hsbc.com.hk

Priya Mehrishi +91 97 3916 9567
priya.mehrishi@hsbc.co.in

## CEEMEA

Chief Economist, CEEMEA Simon Williams +971 50 9143382 simon.williams@hsbc.com

Senior Economist, Central & Eastern Europe  
Agata Urbanska-Giner +44 20 7992 2774  
agata.urbanska@hsbcib.com

Senior Economist, CEEMEA  
Melis Metiner +44 20 3359 2636  
melismetiner@hsbcib.com

Senior Economist, South Africa  
Hugo Pienaar +44 20 7718 9563  
hugo.pienaar@hsbc.com

## Latin America

Chief Economist, Mexico
Jose Carlos Sanchez +52 55 5721 5623
jose.c.sanchez@hsbc.com.mx

Head of Brazil Economics Research
Daniel Lavarda +55 11 2802 2640
daniel.lavarda@hsbc.com
"""
