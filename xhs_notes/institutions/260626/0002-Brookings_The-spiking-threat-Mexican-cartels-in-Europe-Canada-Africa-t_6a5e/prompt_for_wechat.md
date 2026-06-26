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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份布鲁金斯学会研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
## CHINA-LINKED WILDLIFE POACHING AND TRAFFICKING IN MEXICO

MARCH 2022

VANDA FELBAB-BROWN

## TABLE OF CONTENTS

EXECUTIVE SUMMARY
I. INTRODUCTION
Methodology
II. WILDLIFE TRAFFICKING IN MEXICO, CONNECTED AND UNCONNECTED TO CHINA
Terrestrial species
Marine species
Organized crime's takeover of Mexico's fisheries
The evolving relationship between Mexican organized crime and Chinese traders
III. MONEY LAUNDERING AND VALUE TRANSFER
IV. CHINA'S DIPLOMACY AND LAW ENFORCEMENT COOPERATION WITH MEXICO AGAINST WILDLIFE TRAFFICKING
Interdiction and crackdown on retail markets
China's public narratives regarding Mexico-linked wildlife trafficking
Anti-money laundering efforts
Trilateral anti-wildlife crime efforts
Legal assistance
V. "FIX IT YOURSELF, MEXICO": ENVIRONMENTAL REGULATION ENFORCEMENT, CAPABILITIES, AND CHALLENGES IN MEXICO
VI. CONCLUSIONS AND RECOMMENDATIONS
Law enforcement
Economic incentives to counter poaching
Shutting down problematic markets
Protecting the protectors
REFERENCES
ABOUT THE AUTHOR
ACKNOWLEDGEMENTS

# CHINA-LINKED WILDLIFE POACHING AND TRAFFICKING IN MEXICO

VANDA FELBAB-BROWN

## EXECUTIVE SUMMARY

Wildlife trafficking from Mexico to China receives little international attention, but it is growing, compounding the threats to Mexican biodiversity posed by preexisting poaching for other markets, including the United States. Since Mexican criminal groups often control extensive territories in Mexico which become no-go-zones for government officials and environmental defenders, visibility into the extent of poaching, illegal logging, and wildlife trafficking in Mexico is limited. It is likely, however, that the extent of poaching and trafficking, including to China, is larger than commonly understood.

Terrestrial and marine species, as well as timber, illegally harvested in Mexico for Chinese markets increasingly threaten Mexico's biodiversity. Among the species poached in Mexico and smuggled to China, sometimes via the United States, are reptiles, sea cucumbers, totoaba, abalone, sharks, and increasingly also likely jaguars as well as various species of rosewood.

Legal wildlife trade from Mexico to China, such as in sea cucumbers and crocodilian skins, provides cover for laundering poached animals. Illegal fishing accounts for a staggering proportion of Mexico's fish production, but even the legitimate fishing and export industry provides a means to channel illegally-caught marine products to China.

The legal trade in wildlife also increasingly facilitates the money laundering activities of Mexican criminal groups, with various wildlife products used by Mexican criminal groups as a value transfer mechanism to Chinese traders in exchange for precursor chemicals for illegal drugs as such fentanyl and methamphetamine, which are then produced in Mexico from the precursors. Indeed, in Mexico, far more so than in other parts of the world, poaching and wildlife trafficking for Chinese markets is increasingly thickly intermeshed with drug trafficking, money laundering, and value transfer in illicit economies. Yet the relationship between Chinese wildlife traders and Mexican organized crime groups is also undergoing significant shifts.

Organized crime groups across Mexico, especially the Sinaloa Cartel, seek to monopolize both legal and illegal fisheries along the entire vertical supply chain. Beyond merely demanding a part of the profits, they dictate to legal and illegal fishers how much the fishers can fish, insisting that the fishers sell the harvest only to the criminal groups, and that restaurants, including those catering to international tourists, buy fish only from the criminal groups. Mexican organized crime groups set prices at which fishers can be compensated and restaurants get paid for the cartels' marine products. The criminal groups also force processing plants to process the fish brought in by the criminal groups. And they charge extortion fees to seafood exporters.

This takeover of the fisheries by Mexican criminal groups puts Chinese traders further into direct contact with them and alters the relationship patterns. Whereas a decade and a half ago, Chinese traders in legal wildlife commodities and illegal wildlife products dealt directly with local hunters, poachers, and fishermen, increasingly, Mexican organized crime groups forcibly inserted themselves as middlemen, dictating that producers need to sell to them and that they themselves will sell to the Chinese traders and traffickers who move the product from Mexico's borders to China.

Conversely, as in illegal logging, the interest of Chinese traders in an animal or plant species and efforts to source them in Mexico on a substantial scale for Chinese markets attracts the attention of Mexican criminal groups.

The Chinese government, for the most part, rejects China's responsibility for poaching and wildlife trafficking in Mexico and insists that these problems are rather for the Mexican government to solve. Prevention and enforcement cooperation has been minimal and sporadic. The Chinese government has not been keen to formalize either China-Mexico or China-Mexico-United States cooperation against wildlife trafficking, preferring informal case-by-case cooperation.

Nonetheless, under intense international pressure, the Chinese government moved beyond seizures of the totoaba swim bladder smuggled to China from Mexico and in 2018 mounted several interdiction raids against retail markets. These raids ended the openly-visible and blatant sales of illegal wildlife commodities. Such retails moved behind closed doors and onto private online platforms. But it does not appear that China has maintained efforts to counter the now-more hidden illegal retail and mount raids against clandestine sales.

Mexican environmental protections and environmental enforcement agencies are becoming weaker as a result of actions of the Andrés Manuel López Obrador administration, even as Mexican natural resources are increasingly under threat from organized crime and wildlife traffickers. Mexican environmental agencies lack mandates, personnel, and equipment to prevent and stop environmental crime. Government officials, legal traders in wildlife commodities, and even law enforcement agencies in Mexico are systematically corrupted and intimidated by organized crime and the poor rule of law environment facilitates poaching, illegal logging, and wildlife trafficking to China.

Preventing far greater damage to Mexico's biodiversity from illegal harvesting and poaching and wildlife and timber trafficking requires urgent attention in Mexico with far more dedicated resources, as well as meaningful international cooperation, to identify and dismantle smuggling networks and retail markets.

## I. INTRODUCTION

China's presence and role in Southeast Asian and African wildlife trade and trafficking are deeply established, extensive, often devastating, and well-known. $^{1}$ China's role in the legal and illegal wildlife trade in Mexico is smaller and less known, receiving far less focus than China-linked wildlife trafficking in the Amazon.

Like elsewhere in the Americas and globally, not all poaching and wildlife trafficking in Mexico is linked to China. But China's demand for Mexican wildlife products, whether legally harvested or poached from the wild, is growing, diversifying, and having severe consequences for biodiversity preservation.

Moreover, China-linked wildlife trafficking in Mexico is expanding amidst an inadequate regulatory environment and enforcement regime. Powerful criminal groups in Mexico which have extensive and growing territorial, political, and economic influence are increasingly entering legal and illegal economies in natural resources, while the rule of law remains weak and the government struggles to mount an effective response.

![](images/9767fba8f25daaa4246dda52774812e9ab7d98de59ad95b1e6a04027af689cb9.jpg)

Far more so than in other parts of the world, poaching and wildlife trafficking for Chinese markets from Mexico is increasingly thickly intermeshed with drug trafficking, money laundering, and value transfer in illicit economies.

Far more so than in other parts of the world, poaching and wildlife trafficking for Chinese markets from Mexico is increasingly thickly intermeshed with drug trafficking, money laundering, and value transfer in illicit economies.

As Chinese wildlife traders in Mexico source an increasing array of animal and plant species for Chinese markets, their relationship with Mexican trafficking groups and local populations has undergone significant shifts. Mexican organized crime groups have inserted themselves as intermediaries between poachers and Chinese traders.

Even as the Chinese government mostly disavows China's responsibility for poaching and wildlife trafficking in Mexico and insists that these problems are rather for the Mexican government to solve, the always weak Mexican environmental protections and environmental enforcement agencies are becoming more emaciated. They lack mandates, personnel, and equipment necessary to effectively prevent and stop environmental crime. Moreover, the government of President Andrés Manuel López Obrador has issued exceptions from environmental impact assessments and oversight under a sweeping executive mandate, $^{2}$ and gutted the budgets of all environmental agencies. Like many other civil society actors, environmental defenders in Mexico face violent intimidation: Between 2012 and 2019, at least 83 were murdered. $^{3}$

The very thin presence of Mexican environmental officials on the ground in protected as well as unprotected areas, coupled with the fact that Mexican criminal groups often exercise dominion and control over extensive territories in Mexico which become no-go zones for government officials and environmental defenders, $^{4}$ also means that visibility into the extent of poaching, illegal logging, and wildlife trafficking in Mexico is difficult, limited, and constrained. Detailed accounts of environmental crime investigations are lacking, as are systematic databases of incidents of environmental crime and data series on poaching. Intrepid work by environmental defenders has documented plant and animal poaching in places such as the Monarch Butterfly Reserve in Michoacán. $^{5}$ However, far more poaching and wildlife trafficking than is reported likely takes place, particularly as Mexican criminal groups are increasingly taking over various economies in natural resources, such as legal and illegal fishing and logging. $^{6}$

In this context and amidst the increasing and diversifying presence of Chinese traders and construction companies in Mexico, ominous trends are likely on the horizon for wildlife in Mexico.

This paper is part of a series of Brookings reports that explores the role of China and Chinese traffickers and consumers in a variety of illegal economies, such as drugs, human trafficking, and natural resources, and China's internal response and international law enforcement cooperation and diplomacy in these issues.

This paper proceeds as follows: It first provides an overview of China-connected wildlife trafficking in Mexico in both terrestrial and marine species, setting it within the broader pattern of poaching and wildlife trafficking in Mexico not related to Chinese markets. It then describes patterns and changes in the interactions and relationships between Mexican organized crime groups and Chinese traders. Next it shows how wildlife trade and trafficking have become means of money laundering and value transfer for the illegal drug trade. In the next part, the report analyzes China-Mexico diplomacy and narratives regarding poaching and wildlife trafficking and China's role in the enforcement of environmental regulations in Mexico. The final section provides detailed recommendations for the governments of Mexico, China, and the United States on how to improve conservation efforts in Mexico and counter poaching and wildlife trafficking from Mexico to China. The recommendations include:

\- law enforcement measures, including interdiction and dismantling of wildlife trafficking networks and in situ law enforcement;

• developing economic incentives for communities not to poach; and

• shutting down problematic retail markets in China.

## Methodology

In addition to consulting the existing literature and building on the author's prior work on wildlife trafficking in Mexico, particularly on totoaba trafficking from Mexico to China, $^{7}$ the report is principally based on 73 interviews with U.S and Mexican diplomats and government and law enforcement officials, Mexican, Chinese, and international conservation biologists, representatives of civil society and environmental NGOs in Mexico, China, and elsewhere and Mexico-based poachers and traders. The author conducted the Mexico-based interviews in person across various parts of the country, including Mexico City, Baja California Sur, Michoacán, and Guerrero. Interviews with interlocutors based in China or elsewhere outside of Mexico were conducted via encrypted virtual platforms. All of the interviews were conducted under extreme sensitivity concerning possible retaliation by China's government (such as government prosecution or visa denials) or by Mexican criminal groups in the form of violence. In some cases, those interviewed had been subject to threats to their life and safety by Chinese as well as Mexican criminal groups. Thus, not only are all the interviews reported below without the use of the name of the source, but at times their location and other identifiers of the interlocutor had to be obscured further. The perception by many Chinese citizens approached for interviews that they had to obtain clearance from the Chinese government before engaging with a U.S. think tank analyst further complicated the interviews. And while Chinese citizens increasingly fear to voice criticism of the Chinese government, access to China for foreign researchers and government officials and information about Chinese law enforcement issues have diminished significantly compared to even just a decade ago.

The author and her research team also examined hundreds of Chinese and international media articles and official government accounts of China's public narratives and policy attitudes toward wildlife trafficking.

## II. WILDLIFE TRAFFICKING IN MEXICO, CONNECTED AND UNCONNECTED TO CHINA

Poaching and wildlife trafficking in Mexico long precedes the emergence of the China connection in both terrestrial and marine species. Mexico features decades-old established poaching for markets within the country, such as in tarantulas for pets or orchids for households, and as part of human-animal conflict, such as the poaching of jaguars to remove presumed threats to cattle. $^{8}$ Much of poaching in Mexico is for local Mexican demand, such as sea turtle meat and eggs, orchids, and birds sold in Guerrero's cities of Acapulco, Chilpancingo, and Chilapa. $^{9}$ Macaws, parrots, hummingbirds, and other birds are also taken from the wild for domestic markets as well as for Central America and the United States for the pet trade and their feathers, or, in the case of hummingbirds, to be made into love protection amulets, in which the dried corpses of poached hummingbirds are wrapped with photographs of loved ones to retain or restore their love. $^{10}$ Mexico City's Sonora Market openly sells endangered plant and animal species, and a wide variety of poached wildlife and wildlife products can be bought in the massive wildlife market in San Luis Potosí. Though perhaps the largest and most well-known, the San Luis Potosí wildlife market is hardly the only market where wildlife trade including in poached species is common, accepted by local communities, and tolerated by government authorities.

Mexico is an important source and transshipment country for poached wildlife smuggled into the United States. Beyond macaws and parrots (for which the United States remains Mexico's principal market), tarantulas, cacti (in which Mexico has the world's greatest biodiversity), and reptiles (alive or their skins) are among the top species trafficked into the United States. $^{11}$ The hummingbird love talismans are also trafficked into the United States for sale among Mexican communities.

In 1997, the Mexican government, motivated to give local communities and private land proprietors economic stakes in conservation and ownership over natural resources on their lands, $^{12}$ implemented the Units for the Conservation, Management, and Sustainable Use of Wildlife (Unidades de Conservación y Manejo de Vida Silvestre or UMA) system. The UMA system grants legal control over the exploitation of natural resources to local communities and private owners. $^{13}$

Such legal and economic control is particularly pertinent for species listed in any category of protection under the Mexican environmental regulations, which UMA grantees can harvest within a government-set quota. Thus, for example, in southern and northern Mexico, several private hunting concessions UMAs have emerged. Local communities have been able to develop their areas for wildlife trade, such as in orchids.

Communities with strong governance structures reap substantial economic profits and have been able to use the system well to protect local biodiversity, when not threatened by organized crime. But these conditions only sometimes materialize, especially as local communities consume wildlife on a relatively small scale, and thus are unable to generate robust income. The last condition — absence of threatening organized crime — has been collapsing across Mexico.

In many parts of Mexico, including areas of richest biodiversity such as southern Mexico, the UMA system has become a gray zone for illegal offtake beyond government permits and quota and the laundering of poached animals. In southern Mexico, for example, UMA owners have been helping American hunters to poach jaguars. $^{14}$

Since anyone who owns land – or can establish even fake land ownership documents – can be granted a UMA, even organized crime groups can buy or forcibly appropriate land and declare it as an UMA. Any such potential criminal group-owned UMAs could become significant areas of major unsustainable harvesting of protecting species for global wildlife markets, such as in China.

Yet monitoring of UMA management and any compliance with harvesting quota in protected species is overwhelmingly weak in Mexico. For one, Mexico does not have “rangers,” i.e., armed law enforcement guards posted in protected areas and able to act against poache

[中间内容因长度限制已省略]

 amordazadas y maniatadas para salvar a la vaquita marina" [NGOs muzzled and handcuffed from saving the vaquita marina], Excelsior, December 15, 2021, https://www.excelsior.com.mx/nacional/ong-maniatadas-salvar-vaquita-marina-alto-golfo-california/1488092.

177 “Sacude’ SEIDO al Cártel del Mar” [SEIDO ‘shake up’ of the Cártel del Mar], Zeta Tijuana, November 16, 2020, https://zetatijuana.com/2020/11/sacude-seido-al-cartel-del-mar/.

178 Author interviews with Mexico-based marine biologists and environmental NGO representatives, by virtual platforms, January and February 2022.

179 Author interviews with current and former Mexican government officials specializing in wildlife crime and environmental protection, Mexican environmental defenders, and U.S. government officials, in Mexico City and other parts of Mexico and by virtual platforms, October and November 2021.

180 Author interviews with current and former Mexican government officials specializing in wildlife crime and environmental protection and U.S. government officials, in Mexico City and other parts of Mexico and by virtual platforms, October and November 2021.

181 Ibid.

182 Author interviews with former Mexican government officials, Mexico City, October 2021.

183 For details, see Vanda Felbab-Brown, The Extinction Market, 198.

184 Enrique Sanjurjo-Rivera, Sarah L. Mesnick, Sara Ávila-Forcada, Oriana Poindexter, Rebecca Lent, Vanda Felbab-Brown, Andrés M. Cisneros-Montemayor, Dale Squires, U. Rashid Sumaila, Gordon Munro, Rafael Ortiz-Rodriguez, Ramses Rodriguez, and Jade F. Sainz, "An Economic Perspective on Policies to Save the Vaquita: Conservation Actions, Wildlife Trafficking, and the Structure of Incentives."

185 Rosie Cooney, Paola Mosig Reidl, and Luis Guillermo Muñoz Lacy, “Community-based trophy hunting of bighorn sheep in Mexico,” (Geneva: CITES, 2019), https://cites.org/sites/default/files/eng/prog/Livelihoods/case\_studies/6.%20Mexico\_bighornsheep\_long\_Aug2.pdf.

186 For examples of payments for ecosystem services and other biodiversity pricing schemes, their design, and the challenges they encounter, see, for example, Ina Porras and Paul Steele, “Making the market work for nature: How biocredits can protect biodiversity and reduce poverty,” (London: International Institute for Environment and Development, March 2020), https://pubs.iied.org/sites/default/files/pdfs/migrate/16664IIED.pdf.

187 For details on the limitations of anti-money laundering measures and their capacity to bankrupt wildlife trafficking groups, see Vanda Felbab-Brown, The Extinction Market, 205-218.

## ABOUT THE AUTHOR

Vanda Felbab-Brown is a senior fellow in Foreign Policy at the Brookings Institution. She is also the director of Brookings's Initiative on Nonstate Armed Actors and co-director of its Africa Security Initiative as well as of the 2020 paper series "The opioid crisis in America: Domestic and international dimensions." Dr. Felbab-Brown is an expert on international and internal conflicts, insurgency, terrorism, urban violence, and illicit economies. Her fieldwork has covered Afghanistan, South Asia, Myanmar, Indonesia, the Andean region, Mexico, Iraq, the Horn of Africa, Nigeria, and other African regions. She is the author of five books: Narco Noir: Mexico's Cartels, Cops, and Corruption (forthcoming); The Extinction Market: Wildlife Trafficking and How to Counter It (2017); Militants, Criminals, and Warlords: The Challenge of Local Governance in an Age of Disorder (2017, co-authored with Shadi Hamid and Harold Trinkunas); Aspiration and Ambivalence: Strategies and Realities of Counterinsurgency and State-Building in Afghanistan (2013); and Shooting Up: Counterinsurgency and the War on Drugs (2010). Dr. Felbab-Brown received her Ph.D. in political science from MIT and her B.A. in government from Harvard University.

## ACKNOWLEDGEMENTS

I am deeply grateful to the anonymous reviewers for their very helpful suggestions. My special thanks go to Kristin Nowell for invaluable field research suggestions as well as several other researchers who prefer to remain anonymous. I would also like to thank Nathan Paul Southern and Lindsey Kennedy for their investigative work in locating additional valuable interlocutors in Asia and the Pacific for me to interview for this project. My deep thanks also go to Bradley Porter, Abigail Zisus, Wazhma Yousafi, and Ryan Harbison for great research assistance and other project support and to Cindy Zhou for her excellent research support in Chinese and more. Enormous thanks also to Ted Reinert for this superb editing of the paper and Rachel Slattery for the terrific layout. Finally, I would like to deeply thank all of my many interlocutors in Mexico, Asia and the Pacific, and the United States who were willing to speak with me, sometimes at the risks of serious repercussions from authoritarian or corrupt government officials or organized crime groups.

Brookings is grateful to the U.S. Department of State and the Institute for War and Peace Reporting for funding this research.

The Brookings Institution is a nonprofit organization devoted to independent research and policy solutions. Its mission is to conduct high-quality, independent research and, based on that research, to provide innovative, practical recommendations for policymakers and the public. The conclusions and recommendations of any Brookings publication are solely those of its author(s), and do not reflect the views of the Institution, its management, or its other scholars.

![](images/2f505c8335626f1501632dacd0ffb9a01bf0df25a5bc651a64395aeac948a49b.jpg)

## BROOKINGS

The Brookings Institution
1775 Massachusetts Ave., NW
Washington, D.C. 20036
brookings.edu
"""
