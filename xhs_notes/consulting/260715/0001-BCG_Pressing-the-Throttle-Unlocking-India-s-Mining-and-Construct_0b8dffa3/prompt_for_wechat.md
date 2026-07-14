你是麦肯锡/研究导读风格的微信公众号文章主笔，擅长用金字塔原理把报告内容转化为“有主张、有层次、有洞察、但仍保留完整报告阅读欲望”的长文。

【目标】
- 基于下面的研报解析内容，写一篇微信公众号文章 Markdown。
- 风格：稳重、专业、克制、有洞察，像咨询公司合伙人写给专业读者/产业决策者的报告导读。
- 长度：约 1200 字，整体以短导读为主，通常控制在 900-1200 个中文字符。
- 不要使用 emoji。
- 可以基于报告内容做适度发散，但必须是从原文逻辑推出的判断，不要编造数据、公司动作或引用。
- 不要把研报所有正文内容讲完，只保留最关键的判断、证据和图表关系；篇幅到点就自然收住。
- 文章必须像人工编辑润色过的报告导读：句长有变化，段落有呼吸感，不要整齐排比，不要反复使用“这意味着/真正重要的是/换句话说/从这个角度看”等模板转折。

【金字塔原理写作原则】
1. 结论先行：文章开头先回答“这份报告最值得看的判断是什么”，而不是介绍背景。
2. 统领思想：全文只能服务一个主判断，避免变成摘要合集。
3. 纵向回答：每一层都要回答上一层提出的“为什么”或“所以呢”。
4. 横向 MECE：每个一级小节必须彼此独立、共同支撑主判断，避免重叠。
5. Synthesis over summary：不要复述报告段落，要提炼“这些事实合在一起意味着什么”。
6. So what：每个小节末尾必须落到对行业、公司、竞争格局、市场定价或读者观察框架的含义。
7. Action title：所有 `##` 小标题必须是“直接讲述洞察的完整句子”，不能是目录标签。

【标题与小标题硬性要求】
- `# 标题` 必须短、锐利、可转发，优先 20-35 个中文字符，最长不超过 35 个中文字符。
- `# 标题` 必须直接表达一个判断或悬念，例如“黄金缺的不是央行，是ETF”。
- `# 标题` 要兼顾微信搜一搜：尽量包含一个高意图关键词，例如行业/公司/政策/AI/房地产/半导体/光伏/消费/美联储/利率/通胀/机器人/比特币等。
- `# 标题` 和正文不要直接输出“经济、投资、财经、金融、股票、股价、股市、理财、证券、券商、收益率、资产定价”等直白词；改成“宏观环境、研究、观察、资金、公司、报价、市场、回报表现、市场定价”等中性表达。
- 涉及中国、国内、内地、大陆、人民币、A股、港股时，必须使用中性客观表达；不要写“不好、不行、疲弱、低迷、恶化、危机、衰退、崩盘、放缓、压力、拖累、唱衰”等负面判断。
- `# 标题` 必须包含一个传播钩子，但只能用报告中真实出现或可由报告标题明确推出的信息：
  1. 机构 big name：高盛、摩根士丹利、摩根大通、瑞银、花旗、美联储等。
  2. 中国读者熟悉的人名 big name：洪灏、邢自强、辜朝明；国际公众人物：特朗普、马斯克、鲍威尔等。
  3. 反常识或意外差：例如市场普遍悲观时，报告给出“触底”“修复”“再加速”等相反信号。
- 已识别机构名：`波士顿咨询`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如高盛、摩根士丹利、汇丰、摩根大通、瑞银、花旗、美国银行、巴克莱、德意志银行、野村。
- 标题里不要同时写中文机构名和英文缩写，禁止“摩根大通：JPM：……”“高盛：GS：……”这类重复；写“摩根大通：……”或“高盛：……”即可。
- 标题禁止出现 GS、JPM、JEF、NOM、BARC、MS、DB、Citi、Ticker、文件编号；如果原文只有英文机构名，请翻译为中文机构名。
- 标题冒号后不要重复机构或来源类型，禁止“联合国贸发会议：联合国贸发报告，……”“麦肯锡：麦肯锡报告称，……”这类写法；冒号后直接写判断或变量。
- 标题只能保留一层信息，不要把多个长分句全部塞进标题；如果原始标题有三段以上信息，只取最有传播性的主判断，其余放在正文第一段自然展开。
- 如果报告是单一公司/个股报告，标题和正文只能写公司情况、行业变化、业务进展、竞争格局和报告里的事实；禁止出现目标价、评级、买入、卖出、增持、减持、推荐、荐股、Buy、Sell、Overweight、Underweight、Outperform、Underperform、PT、TP、PO 等任何卖方操作口径。
- 标题可以用问句或对比句，但不要标题党到超出原报告证据。避免“震惊”“爆了”“彻底反转”“一夜变天”等廉价词。
- 标题不要晦涩抽象。少用“结构性分化”“二阶影响”“再定价框架”这类泛化词；如果必须使用，要落到一个具体对象。
- 机构名只要求出现在 `# 标题` 中，正文可以克制提及，不要为了重复机构名牺牲可读性。
- 禁止使用以下机械标题：
  - 一、核心判断
  - 二、真正重要的是结构性变量
  - 三、报告没有说透
  - 四、对读者的启发
  - 关键变化
  - 观察提示
  - 总结
- 所有 `##` 标题都要像麦肯锡报告里的 action title：读完标题就知道这一节结论。
- 小标题可以带序号，但序号后必须是一句洞察，例如：`## 1. 这轮变化真正考验的是企业能否把规模转化为议价权`。

【建议结构，但不要机械照抄标题】
1. `# 标题`：机构中文名或报告中的 big name + 一句主判断，20-35 个中文字符。
2. 开头 2-3 段：直接给出主判断、为什么现在重要、报告提供了什么新信号；自然带出 4-6 个长尾关键词，覆盖国家/行业/公司/政策/数据/技术词，但不要写成关键词堆砌。
3. 3-4 个 `##` 小节：每个小节标题都是洞察句，不是栏目名。
4. 在正文中穿插 1-2 个 `> **KC评论：** ...` 引用块，每个 1-2 句，用更平白的话解释“这张图/这个判断对读者意味着什么”，不要夹带任何推广话术。
5. 正文中间禁止插入 CTA、广告、扫码、社群、知识星球、每日汇编、喂给 AI 等表达；中间只允许出现分析正文、图表占位和 `KC评论`。
6. 禁止设置“该报告未解决的问题”“报告尚未回答”“研究留白”“开放问题”“报告局限”等独立小节；原报告明确写出的限制，只能在相关段落中用一句客观陈述带过。
7. 至少一个小节给出可复用的观察框架，但不要命名为“对读者的启发”。
8. 不要写任何 CTA、广告、扫码、社群、知识星球、网站、域名或关注引导；系统会在最结尾统一插入固定信息。
9. 在免责声明前，单独插入这张图片链接：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`
10. 结尾只输出英文灰色免责声明：`<p style="color:#999999;font-size:12px;">For informational purposes only. Portions may be generated, translated, summarized, or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment, legal, tax, accounting, or other professional advice.</p>`

【CTA 要求】
- 不要输出任何 CTA。不要写“加入社群”“扫码”“星球”“完整报告领取”“网站”“域名”“关注”“星标”“更多查看”等表达。
- 文末也不要写 CTA；系统会在最结尾统一插入固定信息。
- 正文中间不要出现“如果你从某些关键词搜到这里”“单篇文章只能解决一个切片”“我每天会把……”“这篇可以沿着……”这类表达。

【KC评论要求】
- `KC评论` 不是复述原文，而是读者友好的解释或提醒。
- 每条 `KC评论` 先说白话结论，再指出相关图表、假设或细分拆解中最容易被忽略的关系。
- 语气可以有判断力，但不要编造报告没有的数据或结论。
- `KC评论` 里禁止夹带 CTA，不要写扫码、社群、知识星球、每日汇编、喂给 AI、市场主线、完整报告领取等表达；它只能做解释、提醒或追问。

【人工编辑感要求】
- 段落不要像 AI 摘要清单。每段只推进一个意思，必要时用短句收住。
- 不要展开成完整长文。每个小节只保留最有信息量的一段，细节留给原文和图表。
- 避免连续使用同一种句式开头，避免连续三段都是“报告指出/这意味着/真正重要的是”。
- 不要机械重复标题、机构名或同一句判断。标题已经写过的内容，正文第一段要换一种说法展开。
- 保留一点自然语气，但不要口水化；像一个认真读过报告的人在做导读。

【图片要求】
- 不要主动生成 MinerU 图片 markdown；系统会在文章生成后自动插入 MinerU 原始图片。
- 但文末免责声明前必须保留知识星球图片：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`。

【内容边界】
- 只能基于研报原文和解析结果推导，不要编造数据、公司动作、引用。
- 遇到不确定内容，要用“这里仍需验证”“报告没有完全展开”等表达。
- 避免“震惊”“爆款”“一文看懂”等浮夸表达。
- 单公司报告不能写成交易提示；不要输出目标价、评级、买入、卖出、增持、减持、推荐、荐股、Buy、Sell、Overweight、Underweight、Outperform、Underperform、PT、TP、PO，也不要保留这些英文/中文卖方评级词。
- 不要出现小红书话题标签。
- 不要出现 emoji。
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份波士顿咨询研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
# Pressing the Throttle

# How India's Mining and Construction Equipment Industry can support domestic ambitions and become a global force

July 2026

Copyright © (2026) Confederation of Indian Industry (CII) and Boston Consulting Group (BCG). All rights reserved.

Without limiting the rights under the copyright reserved, this publication or any part of it may not be translated, reproduced, stored, transmitted in any form (electronic, mechanical, photocopying, audio recording or otherwise) or circulated in any binding or cover other than the cover in which it is currently published, without the prior written permission of CII and BCG.

All information, ideas, views, opinions, estimates, advice, suggestions, recommendations (hereinafter ‘content’) in this publication should not be understood as professional advice in any manner or interpreted as policies, objectives, opinions or suggestions of CII and BCG. Readers are advised to use their discretion and seek professional advice before taking any action or decision, based on the contents of this publication. The content in this publication has been obtained or derived from sources believed by CII and BCG to be reliable but CII and BCG do not represent this information to be accurate or complete. CII and BCG do not assume any responsibility and disclaim any liability for any loss, damages, caused due to any reason whatsoever, towards any person (natural or legal) who uses this publication.

This publication cannot be sold for consideration, within or outside India, without express written permission of CII and BCG. Violation of this condition of sale will lead to criminal and civil prosecution.

## Published by

\- Confederation of Indian Industry (CII), The Mantosh Sondhi Centre; 23, Institutional Area, Lodi Road, New Delhi 110003, India, Tel: +91-11-45771000; Email: info@cii.in; Web: www.cii.in; and

\- Boston Consulting Group, G2 (Ground Floor), 2, North Avenue, Maker Maxity, Bandra Kurla Complex, Mumbai 400051 India

For information or permission to reprint, please contact BCG at permissions@bcg.com. To find the latest BCG content and register to receive e-alerts on this topic or others, please visit bcg.com. Follow Boston Consulting Group on LinkedIn, Instagram, Facebook, and X.

© Boston Consulting Group 2026. All rights reserved. 7/26

![](images/76506174f4139539d156eddd2bfcb0343f6c0d2b691fad0a62acb56425c9fc08.jpg)

## Table of Contents

![](images/39a3ca79022497fd7a30efebf742663dcf7e83a338b5a3c1501235aab49de55a.jpg)

MCE Industry at a glance

Beyond India, MCE industry needs to think global

10-point agenda to unlock industry's potential

Executive Summary

![](images/1b93023ce85f9423d5166b20ddebb2556b857c1d001786b9fef7110b20388d84.jpg)

Strategic relevance of MCE industry in India's growth story

The trends re-shaping the industry

Acknowledgement,
Authors and References

The next phase of growth will depend on deeper collaboration between industry, government, financial institutions, technology providers, academia, and end users. Creating an enabling environment for investment, accelerating innovation, supporting skill development, and improving ease of doing business will be critical to building a sector that is resilient, future-ready, and globally benchmarked.

## Chandrajit Banerjee

Director General,
Confederation of Indian Industry (CII)

India's growth trajectory over the coming decade will be shaped by its ability to expand infrastructure capacity, strengthen industrial competitiveness, secure critical mineral resources, and build resilient supply chains. The Mining and Construction Equipment (MCE) sector occupies a strategic position in this growth agenda, with its performance increasingly influencing the pace of infrastructure creation, industrial expansion, and economic development.

The sector today stands at an important stage of evolution. Rising public and private investments, increasing project complexity, greater expectations around productivity, and changing operating conditions are creating demand for more advanced equipment, higher efficiency, and stronger service capabilities. At the same time, digital technologies, automation, data-led operations, predictive maintenance, and sustainability considerations are reshaping how equipment is designed, manufactured, deployed, and managed across its lifecycle.

Within a decade, MCE has gone from a small, import-led market to a genuine global growth platform, with India now emerging as a net exporter of MCE equipment. This demonstrates the growing prowess of the Indian manufacturing sector.

![](images/cd5136510cc1e0a2b28c711bb6853d50c3c0f53dbb3fe5579f0debba3f099a59.jpg)

The next phase of growth will depend on deeper collaboration between industry, government, financial institutions, technology providers, academia, and end users. Creating an enabling environment for investment, accelerating innovation, supporting skill development, and improving ease of doing business will be critical to building a sector that is resilient, future-ready, and globally benchmarked.

This report, prepared in association with BCG, brings together perspectives from industry leaders and stakeholders across the MCE ecosystem. It examines emerging market shifts, growth opportunities, structural challenges, and strategic priorities that will influence the sector in the years ahead. It also presents a forward-looking agenda to support India's ambition of creating a globally competitive and future-ready MCE ecosystem.

I hope this publication contributes to informed dialogue and encourages collective action from all stakeholders. As India enters a new phase of economic expansion, the MCE sector can move beyond supporting growth to actively shaping it. The choices made today in technology, manufacturing, sustainability, skills, and collaboration will determine the sector's contribution to India's next chapter of development.

Not long ago, the best machines on Indian sites came from elsewhere. Today, our equipment works in close to 100+ countries. That tells you what this industry can do.

## Vivek Bhatia

## Chairman, CII Mining and Construction Equipment Division and Managing Director & CEO TKIL Industries

I have spent my working life around this industry, and the change has been something to see. Not long ago, the most capable machines on an Indian site came from other parts of the world. Today, our factories are increasingly building equipment that holds its own on quality, and Indian machines work in close to 100 countries. That did not happen by accident, and it tells you what this sector is capable of, when industry and the country pull in the same direction.

CII's Mining and Construction Equipment Division commissioned this report to look further out than the next quarter or year. The questions that matter are long-horizon ones. How quickly can we build real capability in underground mining and the larger, technology-led machines where India is still dependent on imports? How well can we train the skilled operators and service technicians, that safe, productive sites depend on? How do we build the after-sales and financing

![](images/d7dbd88d21448cdce47ff613cfa203427d63a8dd4c5a20324ba2b4f8e5012788.jpg)

ecosystems that decide whether a customer buys Indian machines a second time, and makes the MCE equipment more accessible to larger customer base? And, How do we enable relentless focus on cost and quality, so that our machines are more and more competitive globally? These are the things that will determine where the industry sits a decade from now.

Government has been an important partner in the progress so far, and a continued enabling environment - on the duty structure, on focused support for equipment manufacturing, and on the export ecosystem, would help the sector realize its full potential. I am grateful to every leader who shared their perspective, and to our partners at BCG. The long-term opportunity is real, and well within our reach if we keep building it together.

For years, India's story in the MCE industry was about catching up. Today it is a sunrise sector, helping to power India's infrastructure and growth story as the country builds towards the vision of Viksit Bharat. As the industry reinvents itself through cleaner fuels, autonomous vehicles and connected fleet ecosystems, the question is no longer whether India can keep pace, but how far it can lead.

## Abhishek Bhatia

Managing Director and Partner, Boston Consulting Group

Once in a while an industry rewrites the rules of who comes out ahead, and mining and construction equipment is at that point now. India has spent years catching up. What lies ahead is the chance to lead.

The pull at home is strong and lasting, simply because so much of India is still to be built, and every phase of that build runs on this equipment. But, the industry is being reinvented as we speak, in terms of how machines are powered, how they run, how they talk to each other, and how they are paid for. Engines are giving way to cleaner and electric powertrains. Machines that once depended entirely on an operator are starting to run with far more autonomy. Sensors and connectivity are turning a fleet into a stream of data that tells an owner what will fail before it does, and ownership itself is shifting from buying the equipment to paying for uptime and output. Taken together, these changes are turning hardware into something much closer to a connected, intelligent system. The firms that treat this as the core of the product, not a feature added later, will be the ones that set the pace.

![](images/2243a3b60a10f8a2c9c7855eef23b002a1b5637d95ec624e26152850d2899327.jpg)

For Indian players this is a real opportunity. We have worked alongside industrial leaders through transitions of this kind across the world, and the pattern holds: the ones who do well start early. It has been a privilege to work with CII's MCED on this report. I hope it informs, and I also hope it prompts a few conversations, ours included, about how India makes the most of a moment like this.

## Executive Summary

India's Mining and Construction Equipment (MCE) industry is entering a decisive decade. The sector sits at the centre of the country's infrastructure expansion. Roads, railways, ports, airports, mines, factories, logistics networks, and power systems being developed all depend on the machines that move earth, lift loads, drill, crush, and pave at scale. The global MCE industry is worth about USD 420-440 billion, with Asia-Pacific accounting for \~55% of it. Within that landscape India has become one of the fastest growing major markets, with domestic demand exceeding USD 17 billion in 2025.

India's rise has been built on four structural drivers. First, sustained infrastructure investment has widened the need for earthmoving, concrete, lifting, tunnelling, roadbuilding, and material-handling equipment. Second, mining growth and mineral-security priorities are pulling in more advanced equipment across coal, metals, and critical minerals. Third, deeper localisation by domestic and global OEMs is strengthening the country's manufacturing base. Fourth, exports have become a real part of the story, having nearly tripled over the past decade to \~USD 4.9 billion in 2025 and India becoming a net exporter of mining and construction equipment.

North America, the EU, Australia and the UK are a longer-term opportunity, as they will require higher-specification products, stronger compliance and more reliable overseas after-market service networks. By 2047, India could aspire to capture at least 20% of the global export market - an opportunity of USD 75+ billion.

The equipment itself is changing at the same time. The report examines six shifts remaking the industry worldwide, from cleaner powertrains and connected digital fleets to autonomy, deeper underground mining, mechanisation of mining operations, and new ways of owning and financing machines. Keeping pace through this transition is now essential for Indian OEMs to compete at a global level.

The way forward calls for a coordinated effort between government and industry. This report sets out a ten-point framework covering the policy and regulatory actions for government's consideration, the commitments industry must make to amplify these initiatives, and the priority areas where both need to act together.

Government can promote Make in India through a tiered duty structure, firm action against dumping practices, and stronger public procurement preference for domestically built machines, including domestic capability in critical-mineral processing equipment. It could also consider strengthening site safety through a purpose-built fleet scrappage and renewal mechanism, tighter enforcement against counterfeit aftermarket parts, and a single empowered nodal agency for the sector. Industry must build on this with its own commitments. OEMs should deepen Tier-2 supplier ecosystems and clusters, make bolder export moves through overseas subsidiaries, distribution, and after-sales networks in priority geographies, and design products for the needs of export markets. They must also bring the best available technologies to Indian mining and construction sites, helping move the sector up the automation and mechanisation curve. Alongside these actions, government and industry can jointly work on the sector's shared priorities. This includes scaling R&D and innovation centres, supported by academia partnerships and closer work with end-users. The sector can also benefit from MCE-specific operator and technician certification through upgraded ITIs run on a government-owned and industry-managed model. Finally, while industry should invest in connected, automated, and higher efficiency equipment, it could be matched by demand through mandated adoption in public tenders and large PSU contracts.

![](images/30b5b6e0b27376f25b27aaf518c3f6c7589101dc4046237ff465a7a378ee350f.jpg)

# MCE industry at a glance

The global Mining and Construction Equipment industry serves the large mining and construction sector, valued at over USD 18 trillion in 2025, around 15% of global GDP $^{1}$ . The equipment industry that enables this activity is worth roughly USD 420-440 billion $^{2,4}$ , expected to grow at 4-5% CAGR $^{2,4}$ over the next five years.

# Center of gravity continues to be Asia Pacific

The developed markets of North America and Europe are expected to grow at a relatively modest 2-3% CAGR over the next five years, while the Asia-Pacific region is expanding at 6-7% $^{2}$ CAGR, on the back of sustained infrastructure creation, rapid urbanization, wider mining activity, and the localisation of manufacturing. Asia Pacific remains the largest demand centre for MCE, at an estimated size of USD 230-240 billion in 2025 - roughly 55% of global demand $^{4}$ . The story of the global industry over the coming decade will be largely the story of Asia.

Within Asia, India is one of the fastest-growing major markets. At approximately USD 17 billion, domestic demand is expanding at $10 - 12\%$ a year $^{3}$ - among the most dynamic growth rates anywhere in the region. China remains substantially larger, at an estimated USD 140-150 billion $^{4}$ , but it is a more mature market and is growing more slowly. India's mix of scale and pace is what makes it increasingly central to global OEMs' investment, localisation, and export strategies: a market that matters not only for what it is today, but for what it is rapidly becoming.

India's share continues to grow in global MCE industry  
![](images/e00c96ee51f79dba6bb08ab9e36bb5e24bb69d930d833604c1e885e30ea0705e.jpg)  
Source: BCG Analysis

## India today - from marginal player to fast-growing global force

Over the past decade, India's MCE sector has transitioned from a small, import dependent market to a meaningful global growth platform. The shift rests on the sheer scale of India's infrastructure and mining economy, steadily rising mechanisation, and a deepening base of localized manufacturing. India's share of global MCE industry size has doubled - from around $2.5\%$ to $4\%$ today - and is expected to rise further to about $6.5\%$ over the next five years $^{4}$ , placing it among the world's fastest-growing major markets.

This growth sits on a large underlying economy. India's mining and construction output is estimated at around USD 430 billion in 2025, close to $11\%$ of $\mathrm{GDP}^5$ , and supports the livelihoods of more than 70 million people across the value chain. The equipment sector that serves it has reached meaningful scale: USD $17+$ billion in 2025, comprising around USD 10-10.5 billion of construction equipment and USD 6.5-7 billion of mining equipment, having added USD $1+$ billion of output over the past year.

## 4 structural drivers have enabled growth, and continue to shape it

India's growth until now has been enabled by 4 key pillars, and will continue to shape how the sector progresses over the coming years.

## 1. Sustained infrastructure investment

Public investment over the past decade has been across the full span of India's infrastructure, from roads and rails to airports and ports. The national-highway network expanded from 91,287 km in 2014 to about 1,46,300 km in $2025^{6}$ ; metro-rail grew roughly fourfold, from 248 km across five cities to over 1,000 km across 23 cities; and operational airports more than doubled, from 74 to about 160, widened by the UDAN scheme. India has also commissioned major new megaprojects: the Dedicated Freight Corridors now carrying 400+ freight trains a day, its first High-Speed Rail corridor, and deep-draft ports such as Vadhavan and a new build at Great Nicobar. Each expands demand for earthmoving, concrete, lifting, tunnelling, and material-handling equipment.

## 2. Mining growth under-pinned by rising downstream industries demand

A sharper focus on mineral security, backed by successive MMDR Act amendments $^{10}$ that opened restricted minerals to private exploration and eased auctions, has lifted demand for advanced equipment across coal, metals, and an emerging critical-minerals agenda. Iron ore production rose from 155 MT to 300 MT, limestone increased from 320 MT to 450 MT whereas coal production alone rose from 609 MT to 1,000 MT over the decade and the frontier now extends to drilling, excavation, hauling, and underground systems India once imported.

This mineral growth is ultimately driven by rising downstream consumption, in industries such as steel, cement, and power. As India continues to build out its infrastructure and industrial base, demand from these downstream sectors will kee

[中间内容因长度限制已省略]

mation Bureau), 2026

SECL's DigiCOAL Showcased at Central Vigilance Commission's National Workshop

## - Caterpillar, 2026

Caterpillar teams with Geotab to strengthen full fleet offering

## - CEEW (Council on Energy, Environment and Water), 2026

Assessing India's Coal Mine Workers: Skills, Preferences, and Future Opportunities

## - NPR, 2026

Deadliest coal mine explosion in China in years kills at least 82 people

## • IMARC Group, 2026

India Construction Equipment Market Size, Share, Trends and Forecast, 2026-2034

## • Ministry of Defence, Government of India (Press

Information Bureau), 2025
Defence Atmanirbharta: Record Production and Exports

## - Niveshaay, 2025

India's Defence Sector: From Dependent to Dominant

## - The State Council of the People's Republic of China, 2024

China promotes large-scale equipment upgrades, trade-in of consumer goods to open up trillion-yuan market

## • Autocar Professional, 2023

Construction Equipment manufacturers seeks unified emission norms for all machines

## • Manufacturing Today India, 2024

Transforming India's Construction: SANY India's journey and innovations

## • Business Standard, 2026

West Asia war impact: Domestic sales of construction equipment fall 6.7%

## • Equipment Times, 2025

India's Construction Equipment Industry – Powering infrastructure growth and employment generation

\- Ministry of New and Renewable Energy, Government of India (Press Information Bureau), 2026
India Ranks Third Globally in Renewable Energy Installed Capacity

\- Sandvik Underground & Surface Mining Equipment & Technology
(NBM&CW interview)

## - Sandvik, 2013

All Eyes on India

## - Sandvik, Made in India

Surface Drills

## - NBM & CW

Sandvik Inaugurates New Tunnelling Jumbo Drill Manufacturing Facility in Pune

## - Tracxn. 2026,

Sandvik Mining and Rock Technology India Private Limited Company Profile & Financials

## - BEML India

Indigenisation

\- DCFmodeling, 2026, BEML (BEMLNS): History, Ownership, Mission

## • The Machine Maker, 2024

BEML Secures INR 246.78 Crore Order from CCL for Mining Trucks

## - Elets eGov. 2026

BEML Unveils India's First 35-Ton Electric Dump Truck

## • Construction World, 2026

BEML Launches 35-Tonne Electric Dump Truck for Green Mining

## Notes

![](images/14a8dde095d00e3b8536b16460ee46bae8aee3408537d3cf236ff3fc3d102587.jpg)

The Confederation of Indian Industry (CII) works to create and sustain an environment conducive to the development of India, partnering Industry, Government and civil society through advisory and consultative processes.

CII is a non-government, not-for-profit, industry-led and industry-managed organisation, with over 10,500 members from the private as well as public sectors, including SMEs and MNCs, and an indirect membership of over 365,000 enterprises from 332 national and regional sectoral industry bodies.

For more than 130 years, CII has been engaged in shaping India's development journey and works proactively on transforming Indian Industry's engagement in national development. CII charts change by working closely with the Government on policy issues, interfacing with thought leaders, and enhancing efficiency, competitiveness, and business opportunities for industry through a range of specialised services and strategic global linkages. It also provides a platform for consensus-building and networking on key issues.

Through its dedicated Centres of Excellence and Industry competitiveness initiatives, promotion of innovation and technology adoption, and partnerships for sustainability, CII plays a transformative part in shaping the future of the nation. Extending its agenda beyond business, CII assists industry to identify and execute corporate citizenship programmes across diverse domains, including affirmative action, livelihoods, diversity management, skill development, empowerment of women, and sustainable development, to name a few.

For 2026-27, CII has identified “Accelerating Competitiveness: Growth, Resilience, Inclusion, Sustainability, and Trust” as its theme, prioritising five key pillars. During the year, CII will align its policy advocacy, institutional initiatives, partnerships, and outreach to support Indian industry in strengthening these five interconnected pillars of competitiveness.

With 70 offices, including 12 Centres of Excellence, in India, and 9 overseas offices in Australia, Egypt, Germany, Indonesia, Singapore, UAE, UK, and USA, as well as institutional partnerships with 255 counterpart organisations in 102 countries, CII serves as a reference point for Indian industry and the international business community.

Confederation of Indian Industry
The Mantosh Sondhi Centre
23, Institutional Area, Lodi Road, New Delhi – 110 003 (India)
T: 91 11 45771000 | E: info@cii.in | W: www.cii.in

Follow us on:

![](images/e5b8b8115524644c2f8b31926c6d2eac547d6990758eb2387f355e479b10567a.jpg)

Reach us via CII Membership Helpline: 1800-103-1244

## Where Strategic Clarity Meets Applied AI

We are navigating an era of unprecedented change and disruption—powered by technology, marked by complexity, where change amplifies at scale. To lead, companies need a partner that can bridge the gap between ambition and outcomes. BCG is built for this moment. We bring strategic clarity, rooted in over 60 years of deep domain knowledge, to ensure leaders make the right choices. We combine it with applied AI, shaped and wielded by our practitioners, teaming shoulder-to-shoulder with your teams to deliver transformative impact at scale. The result? Stronger returns, transferred capabilities, and change that sticks. We are BCG.

![](images/214f6b6daabca82557c13d82992e5c05f009058afa661555c5a68ee40ac7d84e.jpg)
"""

【DeepSeek 交稿硬约束】
1. 全文只服务一个主判断。不要按原报告目录逐段摘要，也不要把多个结论平铺成清单。
2. 开头直接使用原文中最有辨识度的事实、数字、对比或矛盾切入；禁止用“在……背景下”“随着……”“近年来……”空泛起笔。
3. 正文至少使用三个原文锚点：一个可核验的数字或日期、一个具体主体/项目/制度名、一个比较或因果关系。判断必须紧挨证据，保留“可能、样本显示、报告认为”等限定词。
4. 句子长短要自然变化。大多数段落写 2-4 句，允许用一句短句收住；不要连续使用“报告指出、这意味着、换句话说、真正重要的是、值得注意的是”等模板转折。
5. KC评论只写一条具体、平白的解释或提醒，不能复述正文，不能提推广、原文领取、完整报告、读者行动或网站。
6. 禁止单独设置“该报告未解决的问题、报告尚未回答、研究留白、开放问题、报告局限、还需追问”等小节，也禁止用问句收尾。若原报告明确写了限制，只能在相关正文中用一句客观陈述自然带过。
7. 最后一段必须仍是实质内容或 KC评论。不要添加总结、结语、延伸阅读、继续阅读、关注引导、社群、扫码、网站或任何 CTA；系统会统一处理文末固定信息。
8. 不要虚构“我读完后”“我们采访了”等个人经历，不要故意口语化或加入情绪。人工编辑感来自具体证据、准确取舍和自然节奏。
9. 输出前自行核对：标题与导语不重复；每个小标题都是完整判断；没有元话语、推广语和未解问题栏目。只输出最终 Markdown，不输出核对过程。
