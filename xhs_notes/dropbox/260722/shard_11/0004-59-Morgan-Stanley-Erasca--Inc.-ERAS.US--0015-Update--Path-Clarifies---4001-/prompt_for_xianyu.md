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
# '0015 Update: Path Clarifies; '4001 Next Catalyst

<table><tr><td colspan="3">WHAT&#x27;S CHANGED</td></tr><tr><td>Erasca, Inc. (ERAS.O)</td><td>From</td><td>To</td></tr><tr><td>Price Target</td><td>$12.00</td><td>$21.00</td></tr></table>

We raise our price target following the recent ERAS-0015 updates reflecting a strengthening profile and clearer path to registration, but remain Equal-weight as we await more mature and durable data. ERAS appears well positioned within a competitive RAS landscape.

Incremental progress, but awaiting further validation. Recent updates improve visibility into a differentiated, multi-indication registration opportunity, but we remain Equal-weight pending more mature data and longer follow-up. The initial ERAS-0015 update highlighted potential best-in-class attributes, though the thesis remains anchored to a small, early Phase 1 dataset, an emerging combination signal, and an evolving path from expansion into registration. The latest data begin to address these elements. Efficacy has been sustained and, in some cases, improved with additional patients and follow-up, early combination feasibility has been demonstrated at standard doses, and mgmt. has outlined a clearer and more accelerated path into registration-enabling studies. Upcoming readouts, including ERAS-4001 preliminary Phase 1 monotherapy data in 2H26 and '0015 monotherapy expansion and combination dose-escalation data, including panitumumab, in 1H27, should be important for further validation. Taken together, ERAS appears well positioned as a funded, multi-indication registration story, but we believe additional data and follow-up will remain key.

The recent update (deck here) strengthens the PDAC efficacy profile, though durability remains immature. The data provide a consistent cut-to-cut comparison across a US-only 2L+ population using a ≥8-week efficacy-evaluable definition (April vs. May data cutoffs). uORR increased from 14% to 25% at 24mg, from 50% to 57% at 32mg, and from 27% to 40% across pooled 24-32mg RDEs. In the US 2L+ KRAS G12X PDAC subset, uORR (≥8 weeks) at 32mg was 57% (4/7), up from 50% (2/4), as the cohort expanded from four to seven evaluable patients, with responses increasing from two to four. Across pooled 24-32mg RDEs, activity improved to 40% (6/15) from 27% (3/11), with all responders (confirmed and unconfirmed) remaining on treatment. A dose-response trend remains evident (11%/0%/25%/57% across 8/16/24/32mg), and PK data show dose-dependent exposure without an observed plateau. That said, the 57% uORR at 32mg is based on a small sample size with limited durability follow-up, and will require confirmation through greater consistency and depth of response with additional patients and longer follow-up.

<table><tr><td colspan="2">MS &amp; CO. LLC</td></tr><tr><td colspan="2">Sean Laaman, Ph.D.</td></tr><tr><td colspan="2">Equity Analyst</td></tr><tr><td>Sean.Laaman@morganstanley.com</td><td>+1 212 761-4947</td></tr><tr><td colspan="2">Katherine Sun</td></tr><tr><td colspan="2">Research Associate</td></tr><tr><td>Katherine.Sun@morganstanley.com</td><td>+1 212 761-5968</td></tr><tr><td colspan="2">Michael H Riad, Ph.D.</td></tr><tr><td colspan="2">Research Associate</td></tr><tr><td>Michael.Riad@morganstanley.com</td><td>+1 212 761-1309</td></tr><tr><td colspan="2">Natasha Arya</td></tr><tr><td colspan="2">Research Associate</td></tr><tr><td>Natasha.Arya@morganstanley.com</td><td>+1 212 761-6294</td></tr></table>

<table><tr><td>Stock Rating</td><td>Equal-weight</td></tr><tr><td>Industry View</td><td>Attractive</td></tr><tr><td>Price target</td><td>$21.00</td></tr><tr><td>Shr price, close (Jul 16, 2026)</td><td>$19.02</td></tr><tr><td>Mkt cap, curr (mm)</td><td>$5,788</td></tr><tr><td>52-Week Range</td><td>$24.28-1.33</td></tr></table>

<table><tr><td>Fiscal Year Ending</td><td>12/25</td><td>12/26e</td><td>12/27e</td><td>12/28e</td></tr><tr><td>EPS ($)**</td><td>(0.44)</td><td>(0.90)</td><td>(0.55)</td><td>(0.66)</td></tr><tr><td>Prior EPS ($)**</td><td>-</td><td>(0.94)</td><td>(0.49)</td><td>(0.56)</td></tr><tr><td>P/E</td><td>NM</td><td>NM</td><td>NM</td><td>NM</td></tr><tr><td>EPS ($)$</td><td>(0.44)</td><td>(0.95)</td><td>(0.56)</td><td>(0.66)</td></tr><tr><td>Div yld (%)</td><td>-</td><td>-</td><td>-</td><td>-</td></tr></table>

Unless otherwise noted, all metrics are based on MS ModelWare framework  
\*\* = Based on consensus methodology  
§ = Consensus data is provided by Refinitiv Estimates  
e = MS estimates

<table><tr><td colspan="6">QUARTERLY EPS ($)</td></tr><tr><td>Quarter</td><td>2025</td><td>2026e Prior</td><td>2026e Current</td><td>2027e Prior</td><td>2027e Current</td></tr><tr><td>Q1</td><td>(0.11)</td><td>-</td><td>(0.60)a</td><td>(0.12)</td><td>(0.13)</td></tr><tr><td>Q2</td><td>(0.12)</td><td>(0.11)</td><td>(0.11)</td><td>(0.12)</td><td>(0.13)</td></tr><tr><td>Q3</td><td>(0.11)</td><td>(0.12)</td><td>(0.11)</td><td>(0.13)</td><td>(0.14)</td></tr><tr><td>Q4</td><td>(0.10)</td><td>(0.12)</td><td>(0.11)</td><td>(0.13)</td><td>(0.15)</td></tr></table>

e = MS estimates, a = Actual Company reported data

MS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.

For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

Exhibit 1: Efficacy data for 2L+ KRAS G12X PDAC pts across April and May data cutoffs  
![](images/a9459d1e6c01c672a8fc7033a362f13015bb2e7813941fdbeafc4eec169a2891.jpg)  
Source: Company reports

Exhibit 2: Updated time on treatment for 2L+ KRAS G12X PDAC pts  
![](images/202e0422be6466516e34816c43bd20574b93602f8b6019e8d3a2a720980458c8.jpg)  
Source: Company reports

Exhibit 3: ERAS-0015 efficacy vs. comparator pan-RAS molecular glue RMC-6236 benchmark

![](images/6efb31e9d90489ea59194fb0dc3d2d7ff3ce142a375a0175e1fc061207cc1742.jpg)  
Exhibit 4: ERAS-0015 safety vs. comparator pan-RAS molecular glue RMC-6236 benchmark  
Source: Company reports

![](images/d2a7d0f0b2539ea9aba145ba7589d8d78c96384d6c4c300bdbeef9939bec2f71.jpg)  
Source: Company reports

Safety profile supports sustained dosing and combination potential. At 16-32mg, the safety database has expanded to N=72 (from 43 previously). Rash occurred in 72% of patients (including 3% Gr3), diarrhea in 32% (1% Gr3), and stomatitis in 19% (3% Gr3). Dose interruptions occurred in 13% of patients, reductions in 8%, and there were no TRAE-related discontinuations. There is no clear dose gradient in common toxicities, with rash observed in 81%/75%/64% of patients at 16/24/32mg, respectively. Median relative dose intensity (RDI) was 100% across all dose levels, with mean RDI of 95.0% at 24mg, 93.5% at 32mg, and 95.9% pooled. Cross-study comparisons against daraxonrasib (RMC-6236) suggest lower rates of Gr3+ rash and stomatitis and fewer dose modifications for '0015, though the comparison spans different trial phases and populations and '0015 follow-up remains less mature. Notably, each program has reported a single Gr5 pneumonitis event: '0015 in AURORAS-1 (a Gr3 event that progressed to Gr5 following patient-elected withdrawal of supportive care) and daraxonrasib in the Ph3 RASolute 302 trial (0.4%). We view this as a possible class-related risk rather than a clearly molecule-specific signal.

Exhibit 5: Updated ERAS-0015 safety summary by grade  
![](images/c2e7cff4e9e05a643059e7a9a959959346adba6cc86484d14f9578ad7127cfb9.jpg)  
Source: Company reports

Exhibit 6: Updated ERAS-0015 safety summary by dose  
![](images/884a8f6e2116fa3db74466c0ef71759942d328ee2a53167a2fa95cbbe5b7c177.jpg)  
Source: Company reports

Combination feasibility emerging as a key point of differentiation... The recent update further supports the combination thesis, particularly around tolerability. As of the July 6 data cut, '0015 16mg + standard-dose panitumumab cleared its initial dose level with no DLTs in four DLT-evaluable patients. Backfill at 16mg and escalation to 24mg are ongoing. While there is no incremental efficacy disclosure beyond the prior uPR, we view this as representing an important step given the historical tolerability challenges associated with RAS combination strategies.

...and beyond panitumumab, the combination opportunity continues to expand. Merck (covered by Terence Flynn) is supplying pembrolizumab as part of the Erasca-sponsored AURORAS-1 study, while Tango will sponsor a Phase 1/2 study of '0015 + PRMT5i vopimetostat in MTAP-deleted pancreatic cancer and RASm NSCLC. We view these collaborations as early signs of potential as the monotherapy dataset matures. While EGFR, PD-1, and PRMT5 combinations suggest the possibility for '0015 to function as a combinable RAS backbone, we view upcoming combination readouts as essential to establish the balance of efficacy, tolerability, dose intensity, and combinability, and ultimately to support a more differentiated positioning.

Clearer path, but contingent on alignment and execution. In addition to the data to date, increased clarity on the registration strategy supports the outlook. The company plans to initiate a potentially registration-enabling 2L+ NSCLC study in 1H27, followed by a 1L PDAC Phase 3 in 2027 and a RASm NSCLC pivotal Phase 3 in 2H27-1H28. If executed, this would move '0015 from early clinical development into three registration-directed programs within \~18-24 months. The sequencing appears logical, with NSCLC leading via a cleaner monotherapy path, while PDAC moves earlier-line where tolerability and combination flexibility may be more impactful. The company also announced an upsized public offering totaling \$632.5mn in gross proceeds, which should support parallel registrational development. That said, execution remains dependent on regulatory alignment and timely trial initiation, particularly as the first NSCLC study is expected to begin within a similar window as upcoming data updates. Taken together, the outlined path is defined and funded, but we acknowledge still requires continued regulatory clarity and operational execution.

IP overhang persists, with a data-dependent path to mitigation. On IP, we continue to see a credible path for the current valuation discount to diminish if clinical differentiation is sustained, though we do not view the risk as resolved at this stage (see our published analysis assessing the patent infringement risk here). Revolution Medicines' (RVMD, not covered) claim relies on the Doctrine of Equivalents rather than literal infringement, and our prior analysis suggests limited precedent for successful claims under this framework, albeit with small sample sizes. More importantly, sustained differentiation across dose, PK/PD, efficacy, safety, dose intensity, and combinability could increasingly support arguments around function-way-result and insubstantial differences. That said, this will require a more mature and clearly differentiated clinical profile over time. Overall, we believe continued strengthening of '0015's efficacy and safety profile could position the program to largely mitigate the IP overhang over time, though additional data will be required to confirm this trajectory.

Balanced risk-reward, with a defined path to a more constructive stance. While risks remain, including small sample sizes at 32mg in PDAC, immature durability, evolving combination data, and dependence on regulatory alignment and trial execution, we view these as addressable with continued data generation.

Importantly, recent progress across efficacy consistency, emerging combination feasibility, a clearer and accelerated registration strategy, external validation, and a funded development plan incrementally improves the risk-reward. For us to become more bullish on the stock, we would look for several key gating items: (1) longer duration of follow-up to establish durability, (2) a larger and more representative patient dataset to confirm consistency of response, and (3) continued execution on trial initiation and enrollment in line with the outlined registration path. Delivery on these elements, particularly more mature data and progression into registration-directed studies, could support an increase in probability of success in NSCLC and PDAC from 50% toward 60%, more consistent with our thresholds for registrational-stage programs, and implying \~20% upside to our price target.

Model updates: We raise our PoS for ERAS-0015/ERAS-4001 in PDAC to 50% (from 40%), NSCLC to 50% (from 35%) and CRC to 45% (from 35%), reflecting increased confidence, accelerated development path and a more validated RAS-targeting landscape. We pull forward our assumed NSCLC launches by one year to 2030/2031, now model simultaneous 1L/2L PDAC launches in 2030, raise our gross price assumption to \$40k (from \$30k) to reflect premium positioning, and adjust our COGS, SG&A, and R&D expenses accordingly. For '0015/'4001, we now model \~\$3.6bn unadj. peak sales (\~\$1.8bn risk-adj.) vs. Street's \~\$4bn unadj. (\~\$1.6bn risk-adj.) in PDAC, \~\$2.4bn unadj. peak sales (\~\$1.2bn risk-adj.) vs. Street's \~\$2.3bn unadj. (\~\$800mn risk-adj.) in NSCLC, and \~\$920mn unadj. peak sales (\~\$400mn risk-adj.) vs. Street's \~\$1.7bn unadj. (\~\$630mn risk-adj.) in CRC. We also incorporate the recent upsized public offering, including the incremental cash and associated dilution. The net result is that our PT goes to \$21 (from \$12).

## Related Research:

- Biotechnology: RAS Oncology Toolkit for ASCO 2026: What You Need to Know (29 May 2026)

- Erasca, Inc.: Assessing the Patent Infringement Risk of ERAS-0015 (26 May 2026)
Biotechnology: Takeaways From Our KOL Call: Recent RAS Data Updates (17 May 2026)

- Erasca, Inc.: Preliminary Phase 1 Data ERAS-0015 Could Appear Compelling – Waiting to Mature (28 Apr 2026)

- Biotechnology: Takeaways From Our KOL Call: RAS-Targeting Agents (2 Mar 2026)

- Biotechnology: Takeaways From Our KOL Call: The RAS-Targeting Landscape (20 Feb 2026)

## Risk Reward – Erasca, Inc. (ERAS.O)

ERAS-0015 and ERAS-4001 Drive Risk/Reward

## PRICE TARGET \$21.00

Our PT is derived from a discounted cash flow analysis that assumes a $15\%$ discount rate and $2.5\%$ terminal growth rate.

<table><tr><td>Consensus Price Target Distribution</td><td>$12.00</td><td>$21.60</td><td>$30.00</td></tr><tr><td></td><td></td><td>MS PT</td><td></td></tr><tr><td></td><td></td><td>Mean</td><td>MS Estimates</td></tr><tr><td colspan="4">Source: Refinitiv, MS</td></tr></table>

![](images/2cd36b4adbb9c16ad9f0c4fd3a50627845a30514ea0791a09c6a1f01f0d2f17d.jpg)

## RISK REWARD CHART

![](images/c6e47bb2ade92a4404eb2bfdeb38c39b7dd84f3c50f20e1cbae5a9994076231d.jpg)  
Source: Refinitiv, MS

## EQUAL-WEIGHT THESIS

We are encouraged by ERAS-0015's emerging clinical profile, potential combination opportunities, and opportunity for an accelerated registration path, but look for further validation in upcoming updates with a larger patient dataset. We also look for updates on ERAS-4001 and potential partnership opportunities for naporafenib. We think ERAS shares may continue trade at a premium to fair value as the company's assets ("RAS oncology") hold potential strategic value.

![](images/01030cf6541ad09efc19e46985f08b05e51fe5eee0fd1a39215c97e360bd2efb.jpg)

## Risk Reward Themes

Disruption: Positive View descriptions of Risk Rewards Themes here

## BULL CASE \$32.00 BASE CASE

## DCF

Better-than-expected data are reported for ERAS-0015 and ERAS-4001, resulting in higher PoS and peak market shares. We model higher PoS for naporafenib.

## DCF

ERAS-0015 and ERAS-4001 data support continued advancement in RAS

[中间内容因长度限制已省略]

td>$2.67</td></tr><tr><td>Dyne Therapeutics Inc (DYN.O)</td><td>O (04/30/2024)</td><td>$22.72</td></tr><tr><td>Fractyl Health Inc (GUTS.O)</td><td>E (01/29/2026)</td><td>$0.85</td></tr><tr><td>Ionis Pharmaceuticals Inc (IONS.O)</td><td>O (07/30/2025)</td><td>$54.65</td></tr><tr><td>Kyverna Therapeutics (KYTX.O)</td><td>O (03/04/2024)</td><td>$7.44</td></tr><tr><td>Mirum Pharmaceuticals (MIRM.O)</td><td>O (11/13/2023)</td><td>$117.36</td></tr><tr><td>Rhythm Pharmaceuticals Inc (RYTM.O)</td><td>O (12/19/2023)</td><td>$106.09</td></tr><tr><td>Rocket Pharmaceuticals Inc (RCKT.O)</td><td>E (05/27/2025)</td><td>$3.41</td></tr><tr><td>Sarepta Therapeutics Inc (SRPT.O)</td><td>E (06/16/2025)</td><td>$17.23</td></tr><tr><td>Silence Therapeutics Plc (SLN.O)</td><td>O (05/08/2023)</td><td>$10.92</td></tr><tr><td>Tenaya Therapeutics Inc (TNYA.O)</td><td>O (08/24/2021)</td><td>$0.84</td></tr><tr><td>Viking Therapeutics Inc (VKTX.O)</td><td>O (06/27/2024)</td><td>$36.37</td></tr><tr><td>Vir Biotechnology Inc (VIR.O)</td><td>O (01/08/2025)</td><td>$9.40</td></tr><tr><td>Zentalis Pharmaceuticals Inc (ZNTL.O)</td><td>E (06/18/2024)</td><td>$4.57</td></tr><tr><td colspan="3">Sean Laaman, Ph.D.</td></tr><tr><td>ABSCI CORP (ABSI.O)</td><td>E (01/08/2026)</td><td>$8.23</td></tr><tr><td>Acadia Pharmaceuticals Inc (ACAD.O)</td><td>E (08/06/2024)</td><td>$25.63</td></tr><tr><td>Alector Inc (ALEC.O)</td><td>U (11/26/2024)</td><td>$1.47</td></tr><tr><td>argenx SE (ARGX.O)</td><td>O (07/02/2025)</td><td>$857.97</td></tr><tr><td>Axsome Therapeutics (AXSM.O)</td><td>E (01/08/2026)</td><td>$237.04</td></tr><tr><td>BeOne Medicines (ONC.O)</td><td>O (12/02/2024)</td><td>$317.42</td></tr><tr><td>Biomarin Pharmaceutical Inc (BMRN.O)</td><td>O (04/27/2026)</td><td>$60.00</td></tr><tr><td>BridgeBio Oncology Therapeutics (BBOT.O)</td><td>O (12/05/2025)</td><td>$8.31</td></tr><tr><td>BridgeBio Pharma Inc (BBIO.O)</td><td>O (01/06/2026)</td><td>$80.30</td></tr><tr><td>CG Oncology (CGON.O)</td><td>O (02/19/2024)</td><td>$69.50</td></tr><tr><td>Contineum Therapeutics (CTNM.O)</td><td>E (01/08/2026)</td><td>$14.01</td></tr><tr><td>Cullinan Therapeutics (CGEM.O)</td><td>O (03/06/2025)</td><td>$16.41</td></tr><tr><td>Denali Therapeutics Inc (DNLI.O)</td><td>O (03/06/2025)</td><td>$22.73</td></tr><tr><td>Disc Medicine Inc (IRON.O)</td><td>O (11/04/2024)</td><td>$73.47</td></tr><tr><td>Eikon Therapeutics Inc (EIKN.O)</td><td>O (03/02/2026)</td><td>$9.95</td></tr><tr><td>Erasca, Inc. (ERAS.O)</td><td>E (08/17/2025)</td><td>$19.02</td></tr><tr><td>Exelixis Inc. (EXEL.O)</td><td>E (01/08/2026)</td><td>$55.68</td></tr><tr><td>Generate Biomedicines Inc (GENB.O)</td><td>O (03/24/2026)</td><td>$13.66</td></tr><tr><td>Halozyme Therapeutics, Inc (HALO.O)</td><td>O (08/05/2025)</td><td>$77.54</td></tr><tr><td>Immunocore Holdings Ltd (IMCR.O)</td><td>E (12/12/2024)</td><td>$34.47</td></tr><tr><td>MapLight Therapeutics (MPLT.O)</td><td>O (11/21/2025)</td><td>$37.22</td></tr><tr><td>Neurocrine Biosciences Inc (NBIX.O)</td><td>E (01/08/2026)</td><td>$171.55</td></tr><tr><td>Recursion Pharmaceuticals Inc (RXRX.O)</td><td>E (05/22/2023)</td><td>$3.02</td></tr><tr><td>Schrodinger Inc. (SDGR.O)</td><td>E (11/19/2021)</td><td>$15.60</td></tr><tr><td colspan="3">Terence C Flynn, Ph.D.</td></tr><tr><td>Alumis Inc. (ALMS.O)</td><td>O (05/30/2025)</td><td>$27.23</td></tr><tr><td>Amgen Inc. (AMGN.O)</td><td>E (10/16/2023)</td><td>$371.58</td></tr><tr><td>Arcus Biosciences Inc. (RCUS.N)</td><td>E (01/08/2026)</td><td>$27.37</td></tr><tr><td>Arvinas Inc (ARVN.O)</td><td>E (04/06/2022)</td><td>$8.03</td></tr><tr><td>Biogen Inc (BIIB.O)</td><td>E (10/31/2024)</td><td>$208.92</td></tr><tr><td>Biohaven Ltd (BHVN.N)</td><td>O (07/24/2024)</td><td>$15.44</td></tr><tr><td>BioNTech SE (BNTX.O)</td><td>O (09/23/2024)</td><td>$91.56</td></tr><tr><td>Gilead Sciences Inc. (GILD.O)</td><td>O (01/10/2025)</td><td>$136.30</td></tr><tr><td>Intellia Therapeutics Inc (NTLA.O)</td><td>E (01/26/2025)</td><td>$11.86</td></tr><tr><td>Legend Biotech Corp (LEGN.O)</td><td>O (01/31/2022)</td><td>$22.71</td></tr><tr><td>Moderna Inc (MRNA.O)</td><td>E (12/16/2020)</td><td>$63.15</td></tr><tr><td>Nurix Therapeutics Inc. (NRIX.O)</td><td>O (01/08/2026)</td><td>$23.07</td></tr><tr><td>Prime Medicine Inc (PRME.O)</td><td>E (11/14/2022)</td><td>$3.22</td></tr><tr><td>Regeneron Pharmaceuticals Inc. (REGN.O)</td><td>E (12/03/2025)</td><td>$678.94</td></tr><tr><td>Structure Therapeutics Inc (GPCR.O)</td><td>O (09/22/2024)</td><td>$46.03</td></tr><tr><td>United Therapeutics Corp (UTHR.O)</td><td>E (07/11/2024)</td><td>$529.05</td></tr><tr><td>Vertex Pharmaceuticals (VRTX.O)</td><td>++</td><td>$486.03</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.  
\* Historical prices are not split adjusted.

© 2026 MS
"""
