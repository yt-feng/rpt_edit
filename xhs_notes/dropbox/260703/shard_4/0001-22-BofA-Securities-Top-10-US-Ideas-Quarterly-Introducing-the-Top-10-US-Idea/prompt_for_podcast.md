你是财经类 AI Podcast 制作人，擅长把研报内容改写成中文、英文两条独立的访谈式播客脚本。

【目标】
- 基于下面研报解析内容，写两份 podcast 脚本：一份中文，一份英文。
- 每份目标时长约 5 分钟。
- 两份都要是“访谈聊天式”，不是单人念稿。
- 听感：像一位主持人和一位研究员围绕报告做深度但自然的讨论。
- 不要使用 emoji。
- 不要把全文讲完，要留下 1-2 个“完整报告里会继续展开”的悬念。

【输出格式必须严格遵守】
- 中文部分只能使用 `ZH_A:` 和 `ZH_B:` 开头。
- 英文部分只能使用 `EN_A:` 和 `EN_B:` 开头。
- 每一句独立成行。
- 不要输出 Markdown 标题。
- 不要输出舞台说明、音效说明或括号注释。
- 先输出完整中文脚本，再输出完整英文脚本。

【角色设定】
- A 是主持人：负责提问、转场、替听众追问“所以这意味着什么”。
- B 是研究员：负责解释报告逻辑、给出结构化判断和保留悬念。
- 两个角色必须频繁轮换，避免一个人连续说超过 3 句。
- 每句要适合 TTS 朗读：短句、自然、不要太书面。

【中文脚本结构】
1. 开场：A 用一个问题引出报告价值，B 给出主判断。
2. 第一部分：这份报告真正要回答的问题是什么。
3. 第二部分：2-3 个关键洞察，每个洞察都要有“这意味着什么”。
4. 第三部分：哪些问题仍然没有完全展开，为什么值得继续读完整报告。
5. 结尾：自然引导听众加入社群/阅读完整报告，不要硬广。

【英文脚本结构】
- 英文不是中文逐句翻译，而是面向英文听众重新组织。
- 保留同样的主线和洞察，但表达更口语、更 podcast。
- Use natural conversational English.
- Avoid long sentences and avoid reading like a research memo.

【内容边界】
- 可以基于研报内容做适度发散，但必须是从原文逻辑推出的判断。
- 不要编造具体数据、公司动作或引用。
- 对不确定内容要用“这里仍需要继续验证”或 “the report does not fully answer this yet” 表达。
- 默认避免出现具体投行品牌名，比如“GS”“GS”，统一写作“投行研报”或 “a global investment bank report”。

【研报解析内容】
"""
# Top 10 US Ideas Quarterly

# Introducing the Top 10 US Ideas for Q3 2026

Strategy

## High-conviction Ideas to Drive American Alpha

We present our new list of ten short-term stock recommendations among US stocks under coverage based on our view that these stocks could have significant market and business-related catalysts in the quarter ahead. For 3Q26, our Top 10 Ideas include nine Buys and one Underperform across ten sub-sectors. Our Buys are Ford Motor, IBM, Ionis Pharma, JPM Chase, Knight-Swift, Snowflake, Spotify, Visa Inc, and Walmart. Our Underperform is Lennar Corp.

## Red, White, and Bullish (mostly)

BofA's RIC Outlook points to a largely bullish backdrop for the U.S. economy and global equities, with indicators confirming the “new industrial cycle” remains intact and earnings momentum strengthening. The Global Earnings Revision Ratio has improved to a six-month high, with particularly strong readings in the U.S. and broad-based upgrades across regions, while the Global Wave of macro data is rising in tandem with the earnings cycle—historically a supportive signal for equity returns. Although valuations and positioning suggest markets may be somewhat overheated in the near term, we think any summer pullback could be a potential buying opportunity, especially in real assets, credit, and value-oriented areas. See reports linked in the side bar for more on these themes.

## How this list will be maintained and updated

We will publish this list at the beginning of each quarter. Ideas will generally remain on the list through the quarter unless coverage is dropped or the rating changes. Any security that is removed will not be replaced. If there are changes to the list during the quarter, we will publish the change in a research report. Securities are intended to stay on the list for one quarter, although some may be chosen for the next quarter's list. We will publish performance quarterly.

## Table 1: Top 10 US Ideas List – 3Q26

High-conviction, short-term stock recommendations for the quarter ahead.

<table><tr><td>Company</td><td>Ticker</td><td>Analyst</td><td>Rating</td><td>Rec</td><td>Price</td><td>PO</td><td>Mkt Cap (bn)</td></tr><tr><td>Ford Motor</td><td>F</td><td>Perry,Alexander</td><td>C-1-7</td><td>BUY</td><td>$13.90</td><td>$20.00</td><td>$63,694.68</td></tr><tr><td>Int Business Machine</td><td>IBM</td><td>Mohan,Wamsi</td><td>B-1-7</td><td>BUY</td><td>$281.21</td><td>$315.00</td><td>$267,716.92</td></tr><tr><td>Ionis</td><td>IONS</td><td>Gerberry,Jason</td><td>C-1-9</td><td>BUY</td><td>$79.29</td><td>$111.00</td><td>$12,325.28</td></tr><tr><td>JPM Chase</td><td>JPM</td><td>Poonawala,Ebrahim</td><td>B-1-7</td><td>BUY</td><td>$327.33</td><td>$362.00</td><td>$820,571.45</td></tr><tr><td>Knight-Swift</td><td>KNX</td><td>Hoexter,Ken</td><td>B-1-7</td><td>BUY</td><td>$77.87</td><td>$84.00</td><td>$12,101.35</td></tr><tr><td>Snowflake</td><td>SNOW</td><td>Ikeda,Koji</td><td>C-1-9</td><td>BUY</td><td>$254.50</td><td>$300.00</td><td>$65,730.39</td></tr><tr><td>Spotify</td><td>SPOT</td><td>Reif Ehrlich,Jessica</td><td>C-1-9</td><td>BUY</td><td>$459.13</td><td>$685.00</td><td>$95,154.32</td></tr><tr><td>Visa</td><td>V</td><td>O’Neill,Matthew</td><td>B-1-7</td><td>BUY</td><td>$343.09</td><td>$410.00</td><td>$547,438.72</td></tr><tr><td>Walmart</td><td>WMT</td><td>Nardone,Christopher</td><td>B-1-7</td><td>BUY</td><td>$113.26</td><td>$144.00</td><td>$967,199.99</td></tr><tr><td>Lennar Corporation</td><td>LEN</td><td>Jadrosich,Rafe</td><td>B-3-7</td><td>U/P</td><td>$90.49</td><td>$77.00</td><td>$24,563.29</td></tr></table>

Source: BofA Global Research, Bloomberg  
BofA GLOBAL RESEARCH

Trading ideas and investment strategies discussed herein may give rise to significant risk and are not suitable for all investors. Investors should have experience in relevant markets and the financial resources to absorb any losses arising from applying these ideas or strategies.
BofA does and seeks to do business with issuers covered in its research reports. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of this report. Investors should consider this report as only a single factor in making their investment decision.
Refer to important disclosures on page 30 to 34. Analyst Certification on page 23. Price Objective Basis/Risk on page 20.
12989472

## 01 July 2026

Equity
United States

Anthony Cassamassino
Strategist
BofAS
+1 212 449 6874
anthony.cassamassino@bofa.com

See Team Page for List of Analysts

## BofA Global Research Reports

<table><tr><td>Title: Subtitle</td><td>Primary</td><td>Date</td></tr><tr><td></td><td>Author</td><td>Published</td></tr></table>

S&P 500 Target Update: Savita 30 June

Mid-year 2026: take Subramanian 2026

Global Wave: Macro and Nigel Tupper 25 June earnings converge 2026

The RIC Report: Research 10 June

Exceptional economy, Investment 2026

remarkable markets Committee

## Ford (F)

Alexander Perry
Research Analyst
BofAS
+1 646 855 1365
aperry3@bofa.com

## Buy, PO \$20

## 3Q investment thesis

We expect continued upward estimate revisions for Ford given: 1) Ford's primary North America market is better positioned compared to Europe/China given a protectionist trade agenda (no Chinese EV disruption), a favorable regulatory environment given the roll off of emission standards programs that allows Ford to produce its highest margin accretive ICE vehicles, and resilient demand despite higher gas prices, 2) mix benefit from shift to higher margin trims at F Blue including off-road & V8 trims, 3) Novelis recovery progressing better than expected, 4) outsized growth in F's high margin software & services business, 5) support from Ford's new battery energy storage business & the scaling of its new EV platform with the launch of an affordable pickup next year.

Table 2: We highlight Ford as a 3Q26 top pick F key stock data

<table><tr><td>Industry</td><td>Automotive</td></tr><tr><td>Market cap (mm)</td><td>$63,695</td></tr><tr><td>Price</td><td>$13.90</td></tr><tr><td>P/E (2027)</td><td>6.8x</td></tr><tr><td>% of sell-side rated Buy</td><td>21%</td></tr><tr><td>Short Interest % of float</td><td>2.93%</td></tr></table>

Source: BofA Global Research estimates, Bloomberg  
BofA GLOBAL RESEARCH

## Catalysts:

Mix should improve from shift to higher margin trims at F Blue: We think Ford should see a continued mix benefit as production shifts toward higher-margin trims, including the Ranger Raptor, Explorer Tremor, and potentially higher V8 penetration on the F-150. Ford had been under-producing certain margin-accretive products relative to demand given the prior regulatory backdrop, and we expect management to lean further into its truck/SUV profit pools as constraints ease. We think this reinforces Ford's exposure to the right North America profit pools, while Ford's middle-upper income truck/SUV customer base appears relatively resilient despite the recent period of higher gas prices.

Expect Novelis recovery to support production and soften costs: We think the Novelis, Ford's key aluminum supplier, Oswego plant recovery following a fire should lessen recent production volatility for Ford's high margin F-Series. Novelis' restart appears largely in line with Ford's expectations. This should help reduce reliance on alternatively sourced aluminum, where Ford expects a \$1.5-\$2.0bn headwind. Ford's F-Series production also appears to be improving, with May production the highest year-to-date.

BESS opportunity offers diversification into faster growing end market: We think customer announcements related to Ford's new battery energy storage system (BESS) offering could be a strong catalyst. We believe Ford is likely to emerge as a credible BESS competitor in a market where hardware differentiation is limited, but demand remains strong across utilities, data centers, and large C&I customers. Tesla remains the benchmark with Megapack, but Ford should benefit from strong brand recognition, its

commercial footprint, and a manufacturing/supply-chain strategy designed to align with ITC and domestic-content requirements, which can reduce eligible project costs by \~30%-40%.

Software and services add high-margin growth lever: We think Ford's software and physical services business offers another high-margin growth lever, with management targeting 8% annual revenue growth through 2030 off a \~\$15bn base in 2025. While Ford Pro represents the majority of current revenue, we see potential for growth to become increasingly weighted toward Ford Blue as BlueCruise expands across more vehicles and functionality advances toward eyes-off autonomy beginning in 2028. Ford also sees opportunity to take share in parts from independents by expanding its catalogue and refining pricing, which could help reduce the perceived premium to consumers while supporting higher-margin recurring revenue.

BofA Global Research Reports

<table><tr><td>Title: Subtitle</td><td>Primary Author</td><td>Date Published</td></tr><tr><td>Automotive Industry: Weekly automotive pit stop: Thoughts on recent Ford rally</td><td>Alexander Perry</td><td>29 May 2026</td></tr><tr><td>Ford Motor: NDR Takeaways: See benefits from mix, UEV scaling, &amp; software &amp; services growth</td><td>Alexander Perry</td><td>07 May 2026</td></tr><tr><td>Ford Motor: Tariff adjustment &amp; timing of investments help drive 1Q beat</td><td>Alexander Perry</td><td>30 April 2026</td></tr><tr><td>Automotive Industry: Switching lanes in 2026: Reinstating coverage on N. American Autos/Auto-tech</td><td>Alexander Perry</td><td>04 March 2026</td></tr></table>

Upside risks: Upside risks to our PO are: 1) continued resilience in US light vehicle auto sales, 2) better than expected growth in higher margin revenue streams, incl. software & services and Ford Energy, 3) mix and pricing remain favorable, and 4) stronger production of ICE SUVs/trucks.

Downside risks: Downside risks to our PO are: 1) material downturn in US auto sales from weak consumer confidence & affordability challenges, 2) a sharp and sustained rise in input costs, 3) disruption in the supply base, 4) a sustained period of higher gas prices, 5) new vehicle pricing deteriorates, and 6) F energy ramps slower than expected.

Company Description: Ford Motor is one of the world's largest vehicle producers, with over 4mm units manufactured/sold globally under the Ford and Lincoln brands. In 2023, Ford re-segmented the business into Ford Blue, Ford Model e, Ford Pro, and Ford Credit. Most recently, Ford announced its entrance into the Battery Energy Storage Systems (BESS) market through Ford Energy, which plans to provide U.S.-assembled storage solutions for utilities, data centers, and large industrial/commercial customers. Ford's primary profit center remains North America, though the company also operates across Europe, South America, and Asia Pacific/China. Ford remains focused on positioning itself for the evolving auto industry through balanced investments across ICE/hybrid trucks and SUVs, electrification, software/services, autonomy, and mobility-adjacent opportunities.

# International Business Machines (IBM)

Wamsi Mohan
Research Analyst
BofAS
+1 646 855 3854
wamsi.mohan@bofa.com

## Buy, PO \$315

## 3Q investment thesis

We expect IBM to be well positioned into 3Q, supported by: 1) a decent F2Q setup that should reinforce the durability of the Software segment 2) Software growth that appears more resilient than recent broader software concerns imply, 3) Consulting expectations that have already been reset to a low bar, 4) continued Red Hat, Data, and Automation momentum, with Data benefiting from Confluent and strong organic trends, 5) underappreciated Infrastructure strength across distributed infrastructure, storage, and Power, 6) FCF durability supported by productivity, mix, and disciplined execution, and 7) quantum as an increasingly visible strategic catalyst where IBM appears to be receiving limited credit today. The broader pullback in software (from agentic AI concerns) and the Consulting-related pressure following peer commentary appear overdone in IBM's case. IBM's software portfolio is concentrated in the infrastructure layer where AI adoption should increase the need for hybrid cloud platforms, governed data, automation, and secure transaction processing rather than displace demand and Consulting represents only a minority of IBM's mix. Our PO of \$315 is based on 21x our C27 EV/FCF.

Table 3: We highlight Int Business Machine as a 3Q26 top pick IBM key stock data

<table><tr><td>Industry</td><td>IT Services</td></tr><tr><td>Market Cap (mn)</td><td>$267,717</td></tr><tr><td>Price</td><td>$281.21</td></tr><tr><td>P/E (2027)</td><td>21.9x</td></tr><tr><td>% of sell-side rated Buy</td><td>71%</td></tr><tr><td>Short interest % of float</td><td>3.21%</td></tr></table>

Source: BofA Global Research estimates, Bloomberg  
BofA GLOBAL RESEARCH

## Catalysts:

F2Q should support a better F3Q setup: IBM guided F2Q constant-currency revenue growth to be similar to F26 of >5%, with operating pre-tax margin expansion of \~50bps as software mix and productivity are partly offset by Confluent dilution. For F26, IBM expects >5% constant-currency revenue growth, \~\$1bn y/y FCF growth, Software growth of 10%+, Consulting growth in the low-to-mid single-digit range, and Infrastructure down low-single-digits, lapping difficult Z17 compares. We expect F2Q to be broadly consistent with this framework, with the potential for modest upside from better Software growth, including Data / Confluent and continued Automation strength, with slight acceleration in Red Hat (lapping tougher comps). Consulting expectations remain low but potential for stronger than guided growth in the 2H as enterprise AI adoption accelerates. Infrastructure trends should benefit from demand across Power, Storage, and broader hybrid infrastructure. A solid F2Q would help reinforce the durability of IBM's model and leave the company better positioned into 3Q.

Software concerns look overdone given IBM's portfolio: Recent software pressure has centered on whether agentic AI could disrupt traditional application software, but IBM's portfolio is tied to the infrastructure layer of enterprise IT which should benefit from agentic AI/enterprise AI adoption due to complexity created by more models, agents, workflows, and data movement across hybrid environments. IBM has emphasized that only a very small portion of its Software portfolio is application-like and we see IBM as better positioned for AI-driven software demand than the broader software pullback has implied.

Consulting concerns overdone relative to the size and setup of the business: Consulting is also only \~15% of IBM, so treating the recent pressure as evidence of a broader IBM demand issue appears too punitive, particularly given signings returned to growth in 1Q and AI is already embedded across a meaningful portion of backlog.

Quantum provides an underappreciated catalyst: Quantum should become a more visible part of the IBM story as interest increases (given recent pure-play Quantum IPOs). IBM reiterated in F1Q that it remains on track to deliver its first large-scale fault-tolerant quantum computer by 2029 and noted that partners could achieve the first examples of quantum advantage this year using IBM hardware. More recently, IBM and the U.S. Department of Commerce announced an LOI to create Anderon, a standalone U.S. quantum chip foundry supported by a proposed \$1bn CHIPS award and a \$1bn IBM cash contribution, followed by IBM announcing plans to invest more than \$10bn in quantum over the next five years. We view these announcements as material for IBM's quantum leadership to receive greater attention and see IBM's quantum business providing optionality for the stock.

BofA Global Research Reports

<table><tr><td>Title: Subtitle</td><td>Primary Author</td><td>Date Published</td></tr><tr><td>International Business Machines Corp.: Takeaways from “View from the Top” Call with IBM CEO Arvind Krishna</td><td>Wamsi Mohan</td><td>10 March 2026</td></tr><tr><td>International Business Machines Corp.: An acquisition of Confluent inline with Hybrid Cloud/Al strategy</td><td>Wamsi Mohan</td><td>08 December 2025</td></tr><tr><td>International Business Machines Corp.: Red Hat: A deeper look into the portfolio and drivers of growth</td><td>Wamsi Mohan</td><td>01 December 2025</td></tr><tr><td>International Business Machines Corp.: Quick thoughts from IBM’s Quantum Investor Day at Watson Research Center</td><td>Wamsi Mohan</td><td>31 October 2025</td></tr><tr><td>International Business Machines Corp.: Why is there so much volatility in Transaction Processing?</td><td>Wamsi Mohan</td><td>29 July 2025</td></tr><tr><td>International Business Machines Corp.: A Deep Dive on Bull/Bear cases for IBM stock; PO to $320</td><td>Wamsi Mohan</td><td>18 June 2025</td></tr><tr><td>International Business Machines Corp.: Transaction Processing: a deep dive into the history, pricing and opportunity</td><td>Wamsi Mohan</td><td>28 May 2025</td></tr><tr><td>International Business Machines Corp.: Will the z17 cycle be better than the prior cycles? Deep dive into historical cycles</td><td>Wamsi Mohan</td><td>29 April 2025</td></tr></table>

Upside risks: 1) faster reacceleration of topline, 2) faster improvement in margins, 3) better-than-expected accretion from M&A, and 4) delivery of upside to FCF.

Downside risks: 1) failure to execute on the company's growth roadmap, 2) inability to realize expected cost savings from restructuring, 3) technology/competitor risk in hardware, software, and services, 4) unforeseen currency impacts on revenue and profits, 5) acquisition integration, given IBM's acquisitive nature, and 6) increased concern of economic uncertainty and tightening corporate IT budgets.

Company Description: IBM is a global technology company focused on hybrid cloud, AI, software, consulting, infrastructure, and financing. The company reports through four

primary segments: Software, Consulting, Infrastructure, and Financing. Software includes Hybrid Cloud / Red Hat, Automation, Data, and Transaction Processing. Consulting includes Strategy and Technology and Intelligent Operations. Infrastructure includes Hybrid Infrastructure, including IBM Z and Distributed Infrastructure, and Infrastructure Support. IBM's strategy is centered on helping large enterprise clients modernize core systems, deploy AI across hybrid environments, govern data and workflows, and run mission-critical workloads with security, resiliency, and scale.

## Ionis (IONS)

Jason 

[中间内容因长度限制已省略]

 co-plaintiffs with or involving issuers mentioned in this material is based on public information. Facts and views presented in this material that relate to any such proceedings have not been reviewed by, discussed with, and may not reflect information known to, professionals in other business areas of BofA in connection with the legal proceedings or matters relevant to such proceedings.

This information has been prepared independently of any issuer of securities mentioned herein and not in connection with any proposed offering of securities or as agent of any issuer of any securities. None of BofAS any of its affiliates or their research analysts has any authority whatsoever to make any representation or warranty on behalf of the issuer(s). BofA Global Research policy prohibits research personnel from disclosing a recommendation, investment rating, or investment thesis for review by an issuer prior to the publication of a research report containing such rating, recommendation or investment thesis.

Any information relating to sustainability in this material is limited as discussed herein and is not intended to provide a comprehensive view on any sustainability claim with respect to any issuer or security.

Any information relating to the tax status of financial instruments discussed herein is not intended to provide tax advice or to be used by anyone to provide tax advice. Investors are urged to seek tax advice based on their particular circumstances from an independent tax professional.

The information herein (other than disclosure information relating to BofA and its affiliates) was obtained from various sources and we do not guarantee its accuracy. This information may contain links to third-party websites. BofA is not responsible for the content of any third-party website or any linked content contained in a third-party website. Content

contained on such third-party websites is not part of this information and is not incorporated by reference. The inclusion of a link does not imply any endorsement by or any affiliation with BofA. Access to any third-party website is at your own risk, and you should always review the terms and privacy policies at third-party websites before submitting any personal information to them. BofA is not responsible for such terms and privacy policies and expressly disclaims any liability for them.

All opinions, projections and estimates constitute the judgment of the author as of the date of publication and are subject to change without notice. Prices also are subject to change without notice. BofA is under no obligation to update this information and BofA ability to publish information on the subject issuer(s) in the future is subject to applicable quiet periods. You should therefore assume that BofA will not update any fact, circumstance or opinion contained herein.

Subject to the quiet period applicable under laws of the various jurisdictions in which we distribute research reports and other legal and BofA policy-related restrictions on the publication of research reports, fundamental equity reports are produced on a regular basis as necessary to keep the investment recommendation current.

Certain outstanding reports or investment opinions relating to securities, financial instruments and/or issuers may no longer be current. Always refer to the most recent research report relating to an issuer prior to making an investment decision.

In some cases, an issuer may be classified as Restricted or may be Under Review or Extended Review. In each case, investors should consider any investment opinion relating to such issuer (or its security and/or financial instruments) to be suspended or withdrawn and should not rely on the analyses and investment opinion(s) pertaining to such issuer (or its securities and/or financial instruments) nor should the analyses or opinion(s) be considered a solicitation of any kind. Sales persons and financial advisors affiliated with BofAS or any of its affiliates may not solicit purchases of securities or financial instruments that are Restricted or Under Review and may only solicit securities under Extended Review in accordance with firm policies. Neither BofA nor any officer or employee of BofA accepts any liability whatsoever for any direct, indirect or consequential damages or losses arising from any use of this information.

## Research Analysts

Anthony Cassamassino
Strategist
BofAS
anthony.cassamassino@bofa.com

Thomas (T.J.) Thornton
Head of Research Marketing
BofAS
thomas.thornton2@bofa.com

Derek Harris
Portfolio Strategist
BofAS
derek.harris@bofa.com

Paul Ciana, CMT
Technical Strategist
BofAS
paul.ciana@bofa.com

Alexander Perry
Research Analyst
BofAS
aperry3@bofa.com.

Wamsi Mohan
Research Analyst
BofAS
wamsi.mohan@bofa.com

Jason M. Gerberry
Research Analyst
BofAS
jason.gerberry@bofa.com

Ebrahim H. Poonawala
Research Analyst
BofAS
ebrahim.poonawala@bofa.com

Ken Hoexter
Research Analyst
BofAS
ken.hoexter@bofa.com

Koji Ikeda, CFA
Research Analyst
BofAS
koji.ikeda@bofa.com

Jessica Reif Ehrlich
Research Analyst
BofAS
jessica.reif@bofa.com

Matthew C. O'Neill
Research Analyst
BofAS
matthew.c.oneill@bofa.com

Christopher Nardone
Research Analyst
BofAS
christopher.nardone@bofa.com

Rafe Jadrosich
Research Analyst
BofAS
rafe.jadrosich@bofa.com

Trading ideas and investment strategies discussed herein may give rise to significant risk and are not suitable for all investors. Investors should have experience in relevant markets and the financial resources to absorb any losses arising from applying these ideas or strategies.
"""
