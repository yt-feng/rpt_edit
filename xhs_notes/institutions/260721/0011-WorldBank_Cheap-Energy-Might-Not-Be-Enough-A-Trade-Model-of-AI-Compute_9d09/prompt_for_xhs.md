你是资深小红书内容策划 + 投研翻译官，擅长把英文/中文研报改写成高互动、可收藏、可转发的中文小红书笔记。

【目标】
- 把下面的研报解析内容，改写成一篇中文小红书笔记。
- 风格：投研博主风：信息密度高，但像给朋友讲逻辑
- 长度：不超过 1000 字，信息密度高但不要写长文。
- emoji 密度：中

【必须输出的结构】
1. 第一行：标题，20 字以内，不要像论文标题，也不要用夸张极限词。
2. 第二行：封面短标题，10 字以内，适合放在图中间。
3. 第三行：封面副标题，10-18 字，短句。
4. 正文分段清晰，每段不超过 3 行，可以用编号、小标题或加粗。
5. 正文要自然呈现观点，但不要暴露写作框架或思考过程。
6. 末尾可以保留 2-4 个相关标签，只允许从这些标签里选择：`#学习笔记`、`#研究笔记`、`#学习研究`、`#研报解读`。

【严禁输出】
- 不要出现这些栏目名或类似栏目名：`一句话结论`、`我最想提醒的一点`、`配图建议`、`免责声明`、`非投资建议`、`仅做学习交流`、`仅作学习交流`。
- 不要在正文最后追加配图建议，不要告诉我第 2/3/4 张图怎么配文。
- 不要输出任何包含“投资”的免责声明，也不要输出“非投资建议”这种表述。
- 不要输出财经敏感标签：`#投资学习`、`#财经`、`#金融`、`#股票`、`#基金`、`#理财`。
- 不要输出无关标签：`#小红书笔记`、`#笔记分享`、`#干货分享`。
- 不要写“关注”“点赞”“求关注”“评论区见”“评论区留言”等直接互动诱导；可以写“欢迎一起讨论”“可以继续交流”。

【平台发布合规要求】
- 不要写“爆款”“震惊”“必看”“必读”“最强”“最全”“唯一”“全网首发”等极限词或夸张词。
- 不要写“投资建议”“买入”“卖出”“强烈推荐”“稳赚”“保本”“必涨”“抄底”“上车”“内幕”“翻倍”等金融操作或收益承诺表达。
- “投资”相关词尽量改成“投研”“研究”“观察”“学习参考”；如果必须保留，也要放在中性语境里。
- 不要承诺收益，不要引导交易，不要暗示确定性结果。

【内容要求】
- 只能基于研报原文和解析结果推导，不要编造数据、公司动作、引用。
- 可以把专业表达翻成人话，但不能扭曲意思。
- 遇到不确定或缺失信息：用“研报未给出”或“这里是推测”明确标注。
- 默认避免出现具体投行品牌名，比如“高盛”“Goldman Sachs”，统一写作“某外资投行研报”。
- 不要解释你的思考过程，不要输出多余说明。

【推荐写法】
- 开头直接给一个自然判断，不要加“结论：”标签。
- 中间用 1/2/3 拆逻辑，但小标题要像正常内容标题，不要像写作模板。
- 结尾可以留下一个自然讨论问题，但不要引导关注、点赞或评论。
- 最后一行输出 2-4 个标签，优先：`#学习笔记 #研究笔记 #学习研究 #研报解读`。

【研报解析内容】
"""
# Cheap Energy Might Not Be Enough

# A Trade Model of AI Compute Services

Michael Lokshin

POLICY RESEARCH WORKING PAPER 11429

## Abstract

Can energy-rich developing countries convert cheap electricity into AI compute exports? This paper develops a capacity-constrained trade model of AI compute services with bilateral frictions in delivery, regulation, and trust. Calibrating the model across 85 countries shows that several developing economies can produce compute at low cost, but this advantage rarely becomes export competitiveness. Because hardware dominates unit costs and is globally priced, cross-country production costs differ by only 12–20 percent. Modest regulatory, financing, and trust frictions can therefore erase the gains from cheap power. The binding constraint is institutional credibility rather than electricity prices, including enforceable data governance, stable regulation, credible power contracts, access to finance, and geopolitical alignment with buyers.

![](images/62c1c09888403db031082d9706f56345de0ebc23b1cd2d9724a4735f292ad26f.jpg)

# Cheap Energy Might Not Be Enough: A Trade Model of AI Compute Services

Michael Lokshin $^{1}$

Authorized for distribution by Ivailo V. Izvorski, Chief Economist, Europe and Central Asia Region, World Bank Group

JEL Classification: F14, F18, L86, O14, O33, Q40

Keywords: compute trade, FLOPs, artificial intelligence, data centers, comparative advantage, developing countries

## 1. Introduction

The expansion of artificial intelligence drives the demand for computational resources. The compute used to train machine-learning models (ML) has doubled every six months since 2010 (Sevilla et al. 2022). In 2024, data centers accounted for approximately 1.5 percent of global electricity demand, and that share is projected to exceed 3 percent by 2030 (IEA 2025). Rising compute demand creates a new kind of export opportunity: countries can sell computational work across borders. In this paper, we call this FLOP exporting because the service being traded is measured in floating-point operations, the standard unit of computational work. For energy-rich developing countries, this creates a potential path from raw energy exports to higher-value digital services.

Several megaprojects suggest that FLOP exporting is technically and commercially feasible. Armenia is deploying 50,000 GPUs as part of a \$4 billion investment (Firebird 2026). Kenya, Saudi Arabia, and Malaysia have attracted billion-dollar investments in data centers. Google has committed \$15 billion to India, and OpenAI has proposed a \$25 billion “Stargate Argentina” complex (Straub et al. 2026). Global data-center FDI reached over \$310 billion in 2025 (Aykut et al. 2026) and annual cloud computing exports exceeded \$9 billion (World Bank 2025).

Yet the cheapest locations are not the ones attracting the most investment. The cheapest potential producer in our calibration, Kyrgyzstan, has 5 MW of installed capacity and virtually no data-center FDI, while the largest recipients among developing economies (Malaysia, India, Brazil) sit in the middle of the cost ranking (Aykut et al. 2026). Cheap electricity alone is not creating compute exports. The central question, then, is why low-cost countries fail to attract compute investment and what conditions would allow them to convert cheap power into export capacity.

Recent work examines compute governance and the geography of AI infrastructure (Sastry et al. 2024, Lehdonvirta et al. 2024, Pilz et al. 2025), but no formal trade model of compute has been developed. This paper offers the first such model and makes three contributions. First, we develop a capacity-constrained Ricardian model of compute trade. The model treats latency as an iceberg trade cost and geopolitical distrust as a bilateral sovereignty premium that raises delivered costs. Second, we calibrate the model across 85 countries, correcting for energy subsidies that distort headline cost rankings. Third, we characterize the resulting trade regimes and quantify the welfare cost of sovereignty premia.

Cheap power and favorable cooling conditions do not automatically translate into export competitiveness. Hardware amortization accounts for roughly 90 percent of the unit cost and is priced globally, so cross-country production cost differences are limited to 12–20 percent. This narrow spread leaves little room for institutional frictions. Under cost-recovery pricing, several developing countries rank among the lowest-cost producers. However, when bilateral sovereignty frictions are introduced, trust deficits with OECD buyers eliminate nearly all of their export potential. Financing costs reinforce this result: a 10-percentage-point WACC gap between OECD hyperscalers and locally financed developing-country operators adds about \$0.29 per GPU-hour to unit cost, roughly four times the electricity-cost spread among the top twenty producers (Calcaterra et al. 2024).

## 2. Related Literature

Goldfarb and Trefler (2018) argue that AI shifts comparative advantage toward data and human capital. Our model highlights a different margin: compute production depends heavily on electricity costs and climate. Resource-rich countries could therefore export compute even without large domestic AI industries. Korinek and Stiglitz (2021) warn that developing countries may be left behind in the AI revolution; FLOP exporting offers a route in. The concept relates to Hausmann et al. (2007) on export composition and growth, and to Limão and Venables (2001) on infrastructure as a determinant of trade costs. In our setting, network latency plays an analogous role.

The closest precedent to our model is IT services offshoring, which is labor-intensive and skill-biased (Blinder 2006). FLOP exporting differs from traditional IT services offshoring in factor intensity. It is capital- and energy-intensive rather than labor-intensive, so likely exporters are energy-rich countries rather than labor-abundant ones. The structural difference is that GPUs, the main traded input, are priced globally. Cross-country cost variation therefore comes primarily from electricity and facility costs, which together account for only a small share of unit cost. Comparative advantage in compute is consequently narrower and more fragile than in services offshoring, where labor-cost differences are larger.

Several studies examine where firms should build data centers. Flucker et al. (2013) show that climate affects data center cooling costs. Liu et al. (2023) study data center placement under renewable energy constraints. In international trade theory, Brainard (1997) formalizes the proximity-concentration trade-off between serving a market locally and concentrating production abroad. Helpman et al. (2004) extend this to heterogeneous firms choosing between exporting and FDI.

On governance, Sastry et al. (2024) argue that compute is well-suited for regulation. Lehdonvirta et al. (2024) map a “Compute North” with training-capable hardware versus a “Compute South” limited to inference chips. Pilz et al. (2025) project that data center power demand could reach 327 GW by 2030. The World Bank (2025) documents the resulting divide (high-income countries hold 77 percent of colocation capacity), but does not offer a formal framework linking costs to trade patterns. Biglaiser et al. (2024) survey the cloud market in IO, and Stojkoski et al. (2024) estimate cloud export geography but treat services as homogeneous. Our model adds supply-side cost structure and a training–inference distinction.

## 3. Model of Compute Production and Trade

## 3.1 Production Technology and Cost Structure

Consider N countries, each capable of producing compute services. The cost of producing a unit of compute in country j depends on three inputs: electricity, hardware, and data center construction.

A data center consumes electricity for its Graphics Processing Units (GPUs), cooling, power distribution, and lighting. This overhead is measured by the power usage effectiveness (PUE), the ratio of total facility energy consumption to IT equipment energy consumption. The cost per GPU-hour in country j is: $^{2}$

$$
c _ {j} = \mathrm{PUE} (\theta_ {j}) \cdot \gamma \cdot p _ {E, j} + \rho + \eta + p _ {L, j} / (D \cdot H),\tag{1}
$$

where $\gamma$ is GPU power draw (kW), $p_{E,j}$ is the electricity price (\$/kWh), $\rho = P_{GPU} / (L \cdot H \cdot \beta)$ is amortized hardware cost per GPU-hour ( $P_{GPU}$ = purchase price, $L$ = lifetime in years, $H$ = 8,766 hours per year, $\beta = utilization rate$ , ${}^{3}\eta$ is amortized networking cost, and the last term amortizes per-GPU construction costs $p_{L,j} (= per-watt cost \times 700\ W)$ over the facility's lifetime D. Both $\rho$ and $\eta$ are determined in global hardware markets. $^{4}$ Cross-country variation in $c_{j}$ is therefore driven by electricity prices, climate, and construction costs; the construction-cost estimates are described in Appendix E. The PUE function captures temperature-dependent cooling overhead: $\mathrm{PUE}(\theta_{j}) = \varphi + \delta \cdot \max(0, \theta_{j} - \overline{\theta})$ , where $\varphi$ is the base PUE at or below the free-cooling threshold $\overline{\theta}$ , $\delta$ is the marginal PUE penalty per °C above $\overline{\theta}$ , and $\theta_{j}$ is country j's peak summer temperature.

The cost structure is Ricardian: countries differ in production costs because they differ in technology and input prices. The intuition for resource-rich comparative advantage, however, is closer to Heckscher–Ohlin with countries exporting goods intensive in their abundant factors (Heckscher 1919, Ohlin 1933). For compute production, the relevant endowment is not electricity, but the natural resources that generate it, such as hydropower (Kyrgyzstan, Ethiopia, Georgia), oil and gas (Iran, Turkmenistan, Qatar), solar irradiance (North Africa, the Gulf), and geothermal energy (Kenya, Iceland).

## 3.2 Trade Costs

Countries produce and trade two types of compute services that differ in their offshoring costs. Training services (denoted T) include batch workloads such as model training, fine-tuning, and large-scale data processing. Training a state-of-the-art AI model can take weeks to months across thousands of GPUs. The client ships its data to a data center, the computation executes locally, and the output is returned to the client. Since neither input nor output is time-sensitive, network latency plays no role. Inference services (denoted I) encompass real-time workloads such as chatbot responses, autonomous decisions, and interactive agents. Each query must travel to the server and back within milliseconds, so the service quality degrades as delivery delays (latency) increase.

Latency, denoted $l_{jk}$ , is the round-trip time for a data packet to travel from the seller country j to buyer country k, typically 5–10 ms within a country and over 150 ms across continents (Appendix F summarizes workload types and their latency sensitivity).

Governments and firms may prefer to process data domestically for national security, regulatory compliance, or political reasons. This is captured by a bilateral sovereignty premium $\lambda_{ij} \geq 0$ , which acts as a markup on the cost of compute sourced from seller country i by buyer country j. When buyer j sources compute from seller $i \neq j$ , the effective cost is inflated by the factor $(1 + \lambda_{ij})$ . The sovereignty premium is zero for domestic production ( $\lambda_{ii} = 0$ ). The bilateral premium is modeled as a function of geopolitical alignment $G_{ij}$ , measured from the UN General Assembly ideal-point distance (Bailey, Strezhnev, and Voeten 2017) and normalized so that $G_{ij} \in [0, 1]$ , with 0 denoting perfect alignment; regulatory compatibility $R_{ij}$ , coded as 1 for country pairs covered by a mutual data adequacy agreement and 0 otherwise. Pairs under comprehensive trade sanctions ( $S_{ij} = 1$ ) are treated separately as a corner case: trade is prohibited by assumption, so $\lambda_{ij} = \infty$ . For all other (non-sanctioned) pairs, the bilateral premium is:

$$
\lambda_ {i j} = \{\infty \text {if} S _ {i j} = 1; w _ {1} \cdot G _ {i j} + w _ {2} \cdot (1 - R _ {i j}) \text {otherwise} \}.\tag{2}
$$

Two established bodies of literature motivate this functional form. The multiplicative wedge (1 + $\lambda_{ij}$ ) on delivered cost is the standard representation of ad valorem bilateral trade frictions in the gravity literature (Anderson and van Wincoop 2003), where pair-specific wedges capture border effects, policy barriers, and non-tariff measures that raise the price paid by buyer j for seller i's services above the seller's own cost. The linear additive structure of the two components $G_{ij}$ and $R_{ij}$ treats geopolitical, regulatory, and sanctions frictions as separable contributions to the wedge, consistent with the iceberg-equivalent decomposition of services trade costs in Benz and Jaax (2020).

The wedge dependence on bilateral institutional alignment follows from the incomplete-contracts theory (Anderson and Marcouiller 2002, Antràs 2003). Compute trade is contract-intensive. A buyer sends sensitive data to a remote seller and depends on the seller's jurisdiction to enforce confidentiality, service-level obligations, and, in many applications, the buyer's ability to retrieve or delete its data. In countries where these contracts are weakly enforceable, the buyer discounts the seller's effective price, and the size of the discount varies with the pair-specific strength of the enforcement environment. Political alignment $G_{ij}$ proxies dispute-resolution willingness, mutual data adequacy $R_{ij}$ proxies enforceable contractual floors on data handling, and sanctions $S_{ij}$ proxy the extreme case where no enforcement is possible. Equation (2) is thus the natural implementation of the insecure-trade framework in a services-trade setting where the traded object is a compute service bundled with a data-handling contract. The delivered cost of service $s \in \{T, I\}$ from seller j to buyer k is:

$$
P _ {s} (j, k) = (1 + \lambda_ {j k}) \cdot (1 + \tau_ {s} \cdot l _ {j k}) \cdot c _ {j},\tag{3}
$$

where $c_{j}$ is the unit cost of producing one GPU-hour in country j (equation (1)). The bilateral premium $\lambda_{jk}$ is the same object as $\lambda_{ij}$ in equation (2); we relabel the subscripts as $(j, k)$ whenever the premium is paired with a specific seller's production cost $c_{j}$ . We treat governance quality, grid reliability, and similar institutional risks as demand-side frictions. They enter through $\lambda_{jk}$ rather than by a production cost adjustment.

The parameter $\tau$ measures the rate of quality degradation per millisecond of round-trip latency, with $\tau_{T} = 0$ and $\tau_{I} = \tau > 0$ . For training ( $\tau_{T} = 0$ ), the delivered cost is the sum of the production cost and the sovereignty markup. For inference, the delivered cost increases with latency at rate $\tau_{I}$ . Beyond a threshold $\overline{l}$ (typically 200–300 ms for interactive applications), the service becomes unusable regardless of price: $P_{I}(j, k) = \infty$ if $l_{jk} > \overline{l}$ .

## 3.3 Global Compute Demand

The model is closed by specifying demand for compute services. Let $q_{k}$ denote the volume of compute purchased by buyer k. We measure compute demand using installed data center capacity in megawatts (MW):

$$
q _ {k} = \omega_ {k} \cdot Q, \quad \omega_ {k} = M _ {k} / \sum_ {k ^ {\prime}} M _ {k ^ {\prime}},\tag{4}
$$

where $Q$ is the total global compute spending and $\omega_{k}$ is country $k$ 's share of global demand, measured by its share of installed data center capacity $M_{k}$ in MW. $^{5}$

Demand splits between training and inference. Training demand is $q_{Tk} = \alpha \cdot q_k$ and inference demand is $q_{Ik} = (1 - \alpha) \cdot q_k$ , where $\alpha \in (0,1)$ is the exogenous training share. The parameter $\alpha$ should be interpreted as the share of compute that is fully latency-insensitive and freely offshorable. The effective offshorable share may be smaller as intermediate workloads (agentic inference, fine-tuning) grow. $^{6}$

## 3.4 Sourcing and Market Equilibrium

For each service type $s \in \{T, I\}$ , each buyer k chooses the source that minimizes the delivered cost:

$$
j _ {s} ^ {*} (k) = \underset {j} {\arg \min} P _ {s} (j, k).\tag{5}
$$

Each country j is characterized by a capacity ceiling $\overline{K}_{j}$ , measured in GPU-hours per period, representing the maximum volume of compute the country can supply. This ceiling reflects the joint constraint of grid electricity availability, institutional capacity for data center permitting and construction, and access to GPU financing.

Training market. Since $\tau_{T} = 0$ , training is a homogeneous good with no distance-related quality degradation. Country k imports training whenever the world price, after adding the bilateral sovereignty premium, is lower than the price of producing domestically: $(1 + \lambda_{jk}) \cdot p_{T} < c_{k}$ , where $p_{T}$ is the competitive world training price. In the capacity-constrained equilibrium, the c

[中间内容因长度限制已省略]

 tool use</td><td>500–2,000 ms</td><td>Regionally</td><td>Intermediate (fn. 7)</td></tr><tr><td>Interactive inference</td><td>Chatbot, search, recommendation</td><td>50–200 ms</td><td>Limited</td><td> $\tau_{i} > 0$ , threshold  $\bar{1}$ </td></tr><tr><td>Real-time control</td><td>Autonomous vehicles, robotics</td><td>&lt; 20 ms</td><td>No</td><td>Domestic only</td></tr></table>

Notes: Latency tolerance is approximate round-trip time. “Offshorable” refers to whether the workload can be processed in a different country from the end user without significant quality degradation. The model treats fine-tuning and agentic inference as part of the training share $\alpha$ ; footnote 6 notes this simplification.

## Appendix G: Symmetric LRMC Construction

The cost-recovery specification in earlier versions of this paper adjusted electricity prices downward for thirteen developing countries whose observed industrial tariffs reflect explicit fossil-fuel subsidies (IMF 2025), replacing subsidized tariffs with the estimated long-run marginal cost of the dominant generation technology at opportunity-cost fuel prices. No symmetric correction was applied to OECD and high-income tariffs, which also embed distortions: emissions externalities not priced at the retail meter, industrial cross-subsidies financed by residential and commercial rate classes, and regulated-access privileges for incumbents. The asymmetry biases the cross-country cost spread in favor of OECD economies. This appendix constructs a symmetric LRMC specification that corrects distortions on both sides.

Of the 85 calibrated countries, 13 retain the IMF-based LRMC replacement used throughout the paper (Iran, Turkmenistan, Algeria, Egypt, Qatar, Saudi Arabia, United Arab Emirates, Russia, Kazakhstan, Nigeria, South Africa, Ethiopia, and Uzbekistan). Forty-three OECD, EU non-OECD, and high-income non-OECD countries receive a symmetric adjustment. Twenty-nine middle-income developing economies whose observed industrial tariffs already approximate long-run marginal cost retain their observed prices. Three countries (Qatar, Saudi Arabia, United Arab Emirates) appear in both the developing-country subsidy set and the high-income non-OECD set; the IMF-based treatment dominates and no layering is applied.

The carbon-price adder equals the 2024 grid carbon intensity in grams of CO $_{2}$ per kilowatt-hour (EMBER Yearly Electricity Data 2025 release) multiplied by the 2024 annual-average price under the applicable emissions-trading or carbon-tax regime: EU ETS (\$70.94 per tonne, applied to EU27 plus Norway, Iceland, and Switzerland via the linked Swiss ETS), UK ETS (\$47.32), Canadian federal backstop (\$58.48), California Cap-and-Trade plus RGGI coverage-weighted for the United States (\$3.81 effective national average), New Zealand ETS (\$39.50), and Singapore carbon tax (\$18.60). Nominal instruments with effective prices below ten dollars per tonne (Korea K-ETS, Japanese carbon tax, Australian safeguard mechanism, Israel, Chile, Mexico, Turkey, Colombia) are set to zero.

Only well-documented, quantified industrial cross-subsidies exceeding \$0.005 per kilowatt-hour are included. Germany receives the largest add-back (\$0.038/kWh) reflecting the EEG renewables-surcharge exemption and grid-fee exemption for energy-intensive industry (Agora Energiewende; BDEW). France receives \$0.015/kWh for postARENH regulated nuclear access. Spain, Italy, the Netherlands, and Belgium receive \$0.010/kWh each from the Eurostat nrg\_pc\_205 subsidies column (industrial band IB6). The United States receives \$0.015/kWh reflecting the industrial–residential rate differential in excess of cost-of-service documented by Borenstein (2012) and Davis and Hausman (2016). Korea receives \$0.020/kWh reflecting KEPCO industrial tariffs below cost-of-service (OECD Energy Policy Review). All other countries receive zero. $^{15}$

Three choices warrant note. First, the carbon adder uses 2024 annual-average market prices, not the social cost of carbon; using US EPA (2023) social-cost values would widen the OECD adjustment further. Second, we use existing-asset variable cost rather than replacement-cost capital for OECD nuclear and hydro; a replacement-cost treatment would raise Norwegian and French LRMCs materially. Third, the largest ten changes in per-kWh prices occur in Germany, Poland, Cyprus, Estonia, Netherlands, Czechia, Italy, Bulgaria, Malta, and Greece; the corresponding rank shifts in Table A1 illustrate how the symmetric specification reallocates comparative advantage toward countries with cleaner grids or cost-reflective tariffs rather than toward those with below-marginal-cost industrial rates.

Under the symmetric LRMC specification, the five lowest-cost producers are Kyrgyzstan, Ethiopia, Kosovo, Canada, and Tajikistan. Canada falls from second to fourth after a modest carbon adder of \$0.008 per kilowatt-hour. Poland drops 21 positions, Germany 10, the United States 10, and France 12, while Nordic low-carbon grids and Switzerland move by two positions or fewer. The qualitative conclusion is therefore reinforced rather than overturned: countries with cheap, clean electricity retain their cost advantage once both sides of the distortion are corrected.
"""
