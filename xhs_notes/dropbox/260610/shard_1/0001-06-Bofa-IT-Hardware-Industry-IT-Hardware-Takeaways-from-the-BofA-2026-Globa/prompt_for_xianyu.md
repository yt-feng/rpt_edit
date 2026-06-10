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
## IT Hardware Industry

# IT Hardware Takeaways from the BofA 2026 Global Technology Conference

Price Objective Change

## Themes: strong demand, supply restricted in some cases

AI infrastructure demand remains broader, deeper, and more durable with our conference reinforcing that beneficiaries extend across all segments of the IT Hardware landscape. Demand visibility is improving and companies with differentiated IP, scale, and supply access are benefiting on revenue, share, and margin expansion. Strong demand combined with restricted supply growth is helping reshape the memory and HDD markets with SNDK highlighting its new business models that include both volume commitments, as well as fixed pricing for an initial period, followed by variable pricing over the rest of the contract. Both STX and WDC remain focused on adding exabyte capacity via technology (higher areal density) without adding unit capacity. Following the bullish tone around sustainable strong demand trends across the conference, we are raising our price objectives on IBM, NTAP, STX and WDC.

## Inference driving meaningful traditional compute demand

Inferencing and agentic AI are emerging as the next driver of demand for traditional compute, creating a stronger case for CPU-intensive servers and broader enterprise infrastructure. Agentic workloads shift part of the compute from parallel GPU processing to sequential CPU processing. While AI server vendors (DELL, HPE, SMCI) continue to see strong demand, Dell and HPE are also seeing meaningful demand for traditional compute and IBM highlighted examples of inferencing and modernization driving consumption on non-GPU platforms (mainframe). DOCN is adding capacity, and over time, benefits from incremental ARR per MW. On-prem adoption of AI by enterprises is also increasing.

## HDD & Storage demand continues higher

Storage is becoming a more strategic AI bottleneck as training, inferencing, and agentic workflows all increase the amount of data that must be stored, protected, queried, and fed back into models. WDC framed HDD EB growth as potentially $>25\%$ for the next 3-5 years and STX noted demand remains above supply, orders are in place for the next 4-5 qtrs, and customers are planning EB allocations multiple years out. On the enterprise storage side, Dell ISG President Lewis noted agentic data growth means there is no longer “cold” or “dark” data, Everpure noted strong demand for high-performance systems and Storage-as-a-Service, and NTAP highlighted AI wins, all-flash upgrades, hybrid flash resilience, and Public Cloud growth.

## Demand sustainability, OEM pricing, Distributors & EMS

The component environment is tight, with memory, CPUs, HDDs, NAND all showing signs of pricing/cost inflation. Distributors (ARW, AVT) and EMS (FLEX, CLS, SANM) benefit from data center infrastructure demand, complexity, supply-chain services, inventory visibility, and customers' growing need for partners that can secure supply and manage long lead times. While PC units could be down high-teens in 2H26, HPQ could still see modest rev growth on pricing and mix. CNXC mgmt. continues to see customers prioritizing AI that augments human advisors and improves complex interactions rather than wholesale replacement.

## 08 June 2026

Equity

United States

IT Hardware

Wamsi Mohan

Research Analyst

BofAS

+1 646 855 3854

wamsi.mohan@bofa.com

Ruplu Bhattacharya

Research Analyst

BofAS

+1 646 855 0315

ruplu.bhattacharya@bofa.com

Aisling Grueninger

Research Analyst

BofAS

+1 646 855 4273

aisling.grueninger@bofa.com

Ryan Seungin Choi

Research Analyst

BofAS

+1 646 743 0587

ryan.choi2@bofa.com

<table><tr><td>Ticker</td><td>Old PO</td><td>New PO</td></tr><tr><td>IBM</td><td>$300</td><td>$315</td></tr><tr><td>NTAP</td><td>$150</td><td>$180</td></tr><tr><td>STX</td><td>$900</td><td>$1000</td></tr><tr><td>WDC</td><td>$572</td><td>$610</td></tr></table>

BofA does and seeks to do business with issuers covered in its research reports. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of this report. Investors should consider this report as only a single factor in making their investment decision.

Refer to important disclosures on page 26 to 29. Analyst Certification on page 25. Price Objective Basis/Risk on page 19. 12982

# Key takeaways from the fireside chats

# Day 1 of the 2025 BofA Technology Conference

## Dell Technologies Inc (ticker: DELL)

We hosted a fireside chat with President of Infrastructure Solutions Group (ISG) Arthur Lewis from Dell Technologies. We discussed the step-change in ISG demand, the company's supply-gated F27 guide, the broadening of AI beyond GPUs into traditional servers (ISS), and Dell's increasingly strategic role in helping customers move from legacy data centers to agentic AI architectures. Mr. Lewis framed the F27 revenue guide increase as constrained by supply rather than demand, with demand far exceeding available supply and customer visibility extending into 2026, 2027, and parts of 2028 across GPUs, core servers, storage, and networking. This supports a more durable revenue trajectory than a one-quarter pull-forward narrative (or “peak”), particularly as customers are engaging Dell on multiyear infrastructure planning rather than transactional hardware purchases. The tone around ISG was notably stronger than just “AI servers are growing,” with Mr. Lewis highlighting record AI server orders, a record backlog, continued share gains, and operating profit growth outpacing revenue growth, reinforcing that Dell is scaling into the AI infrastructure cycle with better profitability than many expected.

Mr. Lewis also made a compelling case that traditional servers and storage are becoming direct beneficiaries of agentic AI, not separate or lagging parts of the portfolio. We see this as important for Dell's narrative as margin and EPS growth is not only centered around lower margin AI servers. ISS strength was driven by a combination of legacy workload growth, modernization of an aging installed base, and new CPU-intensive AI workloads as agents increasingly act, manage, and orchestrate tasks that require sequential processing. We expect this to remain an important growth driver for Dell because customers are refreshing aged infrastructure as well as consolidating workloads to free up space, power, and cooling for AI projects. This leads to more durable demand growth, lessening the risk of demand destruction in the near-term from recent pricing actions.

Storage was similarly framed as moving from a slower-growth infrastructure category to a critical layer of the AI architecture, with Mr. Lewis pointing to Dell IP storage demand growing ahead of market for five consecutive quarters and new offerings such as AI Data Platform, Lightning, Exascale, PowerStore Elite, and cyber resiliency solutions strengthening Dell's position in higher-value storage. Mr. Lewis emphasized that agentic AI changes the way data centers are architected and materially increases the need for higher-quality, constantly circulating enterprise data. This supports a higher-quality ISG mix over time, with Dell IP storage carrying better economics and helping offset the margin dilution from rapid AI server growth.

## International Business Machines Corp (ticker: IBM)

We hosted a fireside chat with SVP of Infrastructure Ric Lewis from IBM. We discussed the accelerating AI-driven uplift across IBM's Infrastructure portfolio, including Z17 momentum, the expanding monetization opportunity around AI MIPS, strength in Power and storage, the durability of mainframe demand, and IBM's longer-term quantum roadmap. SVP Lewis framed IBM Infrastructure as increasingly less cyclical and more structurally advantaged, with AI creating incremental demand across the full stack rather than only in GPUs. That is most visible in Z, where program-to-program growth has accelerated from roughly 110% several generations ago to 120% to 125% in the prior cycle and roughly 135% for Z17, supported by AI workloads moving beyond fraud detection into broader inferencing use cases such as insurance, actuarial modeling, and transaction-level intelligence. IBM benefits from both a refresh cycle and seeing higher-value workloads attach to its installed base. This supports more durable revenue, stronger monetization per MIP, and a better mix of software, subscriptions, cards, and services around the platform. As such, we raise our PO to \$315 on 21x C27 EV/FCF

(prior \$300 on 20x unchanged C27 EV/FCF). We use a higher multiple to reflect the more durable revenue opportunity. Reiterate Buy.

SVP Lewis also pushed back on the idea that AI-enabled code modernization weakens mainframe stickiness, arguing that tools such as Watsonx Code Assistant for Z are actually expanding usage rather than enabling migration away. Customers using the tool are growing MIPs utilization at 2-3x the broader base, while specialty MIPS tied to Linux, containers, and adjacent workloads have been growing 3-4x faster than core MIPS. This supports the idea that modernization is a demand unlock, as customers can write in modern languages and still benefit from Z's throughput, resiliency, security, and economics. This also extends to Power and IBM i, where SVP Lewis described a meaningful resurgence in new workloads as software tools reduce skills-related friction. In parallel, supply-chain tightness and higher component costs are creating incremental demand for IBM's higher-efficiency systems, with SVP Lewis noting that memory, CPU, disk, and storage inflation makes Power, tape, storage, and integrated software more attractive. We see IBM's vertically integrated stack as having more pricing control and better ability to protect margin while also benefiting from customer urgency around AI infrastructure.

Storage emerged as another underappreciated AI beneficiary, with SVP Lewis emphasizing that AI is ultimately about data that needs to be stored, moved, fed, and processed. IBM is seeing strong demand across DS8000, FlashSystem, Storage Scale, and Fusion, with the hardware tied to its storage software growing roughly 50% to 60% and broader storage hardware growing double digits or better. While GPUs and servers have captured more attention, SVP Lewis' commentary suggests IBM has a credible path to participate in the next layer of AI infrastructure spending as enterprises move from experimentation into production and need trusted systems for data-heavy workloads.

IBM's roadmap for quantum advantage this year and a 2,000-qubit fault-tolerant machine by 2029 adds another long-duration technology optionality layer. Overall, the fireside reinforced that IBM's Infrastructure business is positioned to compound through a combination of accelerating Z demand, AI-driven workload expansion, storage strength, and better monetization across a differentiated full-stack architecture.

## Arrow Electronics Inc. (ticker: ARW)

We hosted a fireside chat with Board member and Interim CEO Bill Austen. We discussed the breadth of the components recovery, the quality of recent upside, the durability of operating leverage, and Arrow's positioning across both hardware components and enterprise software tied to AI and cloud. CEO Austen framed the cycle as still early, with book-to-bill now meaningfully above parity across all three regions, backlog filling in through 2Q, 3Q and 4Q, and in some cases visibility extending into 1Q27. The most constructive element was that the recovery is being driven by unit volume rather than price, with little to no price contribution in 1Q, and with management repeatedly pushing back on comparisons to the Covid shortage cycle or concerns around double ordering. That distinction is important because a unit-led, broad-based recovery across Western industrial, transportation, aerospace and defense, and mass-market customers makes the margin improvement higher-quality vs a price-led or shortage-driven cycle.

CEO Austen also emphasized that Arrow is not running the same playbook it has in prior upcycles, with the company focused on selecting higher-quality revenue, holding the line on fixed costs, and using value-added services to improve the earnings profile. Global Components operating margin reached 5.5% in 1Q, and management believes a “five handle” is sustainable as volume improves, reflecting better regional mix, a more efficient cost base, and a larger contribution from supply chain, demand creation, engineering services, and IP&E. Value-added services generated roughly 30% of operating income last year and remain a central lever, particularly supply chain services for hyperscalers, where Arrow manages complex logistics, AR/AP flows, and material

deployment in an inventory-light, fee-based model. ECS adds another layer of diversification, with roughly 75% of that business tied to enterprise software and the remainder to higher-end hardware, giving Arrow exposure to cloud, cybersecurity, virtualization, data protection, and AI workload migration while also helping balance working capital needs in Components. This supports the case that earnings power can move higher in an upcycle, but we look for further proof points on the sustainability of demand and margins, and that supply chain services get to steady state without a sharper profit step-down, and the CEO transition does not disrupt execution.

Overall, the fireside reinforced a more constructive cyclical setup for ARW, with broader demand, better visibility, and improved operating discipline pointing to higher earnings power as the components cycle recovers. We still believe sustained upside likely requires evidence that the current recovery remains volume-led, Western demand continues to broaden, and Arrow can hold a structurally higher margin framework through the next several quarters. Maintain Neutral.

## Avnet Inc. (ticker: AVT)

We hosted a fireside chat with CEO Phil Gallagher and CFO Ken Jacobson from Avnet. We discussed the broadening components recovery, backlog/book-to-bill trends, tightening lead times, memory-driven pricing, Avnet's strategic relevance as supply chains get more complex, Farnell's recovery path, and the margin leverage opportunity as the cycle improves. CEO Gallagher framed the current upturn as materially different from prior inventory-led cycles, with recovery now spreading beyond data center and hyperscale into industrial, transportation, aerospace and defense, consumer, and geographies including Asia, Europe, and the Americas. We see this breadth as the most constructive part of the AVT setup, as a more diversified recovery reduces reliance on any single end market and gives the company a clearer path to sustaining revenue momentum after a strong F3Q print and above-seasonal F4Q guide. At the same time, management's comments support a balanced view, as memory pricing has become a meaningful near-term revenue tailwind, with CFO Jacobson noting memory increased from roughly 5% to 7% of the business in C25 to roughly 10% to 15% in the March quarter largely because prices doubled, rather than because of a similar increase in units.

Visibility has improved, with CEO Gallagher noting backlog is 50% to 80% higher than a year ago, book-to-bill remains positive across regions and verticals, even excluding memory inflation, and the next six months look solid based on the backlog Avnet can reasonably assess. Tightening lead times in memory, high-power products, mil/aero, controllers, and data-center-related components should support near-term demand capture and potentially better pricing, while also increasing the value of Avnet's inventory position and supply chain services. Management repeatedly emphasized that complexity is a positive

[中间内容因长度限制已省略]

 the extent this material discusses any legal proceeding or issues, it has not been prepared as nor is it intended to express any legal conclusion, opinion or advice. Investors should consult their own legal advisers as to issues of law relating to the subject matter of this material. BofA Global Research personnel's knowledge of legal proceedings in which any BofA entity and/or its directors, officers and employees may be plaintiffs, defendants, co-defendants or co-plaintiffs with or involving issuers mentioned in this material is based on public information. Facts and views presented in this material that relate to any such proceedings have not been reviewed by, discussed with, and may not reflect information known to, professionals in other business areas of BofA in connection with the legal proceedings or matters relevant to such proceedings.

This information has been prepared independently of any issuer of securities mentioned herein and not in connection with any proposed offering of securities or as agent of any issuer of any securities. None of BofAS any of its affiliates or their research analysts has any authority whatsoever to make any representation or warranty on behalf of the issuer(s). BofA Global Research policy prohibits research personnel from disclosing a recommendation, investment rating, or investment thesis for review by an issuer prior to the publication of a research report containing such rating, recommendation or investment thesis.

Any information relating to sustainability in this material is limited as discussed herein and is not intended to provide a comprehensive view on any sustainability claim with respect to any issuer or security.

Any information relating to the tax status of financial instruments discussed herein is not intended to provide tax advice or to be used by anyone to provide tax advice. Investors are urged to seek tax advice based on their particular circumstances from an independent tax professional.

The information herein (other than disclosure information relating to BofA and its affiliates) was obtained from various sources and we do not guarantee its accuracy. This information may contain links to third-party websites. BofA is not responsible for the content of any third-party website or any linked content contained in a third-party website. Content contained on such third-party websites is not part of this information and is not incorporated by reference. The inclusion of a link does not imply any endorsement by or any affiliation with BofA. Access to any third-party website is at your own risk, and you should always review the terms and privacy policies at third-party websites before submitting any personal information to them. BofA is not responsible for such terms and privacy policies and expressly disclaims any liability for them.

All opinions, projections and estimates constitute the judgment of the author as of the date of publication and are subject to change without notice. Prices also are subject to change without notice. BofA is under no obligation to update this information and BofA ability to publish information on the subject issuer(s) in the future is subject to applicable quiet periods. You should therefore assume that BofA will not update any fact, circumstance or opinion contained herein.

Subject to the quiet period applicable under laws of the various jurisdictions in which we distribute research reports and other legal and BofA policy-related restrictions on the publication of research reports, fundamental equity reports are produced on a regular basis as necessary to keep the investment recommendation current.

Certain outstanding reports or investment opinions relating to securities, financial instruments and/or issuers may no longer be current. Always refer to the most recent research report relating to an issuer prior to making an investment decision.

In some cases, an issuer may be classified as Restricted or may be Under Review or Extended Review. In each case, investors should consider any investment opinion relating to such issuer (or its security and/or financial instruments) to be suspended or withdrawn and should not rely on the analyses and investment opinion(s) pertaining to such issuer (or its securities and/or financial instruments) nor should the analyses or opinion(s) be considered a solicitation of any kind. Sales persons and financial advisors affiliated with BofAS or any of its affiliates may not solicit purchases of securities or financial instruments that are Restricted or Under Review and may only solicit securities under Extended Review in accordance with firm policies.

Neither BofA nor any officer or employee of BofA accepts any liability whatsoever for any direct, indirect or consequential damages or losses arising from any use of this information.
"""
