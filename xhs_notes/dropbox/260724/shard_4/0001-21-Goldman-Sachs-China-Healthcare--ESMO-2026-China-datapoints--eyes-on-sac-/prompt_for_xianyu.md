你是闲鱼资料类商品文案编辑，擅长把一份投研/行业/公司研报改写成适合闲鱼发布的商品说明。

【目标】
- 基于下面研报解析内容，生成一份可以复制到闲鱼商品详情里的中文文案。
- 风格参考用户提供的闲鱼对标笔记：标题直给、信息密度高、用途明确、适合人群明确、交付方式清楚。
- 语言要自然，像真实卖家发布，不要像公众号文章、小红书笔记或 AI 摘要。
- 不要使用太夸张的营销词，不要承诺收益，不要说“稳赚”“内幕”“必涨”。
- 可以适度口语化，但不要低俗。
- 硬性要求：全文不要使用任何 emoji 或符号表情。
- 硬性要求：全文必须低于 1500 字，宁可少写，也不要超长。

【必须输出结构】
1. `闲鱼标题：` 一行，控制在 30 字以内，适合商品标题。
2. `商品描述：` 正文，适合直接粘贴到闲鱼详情页。
3. `Hashtag：` 一行，给 6-10 个平台可用标签，用 `#` 开头，空格分隔。

【长度硬性要求】
- 输出总字数必须低于 1500 字，包括标题、商品描述、Hashtag。
- 商品描述控制在 900-1200 字以内，避免写成长文。
- 亮点 bullet 每条控制在 30 字以内。

【严禁输出】
- 不要输出 `建议价格：`。
- 不要输出 `搜索关键词：`。
- 不要输出“搜索词”“关键词”“搜索关键词”等栏目。
- 不要给具体价格区间、成交承诺或价格建议。
- 不要使用任何 emoji，例如 ✅、🔥、📌、👉、💰、⭐ 等。

【商品描述写法】
- 第一段：直接说明这是什么报告，页数/语言/主题/公司或行业。如果页数、日期、语言不确定，就不要编。
- 第二段：说明适合谁，比如投研、券商面试、PE/VC、行业研究、学习参考、写报告等。
- 第三段：用 3-5 个亮点 bullet，风格参考：
  - 三大情景框架：DCF、P/ARR、EV/Sales
  - 关键变量分析
  - 估值逻辑、假设、终值占比等核心内容覆盖
  - 适合准备 AI 相关面试、研究 AI 估值的同学
- 第四段：交付说明，参考：`资料为电子版 PDF，拍下后 24 小时内发网盘链接或邮箱。`
- 第五段：虚拟商品说明，参考：`电子类资料一经发货不退不换，有问题可以提前咨询。`
- 可以补一句：`需要其他报告也可以私聊，支持一站式咨询。`

【Hashtag 写法】
- 只输出平台相对安全、偏学习和资料属性的标签。
- 推荐从这些里选择：`#学习资料` `#研究笔记` `#学习笔记` `#行业研究` `#研报资料` `#资料整理` `#报告学习` `#案例研究`。
- 不要输出 `#财经` `#投资` `#股票` `#基金` `#理财` `#暴富` `#内幕` 等敏感标签。

【平台发布合规要求】
- 不要出现“投资建议”“买入”“卖出”“强烈推荐”“稳赚”“保本”“必涨”“抄底”“上车”“内幕”“翻倍”等金融操作或收益承诺表达。
- “投资”相关词尽量改成“投研”“研究”“观察”“学习参考”；如果必须保留，也要保持中性。
- 不要出现“独家”“原版”“内部”“无水印”“全网最低”“最全”“最强”“必看”等高风险或极限词。
- 不要写“关注”“点赞”“求关注”“评论区留言”等直接互动诱导。
- 不要承诺资料一定可用于获利、就业、通过面试或获得收益。

【合规与避坑】
- 默认避免出现具体投行品牌名，比如“GS”“GS”“MS”，统一写作“投行研报”或“投行研报”。
- 不要承诺研究或交易结果。
- 不要伪造页数、日期、作者、公司覆盖范围。研报未给出时就不写。
- 不要输出解释说明，只输出闲鱼文案本身。

【研报解析内容】
"""
# China Healthcare: ESMO 2026 China datapoints: eyes on sac-TMT Lung06 data and Zoci in 1L SCLC

The 2026 European Society for Medical Oncology (ESMO) Congress, taking place in Madrid on October 23-27, has released regular abstract titles, and we summarize key assets and datapoints from selected China pharma/biotech companies to watch, and highlight PD-1 multi-specifics, DLL3-targeting therapies (led by Zai Lab's ZL-1310), evolving ADC landscape, and emerging RAS inhibitors. Late-breaking abstracts (LBA) titles will be released on September 25, and full abstracts will be available on October 19, 00:05 CEST, for detailed readouts.

Following Kelun Biotech's announcement that China ph3 OptiTROP-Lung06 trial (1L nsq-NSCLC with PD-L1 TPS<1%) has met the primary endpoints (PFS), anticipation is building for the potential release of detailed data at ESMO as LBA (see our note). While the LBA submission is still in process (deadline on Sep 8), we await the final release of titles on Sep 25, and expect Lung06 data to be one of the top focuses if its attendance is confirmed. We also see a broadening horizon for ADCs with notable clinical outcomes, including 1) ADC combo data: ph2 data of SHR-1826 (cMET ADC, Hengrui) in combo with PD-L1 and CTLA-4 inhibitors in 2L+ nsqNSCLC, and ph1 data of SHR-A1904 (CLDN18.2 ADC, Hengrui) in combo with adebrelimab (± chemo) in 1L GC/GEJC will be released, while our eyes will be on compatibility – the combination impact on the treatment profile, especially the balance between the overlapping toxicity and incremental benefits it would bring; and 2) novel ADC clinical data debut: a bispecific ADC targeting EGFR/c-MET(HS-20122, Hansoh) and a new CDH17 ADC (CM518D1, Keymed) will have preliminary ph1 readouts in solid tumors, as we monitor differentiation trends in this modality.

DLL3 therapies in SCLC with eyes on zoci in front-line: New clinical progress from DLL3-targeting therapies for SCLC will be presented at the conference, featuring 1) ph1b/1c results of zoci (ZL-1310, DLL3 ADC, Zai Lab) in 1L SCLC in combo with atezo ± carboplatin. We noted that this data, as the key catalyst for Zai Lab in 2H26, will be crucial for zoci to deepen its differentiation in the SCLC landscape together with its well-controlled safety profile, given the largely comparable efficacy across competing therapies in 2L setting; 2) updated OS from ph1 of alveltamig (DLL3/DLL3/CD3 TsTCE, Zelgen) as monotherapy in 2L+ SCLC with extended follow-up. Recall that alveltamig showed an 18-month OS rate of 58.6% in the ASCO readout, implying potentially 20-25 months of median OS to be confirmed this time. This result can be compared to tarlatamab's latest 2L OS updates from its ph3 DeLLphi-304, which will also be released at the conference (previously reported at

Ziyi Chen
+852-2978-0526 | ziyi.chen@gs.com
GS (Asia) L.L.C.

Linhai Zhao, Ph.D.
+852-3966-4059 | linhai.zhao@gs.com
GS (Asia) L.L.C.

Honglin Yan
+852-2978-6666 | honglin.yan@gs.com
GS (Asia) L.L.C.

Eddie Song  
+852-2978-6426 | eddie.song@gs.com  
GS (Asia) L.L.C.

13.6m). We view this comparison as a benchmark for the positioning of alveltamig in the SCLC competition; 3) long-term ph1 survival data update of Hengrui's DLL3 ADC (SHR-4849) in 2L+ SCLC, plus first ph1/2 data from a DLL3 TCE (SHR-7787); and 4) potential peek at early phase 3 data of Hansoh's HS-20093 (B7H3 ADC) in 2L SCLC from its Trial-in-progress (TiP) abstract, which could further validate the efficacy of B7H3 class on 2L SCLC beyond preliminary phase 2 data and provide better visibility on 2L landscape. Aside from DLL3, SKB500 (B7H3 ADC, Kelun Biotech) will also have data in 2L+ SCLC presented with efficacy and safety updates.

Incremental updates from PD-1 multi-specifics: This year's ESMO features a developing multi-specific antibody landscape with maturing clinical data, we highlight 1) ivonescimab (PD-1/VEGF BsAb, Akeso) in a basket of solid tumors as front-line therapy (renal cell carcinoma (RCC), thymic carcinoma, esophageal squamous cell carcinoma (ESCC), and endometrial cancer), as well as a sub-cohort study on intracranial PFS in NSCLC patients with brain metastases; 2) ph2 dose expansion data from CStone's trispecific CS2009 (PD-1/VEGF/CTLA-4 TsAb) in advanced NSCLC and ph1/2 data in mCRC, as an update to the preliminary readout announced at ASCO2026. We view the incremental data as important support for the planned ph3 MRCT initiation starting YE26; 3) updates from Innovent's IBI363 (PD-1/IL-2α-bias BsAb) in 1L NSCLC (+ chemo) and in a head-to-head trial with docetaxel in IO-resistant AGA(-)NSCLC (+ bevacizumab), together with first readouts from ph1 trial in 1L gastric or gastroesophageal junction adenocarcinoma (G/GEJA). We pay attention to the special dosing scheme for 1L NSCLC, and the differentiated long-tail benefit in IO-treated squamous NSCLC, as previously shown in the ASCO update; 4) pumitamig's ph2 readouts (PD-L1/VEGF-A BsAb, BioNTech) in neuroendocrine neoplasms and SCLC or TNBC with brain metastases; and 5) first global ph2 data of a combo between PD-L1/VEGF BsAb (pumitamig, BioNTech) and ADC (DB-1311, B7-H3 ADC, Duality/BioNTech) in solid tumors.

Emerging targeted therapies on RAS mutants: Treatments targeting RAS mutation have received increasing attention, especially after Revolution Medicines (RevMed) announced a bar-setting result from ph3 RASolute302 of its panRAS inhibitor daraxonrasib in 2L+ PDAC earlier this year. At ESMO, we see a collection of RAS/KRAS inhibitors to present newest data, including 1) KRAS G12D inhibitors: HRS-4642 (Hengrui), INCB161734 (Incyte) and GFH375 (GenFleet, in LBA per company) will all have ph1/ph2 readouts in PDAC with KRAS G12D mutation, which can be cross-compared against zoldonrasib's data (KRAS G12D inhibitor, RevMed) released at ESMO GI; and 2) panRAS molecular glue: GenFleet's GFH276 will publicize its first ph1 data in solid tumors as LBA (per company).

Exhibit 1: Abstract information at ESMO 2026 from Chinese pharma/biotech

<table><tr><td>Abstract</td><td>Session</td><td>Asset</td><td>MoA</td><td>Modality</td><td>Study focus</td><td>Regimen</td><td>Data type</td><td>Must-read</td></tr><tr><td colspan="9">Abbisko (2256.HK)</td></tr><tr><td>3747P</td><td>Poster</td><td>pimicotinib</td><td>CSF-1R</td><td>Small molecule</td><td>TGCT</td><td>Mono</td><td>Phase 3</td><td>★</td></tr><tr><td colspan="9">Akeso (9926.HK)</td></tr><tr><td>4156RO</td><td>Rapid Oral</td><td>ivonesimab</td><td>PD-1/VEGF</td><td>BsAb</td><td>1L r/m thymic carcinoma</td><td>+ chemo</td><td>Phase 2</td><td>★★</td></tr><tr><td>3592RO</td><td>Rapid Oral</td><td>ivonesimab</td><td>PD-1/VEGF</td><td>BsAb</td><td>1L aRCC</td><td>Mono</td><td>Phase 1b/2</td><td>★★</td></tr><tr><td>2711P</td><td>Poster</td><td>ivonesimab</td><td>PD-1/VEGF</td><td>BsAb</td><td>Adv NSCLC</td><td></td><td></td><td>★</td></tr><tr><td>2649P</td><td>Poster</td><td>ivonesimab</td><td>PD-1/VEGF</td><td>BsAb</td><td>Adv NSCLC</td><td></td><td>Phase 3</td><td>★</td></tr><tr><td>706P</td><td>Poster</td><td>ivonesimab</td><td>PD-1/VEGF</td><td>BsAb</td><td>Glioblastoma</td><td>+ temozolomide</td><td>Phase 1b/2</td><td>★</td></tr><tr><td>1266P</td><td>Poster</td><td>ivonesimab</td><td>PD-1/VEGF</td><td>BsAb</td><td>EC</td><td>Mono</td><td>Phase 2</td><td>★</td></tr><tr><td>2908P</td><td>Poster</td><td>ivonesimab</td><td>PD-1/VEGF</td><td>BsAb</td><td>1L ESCC</td><td>+ chemo</td><td>Phase 2</td><td>★★</td></tr><tr><td>3605P</td><td>Poster</td><td>cadonilimab</td><td>PD-1/CTLA4</td><td>BsAb</td><td>2L aRCC</td><td>+ lenvatinib</td><td>Phase 2</td><td>★</td></tr><tr><td>4180P</td><td>Poster</td><td>cadonilimab</td><td>PD-1/CTLA4</td><td>BsAb</td><td>Mesothelioma</td><td>+ chemo</td><td>Phase 2</td><td>★</td></tr><tr><td>2900P</td><td>Poster</td><td>cadonilimab</td><td>PD-1/CTLA4</td><td>BsAb</td><td>ESCC</td><td>+ chemo</td><td>Phase 2</td><td>★</td></tr><tr><td colspan="9">Alphamab (9966.HK)</td></tr><tr><td>1243RO</td><td>Rapid Oral</td><td>JSKN033</td><td>HER2/PD-L1</td><td>ADC+mAb</td><td>2L+ CC</td><td>FDC</td><td>Phase 1</td><td>★</td></tr><tr><td>1253P</td><td>Poster</td><td>JSKN033</td><td>HER2/PD-L1</td><td>ADC+mAb</td><td>PROC</td><td>FDC</td><td>Phase 1</td><td>★</td></tr><tr><td colspan="9">Antengene (6996.HK)</td></tr><tr><td>2886P</td><td>Poster</td><td>ATG-022</td><td>CLDN18.2</td><td>ADC</td><td>G/GEJC</td><td>Mono</td><td>Phase 2</td><td>★★</td></tr><tr><td>2087P</td><td>Poster</td><td>ATG-037</td><td>CD73</td><td>Small molecule</td><td>CPI-resistant melanoma</td><td>+ pembro</td><td>Phase 1/1b</td><td>★</td></tr><tr><td colspan="9">BeOne (ONC/6160.HK/688235.SH)</td></tr><tr><td>1679RO</td><td>Rapid Oral</td><td>BGB-B2033</td><td>GPC3/4-1BB</td><td>BsAb</td><td>Adv HCC</td><td>Mono</td><td>Phase 1</td><td>★★</td></tr><tr><td>1980P</td><td>Poster</td><td>BGB-A445</td><td>OX40</td><td>Small molecule</td><td>UC, RCC &amp; melanoma</td><td>+/- tislei</td><td>Phase 1b/2</td><td>★★</td></tr><tr><td>1043P</td><td>Poster</td><td>BGB-58067</td><td>PRMT5</td><td>Small molecule</td><td>MTAP-deficient adv tumor</td><td>Mono</td><td>Phase 1</td><td>★★</td></tr><tr><td>1885TiP</td><td>Trial in Progress</td><td>BGB-43395</td><td>CDK4</td><td>Small molecule</td><td>1L met HR+/HER2- BC</td><td>+ letrozole</td><td>Phase 3</td><td>★</td></tr><tr><td colspan="9">Biokin/SystImmune (688506.SH)</td></tr><tr><td>1542RO</td><td>Rapid Oral</td><td>Iza-Bren</td><td>EGFR/HER3</td><td>ADC</td><td>r/m HNSCC</td><td>+ pembro</td><td>Phase 2</td><td></td></tr><tr><td>2575P</td><td>Poster</td><td>Iza-Bren</td><td>EGFR/HER3</td><td>ADC</td><td>1L EGFRmut NSCLC</td><td>+ osimertinib</td><td>Phase 1b/2</td><td></td></tr><tr><td colspan="9">CARsgen (2171.HK)</td></tr><tr><td>1056P</td><td>Poster</td><td>satri-cel</td><td>CLDN18.2</td><td>CAR-T</td><td>G/GEJC</td><td>Mono</td><td>Phase 1</td><td>★</td></tr><tr><td colspan="9">CSPC (1093.HK)</td></tr><tr><td>5RO</td><td>Proffered Paper</td><td>SYS6043</td><td>B7-H3</td><td>ADC</td><td>Adv BC</td><td>Mono</td><td>Phase 1</td><td>★★</td></tr><tr><td>1028P</td><td>Poster</td><td>SYS6023</td><td>HER3</td><td>ADC</td><td>Solid tumors</td><td>Mono</td><td>Phase 1</td><td>★</td></tr><tr><td>1466P</td><td>Poster</td><td>HE071</td><td>TOP2</td><td>Small molecule</td><td>1L PTCL</td><td>+ COEP</td><td>Phase 2</td><td>★</td></tr><tr><td colspan="9">CStone (2616.HK)</td></tr><tr><td>2616RO</td><td>Rapid Oral</td><td>CS2009</td><td>PD-1/VEGF/CTLA-4</td><td>TsAb</td><td>Adv NSCLC</td><td>Mono/+chemo</td><td>Phase 2</td><td>★★</td></tr><tr><td>1953RO</td><td>Rapid Oral</td><td>CS2009</td><td>PD-1/VEGF/CTLA-4</td><td>TsAb</td><td>mCRC</td><td>Mono/+chemo</td><td>Phase 1/2</td><td>★★</td></tr><tr><td colspan="9">Duality (9606.HK)</td></tr><tr><td>990O</td><td>Proffered Paper</td><td>DB-1311</td><td>B7-H3</td><td>ADC</td><td>Solid tumors</td><td>+ pumitamig</td><td>Phase 2</td><td>★★</td></tr><tr><td>1255P</td><td>Poster</td><td>DB-1311</td><td>B7-H3</td><td>ADC</td><td>PROC</td><td>Mono</td><td>Phase 2</td><td>★</td></tr><tr><td>1846P</td><td>Poster</td><td>DB-1310</td><td>HER3</td><td>ADC</td><td>2L+ HR+/HER2- BC</td><td>Mono</td><td>Phase 1/2a</td><td>★</td></tr><tr><td colspan="9">Fosun (2196.HK)</td></tr><tr><td>1859P</td><td>Poster</td><td>fovinaciclib</td><td>CDK4/6</td><td>Small molecule</td><td>1L adv BC</td><td>Mono</td><td>Phase 3</td><td>★</td></tr><tr><td colspan="9">Hansoh (3692.HK)</td></tr><tr><td>1000O</td><td>Proffered Paper</td><td>HS-20122</td><td>EGFR/c-MET</td><td>ADC</td><td>Solid tumors</td><td>Mono</td><td>Phase 1</td><td>★★</td></tr><tr><td>1457O</td><td>Proffered Paper</td><td>rocbrutinib</td><td>BTK</td><td>Small molecule</td><td>1L BCL</td><td>+ R-CHOP</td><td>Phase 1b</td><td>★</td></tr><tr><td>2615RO</td><td>Rapid Oral</td><td>aumolertinib/dalmelitinib</td><td>EGFR/c-MET</td><td>Small molecule</td><td>MET+ NSCLC post EGFR TKI</td><td>Combo</td><td>Phase 3</td><td>★</td></tr><tr><td>1071P</td><td>Poster</td><td>HS-20093</td><td>B7-H3</td><td>ADC</td><td>Solid tumors</td><td>Mono</td><td>Phase 1</td><td>★</td></tr><tr><td>3861TiP</td><td>Trial in Progress</td><td>HS-20093</td><td>B7-H3</td><td>ADC</td><td>SCLC</td><td>Mono</td><td>Phase 3</td><td>★</td></tr><tr><td>1340TiP</td><td>Trial in Progress</td><td>HS-20089</td><td>B7-H4</td><td>ADC</td><td>3L+ adv/r EC</td><td>Mono</td><td>Phase 3</td><td>★</td></tr><tr><td colspan="9">Hengrui (1276.HK/600276.SH)</td></tr><tr><td>4155RO</td><td>Rapid Oral</td><td>rivoceranib</td><td>VEGFR-2</td><td>Small molecule</td><td>2L+ mTET</td><td>Mono</td><td>Phase 2</td><td>★</td></tr><tr><td>3530O</td><td>Proffered Paper</td><td>camrelizumab</td><td>PD-1</td><td>mAb</td><td>LARC</td><td>+ chemo</td><td>Phase 3</td><td>★★</td></tr><tr><td>1686P</td><td>Poster</td><td>camrelizumab</td><td>PD-1</td><td>mAb</td><td>uHCC</td><td>+ rivoveranib</td><td>Phase 3</td><td>★</td></tr><tr><td>3156P</td><td>Poster</td><td>camrelizumab</td><td>PD-1</td><td>mAb</td><td>1L mPC</td><td>+ chemo</td><td>Phase 2</td><td>★</td></tr><tr><td>1244RO</td><td>Rapid Oral</td><td>SHR-A2102</td><td>Nectin-4</td><td>ADC</td><td>r/m CC</td><td>Mono</td><td>Phase 2</td><td>★★</td></tr><tr><td>2634P</td><td>Poster</td><td>SHR-A2102</td><td>Nectin-4</td><td>ADC</td><td>EGFRmut NSCLC</td><td>+ EGFR TKI</td><td>Phase 2</td><td>★</td></tr><tr><td>1847P</td><td>Poster</td><td>SHR-A2102</td><td>Nectin-4</td><td>ADC</td><td>HR+/HER2- BC</td><td>ADC</td><td>Phase 1</td><td>★</td></tr><tr><td>1061P</td><td>Poster</td><td>HRS-7058</td><td>KRAS G12C</td><td>Small molecule</td><td>Solid tumors</td><td>Mono</td><td>Phase 1</td><td>★★</td></tr><tr><td>3150P</td><td>Poster</td><td>HRS-4642</td><td>KRAS G12D</td><td>Small molecule</td><td>PDAC</td><td>+ nimotuzumab</td><td>Phase 1b/2</td><td>★★</td></tr><tr><td>2653P</td><td>Poster</td><td>HRS-4642</td><td>KRAS G12D</td><td>Small molecule</td><td>NSCLC</td><td>+ adeb + chemo</td><td>Phase 1b/2</td><td>★★</td></tr><tr><td>3157P</td><td>Poster</td><td>HRS-4642</td><td>KRAS G12D</td><td>Small molecule</td><td>PC</td><td>+IO + chemo</td><td>Phase 2</td><td>★</td></tr><tr><td>3165P</td><td>Poster</td><td>HRS-4642</td><td>KRAS G12D</td><td>Small molecule</td><td>PC</td><td>+ adeb + chemo</td><td>Phase 2</td><td>★</td></tr><tr><td>467P</td><td>Poster</td><td>SHR-8068</td><td>CTLA-4</td><td>mAb</td><td>1L adv BTC</td><td>+ adeb + chemo</td><td>Phase 2</td><td>★★</td></tr><tr><td>1031P</td><td>Poster</td><td>SHR-9839</td><td>EGFR/cMET</td><td>BsAb</td><td>Solid tumors</td><td>Mono</td><td>Phase 1</td><td>★★</td></tr><tr><td>2659P</td><td>Poster</td><td>SHR-1826</td><td>c-MET</td><td>ADC</td><td>2L+ nsqNSCLC</td><td>+ PD-L1 + CTLA-4</td><td>Phase 2</td><td>★★</td></tr><tr><td>1778P</td><td>Poster</td><td>SHR-A1811</td><td>HER2</td><td>ADC</td><td>HER2+ mBC</td><td>+ pertuzumab</td><td>Phase 1b/2</td><td>★★</td></tr><tr><td>2662P</td><td>Poster</td><td>SHR-A1811</td><td>HER2</td><td>ADC</td><td>HER2+ NSCLC</td><td>adebre</td><td>Phase 1b/2</td><td>★★</td></tr><tr><td>2663P</td><td>Poster</td><td>SHR-A2009</td><td>HER3</td><td>ADC</td><td>2L+ NSCLC</td><td>beva</td><td>Phase 1b/2</td><td>★★</td></tr><tr><td>3825P</td><td>Poster</td><td>SHR-7787</td><td>DLL3</td><td>TCE</td><td>SCLC and NEC</td><td>Mono</td><td>Phase 1/2</td><td>★★</td></tr><tr><td>3815P</td><td>Poster</td><td>SHR-4849</td><td>DLL3</td><td>ADC</td><td>SCLC and NEC</td><td>Mono</td><td>Phase 1/2</td><td>★</td></tr><tr><td>2228P</td><td>Poster</td><td>SHR-4394</td><td>PSMA</td><td>ADC</td><td>PC</td><td>Mono</td><td>Phase 1</td><td>★</td></tr><tr><td>2912P</td><td>Poster</td><td>SHR-A1904</td><td>CLDN18.2</td><td>ADC</td><td>CLDN18.2+ GC/GEJC</td><td>+ adebre 5-FU</td><td>Phase1b/3</td><td>★★</td></tr></table>

Source: ESMO 2026, GS Global Investment Research

Exhibit 2: Abstract informa

[中间内容因长度限制已省略]

 including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
