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
- 已识别机构名：`摩根斯坦利`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、MS、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
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
7. 文末自然承接未解问题，引导读者加入社群/微信群继续讨论。不要照抄固定话术，请基于本文未解问题每次重新写一段自然 CTA；语义可以参考：更多国际信源汇编&评论，扫码交流，每日更新，汇总国际主流叙事&数据&图表，观测边际变化。汇聚了头部券商、PE/VC、投行、并购、hedge fund、资管机构、战略咨询、智库等朋友，期待交流。
8. 在免责声明前，单独插入这张图片链接：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`
9. 结尾只输出英文灰色免责声明：`<p style="color:#999999;font-size:12px;">Personal reading notes and learning share only. Not investment advice.</p>`

【hook 要求】
- 不要硬插“加入社群”。
- hook 应该来自正文自然出现的未解问题，比如：关键假设尚未验证、竞争优势仍需拆解、图表背后的二阶影响没有展开。
- 文末 CTA 要像“顺着这些未解问题继续读完整报告/继续讨论”，不是广告口吻。
- CTA 必须每篇重新写，不能固定套话。它需要自然包含这些信息：更多国际信源汇编&评论，扫码交流，每日更新，汇总国际主流叙事&数据&图表，观测边际变化；汇聚了头部券商、PE/VC、投行、并购、hedge fund、资管机构、战略咨询、智库等朋友，期待交流。

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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份摩根斯坦利研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
# Key Investor Questions

Debates on Powering AI and Energy Security, as well as globalisation of natural gas and fuel shortages, have become nuanced. We flag 12 stocks that got most interest among the 70 plays we've highlighted globally as energy meets computing.

## Key Takeaways

US investors are more focused on the Energy Security theme in Asia than their Asian peers.

Powering AI, fossil-based power generation, and energy storage batteries are being looked at with more bottom-up ideas in focus.

Over the last two weeks, we had 50+ discussions with investors across Asia and the US on our Energy Security & Powering AI Blupepaper. We got notable pushback on our estimated size of investments for Asia. Investors find it low at US\$5.5 trillion – they see upside to our power grid, power generation, and energy storage estimates.

## What's consensus and got most investor mindshare:

1. Positive view on shipyards, clean tankers, gas pipelines, and energy storage batteries/fuel; downstream energy (fuel refiners) over pure upstream players got limited pushback.

2. Diversification in portfolio exposure from power equipment supply chain (transformers and turbine manufacturers) to power generation for playing the next leg of Powering AI;

3. Greater need for battery storage and fuel storage infrastructure in Asia.

## Key debates and areas of pushback include:

1. Coal or renewables; is coal back as part of the energy security theme?

2. Does more power for Al mean more natural gas or more energy storage?

3. Will US natural gas adoption slow in Asia vs. expectations before the Middle East conflict as coal comes back? What gas economics tip the scale?

4. Beyond the conflict, as oil and natural gas supply picks up, will naphtha-based chemicals finally outperform after three years?

5. Fuel refining and tankers and shipyards – aren't they becoming bigger bottlenecks than even power?

## Stocks of most interest in Asia:

• Fuel refiners (Thai Oil, HPCL, S-Oil);

• Coal equipment (Komatsu, Sany);

• Power generators and grids (Gulf Development, Adani Power, Tenaga);

\- Equipment (Doosan Enerbility, diesel power generator manufacturers);

• Energy storage (CATL).

Mayank Maheshwari  
Equity Analyst  
Mayank.Maheshwari@morganstanley.com +65 6834-6719

Ryan M Heng  
Equity Analyst  
Ryan.Heng@morganstanley.com +65 6834-6465

Vivek Rajamani  
Equity Analyst  
Vivek.Rajamani@morganstanley.com +65 6834-6740

MS INDIA COMPANY PRIVATE LIMITED+

Pranitha Shetty  
Research Associate  
Pranitha.Shetty@morganstanley.com +91 22 6118-3022

Hinal Choudhary
Research Associate
Hinal.Choudhary@morganstanley.com +91 22 6118-2044

![](images/8c3458ff9739e0e4ebe6faa350bb1b0ea526c687bcbe7898a34ea45ee6d4fdcf.jpg)

Asia Pacific Industry View In-Line

MS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.

For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

+= Analysts employed by non-U.S. affiliates are not registered with FINRA, may not be associated persons of the member and may not be subject to FINRA restrictions on communications with a subject company, public appearances and trading securities held by a research analyst account.

## The US\$5.5 Trillion Investment Super-Cycle

Exhibit 1: Asia's Energy Security – US\$5+trn of investments required

![](images/9a2c2e87840c5b1d46b593a35987eb51a280d11bb339806d7906fe9e921e495b.jpg)  
Source: MS estimates; not drawn to scale

## Ideas to Play

Buy dependable energy security beneficiaries as AI pushes Asia into a US\$5.5trn capex cycle: We recommend owning energy security assets – the theme is inextricably tied to AI. We highlight 70 global equities across the coal equipment supply chain, fuel refiners, petrochemical producers, and natural gas exporters that we expect to benefit the most globally. Areas where we think earnings and dividends could surprise the most in Asia are:

\- Fossil- and nuclear-based power generators;

\- The energy storage supply chain, including power grids; and

\- Fuel refiners and shipyards

We expect tightness in refining markets after the export restrictions in Asia get lifted (India, China, Thailand): We believe this will come in conjunction with higher crude availability from the Strait of Hormuz. Hence, margins for fuel products may decline from the current highs. However, crude discounts cushion the decline and refiners in Asia could actually report stronger-than-expected 3Q earnings (YoY).

The interplay of lower gasoline inventories in the West and higher need for naphtha in the East could also add to strength in refining and chemical markets (vs. what forward curves suggest). While inventory-related losses will lead to a challenged June quarter for refiners, underlying profitability would actually be much stronger than in 2025. We see an 2027 earnings upgrade cycle picking up after 2Q26 reporting season.

Energy storage batteries and LNG: Gauging the need for LNG in Asia is now getting a lot more nuanced – modeling battery storage and its impact, along with coal restarts in power systems, which we see as tipping the need for LNG imports in Asia to be 10-15mntpa lower in the coming five years than we had previously expected. However, this also puts the clearing price (ASP) for Asian consumers to import natural gas much lower – as competition from coal and batteries (after installation) becomes much lower in operating costs and closer to \$7-8/mmbtu LNG.

Exhibit 2: Comparing Power Generation Costs for Round the Clock  
Round the Clock Power Generation Economics (UScents/kwh)  
![](images/1543b32c782e06e351515a00252e2d6b16c3d657e85360ae8eee02e31e16e78b.jpg)  
Source: Company Data, MS Estimates

## How much will Asia need to invest in storage? We estimate >US\$70bn: Energy,

product, and feedstock storage – while arguably the most critical element of energy security infrastructure in the coming years – is also among the least capex-intensive relative to other forms of capacity build-out. IEA countries target 90 days of import cover for fuel and crude. Applying this as a guiding principle for Asia, we estimate \~1.4bn bbls of incremental oil and petroleum fuel storage needs, alongside increased LNG and fertilizer coverage, implying >US\$70bn of required investment across Asia

Exhibit 3: Energy Security and AI: Ways to Play  
![](images/54a1b706d1a255ebf1ffbdc7ac696cddde6b5466846e0d58a33f1ba95609a8f3.jpg)  
Source: MS

## Energy Security: What Asia Is Doing

What Asia is doing to secure energy supply systems and where the largest bottlenecks exist in securing supply chains: Asia's energy capex will nearly double through the end of the decade. By 2030, over US\$1.2 trillion in new investments will be needed to reduce Asia's import dependence by 100bps based on expected consumption growth. This is in addition to US\$4.3trn of investments currently in progress and implies annual capital deployment growth of 11% through 2030 vs. 2% in the past decade.

Exhibit 4: Asia's Energy Security Implementation vs. Urgency Matrix  
![](images/2a9022c7e970e785707449c866a7cdcc46b60cb00ae9e755b5e587685a5ca71f.jpg)  
Source: MS estimates; not drawn to scale

Energy supply chains will realign as countries avoid the current chokepoints: Energy supply chain realignment is shifting from "just-in-time" cost efficiency to "just-in-case" resilience, driven by geopolitical tensions, trade tariffs (e.g., US tariffs, FEOC restrictions), and the need to decouple from dominant suppliers like the Middle East. This restructuring prioritizes friend-shoring, regionalization, and closer to home.

We believe Asia will import a lot more natural gas from the US and Russia incrementally, considering it is essential for power and transport systems, while also importing more oil from LatAm, Canada and Africa.

Fuel systems in Asia are also likely to realign as exports were curbed for the first time by China and Thailand. We have already seen signs of this change with the Australia-Singapore energy cooperation. We expect other economies – such as Japan, Taiwan, and Korea – to look again at fuel sourcing options.

![](images/76b4dd6f7ff52f7f94b2dc46665377743e6e17c06771d33e2f0983359c47fdf3.jpg)

Coal, which is ample in Indonesia, India and China, will also be key for 'just in case' resilience for power systems.

Power grid connectivity in Southeast Asia between countries, such as India-Bangladesh, will get more traction after two decades of limited progress.

Exhibit 5: Energy Security and Powering AI: A Supercycle Recharges – A Snapshot by 2030

## Energy Security & AI: A Supercycle Recharges

![](images/f1826eb46379e80cc9ccb70137a3ce154ab5a3a773e965bb7d3139ec95aa7397.jpg)  
US\$9trn in Enterprise Value creation

![](images/b2875c5cb156ed3b92b9482e5d0a919d42cea50d3dccbd5016be9a8cb212ba9d.jpg)

![](images/acafec48ba2c2f99f22ac8209ee39df0633666d1b0489b083e16c73163116028.jpg)  
... from US\$5+trn of investments

![](images/c1c682a77ebc6763690610ec335b9ee11e0e8e12f0cf8892d999c4ebc5ac01c9.jpg)

![](images/0d6f2c3fe5407000492fe8bd1a71c7b5df038f0f74cac3ad21c67597b4ab898c.jpg)  
Reducing Asia's Incremental Energy Dependency from 36% to 29%

![](images/c4273515fb8209ef4e8e22d8ccf79c55c65f3d4fb2e5e136be195aad8576f290.jpg)

## Total Energy Investments by Economy

![](images/9c968c0f99a6d5169eb0e24189243268fd0883c0470904547f3eb5a152849a21.jpg)  
US\$3,089bn

![](images/8735a2a11c9afe1a9c5fe896b8bba3a44e808f360dafb94076c5cb21f8d34581.jpg)  
US\$552bn

![](images/a5101610020fe1cf4e9bc0539e5315442a1deb58e468ffc459b6808024567caf.jpg)  
US\$116bn

![](images/6ed25886d10a1a4651694e37528e6e27fb31cc0e26aa0a949bb1f819e2e986d2.jpg)  
South Korea  
US\$128bn

![](images/6f37eedf7abfa79e85ed860fdf0825eedbb6e825e5db61aeaa4daed633bf57f0.jpg)  
Australia  
US\$242bn  
ASEAN + Taiwan  
US\$697bn

## Benefiting these subsectors

![](images/2def28590f12399ea6ade4ee88adb83fc388c69299f459987b2649ebea84ff23.jpg)  
Equipment Suppliers (Coal Mining, Power Generation Equipment, Grid Equipment, Refining Equipment)

![](images/5e307c5c62b18e7cc40bba3327202af0bdc5bcee9e67bf099ccfa00a182735aa.jpg)  
Oil Services & logistics (Rig operators, offshore energy, tankers)

![](images/7b2306e986c79f5dfe1286a19888fa7138e45e44c2078a5c9a4b94f4a6778df5.jpg)  
Power
(Thermal power generators, Grid Operators)

![](images/0601072ebc894623c463a14c59b707524ff02c1f0d998f68a1e2db7d79f2223f.jpg)  
Downstream  
energy (refiners, chemicals, fertilizers)

![](images/6668d8976ffd082e0da18e1d6d5b51c12809f85cf44afc76b6ba338d031050b2.jpg)  
Infrastructure Operators (LNG terminals, Gas pipeline Operators)  
Source: MS estimates

# Coal or Renewables – Which Is Key for Security?

Rather than viewing coal, gas, nuclear, and renewables as competitors, policymakers increasingly are adopting a balanced and pragmatic multi-track approach: Diversified installed capacity will form a natural hedge against volatility in geopolitics, commodity prices, and supply chains.

In both China and India, coal retains strong policy support, with clean energy framed not as a replacement but as a supplement – reinforcing a multi-track energy strategy that postpones difficult decisions on coal phaseout as power demand continues to grow. China's coal power generation is higher than ever at \~5.5trn kWh in 2025, even as the country installed more than 500GW of solar and wind power in the same year.

Many Asian countries – particularly import-dependent and fossil-fuel-intensive ones – still need to invest in a more balanced generation mix: Expanding homegrown renewable energy capacity – along with supporting grid upgrades, storage, and even selective use of cleaner gas or nuclear power – is widely seen as vital to further fortify Asia's power systems against fuel shocks.

However, it is not enough. Renewables' intermittency and reliability remain a key risk in providing holistic energy security. A significant proportion of renewable generation would lead policymakers to trade fossil fuel accessibility risk with geographical and environmental resource risks (sunlight, wind, reservoir water levels). We see coal and gas power generation remaining highly relevant for the rest of the decade as access to reliable power remains key for policyholders.

Exhibit 6: Asia's power generation mix  
![](images/d0617e0c897abfb59d3d200ecb4850b3159eeb1aba20590980e7107529c65c8f.jpg)  
Source: Statistical Review of World Energy, MS estimates

More Power for AI

Is this the end game? Powering AI for US hyperscalers in Asia while securing energy supply chains in Asia using US energy: Securing energy supply for AI has emerged as a durable, system-level investment theme across the power and fuel value chains, distinct from decarbonization targets or short-term price signals. Recent LNG disruptions and extreme price volatility have shifted policymaker and corporate behavior toward reliability, dispatchability, and domestic or regional resilience over pure economic optimization. We think this will drive a new sustained capex cycle across grid infrastructure, battery storage, strategic reserves, utilities, and selective generation technologies. Overall electricity will account for \~30% of Asia's energy needs, up from \~25% currently, as the region electrifies.

Artificial intelligence and the associated proliferation of data centers represent the most significant new source of electricity demand growth in developed economies in decades: Data centers currently account for \~2% of global power consumption and we forecast they will add 1.2 trillion units (20% of total incremental power demand) to global power consumption, accounting for 5% of power demand by 2030. While there will be varied adoption rates globally, about 45% of these units will be consumed in Asia and 45% in the US, with Europe largely accounting for the rest.

\- We see a 25% CAGR in power consumption from data centers in 2024-27 and a 20% CAGR in 2027-30.

\- We expect data centers to account for 75% of US power demand growth through 2030, while in Europe they will account for 40% and in Asia 13%

Exhibit 7: Potential shortfall in power for US data centers  
![](images/0a2853cf007cf5fd1dc4c44ad765de60a672ef6fcb9b1ec06e2d4fb713bd4ba6.jpg)  
Source: MS Estimates

Japan South Korea Thailand Singapore Malaysia Other

## US Natural Gas Needs in Asia – Slow vs. Expectations?

How large a part the US plays in the story of Asia's diversification in energy; Asia imported only \~10% of its energy imports from the US in 2025. We see the US's share in Asia's energy imports rising as cheaper natural gas, ethane, propane, coal and petcoke support adoption and diversification in power and chemical supply chains. Increased diesel imports will help lower dependence on the Strait of Hormuz.

We forecast a 6% CAGR in global LNG demand over 2025-30, driven by Asia: For Asian consumers, US LNG offers attractive supply diversification and pricing relative to other sources – offering greater stability during periods of supply disruption. We expect the bulk of volumes from export projects currently under construction to flow to end markets in Asia. In addition, in view of recent events in the Middle East, we see the potential for additional long-term gas sales deals from Asian buyers. However the pricing of this gas is going to be near coal parity as Asia restarts \~50GW of its coal fired power plants and also deployed energy storage capacity.

Growing refined product demand from Asia tightens global balances and supports margins: Growing refined product demand across Asia is constructive for US refiners, particularly those with Gulf Coast exposure and access to export markets. As Asia consumption outpaces regional refining capacity additions – driven by sustained transportation growth and petrochemical feedstock demand – incremental barrels will need to be sourced from the global market. As shown by the recent Middle East conflict, the US Gulf Coast is well equipped to be the world's swing refining center, filling gaps left by declining product volumes from key Asian and Middle Eastern exporters.

Exhibit 8: Since the start of the Middle East conflict, shipments to Asia have made up a higher share of total US LNG exports – rising from \~15% prior to \~35% in May so far.  
![](images/476e2c5ed1bddb617cfb9b62bdabe9825d7297de9f5c11abfb2008cf1034cf59.jpg)  
Source: Vortexa, MS

Exhibit 9: The US exports \~3,240 kbpd of refined product, of which \~10% lands in Asia. The Iran conflict has pushed exports to >4 mbpd  
![](images/edfdc79cb45704530c883d8c43d9b54f401fe2a48dd213c1ada9293ff581cfa4.jpg)  
Source: Vortexa, MS

## Disclosure Section

The information and opinions in MS were prepared or are disseminated by MS Asia Limited (which accepts the responsibility for its contents) and/or MS Asia (Singapore) Pte. (Registration number 199206298Z) and/or MS Asia (Singapore) Securities Pte Ltd (Registration number 200008434H), regulated by the Monetary Authority of Singapore (which accepts legal responsibility for its contents and should be contacted with respect to any matters arising from, or in connection with, MS), and/or MS Taiwan Limited and/or MS & Co International plc, Seoul Branch, and/or MS Australia Limited (A.B.N. 67 003 734 576, holder of Australian financial services license No. 233742, which accepts responsibility for its contents), and/or MS Wealth Management Australia Pty Ltd (A.B.N. 19 009 145 555, holder of Australian financial services license No. 240813, which accepts responsibility for its contents), and/or MS India Company Private Limited having Corporate Identification No (CIN) U22990MH1998PTC115305, regulated by the Securities and Exchange Board of India ("SEBI") and holder of licenses as a Research Analyst (SEBI Registration No. INH000001105); Stock Broker (SEBI Stock Broker Registration No. INZ000244438), Merchant Banker (SEBI Registration No. INM000011203), and depository participant with National Securities Depository Limited (SEBI Registration No. IN-DP-NSDL-567-2021) having registered office at Altimus, Level 3

[中间内容因长度限制已省略]

Financial Promotion) Order 2005 (as amended, the "Order"); (ii) are persons who are high net worth entities falling within Article 49(2)(a) to (d) of the Order; or (iii) are persons to whom an invitation or inducement to engage in investment activity (within the meaning of section 21 of the Financial Services and Markets Act 2000, as amended) may otherwise lawfully be communicated or caused to be communicated. RMB MS Proprietary Limited is a member of the JSE Limited and A2X (Pty) Ltd. RMB MS Proprietary Limited is a joint venture owned equally by MS International Holdings Inc. and RMB Investment Advisory (Proprietary) Limited, which is wholly owned by FirstRand Limited. The information in MS is being disseminated by MS Saudi Arabia, regulated by the Capital Market Authority in the Kingdom of Saudi Arabia, and is directed at Sophisticated investors only.

MS Hong Kong Securities Limited is the liquidity provider/market maker for securities of Contemporary Amperex Technology Co. Ltd. listed on the Stock Exchange of Hong Kong Limited. An updated list can be found on HKEx website: http://www.hkex.com.hk.

The information in MS is being communicated by MS & Co. International plc (DIFC Branch), regulated by the Dubai Financial Services Authority (the DFSA) or by MS & Co. International plc (ADGM Branch), regulated by the Financial Services Regulatory Authority Abu Dhabi (the FSRA), and is directed at Professional Clients only, as defined by the DFSA or the FSRA, respectively. The financial products or financial services to which this research relates will only be made available to a customer who we are satisfied meets the regulatory criteria of a Professional Client. A distribution of the different MS Research ratings or recommendations, in percentage terms for Investments in each sector covered, is available upon request from your sales representative.

The information in MS is being communicated by MS & Co. International plc (QFC Branch), regulated by the Qatar Financial Centre Regulatory Authority (the QFCRA), and is directed at business customers and market counterparties only and is not intended for Retail Customers as defined by the QFCRA.

As required by the Capital Markets Board of Turkey, investment information, comments and recommendations stated here, are not within the scope of investment advisory activity. Investment advisory service is provided exclusively to persons based on their risk and income preferences by the authorized firms. Comments and recommendations stated here are general in nature. These opinions may not fit to your financial status, risk and return preferences. For this reason, to make an investment decision by relying solely to this information stated here may not bring about outcomes that fit your expectations.

The trademarks and service marks contained in MS are the property of their respective owners. Third-party data providers make no warranties or representations relating to the accuracy, completeness, or timeliness of the data they provide and shall not have liability for any damages relating to such data. The Global Industry Classification Standard (GICS) was developed by and is the exclusive property of MSCI and S&P.

MS, or any portion thereof may not be reprinted, sold or redistributed without the written consent of MS.

Indicators and trackers referenced in MS may not be used as, or treated as, a benchmark under Regulation EU 2016/1011, or any other similar framework.

The issuers and/or fixed income products recommended or discussed in certain fixed income research reports may not be continuously followed. Accordingly, investors should regard those fixed income research reports as providing stand-alone analysis and should not expect continuing analysis or additional reports relating to such issuers and/or individual fixed income products. MS may hold, from time to time, material financial and commercial interests regarding the company subject to the Research report.

Registration granted by SEBI and certification from the National Institute of Securities Markets (NISM) in no way guarantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.

## INDUSTRY COVERAGE: ASEAN Utilities and Infrastructure

<table><tr><td>COMPANY (TICKER)</td><td>RATING (AS OF)</td><td>PRICE* (07/01/2026)</td></tr><tr><td>Global Power Synergy PCL (GPSC.BK)</td><td>U (09/12/2025)</td><td>Bt44.00</td></tr><tr><td>Gulf Development PCL (GULF.BK)</td><td>O (03/26/2025)</td><td>Bt61.50</td></tr><tr><td>Manila Electric Company (MER.PS)</td><td>O (06/20/2022)</td><td>PP585.00</td></tr><tr><td>Perusahaan Gas Negara (PGAS.JK)</td><td>E (06/18/2026)</td><td>Rp1,365</td></tr><tr><td>SembCorp Industries Ltd (SCIL.SI)</td><td>O (03/23/2026)</td><td>S$6.23</td></tr><tr><td>Tenaga Nasional (TENA.KL)</td><td>O (09/12/2023)</td><td>RM14.20</td></tr><tr><td colspan="3">Ryan M Heng</td></tr><tr><td>Airports of Thailand (AOT.BK)</td><td>O (08/25/2021)</td><td>Bt64.75</td></tr><tr><td>International Container Terminal Service (ICT.PS)</td><td>O (03/04/2024)</td><td>PP900.00</td></tr><tr><td>Maynilad Water Services, Inc. (MYNLD.PS)</td><td>E (06/30/2026)</td><td>PP19.60</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.  
\* Historical prices are not split adjusted.

© 2026 MS
"""
