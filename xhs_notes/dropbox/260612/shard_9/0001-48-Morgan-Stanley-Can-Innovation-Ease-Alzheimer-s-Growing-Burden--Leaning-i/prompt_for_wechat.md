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
- `# 标题` 必须包含报告机构的中文名称。已识别机构名：`摩根斯坦利`。标题格式建议：`# 摩根斯坦利：一句主判断`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、摩根斯坦利、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份摩根斯坦利研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
## Biotechnology | North America

# Can Innovation Ease Alzheimer's Growing Burden? Leaning in on Brain Shuttles

Can biotech innovation bend the late-life Alzheimer's burden created by a top-heavy population mix, or will longer lifespan increasingly convert into higher healthcare spend, caregiver burden, institutionalization, and socioeconomic strain?

## Key Takeaways

Aging is poised to convert added years of life into added years of dependency. Alzheimer's disease (AD) is where that conversion concentrates.  
Aging populations will shift AD from clinical burden into a healthcare-spend and retirement-system problem. We estimate a \$70B US market for AD therapies.  
Life expectancy has risen to an apparent ceiling near \~80yrs, while healthspan (years without disease impairment) has plateaued at \~70yrs.  
The data suggest we are not adding healthy years at the tail (we are adding impaired ones). Alzheimer's is the primary driver for this dislocation.  
Indeed, high-cost years is widening (and AD is its fastest-growing driver). US Seniors consume \~2.4x per-capita health spend of working-age adults.

![](images/2c015bb290fa25dbbc6b40133708329fa756ddbbf8b90eac945936cadaccf9bd.jpg)

## Societal Shifts

A MS Key Theme of 2026

## Alzheimer's is the disease that most efficiently converts longevity into the impaired-years gap.

The Congressional Budget Office (CBO) forecasts the US population peaking around 2050, with a steady decline toward current levels by 2099, from 349M adults in 2026 to 364M in 2050 and back to 349.1M by 2099. This represents a 0.1M net increase in \~73 years, or +0.0004% CAGR. Importantly, as the senior cohort grows, the absolute count of

impaired late-life years increases alongside it. In tandem, clinical AD prevalence rises from \~6.1M in 2020 toward \~12.7M by 2050 (Alzheimer's Association). Because seniors carry per-capita personal health-care (PHC) spend of \~\$22.4k versus \~\$9.2k for adults and \~\$4.4k for children, age mix alone pushes PHC from \~\$3.7T (11.7% of GDP) today to \~\$6.3T (13.1%) by 2050. Currently, we estimate the US AD market at \$50B, assuming 7M US patients with AD, 80% of whom are mild to moderate, and 30% of those are eligible for treatment after screening for safety and comorbidities.

The obesity/diabetes franchises that dominate today's longevity conversation are unlikely to relieve the AD burden. GLP-1 receptor agonists remain one of the most important drug classes of the decade for cardiometabolic risk, but in EVOKE/EVOKE+ Phase 3, oral semaglutide did not slow progression of early symptomatic

MS & CO. LLC

## Sean Laaman, Ph.D.

Equity Analyst

Sean.Laaman@morganstanley.com +1 212 761-4947

## Michael H Riad, Ph.D.

Research Associate

Michael.Riad@morganstanley.com +1 212 761-1309

## Terence C Flynn, Ph.D.

Equity Analyst

Terence.Flynn@morganstanley.com +1 212 761-2230

## Michael E Ulz

Equity Analyst

Mike.Ulz@morganstanley.com +1 212 761-4650

## Chris Yu, J.D., Ph.D.

Equity Analyst

Chris.L.Yu@morganstanley.com +1 212 761-2535

## MS ASIA LIMITED+

## Jack Lin

Equity Analyst

Jack.Lin@morganstanley.com +852 3963-3746

## MS & CO. LLC

## Avraham Novick

Research Associate

Avi.Novick@morganstanley.com +1 212 761-2231

## Katherine Sun

Research Associate

Katherine.Sun@morganstanley.com +1 212 761-5968

## Morgan K Gryga

Research Associate

Morgan.Gryga@morganstanley.com +1 212 761-0824

2026 EXTEL

## ALL-AMERICA RESEARCH POLL

May 26 – June 12, 2026

## VIEW OUR ANALYSTS >

## BIOTECHNOLOGY

## North America

Industry View

Attractive

MS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.

## For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

+= Analysts employed by non-U.S. affiliates are not registered with FINRA, may not be associated persons of the member and may not be subject to FINRA restrictions on communications with a subject company, public appearances and trading securities held by a research analyst account.

AD (the programs were terminated in November 2025). The result suggests the incretin obesity/diabetes franchises dominating the longevity debate are unlikely to relieve the neurological burdens at the tail end.

The historical case for pharmaceutical innovation is strong, but Alzheimer's remains an enigma. Pharmaceuticals have repeatedly bent mortality curves: vaccines, antibiotics, statins, antiretrovirals, targeted oncology, and now GLP-1s for cardiometabolic disease. Reports credit pharmaceuticals with roughly a third of recent US life-expectancy gains, but Alzheimer's is the decisive residual burden at the tail end of life and is the broadest driver of clinical burden for US seniors translating to fiscal and productivity drag. Indeed, the economic value of an AD therapy is not its own revenue line alone, but ability to delay the transition for millions of US seniors from independent living to supervised, institutional care. In 2019, the medical treatment stack for broad dementias was \~\$53k per patient, \$43k (82%) of which is accounted for by unpaid family care, \$7.5k (15%) for nursing care. Pharmaceuticals averaged \~\$172 (\~0.3%), and leading therapies carry a WAC that comes at a meaningful discount to the net price of a patient's medical care. A therapy that delays the transition into a nursing home, even by 12–18 months, delivers value worth multiples of its list price to the US healthcare system.

## Disease-modifying therapy has changed the debate but not yet the cost curve.

Biogen and Eisai's Leqembi (lecanemab) and Eli Lilly's Kisunla (donanemab) validate that amyloid removal slows decline (\~0.45 CDR-SB points / \~27% for Leqembi at 18 months, in line with the roughly one-third slowing for Kisunla), but the clinical effect is modest. Amyloid clearance already appears near-maximal, implying an efficacy ceiling in which faster or deeper clearance may not lead to better clinical outcomes. Indeed, a better-delivered anti-amyloid antibody through a brain shuttle operates on the same Abeta cascade and therefore inherits the same downstream biological constraints.

Brain health is the hard boundary of the longevity trade. If AD is where delivery success and therapeutic success diverge, rare lysosomal disease is where they converge following recent success with TfR brain-penetrant biologics. Denali's Avlayah (tividenofusp alfa, an enzyme transport vehicle/ETV fusing iduronate-2-sulfatase to a TfR-binding Fc) won US accelerated approval in March 2026 for the neurologic manifestations of Hunter syndrome (MPS II). In our view, this largely de-risks the clinical feasibility of brain shuttles for augmenting amyloid clearance. That said, in contrast to targeting amyloid, there are also several ongoing programs targeting intracellular tau. The data from these studies could solidy tau as a disease-modifying target in Alzheimer's disease, given tau pathology correlates more closely with neuronal dysfunction, neurodegeneration, and cognitive decline (than amyloid burden alone).

The debate, then, is whether a shuttle delivers a paradigm shift for how we treat brain health. Before 2026 a program could fail because the molecule never reached the brain at therapeutic concentration; for biologics larger than the \~0.1% that passively crosses, that was frequently the case. In this context, we see Denali's recent FDA approval as a paradigm shift. Denali is a leading pioneer in the field of next-generation biomedicines, securing the first US regulatory approval for a brain shuttle program (and with the potential compatibility across a four-cargo platform).

Indeed, Denali's March 2026 approval effectively converts brain bioavailability from barrier into an engineable obstacle to overcome. What remains is harder and arguably less forgiving in that shuttle platforms makes large biologics, enzymes and protein-replacements, and oligonucleotides deliverable, but it does not make them inherently more or less efficacious on their cognate molecular target. In our view, this positions symptomatic control as a nearer-term framework for alleviating psychosis (muscarinic Cobenfy, MapLight's ML-007, Acadia's 5-HT2A remlifanserin) and for alleviating agitation (Axsome's Auvelity).

Our work suggests aging of the brain as the largest driver for advancing longevity and \$70B addressable market for therapies. We frame the investable opportunity as two distinct layers: (1) disease-modifying therapies (amyloid and tau, increasingly paired with brain-shuttle delivery) addressing a \~\$50B market, and (2) symptomatic control (muscarinics and other mechanisms) addressing a \~\$20B market, net of \$70B. Below we highlight key names against each approach's unadjusted market (100% probability-of-success at 100% market-share).

Exhibit 1: Investable opportunity between disease modifying therapies vs therapies for symptomatic control

<table><tr><td></td><td>Company</td><td>Approach (MOA)</td><td>Market cap ($M)</td><td>MSe market size, unadjusted 100% PoS @ 100% market share, $M)</td><td>Multiplier</td></tr><tr><td></td><td>Disease-modifying therapy</td><td colspan="4">amyloid / tau ± shuttles</td></tr><tr><td>LLY</td><td>LLY (Lilly)</td><td>Anti-amyloid mAb Kisunla + IGF1R shuttle (ABL Bio)</td><td>$1,077,993</td><td rowspan="5">$50,000</td><td>0.05x</td></tr><tr><td>ROG</td><td>RHHBY (Roche)</td><td>Anti-amyloid mAb + TfR shuttle : trontinemab</td><td>$326,600</td><td>0.15x</td></tr><tr><td>BIIB</td><td>BIIB (Biogen)</td><td>Anti-amyloid mAb : lecanemab (w/ Eisai)</td><td>$29,395</td><td>1.70x</td></tr><tr><td></td><td>9926.HK (Akeso)</td><td>Bispecific, receptor undisclosed (spec.)</td><td>$12,000</td><td>4.17x</td></tr><tr><td>DNLI</td><td>DNLI (Denali)</td><td>TfR shuttle: DNL921 (ATV:Abeta) &amp; DNL628 (OTV:MAPT)</td><td>$3,300</td><td>15.15x</td></tr><tr><td></td><td>Symptomatic control</td><td colspan="4">muscarinics + other MOAs</td></tr><tr><td>BMY</td><td>BMY (Bristol Myers)</td><td>M1/M4 muscarinic : Cobenfy (KarXT)</td><td>$115,336</td><td rowspan="4">$20,000</td><td>0.17x</td></tr><tr><td>AXSM</td><td>AXSM (Axsome)</td><td>NMDA antagonist / sigma-1 : Auvelity (agitation)</td><td>$12,641</td><td>1.58x</td></tr><tr><td>ACAD</td><td>ACAD (Acadia)</td><td>5-HT2A inverse agonist : Remlifanserin (ACP-204)</td><td>$3,740</td><td>5.35x</td></tr><tr><td>MPLT</td><td>MPLT (MapLight)</td><td>M1/M4 muscarinic agonist + PAC : ML-007C-MA</td><td>$1,247</td><td>16.03x</td></tr></table>

Source: MS, Company reports

## What's in our report?

1 The demographic shift: a flat population, a top-heavy mix  
2 The spend escalator: aging lifts the curve mechanically  
3 Alzheimer's accelerates the strain on our system, and is only forecasted to grow  
4 The GLP-1 boundary and why is AD harder to crack?  
5 The Amyloid Hypothesis and current treatment landscape for AD  
6 TfR brain shuttles for breaking barriers and AD disease modification

Exhibit 2: Longevity of the Brain: Alzheimer's, the GLP-1 Boundary, and the Next Spend Curve  
![](images/ed73bd7644d894551e7c7674066813ff0bd5ed0700f408d617784571445d5482.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
  A["1 DEMOGRAPHICS & SPEND"] --> B["2 PHARMACEUTICAL INNOVATION"]
  B --> C["3 BRAIN HEALTH & ALZHEIMER'S"]
  C --> D["4 BIOTECHNOLOGY FOR LONGEVITY"]
```
</details>

1 / THE DEMOGRAPHIC AND COST SQUEEZE  
The US population stays roughly flat; the burden rises because the age mix changes.

![](images/743d439186e28a209639bf56e396cc7ab405fffaefbaea7c9106adb68e8cf454.jpg)

18.8% -> 30.5%

Senior share of the population, 2026 to 2099.

![](images/46d639edbd62453e42722d978287fb1c25e5a867744c7544c692e7917f822734.jpg)

\$22.4K vs \$9.2K

US Per-capita PHC spend for Seniors vs Adults.

![](images/58c44f30889e7068b35f161224973c476ee2b8ba94c46dff395d9ab7cdbcc2aa.jpg)

11.7% -> \~13.1%

PHC share of GDP by 2050 from age mix alone.

![](images/3732f83abf92b25bffade728dc2cbbbcb86b06e7fdbbc929c3bd171bec9e513d.jpg)

\~9.0M seniors

Base-case US seniors with AD by 2050; \~7.1M today.

![](images/d64ed767b4788a454269bbc8a2035c2e10c8c19d670a609f0e37d1680f02fcf6.jpg)

\$400-418B

Gross AD-related health spend by 2050; >\$1.2T by 2099.

![](images/2817696f518fa512754da3806dfc83c6581792c11b0ac1fc368e6144ed7c24c2.jpg)

\$28.7K vs \$8.2K

Senior annual HC spend with vs without AD/dementia.

2 / HISTORICAL CASE FOR PHARMACEUTICAL INNOVATION IS COMPELLING, BUT ALZHEIMER'S REMAINS HARD TO TREAT

Across eras, the biggest gains came when biology met a scalable intervention.

Vaccines

Smallpox (1796)

Prevention can eliminate mass mortality.

Endocrine

Insulin (1922)

Type 1 diabetes became survivable.

Anti-infectives

Penicillin (1944)

Bacterial infection became treatable.

Cardiovascular

BP + statins

Risk control cut stroke and renal death.

Oncology

Tamoxifen / imatinib

Targeted biology reshaped outcomes.

Virology

AZT / ART

Viral disease became suppressible.

Metabolic

GLP-1s

Obesity reframed as tractable risk.

3 / EARLY SIGNALS: PROGRESS, NOT A CURE

The clinical bar is high: amyloid clearance is not enough; function and safety matter.

![](images/471c61e3b7fc34561988a8822fbbdd6a8c9b9b22d5f1a3e7d36624f1037026ad.jpg)

EVOKE negative

Oral semaglutide missed in early AD; metabolic risk reduction is indirect.

![](images/1b96851815a73679b4db1d681b0d4c31c98f26042dca68e84072bf6d2da72b2a.jpg)

\~0.45 CDR-SB

Lecanemab/donanemab show modest 18-month slowing.

![](images/25476ae4c0747889f44cd27d207917f2e5bbe7e872970386208a8e462717a78f.jpg)

Trontinemab signal

\~91% below amyloid threshold with ARIA-E <5%; delivery helps.

![](images/87cb73921f855d7dedc73cf4be1c2d7982bb14adf029d29a72fcacc3991db43a.jpg)

>300 trials

>99% failure rates with current approaches

4 / BIOTECHNOLOGY FOR BRAIN HEALTH & LONGEVITY: BBB DELIVERY PLATFORMS  
Shuttles delivered a paradigm shift for antibodies and suggest value in applying the same delivery for enzymes, oligonucleotides and DNA/RNA complexes

<table><tr><td>Company</td><td>Asset / platform</td><td>Target class</td><td>Specific target / epitope / cargo</td><td>Shuttle?</td><td>Delivery logic</td><td>Status / read</td></tr><tr><td colspan="7">Alzheimer&#x27;s ABETA PROGRAMS (SHUTTLE ENABLED)</td></tr><tr><td>Roche</td><td>Trontinemab</td><td>Abeta</td><td>Anti-amyloid</td><td>Yes</td><td>TfR1-Fab shuttle</td><td>Pivotal TRONTIER, 2028 readout</td></tr><tr><td>AbbVie</td><td>ALIA-1758</td><td>Abeta</td><td>Anti-pyroglutamate-Abeta</td><td>Yes</td><td>TfR + CD98hc dual receptor</td><td>Early clinic, Aliada acquisition</td></tr><tr><td>Akeso</td><td>AK152</td><td>Abeta</td><td>Soluble Abeta oligomers + BBB receptor</td><td>Yes</td><td>undisclosed BBB receptor</td><td>NMPA-cleared, receptor undisclosed</td></tr><tr><td>Denali</td><td>DNL921 (ATV:Abeta)</td><td>Abeta</td><td>aggregations of insoluble Aβ</td><td>Yes</td><td>ATV transport</td><td>IND-enabling studies</td></tr><tr><td colspan="7">Other PLATFORMS PROGRAMS (SHUTTLE ENABLED)</td></tr><tr><td>Denali</td><td>Avalayah</td><td>Other</td><td>IDS enzyme / Hunter syndrome</td><td>Yes</td><td>ETVtransport vehicle</td><td>Delivery-to-benefit link ex-AD</td></tr><tr><td>Alector</td><td>ABC platform</td><td>Other</td><td>Platform / cargo-dependent</td><td>Yes</td><td>Distinct TfR epitope</td><td>Lower retic/Fc risk, cash runway</td></tr><tr><td>JCR Pharma</td><td>Pabinafusp alfa</td><td>Other</td><td>IDS enzyme / Hunter syndrome</td><td>Yes</td><td>Anti-TfR / IDS</td><td>Japan approval</td></tr><tr><td>Novartis</td><td>SciNeuro CNS Ab</td><td>Other</td><td>CNS antibody target not disclosed</td><td>Yes</td><td>TfR-enabled antibody</td><td>Large-cap validation</td></tr><tr><td>LLY/GSK/ABL</td><td>Grabody-B</td><td>Other</td><td>Platform / cargo-dependent</td><td>Yes</td><td>IGF1R RMT receptor</td><td>Diversifies beyond TfR</td></tr><tr><td colspan="7">Alzheimer&#x27;s Tau PROGRAMS (only ARWR shuttle enabled)</td></tr><tr><td>Denali</td><td>DNL628 (OTV:MAPT)</td><td>Tau</td><td>MAPT pre-mRNA/mRNA(total-tau knockdown)</td><td>Yes</td><td>OTV transport vehicle</td><td>Phase 1b study of DNL628 initiated dosing in 1Q26</td></tr><tr><td>Arrowhead</td><td>ARO-MAPT / TRiM</td><td>Tau</td><td>MAPT mRNA(siRNA; total-tau knockdown)</td><td>Yes</td><td>BBB-penetrant TRiM (receptor undisclosed)</td><td>Phase 1/2a healthy volunteer data (3Q/4Q26), AD Phase 1/2a data in 2027</td></tr><tr><td>Pinteon Therapeutics</td><td>PNT001</td><td>Tau</td><td>Mid-domain cis pT231 tau</td><td>No</td><td>No shuttle</td><td>Phase 1, early/inactive 2023</td></tr><tr><td>Lundbeck</td><td>Lu AF87908</td><td>Tau</td><td>C-terminal tail</td><td>No</td><td>No shuttle</td><td>Phase 1, early/inactive 2023</td></tr><tr><td>Johnson &amp; Johnson</td><td>Posdinemab</td><td>Tau</td><td>Mid-domain pT217</td><td>No</td><td>No shuttle</td><td>Phase 2b AuTonomy, terminated 2025</td></tr><tr><td>AC Immune / Roche</td><td>Semorinemab</td><td>Tau</td><td>N-terminal domain</td><td>No</td><td>No shuttle</td><td>Phase 2 TAURIEL/LAURIET, terminated 2023</td></tr><tr><td>Biogen</td><td>BIIB076</td><td>Tau</td><td>Mid-domain</td><td>No</td><td>No shuttle</td><td>Phase 1, terminated 2022</td></tr><tr><td>Eli Lilly</td><td>Zagotenemab</td><td>Tau</td><td>N-terminal domain</td><td>No</td><td>No shuttle</td><td>Phase 2 PERISCOPE-ALZ, terminated 2021</td></tr><tr><td>Biogen / BMY</td><td>Gosuranemab</td><td>Tau</td><td>N-terminal domain</td><td>No</td><td>No shuttle</td><td>Phase 2 TANGO, terminated 2021</td></tr><tr><td>AbbVie / C2N</td><td>Tilavonemab</td><td>Tau</td><td>N-terminal domain</td><td>No</td><td>No shuttle</td><td>Phase 2, terminated 2021</td></tr></table>

KEY TAKEAWAY

The debate is whether a brain shuttle delivers a paradigm shift for how we treat brain health (and will take some time to evaluate).

Nearer-term, this positions symptomatic control as able to dampen the cost, at least until BBB platforms demonstrate their value.

## Executive Summary

Aging is shifting from a demographic observation into a portfolio-construction problem. The US does not need population growth for its health bill to rise. A larger senior cohort means higher per-capita consumption, more long-duration neurodegenerative disease, a heavier informal-care burden, and more pressure on public and private re

[中间内容因长度限制已省略]

)</td><td>O (03/01/2021)</td><td>$2.82</td></tr><tr><td>Tscan Therapeutics Inc (TCRX.O)</td><td>E (11/13/2025)</td><td>$0.97</td></tr><tr><td>Ultragenyx Pharmaceutical Inc (RARE.O)</td><td>O (03/27/2019)</td><td>$22.79</td></tr><tr><td colspan="3">Michael E Ulz</td></tr><tr><td>Aardvark Therapeutics Inc. (AARD.O)</td><td>U (05/15/2026)</td><td>$3.58</td></tr><tr><td>Alnylam Pharmaceuticals Inc (ALNY.O)</td><td>E (09/09/2022)</td><td>$297.69</td></tr><tr><td>Arrowhead Pharmaceuticals Inc (ARWR.O)</td><td>O (04/21/2026)</td><td>$73.33</td></tr><tr><td>BioAge Labs Inc (BIOA.O)</td><td>E (12/05/2025)</td><td>$15.80</td></tr><tr><td>Cabaletta Bio Inc (CABA.O)</td><td>O (01/27/2023)</td><td>$3.22</td></tr><tr><td>Dyne Therapeutics Inc (DYN.O)</td><td>O (04/30/2024)</td><td>$17.92</td></tr><tr><td>Fractyl Health Inc (GUTS.O)</td><td>E (01/29/2026)</td><td>$0.66</td></tr><tr><td>Ionis Pharmaceuticals Inc (IONS.O)</td><td>O (07/30/2025)</td><td>$74.58</td></tr><tr><td>Kyverna Therapeutics (KYTX.O)</td><td>O (03/04/2024)</td><td>$7.85</td></tr><tr><td>Mirum Pharmaceuticals (MIRM.O)</td><td>O (11/13/2023)</td><td>$95.48</td></tr><tr><td>Rhythm Pharmaceuticals Inc (RYTM.O)</td><td>O (12/19/2023)</td><td>$87.86</td></tr><tr><td>Rocket Pharmaceuticals Inc (RCKT.O)</td><td>E (05/27/2025)</td><td>$2.65</td></tr><tr><td>Sarepta Therapeutics Inc (SRPT.O)</td><td>E (06/16/2025)</td><td>$15.89</td></tr><tr><td>Silence Therapeutics Plc (SLN.O)</td><td>O (05/08/2023)</td><td>$6.01</td></tr><tr><td>Tenaya Therapeutics Inc (TNYA.O)</td><td>O (08/24/2021)</td><td>$0.71</td></tr><tr><td>Viking Therapeutics Inc (VKTX.O)</td><td>O (06/27/2024)</td><td>$29.23</td></tr><tr><td>Vir Biotechnology Inc (VIR.O)</td><td>O (01/08/2025)</td><td>$8.51</td></tr><tr><td>Zentalis Pharmaceuticals Inc (ZNTL.O)</td><td>E (06/18/2024)</td><td>$3.58</td></tr><tr><td colspan="3">Sean Laaman, Ph.D.</td></tr><tr><td>ABSCI CORP (ABSI.O)</td><td>E (01/08/2026)</td><td>$6.83</td></tr><tr><td>Acadia Pharmaceuticals Inc (ACAD.O)</td><td>E (08/06/2024)</td><td>$21.84</td></tr><tr><td>Alector Inc (ALEC.O)</td><td>U (11/26/2024)</td><td>$1.63</td></tr><tr><td>argenx SE (ARGX.O)</td><td>O (07/02/2025)</td><td>$884.00</td></tr><tr><td>Axsome Therapeutics (AXSM.O)</td><td>E (01/08/2026)</td><td>$245.64</td></tr><tr><td>BeOne Medicines (ONC.O)</td><td>O (12/02/2024)</td><td>$268.17</td></tr><tr><td>Biomarin Pharmaceutical Inc (BMRN.O)</td><td>O (04/27/2026)</td><td>$57.91</td></tr><tr><td>BridgeBio Oncology Therapeutics (BBOT.O)</td><td>O (12/05/2025)</td><td>$7.26</td></tr><tr><td>BridgeBio Pharma Inc (BBIO.O)</td><td>O (01/06/2026)</td><td>$67.68</td></tr><tr><td>Centessa Pharmaceuticals, Inc (CNTA.O)</td><td>++</td><td>$39.76</td></tr><tr><td>CG Oncology (CGON.O)</td><td>O (02/19/2024)</td><td>$56.67</td></tr><tr><td>Contineum Therapeutics (CTNM.O)</td><td>E (01/08/2026)</td><td>$11.43</td></tr><tr><td>Cullinan Therapeutics (CGEM.O)</td><td>O (03/06/2025)</td><td>$13.18</td></tr><tr><td>Denali Therapeutics Inc (DNLI.O)</td><td>O (03/06/2025)</td><td>$20.79</td></tr><tr><td>Disc Medicine Inc (IRON.O)</td><td>O (11/04/2024)</td><td>$68.34</td></tr><tr><td>Eikon Therapeutics Inc (EIKN.O)</td><td>O (03/02/2026)</td><td>$8.77</td></tr><tr><td>Erasca, Inc. (ERAS.O)</td><td>E (08/17/2025)</td><td>$13.41</td></tr><tr><td>Exelixis Inc. (EXEL.O)</td><td>E (01/08/2026)</td><td>$52.99</td></tr><tr><td>Generate Biomedicines Inc (GENB.O)</td><td>O (03/24/2026)</td><td>$13.19</td></tr><tr><td>Halozyme Therapeutics, Inc (HALO.O)</td><td>O (08/05/2025)</td><td>$71.48</td></tr><tr><td>Immunocore Holdings Ltd (IMCR.O)</td><td>E (12/12/2024)</td><td>$28.52</td></tr><tr><td>MapLight Therapeutics (MPLT.O)</td><td>O (11/21/2025)</td><td>$29.27</td></tr><tr><td>Neurocrine Biosciences Inc (NBIX.O)</td><td>E (01/08/2026)</td><td>$165.24</td></tr><tr><td>Recursion Pharmaceuticals Inc (RXRX.O)</td><td>E (05/22/2023)</td><td>$3.22</td></tr><tr><td>Schrodinger Inc. (SDGR.O)</td><td>E (11/19/2021)</td><td>$14.52</td></tr><tr><td colspan="3">Terence C Flynn, Ph.D.</td></tr><tr><td>Alumis Inc. (ALMS.O)</td><td>O (05/30/2025)</td><td>$20.01</td></tr><tr><td>Amgen Inc. (AMGN.O)</td><td>E (10/16/2023)</td><td>$344.57</td></tr><tr><td>Arcus Biosciences Inc. (RCUS.N)</td><td>E (01/08/2026)</td><td>$23.64</td></tr><tr><td>Arvinas Inc (ARVN.O)</td><td>E (04/06/2022)</td><td>$7.21</td></tr><tr><td>Biogen Inc (BIIB.O)</td><td>E (10/31/2024)</td><td>$199.10</td></tr><tr><td>Biohaven Ltd (BHVN.N)</td><td>O (07/24/2024)</td><td>$11.09</td></tr><tr><td>BioNTech SE (BNTX.O)</td><td>O (09/23/2024)</td><td>$86.50</td></tr><tr><td>CRISPR Therapeutics AG (CRSP.O)</td><td>U (10/11/2022)</td><td>$51.48</td></tr><tr><td>Gilead Sciences Inc. (GILD.O)</td><td>O (01/10/2025)</td><td>$125.50</td></tr><tr><td>Intellia Therapeutics Inc (NTLA.O)</td><td>E (01/26/2025)</td><td>$12.89</td></tr><tr><td>Legend Biotech Corp (LEGN.O)</td><td>O (01/31/2022)</td><td>$33.49</td></tr><tr><td>Moderna Inc (MRNA.O)</td><td>E (12/16/2020)</td><td>$47.73</td></tr><tr><td>Nurix Therapeutics Inc. (NRIX.O)</td><td>O (01/08/2026)</td><td>$15.64</td></tr><tr><td>Prime Medicine Inc (PRME.O)</td><td>E (11/14/2022)</td><td>$2.88</td></tr><tr><td>Regeneron Pharmaceuticals Inc. (REGN.O)</td><td>E (12/03/2025)</td><td>$616.18</td></tr><tr><td>Structure Therapeutics Inc (GPCR.O)</td><td>O (09/22/2024)</td><td>$41.25</td></tr><tr><td>United Therapeutics Corp (UTHR.O)</td><td>E (07/11/2024)</td><td>$553.14</td></tr><tr><td>Vertex Pharmaceuticals (VRTX.O)</td><td>O (12/03/2025)</td><td>$445.77</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.

\* Historical prices are not split adjusted.

© 2026 MS
"""
