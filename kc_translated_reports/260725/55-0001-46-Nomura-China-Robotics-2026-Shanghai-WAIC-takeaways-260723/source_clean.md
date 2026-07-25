# 2026 Shanghai WAIC takeaways
## Three shifts for China robotics: bodies scale, brains lag, data bottlenecks bind

From staged demos to deployed fleets: The World Artificial Intelligence Conference (WAIC) 2026 featured fewer acrobatic showcases and a much broader range of robots doing real work. Nearly 60 humanoids delivered actual services across venues hosting 1,100+ exhibitors, and almost every major vendor pitched deployment capability, data assets and "robot brains" ahead of hardware parameters.

## Mass production inflects, demand remains uncertain

WAIC 2026 confirmed, in our view, that embodied AI has crossed the mass-production inflection, shifting the narratives from TAM (total addressable market) to shipments, ASPs and margins, and actual deployment. For example, AgiBot (unlisted) reported 15,000 cumulative units produced; on-site, nearly 60 humanoids performed real services among 1,100+ exhibitors, and management framed reliable manufacturing, delivery and integration as the new yardstick. We see a replay of the 2019-20 EV (electric vehicle) playbook on the manufacturing side, with thematic investing entering the order-verification stage. That said, current shipments of humanoids validate manufacturability, not demand durability. Based on our industry survey, 2026E demand still skews toward entertainment/ performance (\~30%), consumer (\~30%), government procurement (\~20%) and education (\~15%), with industrial/commercial at only \~5%. We flag order composition (paying-customer mix, to-G/related-party share) and per-unit economics as the next milestones to monitor, as it may determine whether the volume story converts into earnings.

## Humanoids meet the factory test: MTBF, takt time, and the payback wall

Technology roadmaps have converged on industrial and logistics settings – predictable, repeatable environments – rather than open-ended use cases: AgiBot's G2 Max and OmniHand 3, MagicLab's (unlisted) wheeled MagicBot D1, and dexterous-hand firms mostly target factories, while consumer launches — Fourier's (unlisted) companion GR Nano and Unitree's (unlisted) GD01 rideable mecha — remain sideshows. Wheeled form-factors becoming the industrial workhorse is itself a signal, in our view: vendors are trading anthropomorphism for reliability and cost, deferring bipeds. Yet, we think, "labor" and "industrial-robotic-arms" substitution economics remain unproven: industrial buyers purchase on ROI, MTBF (mean time between failures) and takt time, and at current humanoid ASPs vs labor costs, payback periods at most workstations have yet to reach adoption thresholds, while grippers suffice at structured stations, leaving five-finger hands over-engineered. Real demand today is data collection and training grounds, OEM-subsidised pilots and to-G showcases — funded by robot-maker capex and policy money, not factory labor budgets — reconciling strong shipments with unproven economics; we view this as a supply-side, not demand-side, inflection. The signal that this flips: the first repeat order from a non-related industrial customer, paid out of an operating budget rather than a pilot budget.

## Data is one binding constraint for embodied AI

We note competitive focus is shifting from bodies to brains: the debate between VLA (vision-language-action) and world models settled on fusion — Spirit AI's (unlisted) v1.6 already runs a fused architecture, while Ant Group's (unlisted) LingBot-VLA 2.0 spans 17 OEMs and 20+ configurations. Our industry survey shows the binding constraint is high-quality real physical-interaction data, not architecture or compute: 2026E demand of \~10mn hours vs \~0.5mn hours of global high-quality stock, a 20x gap, with 2,000-5,000 hours needed per deliverable skill. For data collection, we assume a \~CNY4-5bn 2026F China market size, and with 20+ city-level data factories under construction plus offshore crowdsourcing; we expect unit price to decline within 12-24 months. However, cheaper data only eases collection costs — it neither closes the data gap nor unlocks the collect-train-deploy-feedback loop — we expect robot 'brain' maturity to take years: leading robotics firm's estimates point to an embodied-AI 'ChatGPT moment' in 2-3 years and scaled adoption later, as the effective data feedback from deployed fleets is still low of today's data mix.


Frank Fan - NIHK

Donnie Teng - NIHK

## Headline shipments mask a demand base dominated by non-productive use

Beneath the headline volumes, our survey work points to a demand base still dominated by non-productive use. We forecast 2026 industry shipments of 45-50k units — below the \~100k media narrative — driven by accelerating government procurement and consumer demand inflection from low-priced product launches (Optimus ramps; China scales up as cost curves bend lower published on 28 June 2026). Based on our industry survey, 2026E demand still skews toward entertainment/performance (\~30%), consumer (\~30%), government procurement (\~20%) and education (\~15%), with innovative scenarios (industrial/commercial) at only \~5% — a rotation away from 2025's rental-led mix (45-50%), but not yet toward productive use. Rental economics illustrate the fragility: humanoid day-rates of CNY4,000-20,000 are down 50-60% y-y, stabilising only because OEM selling prices have already fallen; the market remains local and fragmented — too small, per the expert, to support platform-style rental businesses — and rising per-event robot counts (one unit in 2025 to four in 2026, occasionally 20-30) drive volume without recurring revenue. Government-backed data-collection factories, \~20% of 2026F demand, carry 3-5-year paybacks, and we expect humanoid data-collection procurement to be soft in 2027F as body-free collection scales. Capital formation, meanwhile, is running well ahead of this demand reality: per GGII, humanoid OEMs raised CNY70.5bn across 98 deals in 1H26 (53% of total sector financing), with embodied foundation models (CNY22.3bn/40deals), world models (CNY19.1bn/17 deals) and data infrastructure (CNY4.4bn/19 deals) absorbing much of the remainder. The funding mix is effectively underwriting a model-driven capability inflection that the shipment mix has yet to validate. We therefore treat repeat orders from non-related industrial customers as necessary for companies' earnings.

Fig. 1: End market demand mix

[[KC_IMAGE_001]]

Source: Company data, NOM

Fig. 2: 1H26 financing by sub-segment

[[KC_IMAGE_002]]

Source: GGII, NOM

## Dexterous hands: three routes converge, hardware iterates faster than demand

Dexterous hands are converging on a three-route roadmap. Linkage hands — low-DOF (≤ 12 degrees of freedom), ASPs of CNY12,000-13,000 and over 80% of industry shipments — form the commoditizing legacy base, led by Inspire Robots (unlisted), with OYMotion (unlisted) and Zhaowei (003021 CH, Not rated) following; sub-CNY10k pricing has already emerged. The high-DOF battleground is tendon-drive versus direct-drive. Tendon designs (15-19 DOF, \~CNY38,000 ASP) most closely replicate the human hand — which proponents argue eases training on human-collected data — championed by LinkerBot (unlisted) and Dexterous Intelligence (unlisted), but face tendon creep and \~2-month lifespans. Direct-drive (20+ DOF, CNY33,000-34,000, volume from 4Q26) is favored by algorithm teams for per-joint force control and RL (reinforcement learning) friendliness — Sharpa (Unlisted) leads, with Sudo's (Unlisted) 22-DOF/840g hand and Kinetix AI's (unlisted) 37-DOF in-palm-motor design at WAIC — but motor heat binds: vendors face a heat-force-size triangle in which only two can be optimized, so hybrid architectures are proliferating. Tactile sensing is consensus at fingertips only; full-palm schemes still diverge. With OEMs such as AgiBot iterating in-house hands (OmniHand 3) and industry shipments guided +80-100% in 2026, hands are the fastest-iterating link in the chain — though supply still runs ahead of end-demand.

Fig. 3: Average ASP for different technology route

[[KC_IMAGE_003]]

Source: Company data, NOM estimates

Fig. 4: Dexterous hand gripper penetration in humanoid

[[KC_IMAGE_004]]

Source: Company data, NOM estimates

Fig. 5: Technology roadmap of dexterous hands


Source: Company data, NOM

Fig. 6: Market survey on dexterous hand and component firms


Source: Company data, NOM

## The brain race runs through data: brain maturity may take years on scarce feedback

WAIC made the data bottleneck visible on the show floor, where data tooling emerged as a product category in its own right (Data emerges as the critical part for robotics published on 5 July 2026). Exhibitors moved beyond robots to full acquisition stacks — PsiBot's (unlisted) SynCap system synchronizing vision, language, tactile and motion streams, BrainCo's (unlisted) training-platform-plus-collection solution and a cluster of exoskeleton-glove and teleoperation rigs — while DexForce (unlisted) open-sourced a human-simulation-real aligned dataset and JD.com (JD US, Buy) was reported to be building a large-scale collection center, signaling platform capital entering the trade. Standardized collection-simulation-evaluation-deployment pipelines were the common pitch — echoing the closed-loop model we favor — and are gaining regulatory scaffolding: a national standard on humanoid dataset quality evaluation was formally initiated in July 2026 (under China's robotics standards committee TC591), alongside an MIIT industry standard on training-data management now in public consultation—though vendors guarding private standards may slow adoption. We expect that VLA's generalization and long-horizon limits, acknowledged since 4Q25, are at core a data problem, pushing vendors toward world-model fusion — pretraining corpora already run near 1:9 real-to-synthetic, lowering but not eliminating real-data needs — while the simulation-heavy US route contrasts with China's real-machine teleoperation weighting.

Fig. 7: Data collection market size

[[KC_IMAGE_005]]

Source: Company data, NOM estimates

Fig. 8: Share and ASP in different data collection types

[[KC_IMAGE_006]]

Source: Company data, NOM estimates

## Appendix A-1

This report has been produced by NOM International (Hong Kong) Ltd. (NIHK), Hong Kong. See Disclaimers for NOM Group entity details.
