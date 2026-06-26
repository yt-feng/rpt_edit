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
- 已识别机构名：`世界银行`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如高盛、摩根士丹利、汇丰、摩根大通、瑞银、花旗、美国银行、巴克莱、德意志银行、野村。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份世界银行研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
# Bridging Conflicts and Biodiversity Protection The Critical Role of Reliable and Comparable Data

Brian Blankespoor

Susmita Dasgupta

David Wheeler

POLICY RESEARCH WORKING PAPER 11076

## Abstract

Biodiversity is essential for ecological stability, human well-being, and economic progress, providing critical ecosystem services such as clean water, food, and climate regulation. However, it faces unprecedented threats, with extinction rates accelerating to 1,000 times the natural baseline due to habitat destruction, overexploitation, pollution, invasive species, illegal trade, and climate change. Effective conservation requires urgent, coordinated global action, as ecosystems and species habitats often transcend national borders. Collaboration among governments, industries, and communities is essential to restore habitats, protect endangered species, strengthen policies, and enforce conservation measures. The challenges of biodiversity conservation are particularly acute in geopolitically sensitive and overlapping regions, including non-determined legal status territories, fragile and conflict-affected situations, and transboundary ecosystems. In these areas, effective conservation is hindered by weak policies, inconsistent enforcement, and institutional fragility. This paper addresses these challenges by providing baseline data to guide conservation strategies. Using newly developed World Bank species occurrence maps based on open-access, date-stamped records from the Global Biodiversity Information Facility, the study evaluates species richness, endemism, and extinction risks across 35 non-determined legal status territories, 19 conflict-affected countries, 20 fragile states, 18 marine joint regimes, and 311 international river basins. The data sets reveal that these regions host numerous, often vulnerable, species. Biodiversity conservation emerges as a pathway for trust-building and collaboration, aligning stakeholders around shared goals such as climate resilience and sustainable livelihoods. Reliable and comparable data sets are critical for evidence-based planning, fostering dialogue and cooperation among divided groups. The estimates presented in this paper aim to support robust, data-driven strategies to safeguard biodiversity in geopolitically sensitive and overlapping regions, with far-reaching implications for global conservation and international cooperation.

# Bridging Conflicts and Biodiversity Protection: The Critical Role of Reliable and Comparable Data

Brian Blankespoor, $^{a}$ Susmita Dasgupta, $^{b}$ and David Wheeler $^{c}$

a. Senior Geographer, Development Economics Data Group, World Bank, bblankespoor@worldbank.org

b. Lead Environmental Economist, Development Research Group, World Bank, sdasgupta@worldbank.org

c. Consultant, World Bank, wheelrdr@gmail.com

Corresponding author: Brian Blankespoor, Senior Geographer, Development Economics Data Group, MC-9-204, The World Bank, 1818 H Street, Washington, DC 20008, USA. Tel: 1-202-473-1546. Email: bblankespoor@worldbank.org

Keywords: Biodiversity Conservation; Non-determined legal status Territories; Fragile and Conflict-Affected Situations, Transboundary Ecosystems; Marine Joint Regimes; International River Basins

JEL Classifications: Q34; Q25; Q57

Funding: This research was funded by the Global Environment Facility (GEF).

Acknowledgments: This research was funded by a grant from the Global Environment Facility to a World Bank program managed by Nagaraja Harshadeep Rao, Susmita Dasgupta and Brian Blankespoor. Georeferenced species occurrences reported by GBIF were accessed from Google BigQuery on 2024-02-17. We are thankful to Ms. Polly Means and Mr. Pritthijit (Raja) Kundu for their help with the graphics.

The findings, interpretations, and conclusions expressed in this paper are entirely those of the authors. They do not necessarily represent the views of the International Bank for Reconstruction and Development/World Bank and its affiliated organizations, or those of the Executive Directors of the World Bank or the governments they represent.

## Introduction

Biodiversity conservation is essential for sustainable development, poverty reduction, and a healthy planet. It supports ecosystems that are fundamental to human livelihoods by providing food, clean water, and climate stability. Healthy ecosystems ensure the availability of natural resources critical to agriculture, fishing, and forestry, helping to alleviate poverty and promote sustainable economic growth. Additionally, biodiversity preservation supports industries like ecotourism and pharmaceuticals, which generate revenue and create jobs, further contributing to shared prosperity. Maintaining biodiversity is also a key to a livable planet, as it strengthens the resilience of ecosystems that regulate the climate by sequestering carbon and mitigating the impacts of climate change. Ecosystems such as forests, wetlands, and oceans act as natural buffers, stabilizing global temperatures and sustaining life on Earth. Thus, investing in biodiversity conservation is crucial not only for environmental health, but also for human well-being and global sustainability.

However, biodiversity is declining at an alarming rate. A recent UN report by the Intergovernmental Science-Policy Platform on Biodiversity and Ecosystem Services revealed that 1 million species are near extinction, with the rate of extinctions accelerating despite increasing awareness of the interconnectedness between human life and nature (IPBES 2019). This report, based on a systematic review of approximately 15,000 scientific and governmental sources, aligns with the findings of the Living Planet Index, $^{1}$ which has recorded a 68% decline in global biodiversity since 1970. The primary drivers of this crisis include habitat destruction, overexploitation of resources, pollution, illegal wildlife trade, invasive species and climate change.

In response to these unprecedented losses, immediate and coordinated international action is required. Every country and territory must actively engage in biodiversity conservation to halt further biodiversity decline. Nations need to implement effective policies and conservation strategies tailored to local ecosystems, while leveraging global frameworks such as the Convention on Biological Diversity (CBD) and the United Nations Sustainable Development Goals (SDGs).

One of the significant barriers to effective conservation is the impact of human conflicts, particularly in weakly-governed areas. These regions often experience destructive effects on biodiversity, spanning terrestrial, marine, and freshwater ecosystems. Physical damage to landscapes, habitat destruction, pollution, and overexploitation of natural resources are common consequences of such conflicts. Military dimensions of conflicts can further exacerbate these challenges by diverting resources from environmental protection and disrupting natural food webs and migratory patterns (Rist, Norstrom, and Queiroz 2024; Parkinson and Cottrell 2022). The academic literature extensively documents the challenges of biodiversity conservation within non-determined legal status territories and conflict zones (e.g., Greiner 2012; Daskin and Pringle 2018; Hanson 2018).

Moreover, weak governance and fragmented authority in non-determined legal status territories create additional complications. Conflicting territorial claims can undermine environmental protection and allow unchecked exploitation of natural resources. The institutional landscape in these areas often features competing authorities, which results in inconsistencies in law enforcement and resource management (Beckman, 2013). Although international interventions aim to foster stability, they frequently lack robust enforcement mechanisms. This instability can prolong conflicts, deepen socio-economic inequalities, and intensify environmental degradation (Buhaug et al., 2014).

In conflict zones, governance often collapses, making effective environmental protection nearly impossible. For instance, recent events in the Syrian Arab Republic and the Republic of Yemen have led to the collapse of public institutions, with attention shifting to immediate survival and security needs, leaving environmental concerns neglected (World Bank, 2011). To address these challenges, efforts to conserve biodiversity in affected regions must be preceded by the restoration of national and international cooperation to rebuild trust and establish shared conservation goals (Gaind et al., 2016).

While human conflict areas present significant challenges for biodiversity conservation due to governance gaps and instability, transboundary river basins also face complex issues—ranging from competing national interests to opportunities for cooperation—requiring coordinated efforts to address shared environmental concerns and manage resources sustainably across borders. Effective conservation in such areas requires objective, reliable, and comparable data from all riparian entities. In practice, weak governance and political or social instability often make it difficult for officially-designated institutions to collect the necessary data (Cohen and Arieli 2011). This is particularly true in regions with competing territorial claims, where data collection and conservation efforts are frequently obstructed. In this context, recent studies (Turner et al., 2015; Levin et al., 2019; Mobaied and Rudant 2019; Garzón and Valánszki 2020; Aung 2021) have emphasized the potential importance of remote sensing from satellite platforms. These technologies offer a promising solution by providing valuable and consistently collected real-time data from areas that may otherwise be inaccessible or where traditional monitoring is too challenging.

The Global Biodiversity Information Facility (GBIF) is also playing a critical role in overcoming these barriers. By acquiring and distributing data on species sightings from concerned organizations and individuals, the GBIF is providing essential information in areas where officially-supported monitoring may be sparse or difficult to implement. This collaboration strengthens global conservation efforts by making vital data more accessible, even in fragile or conflict-affected regions.

To implement effective conservation strategies in such contexts, accurate, location-specific data are crucial. The importance of this data for identifying critical biodiversity areas and tracking conservation progress has been highlighted in numerous studies. However, inconsistencies in data across countries and administrative boundaries hinder the accurate assessment of ecosystem health and biodiversity trends (Urbano et al., 2024; Geijzendorffer et al., 2016; Pereira et al., 2013). Moreover, the growing gap between emerging threats and infrequently updated data, often managed by underfunded institutions, presents an ongoing challenge.

To help address this gap, we have produced new public datasets by utilizing millions of georeferenced species occurrence records from the Global Biodiversity Information Facility (GBIF) (Dasgupta et al. 2024a). Using machine-based pattern recognition, we developed a comprehensive database covering the occurrence regions of nearly 600,000 species. These maps were validated by comparing them with expert-reported maps for mammals, ants, and vascular plants, revealing strong correlations in global distribution patterns. Our expanded database includes a broad array of species across terrestrial, freshwater, and marine environments, encompassing arthropods, mollusks, invertebrates, plants, fungi, and more, alongside traditionally studied amphibians, birds, fish, reptiles, and mammals. Figure 1 illustrates the composition of this expanded database, revealing new global distribution patterns that can inform conservation planning.

In this paper, we focus on the implications of our results for biodiversity protection in transboundary regions, $^{2}$ joint marine regions, $^{3}$ non-determined legal status areas, $^{4}$ and fragile and conflict-affected situations areas (FCS). $^{5}$ Conflicts and coordination failures in such areas have numerous direct and indirect impacts on biodiversity (see Rist, Norstrom and Queiroz (2024) for a review of the relationships between biodiversity, peace and conflict). These are often difficult to address in non-determined legal status areas and FCSs because of weak governance, limited administrative capacity, and insufficient institutions and policies. The effective protection of biodiversity in transboundary areas must rely on cooperation among the parties involved.

Preserving habitats for endemic species, those with restricted ranges, and species at high extinction risk requires special conservation measures tailored to vulnerable and geopolitically complex regions.

The expansion of species information using GBIF records offers a significant expansion of the objective, comparable and reliable data that are critical for successful implementation of transboundary and fragile/conflict state conservation measures. In this paper, we illustrate the potential contribution of our GBIF database data with results for 38 non-determined legal status area areas, 19 conflict-affected countries, 19 countries with pronounced institutional and social fragility, and 311 international river basins.

Figure 1: Total count of species  
![](images/9840bf572b0284d1f0d576ad183fd9e903d45065a5b63ce06d93eda64cc3fdc9.jpg)

<table><tr><td>[Class/Order]</td><td>Group</td><td>Count</td></tr><tr><td rowspan="5">Vertebrates [Class] 50,825</td><td>Amphibians</td><td>5,026</td></tr><tr><td>Birds</td><td>10,845</td></tr><tr><td>Mammals</td><td>4,377</td></tr><tr><td>Reptiles</td><td>7,544</td></tr><tr><td>Fish</td><td>23,033</td></tr><tr><td rowspan="7">Arthropods [Order] 209,908</td><td>Araneae</td><td>10,307</td></tr><tr><td>Coleoptera</td><td>43,660</td></tr><tr><td>Diptera</td><td>23,321</td></tr><tr><td>Hemiptera</td><td>13,123</td></tr><tr><td>Hymenoptera</td><td>25,924</td></tr><tr><td>Lepidoptera</td><td>50,037</td></tr><tr><td>Other</td><td>43,536</td></tr><tr><td rowspan="11">Vascular Plants [Order] 229,595</td><td>Asparagales</td><td>17091</td></tr><tr><td>Asterales</td><td>22841</td></tr><tr><td>Caryophyllales</td><td>9321</td></tr><tr><td>Ericales</td><td>8545</td></tr><tr><td>Fabales</td><td>16194</td></tr><tr><td>Gentianales</td><td>13317</td></tr><tr><td>Lamiales</td><td>16436</td></tr><tr><td>Malpighiales</td><td>12632</td></tr><tr><td>Myrtales</td><td>10253</td></tr><tr><td>Poales</td><td>16,433</td></tr><tr><td>Other</td><td>86,532</td></tr><tr><td>Fungi</td><td></td><td>37,450</td></tr><tr><td colspan="2">Non-animal, non-plant species: protozoans, bacteria, etc.</td><td>16,540</td></tr><tr><td colspan="2">Other Animals: Molluscs, etc.</td><td>53,214</td></tr><tr><td>Total</td><td></td><td>597,532</td></tr></table>

## Data and Method

The data for this study have been provided by the Global Biodiversity Information Facility (GBIF), a global network, funded by various national governments, that offers open access to comprehensive data on global biodiversity. The GBIF provides a repository of georeferenced, time-stamped species occurrence records that are constantly updated in collaboration with the Catalogue of Life partnership (https://www.catalogueoflife.org), Biodiversity Information Standards (https://www.tdwg.org/), Consortium for the Barcode of Life (CBOL) (http://www.barcodeoflife.org/), Encyclopedia of Life (EOL) (http://eol.org), Global Earth Observation System of Systems (GEOSS) (https://earthobservations.org/geoss.php) and other organizations. The GBIF records span multiple taxa, including animals, plants, fungi, and microbes. Users can directly access these records through GBIF's Occurrence and Maps APIs (https://www.gbif.org/developer/occurrence, https://www.gbif.org/developer/maps), and access to the database is also provided by cloud platforms like Google BigQuery and Amazon Web Services (AWS).

For the analysis presented here, we processed large-scale datasets using Google BigQuery, which efficiently handles vast amounts of biodiversity data. The GBIF occurrence records were filtered to include only those that met specific criteria: we selected records from 1970 onwards and focused on species that had at least three unique reporting locations and five occurrence reports. Additionally, to manage computational efficiency, we limited species with excessive data, such as the American Robin (Turdus migratorius), to a maximum of 20,000 randomly sampled records. This filtering approach ensured that computational resources were effectively used, without sacrificing the integrity of the data.

We adhered to GBIF's occurrence reporting protocols, which ensure consistency in the way species records are documented and shared across the global community. This adherence to protocol is essential for maintaining the reliability and comparability of biodiversity data.

## Species Occurrence Mapping

To generate species occurrence maps, we employed machine-based techniques for pattern recognition and cluster analysis. For most species (93.6% of the dataset), we applied a spatial boundary construction method known as the alphahull algorithm (Pateiro-López and Rodríguez-Casal, 2010). This method, well-established in the literature (Guo et al., 2022; Kass et al., 2022), allowed for the precise delineation of species' occurrence regions across terrestrial, freshwater, coastal, and marine environments. For the remaining species, we utilized a k-means clustering algorithm combined with convex hulls to estimate their geographic distributions.

To validate the accuracy of our generated maps, we compared them with expert-verified maps from well-regarded datasets of mammals (Marsh et al., 2022), ants (Kass et al., 2022), and vascular plants (Borgelt et al., 2022). These comparisons demonstrated strong correlations between our maps and those generated by subject-matter experts. Figure 2 provides two examples of species occurrence regions: one for an endemic species, Scherya bahiensis, which is confined to a small region in Brazil, and one for a non-endemic species, Lagidium viscacia (the Mountain Viscacha), which has a broader distribution across several countries in South America. These examples illustrate the contrasting distribution patterns of species with restricted versus extensive geographic ranges.

To illustrate, effective biodiversity conservation plans depend on accurately identifying regions with species that are either endemic (i.e., species confined to a specific geographic area, often within

[中间内容因长度限制已省略]

butions harmonized to three taxonomic authorities. Journal of Biogeography, 49(5), 979-992.

McCracken, M., & Wolf, A. T. (2019). Updating the Register of International River Basins of the World. International Journal of Water Resources Development, 35(5), 732–82. https://doi.org/10.1080/07900627.2019.1572497

McPherson, M., & Ropicki, A. (2021). Network analysis of collaboration and information sharing in the management of the Lower Mekong River Basin. Ocean & Coastal Management, 199, 105356.

Mekong River Commission (MRC). (2024). Vision and mission. https://www.mrcmekong.org/vision-and-mission

Mobaied, S., & Rudant, J. P. (2019). New method for environmental monitoring in armed conflict zones: A case study of Syria. Environmental Monitoring and Assessment, 191(11), 643.

Montefalcone, M., Tunesi, L., & Ouerghi, A. (2021). A review of the classification systems for marine benthic habitats and the new updated Barcelona Convention classification for the Mediterranean. Marine Environmental Research, 169, 105387.

Nile Basin Initiative (NBI). (2010). Agreement on the Nile River Basin Cooperative Framework. https://nilebasin.org/about-us/cooperative-framework-agreement (accessed 11 December 2024).

Nile Basin Initiative (NBI). (2021). Nile Basin Monitoring Guideline, NBI Technical Reports: Wetlands and Biodiversity series, 2021-14: 1-23.

Paisley, R. K., & Henshaw, T. W. (2013). Transboundary governance of the Nile River Basin: Past, present and future. Environmental Development, 7, 59-71.

Parkinson, S., & Cottrell, L. (2022). Estimating the military's global greenhouse gas emissions. https://policycommons.net/artifacts/3154663/sgr2bceobs-estimating\_global\_military\_ghg\_emissions\_nov22/3952525/ (Accessed October 2024).

Pateiro-López, B., & Rodríguez-Casal, A. (2010). Generalizing the convex hull of a sample: The R package Alphahull. Journal of Statistical Software, 34(5).

Pereira, H. M., Ferrier, S., Walters, M., Geller, G. N., Jongman, R. H., Scholes, R. J., et al. (2013). Essential Biodiversity Variables. Science, 339(6117), 277-278.

Petersen-Perlman, J. D., Veilleux, J. C., & Wolf, A. T. (2017). International water conflict and cooperation: Challenges and opportunities. Water International, 42(2), 105-120.

Plumptre, A. J., Davenport, T. R., Behangana, M., & Kityo, R. (2010). Conservation of the Albertine Rift biodiversity. Biological Conservation, 143(5), 1151-1154.

Plumptre, A. J., Davenport, T. R., Behangana, M., Kityo, R., Eilu, G., Ssegawa, P., ... & Moyer, D. (2007). The biodiversity of the Albertine Rift. Biological Conservation, 134(2), 178-194.

Raftopoulos, E. (1992). The Barcelona Convention System for the Protection of the Mediterranean Sea against Pollution: An international trust at work. International Journal of Estuarine & Coastal Law, 7, 27.

Rist, L., Norström, A., & Queiroz, C. (2024). Biodiversity, peace and conflict: Understanding the connections. Current Opinion in Environmental Sustainability, 68, 101431.

Roberson, L. A., Beyer, H. L., O'Hara, C., Watson, J. E., Dunn, D. C., Halpern, B. S., ... & Runting, R. K. (2021). Multinational coordination required for conservation of over 90% of marine species. Global Change Biology, 27(23), 6206-6216.

Stroud, D. A., Davidson, N. C., Finlayson, C. M., & Gardner, R. C. (2022). Development of the text of the Ramsar Convention: 1965–1971. Marine and Freshwater Research, 73(10), 1107-1126.

Tatem, A. J. (2017). WorldPop, open data for spatial demography. Scientific Data, 4, 170004. https://doi.org/10.1038/sdata.2017.4.

Turgul, A., McCracken, M., Schmeier, S., Rosenblum, Z. H., de Silva, L., & Wolf, A. T. (2024). Reflections on transboundary water conflict and cooperation trends. Water International, 49(3-4), 274-288.

Turner, W., Rondinini, C., Pettorelli, N., Mora, B., Leidner, A. K., Szantoi, Z., ... & Woodcock, C. (2015). Free and open-access satellite data are key to biodiversity conservation. Biological Conservation, 182, 173-176.

UN (1997). United Nations Convention on the Law of the Non-Navigational Uses of International Watercourses. United Nations.

Urbano, F., Viterbi, R., Pedrotti, L., Vettorazzo, E., Movalli, C., & Corlatti, L. (2024). Enhancing biodiversity conservation and monitoring in protected areas through efficient data management. Environmental Monitoring and Assessment, 196(1), 12.

Wolmer, W. (2003). Transboundary conservation: The politics of ecological integrity in the Great Limpopo Transfrontier Park. Journal of Southern African Studies, 29(1), 261-278.

World Bank. (2011). World Development Report 2011: Conflict, Security, and Development. Washington, DC: World Bank.

World Bank. (2022). Defueling conflict: Environment and natural resource management as a pathway to peace. https://www.worldbank.org/en/topic/environment/publication/defueling-conflict-environment-and-natural-resource-management-as-a-pathway-to-peace

WorldPop (www.worldpop.org - School of Geography and Environmental Science, University of Southampton; Department of Geography and Geosciences, University of Louisville; Département de Géographie, Université de Namur) and Center for International Earth Science Information Network (CIESIN), Columbia University (2018). Global High Resolution Population Denominators Project - Funded by The Bill and Melinda Gates Foundation (OPP1134076). https://dx.doi.org/10.5258/SOTON/WP00647

Zambezi River Authority, SIDA, & Norwegian Embassy Lusaka. (2008). Integrated Water Resources Management Strategy and Implementation Plan for the Zambezi River Basin (ZAMSTRAT). https://zambezicommission.org/publication/integrated-water-resources-management-strategy-and-implementation-plan-zambezi-river-1 (Accessed 11 December 2024).
"""
