# Cheap Energy Might Not Be Enough
# A Trade Model of AI Compute Services
## Abstract

Can energy-rich developing countries convert cheap electricity into AI compute exports? This paper develops a capacity-constrained trade model of AI compute services with bilateral frictions in delivery, regulation, and trust. Calibrating the model across 85 countries shows that several developing economies can produce compute at low cost, but this advantage rarely becomes export competitiveness. Because hardware dominates unit costs and is globally priced, cross-country production costs differ by only 12–20 percent. Modest regulatory, financing, and trust frictions can therefore erase the gains from cheap power. The binding constraint is institutional credibility rather than electricity prices, including enforceable data governance, stable regulation, credible power contracts, access to finance, and geopolitical alignment with buyers.


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

Training market. Since $\tau_{T} = 0$ , training is a homogeneous good with no distance-related quality degradation. Country k imports training whenever the world price, after adding the bilateral sovereignty premium, is lower than the price of producing domestically: $(1 + \lambda_{jk}) \cdot p_{T} < c_{k}$ , where $p_{T}$ is the competitive world training price. In the capacity-constrained equilibrium, the cheapest producer supplies up to its capacity, then the next cheapest producer enters, and so on until demand is met. The marginal training exporter $m_{T}$ is the index of the producer whose entry just satisfies total export demand. The equilibrium training price equals the marginal exporter's cost: $p_{T} = c_{(m_{T})}$ .

Without capacity constraints, $m_{T} = 1$ and the cheapest country serves all demand at its own cost, earning zero rent. With binding capacity constraints, $m_{T} > 1$ , the price rises to the cost of the marginal entrant, and all infra-marginal exporters earn positive rents: $\pi_{Tj} = (p_T - c_j) \cdot K_{Tj}$ . When a country allocates capacity across multiple uses, the shadow value $\mu_j$ of the capacity constraint equals the margin on the marginal activity. That activity is the least profitable use that still receives capacity. In the training-only case, $\mu_j = \pi_j$ ; in the multi-market case, $\mu_j \leq \pi_j$ because training, as the higher-margin activity, is served first.

Inference market. Since $\tau_{I} = \tau > 0$ , inference suffers distance-dependent quality degradation. The inference market for buyer k is localized, as only countries with latency $l_{jk} \leq \overline{l}$ can participate, and each faces a different delivered cost. The delivered inference price for buyer k is:

$$
p _ {I} (k) = (1 + \tau \cdot l _ {m _ {I} (k), k}) \cdot c _ {m _ {I} (k)},\tag{6}
$$

where $m_{I}(k)$ is the marginal inference supplier to k, determined by the capacity-constrained supply stack for k's inference market. Each GPU-hour of capacity is allocated to its highest-margin use, whether training exports, inference exports to various destinations, or domestic supply.

The cost-based equilibrium identifies the set of countries that could profitably produce and export compute. Whether these countries attract investment also depends on agglomeration economies, hyperscaler market structure, and network connectivity (Krugman 1991). In practice, AWS, Azure, and Google Cloud dominate the cloud compute market, and their location choices reflect scale economies and colocation effects that the competitive model does not capture. The capacity ceilings $\overline{K}_{j}$ partially capture the resulting gap between cost-based potential and realized investment; Section 7 discusses these limitations in more detail.

## 4. Equilibrium Properties

This section derives the properties of the capacity-constrained equilibrium introduced in Section 3. Full derivations are shown in Appendix B.

Proposition 1 (Country Taxonomy). With two service types (training with $\tau_{T} = 0$ , and inference with $\tau_{I} > 0$ ) and three possible statuses (export, domestic production, and import), there are nine potential regime combinations. In equilibrium, only five are realized. Each regime is coded by two letters: the first for training status, the second for inference (E = export, D = domestic production, I = import).

(i) EE. Training exporter + inference exporter. The cheapest producers, with $c_{j} < p_{T}$ , supply training globally and inference to nearby demand centers.

(ii) IE. Training importer + inference exporter. Countries with $c_{j} > p_{T}$ that are not cheap enough to compete in the global training market but serve as regional inference hubs due to low costs and proximity to demand centers ( $l_{jk}$ below the latency threshold $\bar{l}$ ).

(iii) ID. Training importer + inference domestic producer. Countries that import training but produce inference domestically, because the bilateral sovereignty premium $\lambda_{jk}$ or geographic isolation makes all foreign inference sources more expensive than domestic production.

(iv) DD. Domestic producer of both. Countries where $c_{k} \leq (1 + \lambda_{jk}) \cdot p_{T}$ , so the bilateral sovereignty premium is large enough to justify domestic production of both training and inference.

(v) II. Importer of both. High-cost countries with $c_{k} > (1 + \lambda_{jk}) \cdot p_{T}$ that import both training and inference from cheaper or closer suppliers.

The model rules out the remaining four regime combinations. A training exporter cannot simultaneously produce inference domestically or import inference. A country cheap enough to win a global training competition ( $c_j < p_T$ ) is necessarily cheap enough to export inference to nearby buyers (Proposition 4). A country that produces training domestically cannot import inference. The sovereignty premium that justifies domestic training also justifies domestic inference production, which faces latency degradation when imported. A country that produces training domestically while exporting inference would need both a strong domestic-sovereignty motive and very low costs. The model's cost ordering rules out that combination. Table 1 summarizes this taxonomy.

Proposition 2 (Capacity Constraints Reduce Concentration). In the training market, define the Herfindahl–Hirschman Index (HHI) as a measure of market concentration that is equal to the sum of squared market shares:

$HHI_{T} = \sum_{j}\left(\frac{K_{T,j}}{Q_{T,X}}\right)^{2}$ , where $Q_{T,X} = \sum_{k \in M_{T}} q_{T,k}$ denote total training export demand, the sum of training demand across all importing countries, and $K_{T,j}$ is country j's training export allocation (GPU-hours), bounded by the capacity ceiling $K_{T,j} \leq \overline{K}_{j}$ . Without capacity constraints, the cheapest producer captures all training demand and $HHI_{T} = 1$ . With binding capacity constraints on the cheapest producers, $HHI_{T} < 1$ , and $HHI_{T}$ is strictly decreasing in the number of capacity-constrained infra-marginal exporters. When low-cost producers reach capacity limits, residual demand shifts to higher-cost suppliers, reducing market concentration.

Proposition 3 (Sovereignty Switching Threshold). A country produces AI training domestically only when the sovereignty premium is large enough to offset the higher domestic cost. Formally, country k produces training domestically if and only if $\lambda_{jk} \geq \lambda_{k}^{*} = c_{k}/p_{T} - 1$ for every potential supplier j with $c_{j} < c_{k}$ ; equivalently, k imports whenever there exists a supplier j for which $\lambda_{jk} < \lambda_{k}^{*}$ . The threshold is increasing in $c_{k}$ and decreasing in $p_{T}$ . Under capacity constraints, $p_{T} > c_{(1)}$ , so the threshold is lower than in the unconstrained model. Capacity constraints reduce the sovereignty premium required for domestic production because they raise world prices, making imports more expensive. $^{7}$

Corollary. Capacity constraints reduce the welfare cost of sovereignty because the higher equilibrium price narrows the gap between domestic and import costs.

Proposition 4 (Training Exporters Nest Within Inference Exporters). If a country is cheap enough to export training (which can be done from anywhere), it is also cheap enough to export inference to nearby demand centers. $^{8}$ Training exporters therefore also export inference to nearby demand centers, provided that latency remains below the threshold $\overline{l}$ . A training exporter has the globally lowest $c_{j}$ . For inference to proximate demand centers, this cost advantage dominates the latency markup, so the same country wins the inference competition. Since training has no distance penalty while inference does, every country that exports training is also competitive in inference within its geographic neighborhood, but not vice versa.

## 5. Data

The propositions above generate testable predictions that depend on country-specific costs and bilateral frictions. Calibrating the production-cost and trade-cost parameters in equations (1)–(4) requires data on electricity prices, temperatures, construction costs, bilateral latencies, and bilateral sovereignty frictions (geopolitical alignment, regulatory compatibility, and sanctions).

Electricity prices. For European countries, we use prices from Eurostat (industrial band, 20,000–69,999) (Eurostat 2025). For non-European countries, prices are sourced from national regulatory tariff sheets and secondary sources. These include the U.S. Energy Information Administration (EIA 2025) for the United States, KEPCO for South Korea, $^{9}$ national utility tariffs for Central Asian countries, and GlobalPetrolPrices (2025) for the remaining countries. All prices are converted to \$/kWh at 2024 exchange rates.

Temperature and construction. Peak summer temperature is derived from ERA5 data (Hersbach et al. 2020) as the average monthly maximum in the three warmest months, aggregated across populated grid cells. Construction costs per watt of IT capacity are from the Turner & Townsend Data Center Construction Cost Index 2025 (Turner & Townsend 2025), for 37 countries. For the remaining countries, costs are predicted (Appendix E). Since construction is only 3–6 percent of total per-GPU-hour costs, imputation error has a limited impact on cost rankings.

Latency. Inter-country round-trip latency is measured using WonderNetwork's global ping dataset (WonderNetwork 2024). For each country pair, the median round-trip time (RTT) in milliseconds is used. Domestic latency defaults to 5 ms where no intra-country measurement is available.

Demand. Compute demand $q_{k}$ is proxied by installed data center capacity in MW (equation (4)). For the top 15 markets, capacity estimates are based on industry reports (Synergy Research, Cushman & Wakefield, CBRE, Mordor Intelligence). $^{10}$ For smaller markets, capacity is estimated from facility counts (Cloudscene 2025) and regional averages.

Bilateral compute-trade data are not yet available, so we calibrate the model from hardware prices, electricity tariffs, and facility-cost coefficients rather than estimating it from observed trade flows.

The calibration identifies the conditions under which FLOP exporting becomes viable. It also provides a framework that can be taken to gravity-style estimation as transaction-level data emerge.

## 6. Calibration and Results

## 6.1 Parameter calibration

PUE. The baseline $\varphi = 1.08$ matches Google's reported PUE for facilities with free-air cooling in cold climates (Google 2024). The sensitivity coefficient $\delta = 0.015$ per $^{\circ}$ C is estimated from cross-sectional variation in PUE across data center locations with different cooling loads (Liu et al. 2023). The threshold $\overline{\theta} = 15^{\circ}$ C is the outdoor temperature above which mechanical cooling is needed, below which free-air cooling suffices. These assumptions yield PUE values from 1.08 (Iceland, Scandinavia) to 1.41 (UAE), consistent with the industry average of 1.56 (Uptime Institute 2024). $^{11}$

Hardware. The calibration uses the NVIDIA H100 SXM GPU as the reference hardware platform, with a list price of \$25,000, a power of 700W, an economic lifetime of 3 years, and a utilization rate of 70 percent (Barroso et al. 2018). The calibration implies an amortized hardware cost $\rho = \$1.358/\text{hr}$ . This amortization is straight-line and includes no cost of capital. Columns (1)–(3) of Table 3 therefore hold financing costs at zero, so the cross-country spread reflects only electricity, climate, and construction; column (4) adds country-specific financing through the WACC adjustment of Section 7.2. Networking costs are calibrated at $\eta = \$0.15/\text{hr}$ , based on the same three-year horizon (Barroso et al. 2018). GPU and networking equipment prices are assumed to be uniform across countries.

Latency degradation. The parameter $\tau$ is set at $\tau = 0.0008$ per ms, implying that 100 ms of round-trip latency (roughly the intercontinental round-trip between Europe and East Asia) inflates inference cost by 8 percent, consistent with the finding in Deloitte and Google (2020) for e-commerce.


Table 2 reports all model parameters. Country-specific values, including electricity prices, temperatures, construction costs, and resulting unit costs, are reported in Table A1 (Appendix A).

## 6.2 Cost Rankings and Trade Patterns

Figure 1 summarizes the model structure, from country endowments through production costs and prices to equilibrium regimes. We first correct electricity prices for subsidies, then add bilateral trade frictions.

Under observed electricity tariffs, the cheapest producer in our sample of 85 countries is Iran, followed by Turkmenistan and Ethiopia (Column(1) of Table 3). This ranking, however, overstates the role of production-cost advantage. Iran’s headline electricity cost reflects one of the world’s largest fossil fuel subsidies. Turkmenistan, Algeria, Qatar, and several other low-cost producers face similar distortions.

We replace subsidized tariffs with cost-recovery prices to distinguish real comparative advantage from subsidy-driven advantage. The cost-recovery prices are defined as the long-run marginal cost (LRMC) of the dominant generation technology at opportunity-cost fuel prices (IMF 2025, Lazard 2025). We apply this adjustment to 13 countries whose retail electricity prices fall below the estimated LRMC. $^{13}$ Appendix G develops a symmetric specification that additionally corrects OECD and high-income tariff distortions—carbon externalities and industrial cross-subsidies—and confirms that the qualitative ranking is reinforced rather than overturned. The subsidy gap ranges from \$0.000 to \$0.080/kWh. For Iran, a 100 MW IT-load data center would receive \$93 million in implicit transfers per year. At hyperscale, such subsidies are fiscally unsustainable. The resulting cost-recovery ranking (column (2) of Table 3) shifts the top of the ranking toward hydropower-rich countries: Kyrgyzstan, Ethiopia, Kosovo, Canada, and Tajikistan. Iran drops from first to 24th, and Turkmenistan falls 16 places. 35 countries change their trade regimes, but the remaining cross-country variation is narrow (Table A2 extends the ranking to all countries).

The cost ranking diverges sharply from observed investment patterns, indicating that low production cost alone is not sufficient to attract investment. Eight of the twenty cheapest producers have under 100 MW of installed capacity (e.g., Kyrgyzstan: rank 1, 5 MW), while countries outside the top twenty host large clusters (Netherlands: rank 67, 1,800 MW; Ireland: rank 83, 1,260 MW). Thus, the cost ranking should be interpreted as the set of feasible exporters, not as a prediction of realized investment.

Data-center FDI patterns support this interpretation. Among EMDEs, the largest recipients of data-center investment are Malaysia, India, and Brazil, countries with moderate electricity costs but strong regulatory frameworks and credible grid infrastructure. In contrast, the cheapest producers (Kyrgyzstan, Tajikistan, Ethiopia) received virtually no data-center FDI (Aykut et al. 2026). Most investment flows occur between geopolitical allies. This pattern is consistent with the bilateral sovereignty premium and suggests that cost alone does not determine where capacity is built (Straub et al. 2026). Econometric evidence shows that electricity costs do not predict data-center location once market size and the regulatory environment are controlled for (Caoui and Steck 2025).

Policy-readiness indicators reinforce this interpretation. Economies with advanced AI and cloud strategies—such as Singapore, Australia, Japan, and South Korea—record estimated economic impacts from AI and cloud investment of 3–4 percent of GDP, compared with less than 1 percent in Indonesia and Viet Nam (Katz et al. 2025). In the model, institutional quality stands in for the complementary investments that separate these groups: digital skills, regulatory predictability, and grid modernization. Countries that align digital strategies with energy-sector planning are becoming preferred destinations for hyperscalers. Examples include Malaysia’s National Energy Transition Roadmap, Brazil’s electricity mix of more than 80 percent renewables, and the UAE’s nuclear- and solar-powered AI hubs. These cases are consistent with the model’s prediction that moderate costs can attract investment when paired with credible institutions (Aykut et al. 2026).

The bilateral sovereignty premium $\lambda_{ij}$ reshapes trade patterns along geopolitical lines. Between allies with mutual data adequacy agreements (e.g., EU member states), the effective premium is near zero. For geopolitical adversaries, it is effectively infinite—the United States would not source training from Iran regardless of cost, and current sanctions make such transactions illegal. Column (3) of Table 3 reports the bilateral specification. The bilateral sovereignty premium has the strongest effect on inference. Within Europe, latency raises costs by 1–3 percent, so a small sovereignty premium can shift sourcing from foreign suppliers to domestic production.

Trade flows under capacity constraints. Weighting the sourcing patterns by demand shares from equation (4) and applying capacity constraints, the equilibrium training price is $p_T = \$1.60/\text{hr}$ , set by the marginal exporter's cost. Training demand is served by a dominant exporter (HHI = 0.984, with 3 other producers at the margin), leaving the training market close to the unconstrained benchmark of Proposition 2. The largest shadow values of grid capacity are in Kyrgyzstan (\$0.019/hr), Ethiopia (\$0.003/hr), and Kosovo (\$0.001/hr), indicating modest returns to capacity expansion. When bilateral sovereignty premia are added, most countries switch to domestic training. The remaining export market is served by a single exporter at \$1.58 per GPU-hour.

Inference exports are more dispersed, with the top five exporters being Canada (43 percent), Kyrgyzstan (26 percent), Kosovo (10 percent), Indonesia (0.9 percent), and Ukraine (0.5 percent), collectively accounting for 80 percent of cross-border inference demand (HHI = 0.265).

Among developing countries, Kyrgyzstan captures 26 percent of global inference demand by serving China, Kazakhstan, and Uzbekistan, a large share for a country with a GDP of under \$15 billion. Kosovo serves as an inference hub for 21 countries, accounting for 10 percent of global inference demand.

Major demand centers. The model's predictions differ across major AI demand centers because each faces a distinct latency geography. For the United States, the cost-recovery equilibrium sources training from the lowest-cost available producer and inference from Canada. For Germany, France, and the United Kingdom, inference is sourced from Kosovo. For China, the lowest-cost foreign inference supplier is Kyrgyzstan. Inference supply therefore clusters around latency-constrained regional hubs, with each major market served by a nearby low-cost producer.

Among these demand centers, China illustrates the DD regime. China hosts one of the world's largest data-center markets. Yet almost all capacity is built and financed by domestic technology firms and state-owned operators, including Alibaba Cloud, Tencent, Baidu, and China Telecom (Aykut et al. 2026). This outcome fits the mechanism above: China's sovereignty premium is effectively infinite for most Western buyers, yet its large domestic demand and moderate production costs make domestic production of both training and inference the equilibrium strategy. Government initiatives such as the Eastern Data, Western Computing project further support domestic sourcing by shifting energy-intensive computing to western provinces with cheaper power.

Raising the uniform premium to 20 percent shifts five additional countries (including Croatia, Cyprus, and Germany) to domestic training, reducing the share of global training demand available to foreign producers from 3 percent to 0 percent. Inference exports respond less to sovereignty premia because nearby suppliers retain a latency advantage.

Welfare cost of sovereignty. The bilateral sovereignty premium imposes a welfare cost with two components, an import markup (importers pay $\lambda_{ij} \cdot p_{T}$ per unit above the competitive price) and an allocative inefficiency (countries with $p_{T} < c_{k} \leq (1 + \lambda_{ij}) \cdot p_{T}$ produce domestically at above-world-price costs). Under capacity constraints, both components are smaller than in the unconstrained model because the higher world price narrows the gap between domestic and import costs. The demand-weighted welfare cost is 1.6 percent of total compute spending, in the range of the welfare gains from trade in goods estimated in the quantitative trade literature, which range from roughly 0.2 percent to 10 percent depending on country size and specification (Eaton and Kortum 2002, Arkolakis et al. 2012). At current demand levels (approximately $6 \times 10^{10}$ GPU-hours at \$1.50/hr), this amounts to roughly \$1.44 billion per year. At this scale, governments can rationally choose domestic production for sensitive workloads. Examples include military applications, health records, and national statistical systems.

The welfare implications depend on whether the sovereignty premium reflects genuine security concerns or overly broad regulation. Domestic processing may be justified for confidential data, but current policy often extends the logic of sovereignty to routine commercial computation. In the model, the bilateral premium shifts most countries toward domestic production, reducing the gains from specialization. The welfare cost is large in dollar terms but modest relative to total compute spending. Because part of the premium reflects weak international data governance, enforceable data-protection agreements, such as those within the EU, reduce it. In their absence, even commercial buyers have reason to choose domestic processing over cheaper foreign supply.

Sovereignty preferences are not limited to developing countries: France's SecNumCloud certification mandates EU-only data hosting and staffing, effectively excluding U.S. hyperscalers from sovereign workloads. Developing countries that adopt broad data localization requirements risk foreclosing both import savings and regional export opportunities, the specialization gains that the model predicts. The World Bank (2025) frames this as a core policy trade-off: building domestic capacity versus securing affordable access to international cloud services.

## 7. Robustness, Caveats, and Extensions

## 7.1 Robustness to parameter variation

Sensitivity analysis. Cost rankings are robust to substantial variations in parameters. Table A3 (Appendix C) reports results across three robustness specifications that vary the share of hardware costs. A rise in global hardware costs increases the globally priced cost share, compressing the locally penalized component and muting governance penalties for developing-country exporters. On the other hand, improved cooling technology that flattens the PUE–temperature curve narrows the advantage of cold-climate countries but leaves energy-price differences intact. A reduction in sovereignty frictions shifts countries from domestic production to importing. This expands trade volumes but reduces exporter rents.

Hardware cost share. Varying $\rho$ by $\pm4$ percent changes the composition of the top fifteen countries, but the qualitative result is stable across all specifications. Because hardware is globally priced and dominates unit cost, a higher $\rho$ compresses the cross-country cost spread, making electricity price differences less decisive and facilitating entry by developing countries. Countries that combine cheap energy with adequate governance retain their cost advantage regardless of the chosen parameter.

Uniform sovereignty premium. As a robustness check, we compute the equilibrium under a uniform premium $\lambda = 0.10$ . The uniform premium produces similar regime assignments: most countries produce domestically under either specification. The main difference is that the bilateral premium excludes sanctioned countries from serving any demand center, while the uniform premium treats all pairs identically. The bilateral specification is preferred because it captures observed cross-country heterogeneity.

Sovereignty tiers. Each country's demand is divided into three tiers: sovereign workloads (10 percent, domestic only), regulated workloads (20 percent, higher regulatory compatibility weight), and commercial workloads (70 percent, geopolitical alignment only). Under calibrated parameters, tiering leaves regime assignments unchanged for all countries, so Table 3 omits a separate tiered column. Tiering primarily affects inference sourcing: regulated workloads shift toward suppliers with strong data governance, favoring EU and APEC CBPR participants over closer but less regulated alternatives. $^{14}$

## 7.2 Caveats and omitted frictions

The calibration adjusts for energy subsidies and institutional quality, but several constraints remain outside the model and would further narrow the set of viable exporters. GPU export controls bar Iran, Russia, and Belarus from acquiring current-generation hardware. Water scarcity constrains cooling in the Middle East and North Africa; hyperscale data centers can consume billions of liters of water annually, and next-generation high-density GPU clusters increasingly rely on liquid-cooling technologies, intensifying this pressure in water-stressed economies. Regulated tariffs in many developing countries cover operating expenses but not the full capital cost, raising concerns about financial sustainability. Exporting compute at scale while the domestic energy sector cannot maintain its capital stock may prove politically unsustainable. Finally, logistics costs and local distribution markups can raise effective GPU prices by 5–15 percent in developing countries that are not subject to export bans, eroding the thin cost advantages. These omitted constraints all work against developing-country competitiveness. The calibration results should therefore be read as upper bounds.

Endogenous electricity prices. The model treats electricity prices as fixed. In small countries with low-cost power, a hyperscale facility can be large relative to the host grid — a 100 MW data center would consume roughly 3 percent of Kyrgyzstan’s 3,800 MW national output. At the multi-facility scale, data centers would compete with residential and industrial electricity demand, making regulatory intervention likely. The capacity ceiling $\overline{K}_{j}$ partially addresses this, but the fixed-price assumption implies that the cost advantages in Table A1 are upper bounds. Allowing electricity supply curves to slope upward would narrow these apparent advantages. Evidence from the US suggests the AI workloads, combined with broader electrification, could raise wholesale electricity prices by roughly 19 percent between 2025 and 2028 (Chandramowli et al. 2024), and AI data-center expansion alone could increase retail prices by 8–9 percent by 2030 (IMF 2025). Alvarez et al. (2026) find that in the US, a one-unit increase in log cumulative data-center revenue raises local electricity prices by roughly 0.9 percent. Counties that have ever hosted a data center have retail prices about 3.9 percent higher. For small grids such as Kyrgyzstan’s, the proportional impact would likely be larger, further eroding the cost advantages documented above.

Newer GPUs, such as NVIDIA's B200, increase training throughput substantially but also raise power draw to roughly 1 kW. Higher power draw makes electricity prices more important, which modestly strengthens the advantage of low-cost power producers. Because higher capital costs lead developing economies to refresh GPUs less frequently, they are more likely to operate older, less efficient hardware, raising their cost per effective FLOP and partly offsetting their electricity-cost advantage. The qualitative ranking is not driven by the choice of GPU generation.

Form of the sovereignty wedge. $\lambda_{jk}$ is modeled as an ad valorem markup on the cost of compute. This specification is standard in the services trade, but it simplifies how sovereignty frictions operate. Many sovereignty frictions are closer to fixed entry costs than to variable markups. Cloud security certifications, sanctions screening, export control compliance, and bilateral digital services agreements all raise the cost of entering a market. Our model also treats $\lambda_{jk}$ as fixed, but in practice, sanctions, export-control revisions, and regulatory reversals arrive as exogenous shocks. The impact of these two assumptions on the stability of our results could be assessed through a Monte Carlo simulation using stochastic $\lambda_{jk}$ and fixed costs. Both extensions would likely make entry harder for developing-country exporters, so they should strengthen rather than weaken the main result.

Cost of capital. Because hardware dominates the cost stack, financing terms can determine the ranking. At an 8 percent WACC, an OECD hyperscaler pays about \$1.58 per GPU-hour in hardware costs. At an 18 percent WACC, a locally financed developing-country operator pays \$1.87, a \$0.29 gap on hardware alone (Calcaterra et al. 2024). Column (4) of Table 3 reports the cost-recovery ranking with hardware amortized at each country's income-group WACC, using 8 percent for HICs, 12 percent for UMICs, 15 percent for LMICs, and 18 percent for LICs. Once financing costs enter, cheap electricity explains less of the ranking, and several regime classifications shift.

Institutional credibility enters the compute trade through two channels: the sovereignty premium $\lambda_{ij}$ and the cost of capital facing any locally financed operator. Hyperscaler-led foreign direct investment partially bypasses the financial channel. If a multinational owns, finances, and operates the facility outright, it may fund at its home WACC — but partial ownership, local debt, sovereign guarantees, and the pass-through of country risk to operating agreements reintroduce the channel in proportion to the host country's financial exposure. A fully hyperscaler-financed project is therefore best treated as a limiting case rather than the baseline. For this reason, Column (4) is the more realistic benchmark for assessing whether developing countries can capture compute-export rents with domestic capital.

## 7.3 Extensions

Edge computing. Edge computing could relax one of the model's central constraints. As more AI demand comes from real-time inference on lightweight models deployed on local devices, the capacity constraint for inference becomes less binding: inference need not be concentrated in large data centers but can be distributed across many small nodes connected via existing mobile networks. If this trend accelerates, inference exports may become less concentrated, and more countries could serve regional demand. For EMDEs with weak grid infrastructure but adequate mobile connectivity, edge computing may offer a leapfrogging path that bypasses the grid bottlenecks central to the model (Aykut et al. 2026). A fuller trade model could distinguish centralized GPU clusters for training from distributed edge nodes for inference.

## 8. Conclusion

Energy-rich developing countries can produce compute at low cost, but low cost alone does not make them exporters. Training can be traded globally, inference is constrained by latency, and both are affected by bilateral sovereignty frictions. Because hardware is globally priced, electricity and cooling create only a thin cost advantage, while the institutional frictions facing developing-country suppliers are often wider than that advantage.

The 85-country calibration shows that hardware dominance compresses cross-country differences in production costs. Cheap electricity and favorable cooling can make countries cost-competitive quickly, but modest frictions, including a sovereignty premium, weak governance, or a higher cost of capital, can erase that advantage. Compute may therefore be unusually accessible on engineering grounds, yet unusually exposed to policy and financing frictions because the production-cost spread is narrow.

Under the bilateral sovereignty specification, weak institutional credibility eliminates much of the cost advantage that developing countries hold under pure cost-recovery pricing. The binding constraint is often not the electricity price itself but rather non-sanctioned status, credible long-term power contracts, stable network connectivity, enforceable data governance rules, and a regulatory environment that supports capital-intensive investment. Where those conditions are absent, buyers shift toward domestic production despite higher production costs. The resulting welfare loss is large in dollars but modest relative to total compute spending, at about 1.6 percent, so governments with legitimate data-sovereignty objectives may rationally choose domestic supply.

For developing countries pursuing compute exports, the binding policy levers lie mostly outside the electricity tariffs. The first is financing. Because hardware dominates the cost stack, differences in the weighted average cost of capital can exceed the energy-cost advantage by several times. Sovereign guarantees, blended finance, multilateral risk insurance, and hyperscaler co-investment can therefore narrow the competitiveness gap more than any feasible reduction in electricity tariffs. The second lever is regulatory credibility. Data-adequacy status, mutual recognition agreements, and recognized cloud security certifications reduce the trust premium applied by foreign buyers. Broad data-localization mandates raise that premium and can foreclose export opportunities.

The final policy question is how much surplus the host country captures. The Kyrgyzstan facility in Appendix D is NPV-positive, but under full foreign-hyperscaler ownership, the host country retains little beyond electricity payments and construction-phase jobs. The domestic share of operating surplus depends on taxation, equity participation, and royalty terms. Cheap energy can make a country cost-competitive, but rent capture depends on financing, governance, and ownership.

The policy implications differ for training and inference. Restricting training imports raises costs without improving service quality, because training has no meaningful proximity advantage. Domestic inference production is easier to justify, since low latency can provide a genuine quality-of-service benefit, although that rationale weakens for countries located near low-cost regional hubs.

FLOP exporting is best understood as capital-intensive resource processing: imported equipment converts local energy into an exportable digital service with minimal domestic labor input. Unlike extractive commodities, the energy input can be renewable, and demand for compute is growing faster than demand for most physical commodities. Still, the resource-curse literature remains relevant because concentrated compute-export revenues can generate exchange-rate pressure, institutional risks, and exposure to demand cycles. Whether these risks materialize depends on ownership structures, fiscal arrangements, and domestic rent capture. As bilateral compute-trade data become available, this framework can be estimated using gravity-style methods.

Alvarez, F., Argente, D., Chow, J., and D. Van Patten. (2026). “Data Centers and Local Economies in the Age of AI: A Shift-Share Approach.” NBER Working Paper No. 35194.

Anderson, J. and D. Marcouiller. (2002). “Insecure Trade: Reduced-Form Evidence.” Review of Economics and Statistics, 84(2): 342–352.

Anderson, J. and E. van Wincoop. (2003). “Gravity with Gravitas: A Solution to the Border Puzzle.” American Economic Review, 93(1): 170–192.

Antràs, P. (2003). “Firms, Contracts, and Trade Structure.” Quarterly Journal of Economics, 118(4): 1375–1418.

Arkolakis, C., Costinot, A., and A. Rodríguez-Clare. (2012). “New Trade Models, Same Old Gains?” American Economic Review, 102(1): 94–130.


Aykut, D., Ozyurt, S., Jung, K., and E. Vergara Cobos. (2026). “Data Center and AI Investment in EMDEs: Risks and Opportunities.” Watch This Space. Washington, DC: World Bank Group.

Bailey, M., Strezhnev, A., and E. Voeten. (2017). “Estimating Dynamic State Preferences from United Nations Voting Data.” Journal of Conflict Resolution, 61(2): 430–456.

Barroso, L., Hölzle, U., and P. Ranganathan. (2018). The Datacenter as a Computer: Designing Warehouse-Scale Machines, 3rd ed. San Rafael, CA: Morgan & Claypool.

Benz, S. and A. Jaax. (2020). “The Costs of Regulatory Barriers to Trade in Services: New Estimates of Ad Valorem Tariff Equivalents.” OECD Trade Policy Papers, No. 238. Paris: OECD Publishing.

Biglaiser, G., Crémer, J., and A. Mantovani. (2024). “The Economics of the Cloud.” Toulouse School of Economics Working Paper No. 24-1520.

Blinder, A. (2006). “Offshoring: The Next Industrial Revolution?” Foreign Affairs, 85(2): 113–128.

Borenstein, S. (2012). “The Redistributional Impact of Nonlinear Electricity Pricing.” American Economic Journal: Economic Policy, 4(3): 56–90.

Brainard, S. (1997). “An Empirical Assessment of the Proximity-Concentration Trade-off.” American Economic Review, 87(4): 520–544.

Calcaterra, M., Reis, L., Fragkos, P., Briera, T., Boer, H., Egli, F., et al. (2024). “Reducing the Cost of Capital to Finance the Energy Transition in Developing Countries.” Nature Energy, 9(10): 1241–1251.


Chandramowli, S., Cook, P., Mackovyak, J., Parmar, H., and M. Scheller. (2024). Power Surge: Navigating US Electricity Demand Growth. ICF.

Cloudscene. (2025). Global Data Center Directory. cloudscene.com.

Davis, L., and C. Hausman. (2016). “Market Impacts of a Nuclear Power Plant Closure.” American Economic Journal: Applied Economics, 8(2): 92–122.

Deloitte. (2025). “Technology, Media, and Telecommunications Predictions 2026.” Deloitte Insights.

Deloitte and Google. (2020). “Milliseconds Make Millions.” Deloitte Digital and Google.

Eaton, J., and S. Kortum. (2002). “Technology, Geography, and Trade.” Econometrica, 70(5):1741–1779.

EIA. (2025). Electric Power Monthly. U.S. Energy Information Administration.

Epoch AI. (2024). “The Training Compute of Notable AI Models.” epochai.org.

Eurostat. (2025). Electricity Prices for Non-Household Consumers (nrg\_pc\_205). Luxembourg: Eurostat.

Firebird. (2026). “Phase 2 of Armenia AI Megaproject, Scaling to \$4 Billion and 50,000 GPUs.” Press release, January 2026.

Flucker, S., Tozer, R., and R. Whitehead. (2013). “Data Centre Energy Efficiency Analysis to Minimize Total Cost of Ownership.” Building Services Engineering Research and Technology, 34(1): 103–117.

GlobalPetrolPrices. (2025). Electricity Prices Around the World. globalpetrolprices.com.

Goldfarb, A., and D. Trefler. (2018). “AI and International Trade.” In The Economics of Artificial Intelligence. Chicago: Univ. of Chicago Press, pp. 463–492.


Hausmann, R., Hwang, J., and D. Rodrik. (2007). “What You Export Matters.” Journal of Economic Growth, 12(1): 1–25.

Heckscher, E. (1919). “The Effect of Foreign Trade on the Distribution of Income.” Ekonomisk Tidskrift, 21: 497–512.

Helpman, E., Melitz, M., and S. Yeaple. (2004). “Export Versus FDI with Heterogeneous Firms.” American Economic Review, 94(1): 300–316.

Hersbach, H., et al. (2020). “The ERA5 Global Reanalysis.” Quarterly Journal of the Royal Meteorological Society, 146(730): 1999–2049.

IEA. (2025). “Energy Demand from AI.” Published online at iea.org.

IMF. (2025). “Fossil Fuel Subsidies Data: 2025 Update.” IMF Working Paper WP/25/270.

Katz, R., Jung, K., and F. Callorda. (2025). “The Economic Impact of AI and Cloud Investment in Asia-Pacific.” Report prepared for the Asian Development Bank.

Korinek, A., and J. Stiglitz. (2021). “Artificial Intelligence, Globalization, and Strategies for Economic Development.” NBER Working Paper No. 28453.

Krugman, P. (1991). “Increasing Returns and Economic Geography.” Journal of Political Economy, 99(3): 483–499.

Lazard. (2025). Lazard's Levelized Cost of Energy Analysis, Version 17.0. lazard.com.

Lehdonvirta, V., Wu, B., and Z. Hawkins. (2024). “Compute North vs. Compute South: The Uneven Possibilities of Compute-Based AI Governance Around the Globe.” Proceedings of the AAAI/ACM Conference on AI, Ethics, and Society, 7(1): 828–838.

Limão, N., and A. Venables. (2001). “Infrastructure, Geographical Disadvantage, Transport Costs, and Trade.” World Bank Economic Review, 15(3): 451–479.

Liu, Z., Wierman, A., Chen, Y., Raber, B., and J. Moriarty. (2023). “Sustainability of Data Center Digital Twins.” Proceedings of ACM e-Energy, pp. 178–189.

NVIDIA. (2024). NVIDIA H100 Tensor Core GPU Datasheet. nvidia.com.

Ohlin, B. (1933). Interregional and International Trade. Cambridge, MA: Harvard University Press.

Pilz, K., Mahmood, Y., and L. Heim. (2025). AI's Power Requirements Under Exponential Growth. Santa Monica, CA: RAND Corporation, RR-A3572-1.


Stojkoski, V., Koch, P., Coll, E., and C. Hidalgo. (2024). “Estimating Digital Product Trade through Corporate Revenue Data.” Nature Communications, 15: 5262.

Straub, S., He, H., Li, Y., Lyu, X., Steinbuks, J., Vergara Cobos, E., et al. (2026). Infrastructure Foundations: From Current Assets to Future Growth. Sustainable Infrastructure Series. Washington, DC: World Bank.

Turner & Townsend. (2025). Data Centre Construction Cost Index 2025. turnerandtownsend.com.

Uptime Institute. (2024). Global Data Center Survey Results 2024. uptimeinstitute.com.

WonderNetwork. (2024). Global Ping Statistics. wondernetwork.com.

World Bank. (2024). World Development Indicators. Washington, DC.

World Bank. (2025). Digital Progress and Trends Report 2025: Strengthening AI Foundations. Washington, DC: World Bank.

Figure 1. Model structure

[[KC_IMAGE_001]]

Notes: Country endowments (gray) determine production cost $c_{j}$ , which together with capacity $K_{j}$ (purple) sets the world training price $p_{t}^{*}$ and regional inference price $p_{i}^{*}(k)$ . Regime conditions sort countries into five equilibrium regimes (coral) from Proposition 1.

Table 1. Country regime taxonomy (Proposition 1)


Notes: $\checkmark$ = feasible in equilibrium. $X$ = ruled out. Grey cells cannot arise. Roman numerals correspond to regime labels in Proposition 1. Letter codes (EE, IE, ID, DD, II) denote training status (first letter: E = export, I = import, D = domestic) and inference status (second letter), used in Table 3.

Table 2. Model parameters


Notes: Hardware cost $\rho = P(\text{GPU}) / (\text{L} \cdot \text{H} \cdot \beta)$ . $\text{PUE}(\theta) = \varphi + \delta \cdot \max(0, \theta - \bar{\theta})$ . RTT = round-trip time, the network delay for a data packet to travel from client to server and back, measured in milliseconds. Sanctions exposure is captured by the bilateral sovereignty premium $\lambda_{ij}$ (equation 2).

Table 3. Country rankings under alternative cost and sovereignty specifications


Notes: Top 25 countries by delivered price under each specification. P $_{j}$ = delivered price from seller j (\$/GPU-hr) from equation (3). Under specs (1)–(2), $\lambda$ = 0, so P $_{j}$ = c $_{j}$ . Under spec (3), P $_{jk}$ = c $_{j}$ (1 + $\lambda_{jk}$ ) where k = United States. EE = training + inference exporter; IE = inference exporter; ID = hybrid (imports training, domestic inference); DD = domestic producer; II = full importer. (1) Raw: observed electricity tariffs. (2) Cost-recovery: subsidized tariffs replaced with LRMC. (3) Bilateral: cost-recovery prices with bilateral sovereignty premium $\lambda_{jk}$ from equation (2); countries ranked by delivered price to US buyer. (4) CR + host WACC: cost-recovery prices with hardware amortization computed at the host country's weighted average cost of capital (HIC 8%, UMIC 12%, LMIC 15%, LIC 18%; annuity formula applied over a

three-year GPU life). This column isolates the cost-of-capital channel that columns (1)–(3) suppress by amortizing hardware at a single straight-line $\rho$ with no financing cost. \* = sanctioned/GPU-blocked. $\dagger$ = developing-country exporter. See Table A2 for all 85 countries.

Table A1. Country-specific calibration parameters


Notes: Countries sorted by cost-recovery adjusted rank (ascending). $p^{E}$ = national electricity price for industrial/data center consumers (\$/kWh). $\theta_{j}$ = peak summer temperature (°C). PUE = Power Usage Effectiveness. Constr. = predicted data center construction cost (\$/W of IT load). $\bar{k}_{j}$ = installed data center power

capacity (MW). $\omega_{j}$ = country share of global compute demand from equation (4). $c_{j}$ = hourly cost of operating one H100 GPU (electricity + hardware at \$1.36/hr + amortized construction; excludes networking $\eta$ = \$0.15/hr, which is added in the equilibrium computations in Section 6). Cost-Rec. $p^{E}$ = cost-recovery electricity price. For 13 countries with subsidized tariffs, this is the estimated long-run marginal cost of electricity generation (shown in bold). For all other countries, the cost-recovery price equals the observed tariff. The 37 DCCI countries span 52 markets: Australia, Austria, Brazil, Canada, Chile, China, Colombia, Denmark, Finland, France, Germany, Greece, India, Indonesia, Ireland, Italy, Japan, Kenya, Malaysia, Mexico, Netherlands, New Zealand, Nigeria, Norway, Poland, Portugal, Saudi Arabia, Singapore, South Africa, South Korea, Spain, Sweden, Switzerland, UAE, UK, Uruguay, and USA. The 95% prediction intervals for imputed countries span about ±\$3.50/W, which translates to ±\$0.02/hr in total cost (1.5–2% of the mean).

Table A2. Country rankings under alternative cost and sovereignty specifications (all countries)


Notes: See Table 3 notes for column definitions. Countries sorted by specification (2) rank (ascending).

## Appendix B: Model Derivation

This appendix provides the full derivation of the capacity-constrained Ricardian model summarized in Sections 3–4.

## B.1 Primitives

Each country j is endowed with a capacity ceiling $\overline{K}_{j}$ (GPU-hours per period), representing the maximum volume of compute it can supply. Country j faces unit production cost $c_{j}$ from equation (1). On the demand side, total compute demand from country k is $q_{k}$ from equation (4). Training demand is $q_{Tk} = \alpha \cdot q_{k}$ and inference demand is $q_{Ik} = (1 - \alpha) \cdot q_{k}$ . Countries are ordered by cost: $c_{(1)} \leq c_{(2)} \leq \ldots \leq c_{(N)}$ .

## B.2 The Training Market

Country k imports training if and only if $(1 + \lambda_{jk}) \cdot p_{T} < c_{k}$ , where $\lambda_{jk}$ is the bilateral sovereignty premium from equation (2). The set of training importers is $M_{T} = \{ k : c_{k} > (1 + \lambda_{jk}) \cdot p_{T} \}$ and total training export demand is $Q_{T,X} = \sum_{k \in M_{T}} q_{T,k}$ . The marginal training exporter $m_{T}$ is defined by:

$$
m _ {T} = \min \{m: \sum_ {i = 1} ^ {m} K _ {T, (i)} \geq Q _ {T, X} \}.\tag{B.1}
$$

The equilibrium training price is $p_{T} = c(m_{T})$ . Training rent for country j with $c_{j} < p_{T}$ is $\pi_{Tj} = (p_{T} - c_{j}) \cdot K_{Tj}$ .

## B.3 The Inference Market

The feasible supplier set for demand center k is $S(k) = \{j : l_{jk} \leq \bar{l}\}$ . The marginal cost of delivering one effective unit of inference from j to k is:

$$
M C _ {I} (j, k) = (1 + \tau \cdot l _ {j k}) \cdot c _ {j}.\tag{B.2}
$$

The inference rent per GPU-hour allocated to serving $k$ is $r_I(j,k) = p_I(k) / (1 + \tau \cdot l_{jk}) - c_j$ .

## B.4 Capacity Allocation

Let $K_{T,j}$ denote the GPU-hours country $j$ allocates to training exports and $K_{I,j \to k}$ the GPU-hours it allocates to inference exports to buyer $k$ , so that total capacity used by country $j$ is $K_j = K_{T,j} + \sum_k K_{I,j \to k}$ . Each GPU-hour is allocated to its highest-margin use. The margins per GPU-hour are: training exports $r_T(j) = p_T - c_j$ ; inference exports to $k$ : $r_I(j,k) = p_I(k) / (1 + \tau \cdot l_{jk}) - c_j$ . Total rent from operating $K_j$ GPU-hours is:

$$
\Pi_ {j} (K _ {j}) = \sum_ {n = 1} ^ {K _ {j}} r _ {j} ^ {(n)},\tag{B.3}
$$

which is concave and piecewise linear in $K_{j}$ .

## B.5 Equilibrium Definition and Existence

A competitive equilibrium consists of a training price $p_{T}$ , inference prices $\{p_{I}(k)\}$ , and capacity allocations $\{K_{j}\}$ such that: (i) each GPU-hour is allocated to its highest-margin use; (ii) training and inference markets clear; (iii) all allocations are feasible ( $K_{j} \leq \overline{K}_{j}$ ). Existence follows from a fixed-point argument: the training supply curve is a step function with steps at $c_{(i)}$ and widths $\overline{K}_{(i)}$ ; intersection with the demand curve pins down $p_{T}$ .

## B.6 Welfare Cost of Sovereignty

The welfare cost has two components. For each importing country k, let $j_{k}^{*}$ denote its equilibrium supplier (the seller minimizing delivered cost), and write $\lambda_{jk}$ evaluated at $j = j_{k}^{*}$ . Import markup:

$$
D W L _ {i m p o r t} = \sum_ {k \in M _ {T}} q _ {T k} \cdot \lambda_ {j k} \cdot p _ {T}.\tag{B.4}
$$

Allocative inefficiency:

$$
D W L _ {a l l o c} = \sum_ {{k: p _ {T} <   c _ {k} \leq (1 + \min _ {j} \lambda_ {j k}) p _ {T}}} q _ {T k} \cdot (c _ {k} - p _ {T}).\tag{B.5}
$$

Total: DWL = $DWL_{import} + DWL_{alloc}$ . Under capacity constraints, both components are smaller because the higher $p_{T}$ narrows the gap between domestic and import costs.

## Appendix C: Sensitivity Analysis

Table A3 reports cost-recovery rankings under three robustness specifications. The baseline uses the calibrated hardware cost; the alternative scenarios vary the hardware cost share to test sensitivity of the rankings.

Table A3. Sensitivity of cost-recovery rankings to parameter variation


Notes: Each row uses cost-recovery pricing (subsidized tariffs replaced with LRMC). Dev top 15 = number of developing countries in top 15. Max spread = maximum percentage difference between costliest and cheapest producer. Spearman $\rho$ vs baseline = rank correlation with baseline scenario.

## Appendix D: Data Center Investment Model — Kyrgyzstan

This appendix presents a 15-year discounted cash flow (DCF) analysis for a hypothetical 40 MW data center in Kyrgyzstan, the lowest-cost seller in the cost-recovery-adjusted calibration. Table A4 summarizes facility parameters, Table A5 presents the year-by-year cash flow, and Table A6 reports sensitivity to parameter variation.

Table A4. Facility specification


Notes: WACC = 60% × 15% (cost of equity) + 40% × 10% × (1 - 10%) (after-tax debt) = 12.6%. Cost of equity includes a 4% country risk premium and 6% emerging-market equity premium over the 5% risk-free rate.

Table A5. Year-by-year cash flow (\$ millions)


The project yields an NPV of \$353M at a 12.6% WACC, an IRR of 17.6%, and a simple payback in year 6. GPU hardware accounts for \$5850M of the \$6506M total CAPEX (90%), and electricity represents 53% of operating costs.

Table A6. Sensitivity of investment returns to parameter variation


Risks. Kyrgyzstan depends on the Toktogul reservoir for over 80 percent of electricity (ADB 2020); seasonal drawdowns and drought years create acute power shortages. GPU procurement faces US export-control uncertainty. Underdeveloped contract enforcement and regulatory frameworks raise the bilateral sovereignty premium for potential importers. Despite these risks, the engineering economics are clear: electricity at \$0.038/kWh and a PUE of 1.08 yield production costs well below the global median, and the positive NPV survives eight of ten perturbations in Table A6. The share of this surplus retained in Kyrgyzstan depends on the ownership and fiscal structure: if the facility is owned by a foreign hyperscaler, most operating surplus flows abroad as repatriated profits, and the host country retains only the electricity payment and construction-phase employment unless the government captures rent through taxation, equity participation, or resource royalties.

## Appendix E: Construction Cost Regression

Data center construction costs per watt of IT capacity are observed for 37 countries from the Turner & Townsend Data Centre Construction Cost Index 2025 (52 markets). For the remaining countries, construction costs are predicted using the log-linear regression reported in Table A7. The dependent variable is ln(\$/W). Since construction accounts for only 3–6% of total per-GPU-hour costs, imputation error has limited impact on cost rankings.

Table A7. Construction cost regression: ln(\$/W)


Notes: OLS regression on 37 countries from the Turner & Townsend DCCI 2025. Dependent variable: ln(construction cost in \$/W). R $^{2}$ = 0.48, adjusted R $^{2}$ = 0.29, RMSE = 0.160. Reference region: Europe & Central Asia. \*\*\* p < 0.01, \*\* p < 0.05, \* p < 0.10.

## Appendix F: Workload Classification

Table A8 summarizes the latency sensitivity and offshorability of major AI workload types. The model collapses these into two categories — training ( $\tau = 0$ ) and inference ( $\tau > 0$ ) — but the intermediate workloads noted in footnote 6 occupy a middle ground that may narrow the effective offshorable share.

Table A8. Workload classification and offshorability


Notes: Latency tolerance is approximate round-trip time. “Offshorable” refers to whether the workload can be processed in a different country from the end user without significant quality degradation. The model treats fine-tuning and agentic inference as part of the training share $\alpha$ ; footnote 6 notes this simplification.

## Appendix G: Symmetric LRMC Construction

The cost-recovery specification in earlier versions of this paper adjusted electricity prices downward for thirteen developing countries whose observed industrial tariffs reflect explicit fossil-fuel subsidies (IMF 2025), replacing subsidized tariffs with the estimated long-run marginal cost of the dominant generation technology at opportunity-cost fuel prices. No symmetric correction was applied to OECD and high-income tariffs, which also embed distortions: emissions externalities not priced at the retail meter, industrial cross-subsidies financed by residential and commercial rate classes, and regulated-access privileges for incumbents. The asymmetry biases the cross-country cost spread in favor of OECD economies. This appendix constructs a symmetric LRMC specification that corrects distortions on both sides.

Of the 85 calibrated countries, 13 retain the IMF-based LRMC replacement used throughout the paper (Iran, Turkmenistan, Algeria, Egypt, Qatar, Saudi Arabia, United Arab Emirates, Russia, Kazakhstan, Nigeria, South Africa, Ethiopia, and Uzbekistan). Forty-three OECD, EU non-OECD, and high-income non-OECD countries receive a symmetric adjustment. Twenty-nine middle-income developing economies whose observed industrial tariffs already approximate long-run marginal cost retain their observed prices. Three countries (Qatar, Saudi Arabia, United Arab Emirates) appear in both the developing-country subsidy set and the high-income non-OECD set; the IMF-based treatment dominates and no layering is applied.

The carbon-price adder equals the 2024 grid carbon intensity in grams of CO $_{2}$ per kilowatt-hour (EMBER Yearly Electricity Data 2025 release) multiplied by the 2024 annual-average price under the applicable emissions-trading or carbon-tax regime: EU ETS (\$70.94 per tonne, applied to EU27 plus Norway, Iceland, and Switzerland via the linked Swiss ETS), UK ETS (\$47.32), Canadian federal backstop (\$58.48), California Cap-and-Trade plus RGGI coverage-weighted for the United States (\$3.81 effective national average), New Zealand ETS (\$39.50), and Singapore carbon tax (\$18.60). Nominal instruments with effective prices below ten dollars per tonne (Korea K-ETS, Japanese carbon tax, Australian safeguard mechanism, Israel, Chile, Mexico, Turkey, Colombia) are set to zero.

Only well-documented, quantified industrial cross-subsidies exceeding \$0.005 per kilowatt-hour are included. Germany receives the largest add-back (\$0.038/kWh) reflecting the EEG renewables-surcharge exemption and grid-fee exemption for energy-intensive industry (Agora Energiewende; BDEW). France receives \$0.015/kWh for postARENH regulated nuclear access. Spain, Italy, the Netherlands, and Belgium receive \$0.010/kWh each from the Eurostat nrg\_pc\_205 subsidies column (industrial band IB6). The United States receives \$0.015/kWh reflecting the industrial–residential rate differential in excess of cost-of-service documented by Borenstein (2012) and Davis and Hausman (2016). Korea receives \$0.020/kWh reflecting KEPCO industrial tariffs below cost-of-service (OECD Energy Policy Review). All other countries receive zero. $^{15}$

Three choices warrant note. First, the carbon adder uses 2024 annual-average market prices, not the social cost of carbon; using US EPA (2023) social-cost values would widen the OECD adjustment further. Second, we use existing-asset variable cost rather than replacement-cost capital for OECD nuclear and hydro; a replacement-cost treatment would raise Norwegian and French LRMCs materially. Third, the largest ten changes in per-kWh prices occur in Germany, Poland, Cyprus, Estonia, Netherlands, Czechia, Italy, Bulgaria, Malta, and Greece; the corresponding rank shifts in Table A1 illustrate how the symmetric specification reallocates comparative advantage toward countries with cleaner grids or cost-reflective tariffs rather than toward those with below-marginal-cost industrial rates.

Under the symmetric LRMC specification, the five lowest-cost producers are Kyrgyzstan, Ethiopia, Kosovo, Canada, and Tajikistan. Canada falls from second to fourth after a modest carbon adder of \$0.008 per kilowatt-hour. Poland drops 21 positions, Germany 10, the United States 10, and France 12, while Nordic low-carbon grids and Switzerland move by two positions or fewer. The qualitative conclusion is therefore reinforced rather than overturned: countries with cheap, clean electricity retain their cost advantage once both sides of the distortion are corrected.
