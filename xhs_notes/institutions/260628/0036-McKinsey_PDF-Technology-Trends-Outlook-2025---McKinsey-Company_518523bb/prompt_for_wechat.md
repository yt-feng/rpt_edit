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
- 已识别机构名：`麦肯锡`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如高盛、摩根士丹利、汇丰、摩根大通、瑞银、花旗、美国银行、巴克莱、德意志银行、野村。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份麦肯锡研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
# Technology Trends Outlook 2025

July 2025
Fifth edition

# Which frontier technologies matter most for companies in 2025? Our annual tech trends report highlights the latest technology breakthroughs, talent trends, use cases, and their potential impact on companies across sectors.

by Lareina Yee, Michael Chui, Roger Roberts, and Sven Smit

## Contents

## Introduction

![](images/79825a6022a699554f38594049852df8509615bf2b095d505d01f3fa507de835.jpg)

AI revolution 10
01 Agentic AI 11
02 Artificial intelligence 18

![](images/6236d6e142c66cedcb5d7f58871a1956fd99f8f5c177a723338c66ca086921a9.jpg)

Compute and connectivity frontiers 26
03 Application-specific semiconductors 27
04 Advanced connectivity 34
05 Cloud and edge computing 41
06 Immersive-reality technologies 48
07 Digital trust and cybersecurity 55
08 Quantum technologies 63

![](images/18ddba2c30ab01cd9fcb7805cf6f86d19292aa669de7d791ea084c171481900f.jpg)

Cutting-edge engineering 69
09 Future of robotics 70
10 Future of mobility 76
11 Future of bioengineering 83
12 Future of space technologies 90
13 Future of energy and sustainability technologies 97

## Introduction

The global technology landscape is undergoing significant shifts, propelled by fast-moving innovations in technologies. These are exponentially increasing demand for computing power, capturing the attention of management teams and the public, and accelerating experimentation. These developments are occurring against a backdrop of rising global competition as countries and corporations race to secure leadership in producing and applying these strategic technologies.

This year's McKinsey Technology Trends Outlook provides in-depth perspectives on 13—a “baker’s dozen”—frontier technology trends with the potential to transform global business. Executives today face a mandate to navigate rising complexity, scale emerging solutions, and build trust in a world where the lines between digital and physical and centralized and decentralized continue to blur. The insights in this report can help business leaders decide which of these frontier technologies are most relevant to their companies by demonstrating how others are starting to apply them today. These findings emerge from our analysis of quantitative measures of interest, innovation, equity investment, and talent that underpin each of the 13 trends and explore the underlying technologies, uncertainties, and questions around them. (For more about our research, please see the sidebar, “Research methodology.”)

This outlook highlights transformative trends that are driving innovation and addressing critical challenges across sectors. Artificial intelligence stands out not only as a powerful technology wave on its own but also as a foundational amplifier of the other trends. Its impact increasingly occurs via a combination with other trends, as AI both accelerates progress within individual domains and unlocks new possibilities at the intersections—accelerating the training of robots, advancing scientific discoveries in bioengineering, optimizing energy systems, and much more. The evolution of AI solutions in the marketplace increasingly combines

## About the McKinsey Global Institute

## McKinsey Global Institute

This annual report is developed by the McKinsey Global Institute (MGI) to further our understanding of how science and technology can advance economic productivity and innovation. We work together with McKinsey's Technology, Media & Telecommunications Practice; QuantumBlack, AI by McKinsey; and McKinsey Technology to provide insight on how companies are applying these new technologies to transform their businesses.

MGI was established in 1990. Our mission is to provide a fact base to aid decision-making on the economic and business issues most critical to the world's companies and policy leaders.

We benefit from the full range of McKinsey's regional, sectoral, and functional knowledge, skills, and expertise, but editorial direction and decisions are solely the responsibility of MGI directors and partners. We aim for independent and fact-based research and analysis. None of our work is commissioned or funded by any business, government, or other institution; we share our results publicly free of charge; and we are entirely funded by the partners of McKinsey. For further information about MGI and to download all reports for free, please visit McKinsey.com/mgi.

\$1.1

billion
equity investment
in agentic AI, 2024

+985%

difference in postings for jobs in agentic AI, 2023–24 aspects of trends we previously analyzed separately as applied AI and generative AI, so this year, they are examined together.

Even as excitement about AI applications and their use cases builds, realizing AI's full potential across sectors will require continued innovations to manage computing intensity, reduce deployment costs, and drive infrastructure investment. This will also demand thoughtful approaches to safety, governance, and workforce adaptation, creating a wide range of opportunities for industry leaders, policymakers, and entrepreneurs alike.

## New and notable

In addition to the growing reach of AI, another new trend we have chosen to highlight in this year's report is agentic AI, which has rapidly emerged as a major focus of interest and experimentation in enterprise and consumer technology. Agentic AI combines the flexibility and generality of AI foundation models with the ability to act in the world by creating “virtual coworkers” that can autonomously plan and execute multistep workflows. Although quantitative measures of interest and equity investment levels are as yet relatively low compared with more established trends, agentic AI is among the fastest growing of this year’s trends, signaling its potentially revolutionary possibilities.

AI is also the primary catalyst for another trend we highlight this year: application-specific semiconductors. While Moore's Law and the semiconductor layer of the technology stack have long been key enablers of other tech trends, innovations in semiconductors have spiked as reflected in quantitative metrics such as number of patents. These innovations have come in response to exponentially higher demands for computing capacity, memory, and networking for AI training and inference, as well as a need to manage cost, heat, and electric power

consumption. This has given rise to a slew of new products, new competitors, and new ecosystems.

Technology trends also have a variety of profiles along the dimensions we analyzed. AI is a widely applicable, general-purpose technology with use cases in every industry and business function—and thus lots of innovation and interest—and it is scaling rapidly across the business landscape. Quantum technologies have a different profile. Quantum computing has the potential for transformative impact in certain critical domains, such as cryptography and material science, and the basic technology continues to be developed. Recent announcements, particularly by technology giants, have sparked increased interest, but real-world business impact will require even more technology advancements to make quantum computing practical. Other trends and subtrends vary across the multiple dimensions we analyzed, offering different approaches—from watchful waiting to aggressive deployment—to business leaders depending on their industries and competitive positions.

From the rise of robotics and autonomous systems to the imperative for responsible AI innovations, this year's technology developments underscore a future where technology is more adaptive, collaborative, and integral to solving global problems. This is illuminated by themes that cut across trends this year:

— The rise of autonomous systems. Autonomous systems, including physical robots and digital agents, are moving from pilot projects to practical applications. These systems aren't just executing tasks; they're starting to learn, adapt, and collaborate. Autonomy is moving toward broad deployment, whether through coordinating last-mile logistics, navigating dynamic environments, or acting as virtual coworkers, among other skills.

\- New human–machine collaboration models. Human–machine interaction is entering a new phase defined by more natural interfaces, multimodal inputs, and adaptive intelligence. From immersive training environments and haptic robotics to voice-driven copilots and sensor-enabled wearables, technology is becoming more responsive to human intent and behavior. This evolution is shifting the narrative from human replacement to augmentation—enabling more natural, productive collaboration between people and intelligent systems. As machines get better at interpreting context, the boundary between operator and cocreator continues to dissolve.

\- Scaling challenges. The surging demand for compute-intensive workloads, especially from gen AI, robotics, and immersive environments, is creating new demands on global infrastructure. Data center power constraints, physical network vulnerabilities, and rising compute demands have exposed cracks in global infrastructure. But the challenge isn't just technical: Supply chain delays, labor shortages, and regulatory friction around grid access and permitting are slowing deployments. As a result, scaling now means solving not only for technical architecture and efficient design but also for the messy, real-world challenges in talent, policy, and execution.

\- Regional and national competition. Global competition over critical technologies has intensified. Countries and corporations have doubled down on sovereign infrastructure, localized chip fabrication, and funding technology initiatives such as quantum labs. This push for self-sufficiency isn't just about security;

it's about reducing exposure to geopolitical risk and owning the next wave of value creation. The result is a new era of tech-driven competition where nations have a stake in critical industries.

## — Scale and specialization are growing

simultaneously. Growth on these vectors is enabled by innovation in cloud services and advanced connectivity. On one hand, we see rapid growth in general-purpose model training infrastructure in vast, power-hungry data centers, while on the other, we observe accelerating innovation “at the edge,” with lower-power technology embedded in phones, cars, home controls, and industrial devices. This is creating ecosystems that deliver massive large language models with staggering parameter counts, as well as a growing range of domain-specific AI tools that can run almost anywhere. Leaders will balance centralized scale with localized control: Think modular microgrids for clean energy or bespoke robotics for niche manufacturing.

## — Responsible innovation imperatives. As

technologies become more powerful and more personal, trust is increasingly the gatekeeper to adoption. Companies face growing pressure to demonstrate transparency, fairness, and accountability, whether in AI models, gene editing pipelines, or immersive platforms. Ethics are no longer just the right thing to do but rather strategic levers in deployment that can accelerate—or stall—scaling, investment, and long-term impact.

The following illustrations show how different frontier technologies can work together to provide innovative solutions in the future:

Three examples illustrate the combinatorial power of technology trends.

## Factory machine repair

Artificial intelligence
AI model utilizes advanced pattern recognition to diagnose issues

Agentic AI
AI agents autonomously create repair plans, oversee quality checks, and order parts for repairs

![](images/f2029c7cbb3d18f988d9810661e9d4167b36a5edf22c67e54dbb831c90a6d12d.jpg)

Robotics
Robotic arms autonomously perform mechanical repairs

## Personalized medicine delivery

Biometric blockchain technology establishes an immutable chain of custody for each required medication

Bioengineering
Doctors create personalized treatments (eg, turning a tumor biopsy into targeted antibodies that directly attack and eliminate cancer cells)

Future of mobility
Autonomous drones deliver critical medications to the most remote or underserved areas

![](images/2083f7af12afb889d72c1b505dba31225d0af0ce18b53a8b0e637aad32195804.jpg)

## Wind farm maintenance crew

Energy and sustainability
Wind farms need to maintain peak efficiency year-round, maximizing clean-energy output while minimizing downtime and operational costs

Immersive reality
Technicians use augmented reality goggles that provide visual guidance to help them maintain and repair complex turbine systems safely

![](images/5931e253a061242ae789b66ae125aa8901d7eb679396032a6f5b8b7050edb72f.jpg)

Advanced connectivity
Low-Earth-orbit satellites provide technicians with access to real-time data and cloud-based diagnostic tools from remote locations

![](images/b30d6b1b8f5a0d0e26e96c6658572472321b1b6cf81b1cfc9cebd205177883e9.jpg)

After a year in which the macroeconomic environment and broader market weakness provoked significant declines in equity financing for technology across several of our trends, the investment climate for frontier technologies stabilized and, in many cases, rebounded in 2024. Levels of equity investment in trends such as cloud and edge computing, bioengineering, and space technologies increased despite the broader market dip in 2023, while investments in other trends, such as AI and robotics, dipped only to recover to higher levels in 2024 than they achieved two years prior. The two trends with the highest levels of equity investment, the future of energy and sustainability technologies and the future of mobility, declined overall in 2023, but the former bounced back in 2024 (Exhibit 1).

Our baker's dozen of technology trends shaping 2025 underscores the vast potential of emerging technologies and the need for strategic alignment in an AI-powered future.

## Exhibit 1

Equity investments increased in ten of 13 technology trends in 2024.

Trend investments, 2022–24, \$ billion

\- AI revolution
- Compute and connectivity frontiers
- Cutting-edge engineering
○ 2022–24 cumulative change, %

![](images/9a7a31310f1973ee03f13142faee86a26a69f78e08c1c0c1588be47c78e2e364.jpg)

![](images/2d931e49871dc6367b0230f7ebfd64c8a08248e071abb44a6350ac656ac8fa2a.jpg)

![](images/1edb8843f7ce10591ff7718ebd0a1f054ab3462036cd56786f1d8d64d19333b3.jpg)

McKinsey & Company

![](images/135b26963c8c0cd47029657cc05bb29fe0037f905469738a1883f657451c9b2b.jpg)  
Note: Data includes private-market and public-market capital raises across venture capital and corporate and strategic M&A (including joint ventures), private equity investments (including buyouts and private investment in public equity), and public investments (including IPOs). Excludes corporate capital and operational expenditures.
Source: PitchBook; McKinsey analysis

For executives, success will hinge on identifying high-impact domains in which they can apply these trends, investing in the necessary talent and infrastructure, and addressing external factors like regulatory shifts and ecosystem readiness. By fostering collaboration, bridging ecosystem gaps, and maintaining a long-term vision, leaders can accelerate adoption and position their organizations to drive the next wave of technological transformation. Those who act with focus and agility will not only unlock new value but also shape the future of their industries and the future of today's emerging frontier technologies.

## The 13 tech trends

## Exhibit 2

This report lays out considerations for all 13 technology trends. For easier consideration of related trends, we grouped them into three broader categories: the AI revolution, compute and connectivity frontiers, and cutting-edge engineering. Of course, there's significant power and potential in looking across these groupings when considering trend combinations.

To describe the state of each trend, we developed scores for innovation (based on patents and research publications) and interest (based on news and web searches). We also estimated the level of equity investments in relevant technologies and rated their level of adoption by organizations (Exhibit 2).

Each trend is scored based on its level of innovation, interest, equity investment, and adoption.

Innovation, interest, investment, and adoption, by technology trend, 2024

![](images/dc847e369e7d150a35d73460d76bc02f8a580cd9a0ea8d5d00bc7c74ca15cbcd.jpg)  
Note: Innovation and interest scores for the 13 trends are relative to one another. All 13 trends exhibit high levels of innovation and interest compared with other topics and are also attracting significant investment.  
$^{1}$ The innovation score combines the 0–1 scores for patents and research, which are relative to the trends studied. The patents score is based on a measure of patent filings, and the research score is based on a measure of research publications.

## Research methodology

To assess the development of each of the 13 technology trends highlighted in this report, we collected data on six tangible measures of activity: search engine queries, news articles, patents, research publications, equity investment, and talent demand. For each measure or vector, we used a defined set of data sources to find occurrences of keywords associated with each of the trends, screened those occurrences for valid mentions of activity, and indexed the resulting numbers of mentions on a 0–1 scoring scale relative to the trends studied. The innovation score combines the patents and research scores; the interest score combines the news and search scores. (While we recognize that an interest score can be inflated by deliberate efforts to stimulate news and search activity, we believe that each score fairly reflects the extent of discussion and debate about a given trend.) Investment measures the flows of funding from the capital markets

to companies linked with the trend. Data sources for the scores include the following:

— Patents. Data on patent filings are sourced from Google Patents, which highlights data on the number of patents granted.

— Research. Data on research publications are sourced from The Lens.

— News. Data on news articles are sourced from Factiva.

— Searches. Data on search engine queries are sourced from Google Trends.

\- Equity investment. Data on private-market and public-market capital raises across venture capital and corporate and strategic M&A, including joint ventures; private equity investments, including buyouts and private investment in public equity; and public investments, including IPOs, are sourced from PitchBook. Investment data excludes corporate capital and operational 

[中间内容因长度限制已省略]

transfer heat from one location to another, reducing energy consumption in buildings.

— Smart-grid technologies. Advanced electrical-grid systems optimize energy distribution, enable integration of distributed energy resources, and incorporate demand-side flexibility solutions to balance supply and consumption patterns.

— Measurement, reporting, and verification (MRV) systems. These tools and processes accurately quantify and track emissions and removals, ensuring the effectiveness of climate mitigation efforts.

— Energy-efficiency technologies. This set of technologies comprises technologies and practices that reduce energy consumption while maintaining or improving the level of service provided. Examples include high-efficiency appliances, improved insulation, smart systems for building management, and optimized industrial processes.

— Carbon capture or direct air capture (DAC). These technologies are designed to capture $CO_{2}$ emissions either from point sources (for example, power plants or industrial facilities) or directly from the ambient air. The captured $CO_{2}$ can then be stored permanently underground or used in various industrial processes.

— Long-duration storage. These energy storage technologies can store energy for extended periods (ranging from several hours to days or even weeks), addressing the variability of renewable-energy sources and ensuring grid reliability. Examples include advanced batteries, pumped hydro storage, compressed air energy storage, and hydrogen storage.

— Thermal energy storage. These technologies store energy in the form of heat or cold for later use. This can include storing heat from solar thermal collectors, industrial-waste heat, or excess electricity for heating or cooling applications.

— Adaptation solutions. These are measures taken to adjust to the actual or expected effects of climate change. Adaptation encompasses a wide range of actions, from building more resilient infrastructure and developing drought-resistant crops to implementing early-warning systems for extreme weather events and managing coastal retreat.

## Key uncertainties

The major uncertainties affecting energy and sustainability technologies include the following:

— Grid resilience and flexibility. The ability of power grids to handle increasing amounts of variable renewable energy while maintaining stability and reliability is a major uncertainty in the energy transition.

![](images/0b917842515fa4112d8d1117b389fcacbe21f9a237fad6f9490bcc46147954ee.jpg)

## ‘Decarbonizing hard-to-abate sectors requires more than engineering breakthroughs. It demands coordinated action across industries, governments, and communities to ensure that innovation is accessible, affordable, and resilient in the face of global uncertainties.’

— Sebastian Mayer, partner, Munich

— Infrastructure development. The scale of infrastructure upgrades required for the energy transition, including transmission lines, charging stations, and hydrogen pipelines, is vast and faces potential delays and funding challenges.

— Supply chain and resource constraints. The availability and sustainable sourcing of critical materials for clean-energy technologies, such as rare earth elements and lithium, could limit the speed of deployment.

— Market dynamics. The interplay between traditional and emerging energy markets, including the future role of fossil fuels and the competitiveness of renewable-energy sources, remains a key area of uncertainty.

\- Pace of innovation and cost reductions. The speed at which technologies such as green hydrogen electrolyzers, advanced batteries, and synthetic fuels improve cost and performance (for example, achieve cost parity with fossil fuel alternatives) remains uncertain, which affects their scalability and adoption in hard-to-abate sectors.

— Systemic market and regulatory evolution. The ability of electricity market designs and regulatory frameworks to rapidly adapt and incentivize flexibility, resilience, and low-emission investments is uncertain, posing risks to grid stability and affordability.

— Labor and talent availability. The capacity to scale workforce development and training programs to close acute talent shortages in clean energy, sustainability, and digital skills essential for energy transition technologies is uncertain, risking project delays and innovation bottlenecks.

— Macroeconomic impacts on investment. Inflation, rising interest rates, and global trade disruptions create uncertainty about financing costs and investment flows for large-scale clean-energy projects.

## Big questions about the future

Companies and leaders may want to consider a few questions when pursuing energy and sustainability technologies:

— What will it take to accelerate the transition of promising climate technologies from lab to market, particularly in hard-to-abate sectors such as steel and cement?

\- How can digital innovations—like AI, sensors, and advanced analytics—accelerate the deployment and integration of renewables and climate technologies across fragmented energy systems?

\- As global electrification surges, how will energy systems adapt to rising demand, more distributed ownership of generation and storage, and the need for next-generation grid governance?

— How can nations and companies secure resilient, diversified supply chains for critical clean-energy materials amid rising geopolitical tensions?

— What regulatory frameworks and market mechanisms might unlock the investment and coordination required to scale next-generation energy technologies while maintaining affordability and reliability?

![](images/8d8b8ab4e0f252bf0b1a8762dd24679e26276db08f1ecd44793275fca56533c7.jpg)
"""
