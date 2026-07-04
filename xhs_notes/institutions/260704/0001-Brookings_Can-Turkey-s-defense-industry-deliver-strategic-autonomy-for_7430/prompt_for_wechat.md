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
- 已识别机构名：`布鲁金斯学会`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如高盛、摩根士丹利、汇丰、摩根大通、瑞银、花旗、美国银行、巴克莱、德意志银行、野村。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份布鲁金斯学会研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
# From Client to Competitor: The Rise of Turkiye's Defence Industry

Sıtkı Egeli, Serhat Güvenç, Çağlar Kurç and Arda Mevlütoğlu

May 2024

![](images/998cc689b51bd35d224b4fd1711f232a4da172ed85166b788102ff70415cfc78.jpg)

## Acknowledgements

This paper is a part of ‘National Defence Industry: From an Enabler of Turkey’s Pursuit of Strategic Autonomy to a Bridge between Turkey and Europe’, a joint project between the Center for Foreign Policy and Peace Research (CFPPR) and the International Institute for Strategic Studies (IISS). The project is supported by the Centre for Applied Turkey Studies (CATS).

## Disclaimers

The views outlined in this paper are exclusively those of the authors and do not represent institutional views of the CFPPR or the IISS.

## Contents

Executive Summary 4
Introduction 5
Section 1: Stops and Starts: The First 50 Years 7
Turkiye as a Client in the International Arms Production and Trade System: 1923–47 7
Turkiye as a Recipient of US Military Aid: 1947–64 8
The Pursuit of Limited Strategic Autonomy in the Era of Detente: 1964–73 8
The Pivotal Year: 1974 9
Section 2: Revamping the Defence Industry: 1980s and 1990s 10
F-16 Production Comes to Turkiye 10
Prime Minister Özal, the 'Joint Venture' Approach and the Creation of the SSM 10
No Peace Dividend Here: Turkish Defence Procurement in the 1990s 14
Section 3: Turkiye's Indigenous Development Model and the Period of Incubation: 2004–Present 16
Prime Minister Erdoğan and the First Indigenous Designs 16
A Push for the Nationalisation of the Defence Industry 17
Indigenisation Versus International Collaboration 18
Conclusion 25
Notes 27

# Executive Summary

Turkiye's defence industry is at a crossroads, and decision-makers face a difficult choice regarding its future path. On one hand, Turkiye's long-standing ambition to establish a self-sufficient defence industry has led to considerable industrial growth and increased Ankara's strategic autonomy by reducing the influence of foreign suppliers. On the other hand, continued goals of self-sufficiency will become increasingly challenging and costly, particularly as the scale and sophistication of modern weaponry evolve and new competitors enter the marketplace. Although this provides an impetus for increasing industrial cooperation, the development of Turkiye's defence industry has historically been rooted in its response to Western arms embargoes and the country's decision-makers are strongly aware of the vulnerability of defence cooperation to foreign influence.

The international system has provided opportunities and challenges for Turkish defence industrialisation. However, to understand this process and the factors that will shape future decisions, it is necessary to consider how domestic factors such as the attitudes of leaders, a desire for strategic autonomy and the maturation of Turkiye's nascent industry have impacted its trajectory.

Political leaders such as Mustafa Kemal Atatürk in the 1920s and 1930s, Adnan Menderes in the 1950s, Turgut Özal in the 1980s and Recep Tayyip Erdoğan since the 2000s have left their marks on Turkiye's defence industry. In doing so, they have reflected and responded to the changing nature of the international system – ranging from acceptance of and reliance on American defence goods early on during the Cold War to a growing realisation that Turkiye needed its own defence industry in the 1960s. These ambitions were solidified after the 1974 Turkish military operation in Cyprus, when Turkish allies enforced declared and undeclared arms embargoes on Ankara. This catalysed a revamping of Turkiye's defence-industry capabilities.

Alongside the reorganisation of the country's domestic defence industry, the switch from import-substitution to export-driven industrialisation permitted large-scale private-sector involvement in the defence industry. Defence companies that were built from scratch in the 1980s by private-sector investors were encouraged to work with foreign partners to bring in skills, technologies and capital. This approach prompted the rise of joint ventures, which seemed to offer the best model to secure technology transfer. The Undersecretariat for Defence Industries (originally known as the Defence Industry Development and Support Administration Office and as the Defence Industry Agency since 2022) was also a major factor in the growth of the defence industry after the consolidation of much of the industry under the Turkish Armed Forces Foundation (Türk Silahlı Kuvvetlerini Güçlendirme Vakfı) in 1987.

Turkish decision-makers have come to understand that absolute autonomy is practically unattainable. Although the indigenisation of weapon systems permits many freedoms, the process also introduces different forms of dependencies. Furthermore, the 'top-down' strategy employed by Turkiye in establishing its defence-industrial base, going from the platform level down to components and technologies, has also faced criticism, mainly due to poor prioritisation and a lack of a coherent procedural approach.

To offset costs, Turkish defence industrialisation has become highly dependent on arms exports as it continues to indigenise and produce military technologies. Despite its booming turnover and export figures, however, the sector faces long-term challenges, including the emergence of new market competitors and an increasing rate of 'brain drain', especially since the late 2010s.

It is against this backdrop that Turkiye's decision-makers face a crossroads. Although Turkiye would prefer to work with its Western allies, it is also open to cooperation with non-Western countries. This is because dependence, of varying degrees, on foreign arms suppliers could still restrict Turkiye in pursuing its national interests, especially if the policies and priorities of Ankara and its principal suppliers fail to align.

## Introduction

Turkiye's process of defence industrialisation since the early twentieth century perfectly represents the pressures and dilemmas that an emerging state faces in this area. Defence industrialisation does not happen in a vacuum, and the path it takes is formed by both domestic (e.g., historical path dependence, innovation capabilities, the military requirements of the armed forces, institutional capacities and civil-military relations) and international factors (e.g., the impact of globalisation of arms production, alliance politics and the international system). $^{1}$ For Turkiye, shifts in the international environment provided both opportunities and challenges. For example, the multipolar international system of the interwar period (1918–39) enabled Turkiye to establish relations with major powers, draw international investment and build its defence industry. The bipolar world of the Cold War, on the other hand, froze defence industrialisation in Turkiye as immediate security concerns took priority over longer-term defence-industrial development. The end of the Cold War marked new opportunities and a dramatic shift in international arms production, on which Turkiye successfully capitalised. As the world moves toward a more tumultuous era, Turkiye is faced with difficult choices in its defence industrialisation and foreign policy.

The overall trajectory of Turkish defence industrialisation, however, has been most significantly determined by domestic factors. During the interwar years, progress was hindered by the country's weak industrial capability and lack of capital. Then, at the end of the Second World War, the influx of American military aid enabled the newly elected Democrat Party to overlook the needs of the military and the defence industry. This significantly slowed domestic defence-industrial development until the country re-experienced the challenges of dependency on a foreign supplier, when Turkiye's allies enacted arms embargoes against it following its 1974 military operation in Cyprus. Despite this reignition of ambitions to invest in its defence industrialisation, backed by much greater defence spending (see Figure 1), progress in the 1980s and 1990s was impeded by competition between different decision-making actors and their approaches to developing Turkish industrial and managerial capabilities. More recently, as Turkish defence-industrial capabilities have improved and the number of indigenous systems has increased, the sector has become more popular domestically and its products have become symbols of success and prestige. However, the Turkish defence industry has now reached a point where it needs to make difficult choices again.

The Turkish fighter jet Kaan is flown for the first time, 21 February 2024  
![](images/7f502923de57da7b258aceefaa0ad8190145320ab2e5a452f8b1dd9dfc686aa1.jpg)  
(Turkish Defence Industry Agency/Anadolu Agency via Getty Images)

Figure 1: Turkiye: defence spending, 1980–2024  
![](images/74f7ea312d718a06e2f3b550ee07b006e425bd821f907639303210d4f7fb7883.jpg)  
Note: Figures in Turkish lira reflect the revaluation in 2005, which removed six zeros from the currency. Sources: NATO, 'Financial and Economic Data Relating to NATO Defence'; Military Balance+; IISS analysis

Although Turkish defence industrialisation originally aimed at self-sufficiency, financial limitations have moderated this ambition. Producing all systems is not financially feasible. While Turkiye seeks to make its defence industry sustainable through exports, international cooperation provides another avenue for maintaining this growth. Engaging in international cooperation, however, comes at the expense of autarky, and this trade-off can present very difficult choices. In this report, we will present a comprehensive look into Turkiye's process of defence industrialisation – its policy choices, the hurdles it has faced and potential solutions.

# 1. Stops and Starts: The First 50 Years

## Turkiye as a Client in the International Arms Production and Trade System: 1923–47

From 1923–47, three factors shaped Turkiye's approach to arms procurement: 1) historical experience, 2) the interwar international arms-trade system and 3) the availability of funds from international arms suppliers under favourable terms.

The experience of the late Ottoman Empire suggested that relying on a single supplier exposed the state to the influence of major arms-producing powers. This formed a strategic lesson that the new Republic of Turkiye under the leadership of Atatürk drew upon: that is, alliances with stronger powers result in a loss of sovereignty for the minor partner. Ankara therefore shied away from alliances or arms deals that could compromise Turkiye's sovereignty.

The interwar international arms-trade system imposed structural constraints on Turkiye's choice of arms suppliers. Germany was wholly excluded from the system due to the restrictions on its arms production and trade under the Treaty of Versailles. Meanwhile, the United Kingdom and France were uninterested in supplying arms at affordable prices and under favourable credit terms. Turkiye was also not yet considered a politically and economically reliable client for British or French arms. Only Italy and the Soviet Union, therefore, could cater for Turkiye's requirements.

Nevertheless, Germany could figure prominently in terms of financing Turkish arms orders. In 1925, Turkiye placed an order for two coastal submarines from a Dutch shipyard, established by three German shipbuilders – Friedrich Krupp Germaniawerft (Kiel), A.G. Weser (Bremen) and Vulkanwerft (Hamburg and Stettin) – to get around the Versailles restrictions on German submarine production. $^{2}$

Similarly, German aircraft manufacturer, Junkers, set up an assembly plant in Kayseri (Central Anatolia) in 1926 to preserve German know-how on military aircraft production. The plant assembled A-20 and A-20W

Havoc military aircraft as well as a few F-13 civilian airliners to meet Turkish orders, although that venture was ultimately not successful. $^{4}$

In the early republican era, the Turkish defence industry consisted mostly of factories established to manufacture small arms and their ammunition. The German connection was also evident in this period. Companies such as Rheinmetall, Mauser, Nielsen & Winther and Allgemeine Elektricitäts-Gesellschaft were involved in Turkish small-arms and ammunition manufacturing. $^{4}$

This modest industrial base was more or less sufficient to cater for an infantry and cavalry-dominated army. $^{5}$ The Turkish army was introduced to mechanised warfare through a somewhat experimental unit equipped with tanks (T-26Bs) and armoured cars (BA-6s) acquired from the Soviet Union in 1934. $^{6}$ However, the transition from a manpower and horsepower army to a motorised one would prove to be difficult and costly for Turkiye, with an attendant increase in dependence on foreign suppliers and limits on military capability in the interim.

On the eve of the Second World War, Ankara found in the UK a pro-status quo European power that was willing to sell arms to Turkiye under very generous credit terms. London also helped revamp Turkiye's aircraft-manufacturing capability with the licensed assembly of Miles Magister trainer aircraft at the Mechanical and Chemical Industry Corporation's aircraft factory in Ankara. $^{7}$

Turkish diplomatic manoeuvring during the Second World War made it possible for Ankara to procure arms from France, Germany and the UK. Germany offered arms to Turkiye to liquidate debts accrued as a result of barter trade between the two countries. Ankara ordered four new submarines from the German company Krupp AG directly, as Adolf Hitler had unilaterally denounced the Treaty of Versailles restrictions on German arms production. Under this new contract, two boats were to be built in Germany, the other two in Turkiye. $^{8}$ In October 1939, Turkiye signed a tripartite alliance treaty with France and the UK. This resulted in the expedited delivery of British and French tanks and fighter aircraft and led Hitler to suspend arms supplies to Turkiye.

Throughout the war, Turkiye remained neutral; but, in 1942, it became a recipient of the United States' Lend-Lease programme. $^{9}$ This marked the beginning of Turkiye's transformation from a client of arms producers to a mere recipient of US military aid. The availability of surplus US equipment in large quantities spelled the slow death of Turkiye's fledgling domestic-arms industry after the Second World War. $^{10}$ The sheer magnitude of US arms transfers to Turkiye from 1947–80 can be understood from the quantities involved – e.g. 3,085 M48 and M48A2C Patton tanks between 1963 and 1970 and about 260 F-100C/D/F Super Sabre fighter ground-attack aircraft between 1958 and 1973. $^{11}$

## Turkiye as a Recipient of US Military Aid: 1947–64

The Cold War radically altered the drivers of Turkish foreign and defence policy. The flow of US military equipment to Turkiye gathered momentum after the Truman Doctrine was announced in 1947. Ankara then shifted its focus from local production to operating and maintaining the new equipment. In the 1940s, Turkiye's aircraft industry was able to produce an upgraded version of the British Miles Magister trainer aircraft, the MKEK-4 Uğur, to meet the Turkish Air Force's trainer requirements. $^{12}$ However, it stood no chance against the abundance of North American Aviation T-6 Texan trainers donated from US stocks.

Turkiye's political climate at the time also worked against investing in the defence industry. In May 1950, Turkiye transitioned from single-party rule to multi-party politics. For prime minister Adnan Menderes of the newly elected Democrat Party, competitive party politics required prioritising the needs and demands of the electorate over those of the armed forces. The optimum choice for him was to depend solely on US military assistance – provided in return for Turkiye joining NATO – in order to keep the country's large military afloat. This choice often worked to the detriment of local industry. $^{13}$ The result was total dependence on the US for not only equipment procurement but maintenance and logistics as well.

Menderes was ousted and subsequently executed after a military coup in May 1960. This dramatic turn of events did not result in any change in Turkiye's foreign relations. His successors continued the policy of relying heavily on US aid. However, the 1962 Cuban Missile Crisis and the subsequent US decision to remove the nuclear-armed Jupiter medium-range ballistic missiles from Turkiye – despite the latter's initial reluctance – exposed tensions in the relationship. $^{14}$

The 1960s, meanwhile, was a decade of significant change in the United States' approach to foreign military assistance. The administration of president John F. Kennedy devised a new policy aimed at turning US military-assistance recipients into clients under credits. This marked a move away from grants (Mutual Assistance Programs) to the Foreign Military Sales framework. Around the same time, Ankara had to endure the more severe consequences of its total dependence on the US in defence. During the Cyprus Crisis of 1963–64, president Lyndon B. Johnson sent a very strongly worded letter to Turkish prime minister İsmet İnönü that dissuaded him from intervening militarily in Cyprus. The letter served as a harsh reminder to Ankara that Turkiye could not employ US-supplied arms and equipment for non-NATO contingencies.

## The Pursuit of Limited Strategic Autonomy in the Era of Detente: 1964–73

As events in Cyprus unfolded, successive governments in Turkiye sought to develop greater military capabilities to complement diplomacy. This included diversifying its suppliers and beginning production of small-calibre guns and support weapons under German and US licences, respectively. $^{15}$ Moreover, Ankara established foundations for each of the armed services to raise money from the public to produce equipment needed for national contingencies.

Turkiye also began to show interest in European NATO allies' joint arms-production projects. For instance, it offered to manufacture wingtip missile launchers for the F-104G Starfighter as part of a European consortium. The

US turned down this proposal, however, because that particular aircraft part was considered too sophisticated for Turkiye's rudimentary aircraft industry. $^{16}$

In the 1960s and 1970s, the Turkish Armed Forces went through a partial transformation to acquire regional power-projection capabilities for future crises in Cyprus. As part of this process, the Turkish Naval Forces embarked on a programme to build a landing-craft fleet. To overcome engine shortages, decommissioned t

[中间内容因长度限制已省略]

rg/10.1080/01402399708437689.

15 Century of Turkish Defence, p. 62.

16 National Archives and Records Administration, 'From Capt. Holmes, US Mission to NATO, Paris, to Capt. Taylor, ONG-OP415, Washington, DC.', NND 984061, RG6330/64A-2382-41, 400.686, 8 February 1961.

17 Republic of Türkiye Directorate for EU Affairs, 'Screening Chapter 20, Enterprise and Industrial Policy, Agenda Item XV: Defence Industries', 4–5 May 2006, https://www.ab.gov.tr/files/tarama/tarama\_files/20/SC2oDET\_DEFENCE.pdf.

The defence minister, chief of the general staff and head of the SSM (now the SSB) are also members of the SSİK, amongst other cabinet ministers.

İbrahim Sünnetçi, 'Turkey & Stinger MANPADS Missile Procurement,' Defence Turkey, no. 101, November

2020, https://www.defenceturkey.com/en/content/turkey-stinger-manpads-missile-procurement-4253.

Jon Lake, 'Turkey Is First Operator to Complete Deliveries of A400M', Times Aerospace, 28 September 2022, https://www.timesaerospace.aero/features/defence/turkey-is-first-operator-to-complete-deliveries-of-a400m.

Aaron Mehta, 'Turkey Officially Kicked out of F-35 Program, Costing US Half a Billion Dollars', Defense News, 17 July 2019, https://www.defensenews.com/air/2019/07/17/turkey-officially-kicked-out-of-f-35-program/.

'Turkish Military Backs off From SSM Takeover Plan', Jane's Defence Weekly, 21 January 1998, p. 11.

'Savunma Sanayinde Dün, Bugün, Yarın' [Yesterday, Today, Tomorrow in the Defence Industry], Savunma ve Havacılık [Defence and Aviation], vol. 11, no. 4, 1997, p. 30.

Ahmet Davutoğlu, 'Zero Problems in a New Era', Republic of Turkiye, Ministry of Foreign Affairs, 21 March 2013.

'Tank ve helikopter ihaleleri iptal edildi' [Tank and Helicopter Tenders Cancelled], Hurriyet, 14 May 2004, https://www.hurriyet.com.tr/ekonomi/tank-ve-helikopter-ihaleleri-iptal-edildi-225670.

26 Burcu Ozcelik, 'Overcoming Hurdles to Turkish-Israeli Reconciliation', IISS, 6 May 2022.

27 See SSM Undersecretary İsmail Demir's comments in SETA, 'Panel | Stratejik Hava Savunma Sistemleri ve Türkiye'nin

Yol Haritası' [Strategic Air Defence Systems and Turkiye's Road Map], YouTube, 26 October 2015, https://www.youtube.com/watch?v=ueThuoxCkB8.

'Interview with Undersecretary Prof. Dr. Ismail Demir', MSI, 29 May 2017, https://www.savunmahaber.com/en/interview-prof-dr-ismail-demir-undersecretary-for-defence-industries-4/.

Sıtkı Egeli, 'Making Sense of Turkey's Air and Missile Defense Merry-go-round', All Azimuth, vol. 8, no. 1, 2019, pp. 69–92.

Gareth Jennings, 'US, Turkey Continue Talks to Settle F-35 Dispute', JANES, 24 January 2023, https://www.janes.com/defence-news/news-detail/us-turkey-continue-talks-to-settle-f-35-dispute.

'Indigenous UCAV Bayraktar TB2 Completes 750 Thousand Flight Hours', Baykar, 11 December 2023, https://baykartech.com/en/press/indigenous-ucav-bayraktar-tb2-completes-750-thousand-flight-hours/.

32 Interview with former senior SSM official, 24 November 2023.
33 Ibid.

34 Interview with senior think-tank analyst, 23 November 2023.  
35 Interview with senior diplomat, 24 November 2023.

37 Interview with former senior SSM official, 24 November 2023.

38 Interview with senior diplomat, 24 November 2023.

39 Interview with former senior SSM official, 24 November 2023.

![](images/0c8c9609f9c989f5d23b1683af4d2282180a4f7088ef74385dcce49ce9461e2e.jpg)

The Center for Foreign Policy and Peace Research (CFPPR) aims to develop agendas and promote policies that contribute to the peaceful resolution of international and inter-communal conflicts, particularly in the regions surrounding Turkey, through analyzing and interpreting contemporary policies from a critical, comparative, but also constructive, and peace-oriented perspective. Together with All Azimuth, it provides a platform for homegrown international relations and foreign policy research conceptualizations

## CATS Centre for Applied Turkey Studies NETWORK

![](images/ef08c5cbbcae1d0cf1d337cbc3de0397c649648f6ecd88b92285747e80a633ce.jpg)

Federal Foreign Office

![](images/3198c45473b4f5edfa2225ac2f1efc7adc556a29adf04f3d911c56800bae85aa.jpg)  
Stiftung Wissenschaft und Politik
German Institute for
International and Security Affairs

![](images/ecf7e575cb48a1ae0eaf8b0265f558ce4ce8bb300352d31b64fa7ee0d6020c9b.jpg)

The Centre for Applied Turkey Studies (CATS) at the Stiftung Wissenschaft und Politik (SWP) in Berlin is funded by Stiftung Mercator and the Federal Foreign Office. CATS is the curator of the CATS Network, an international network of think tanks and research institutions working on Turkey. 'National Defence Industry: From an Enabler of Turkey's Pursuit of Strategic Autonomy to a Bridge between Turkey and Europe' is a project of CATS Network.

![](images/6ff7fbfa517e54043c28bbaa72055d60a1c175fc39bc2c2623496d333a45cdec.jpg)

The International Institute for Strategic Studies (IISS) is an international institute that owes allegiance to no government. It is a registered UK charity and company. Its core objective is to promote the development of sound policies that further global peace and security, and maintain civilised international relations. IISS experts work from five offices in London, Washington DC, Berlin, Bahrain and Singapore. They carry out fact-based research, convene and frame discussions, and produce publications including The Military Balance, the definitive annual assessment of defence capabilities, and Survival, the global politics and strategy journal. The IISS organises and convenes conferences including the IISS Shangri-La Dialogue and IISS Manama Dialogue, world-leading forums for the discussion of security issues. IISS research helps governments, academics, the media and the private sector.
"""
