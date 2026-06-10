# Nvidia’s Move Into Radio Units Does Not Threaten Ericsson or Nokia — It Forces a Strategic Choice That Will Define the 6G Era

The telecom equipment industry has long been defined by a simple truth: the companies that own the custom silicon own the margin. For decades, Ericsson and Nokia have invested heavily in application-specific integrated circuits (ASICs) for radio units, believing that proprietary hardware was the only path to the performance required by carrier-grade networks. That assumption is now being tested by Nvidia’s reported entry into radio unit silicon, extending its AI-RAN strategy beyond central and distributed units into the low-PHY functions of Massive MIMO radios. The initial market reaction — a selloff in telecom equipment stocks — suggests investors fear a replay of what happened when Nvidia disrupted data center networking. But that fear is misplaced. Nvidia’s move is not a death knell for equipment suppliers. It is a catalyst for a strategic fork in the road that will separate the companies that understand software differentiation from those that remain wedded to hardware lock-in.

The real question is not whether Nvidia will win in radio units. The question is whether Ericsson and Nokia have the strategic clarity to choose their path before the market chooses for them. The answer will determine which company captures the value of 6G and which gets marginalized as a hardware assembler.


![Report chart 1](assets/source_image_01.jpg)

## The Technical Driver Behind Nvidia’s Radio Unit Strategy Is Genuine, but the Market Is Overreading Its Competitive Implications

Nvidia’s reported development of a GPU-based chip for radio units is not a speculative land grab. It is a rational response to a genuine technical problem. As Massive MIMO radios scale from basic 4T/4R configurations toward 128T/128R and potentially 1,024T/1,024R in what some call ultra-MIMO, the compute required for low-PHY functions such as beamforming increases by roughly 32 times. At those scales, fixed-function ASICs become increasingly unattractive because they lack the scale economics of programmable silicon in a non-growth equipment market. Nvidia’s argument — that a GPU-based approach can replace custom ASICs while offering flexibility and programmability — has technical merit.

But the market’s immediate interpretation — that this is a negative for Ericsson and Nokia — conflates technical possibility with competitive inevitability. The belief that Nvidia will replicate its data center dominance in telecom radio units ignores three structural constraints. First, radio units drive roughly 90 percent of network energy consumption, and Nvidia’s GPUs are not known for power efficiency. A sub-100W embedded GPU design, perhaps borrowed from automotive applications, could mitigate this, but it would still face a performance gap versus purpose-built ASICs. Second, telecom operators are notoriously conservative. They do not swap out radio unit silicon the way hyperscalers swap out server accelerators. The qualification cycles are measured in years, not quarters. Third, Nvidia is not entering a vacuum. It is entering a market where Ericsson and Nokia have decades of system-level integration expertise that cannot be replicated by a chip vendor alone.

The more nuanced reading of this news is that Nvidia is creating an option, not a mandate. The equipment suppliers will decide whether to exercise it.

## Nokia Has the Higher Probability of Embracing Nvidia Silicon, and That Is Not a Negative Signal

Nokia has already signaled its direction. The company has indicated that it will standardize on Nvidia’s AI accelerator solutions in its baseband computing units for 6G. This is not a tentative experiment; it is a strategic commitment to moving away from custom ASICs toward standard semiconductors. The logic is straightforward: if hardware becomes a commodity, differentiation shifts to software. Nokia believes that its value will come from the software it writes on top of Nvidia’s platform, not from the silicon itself. For telco customers, the benefit is that hardware and software upgrades become separable, and hardware upgrades could become cheaper over time.

This is a defensible strategy, but it is not without risk. Standard products can never match the performance of custom ASICs. Nokia is betting that the flexibility and cost advantages of a standard platform will outweigh the performance gap for most use cases. The company’s existing relationship with Nvidia on the baseband side gives it a head start. If Nokia decides to extend the Nvidia relationship to the radio unit, it will be able to leverage its CUDA experience and architectural familiarity to move faster than Ericsson.

Investors should not interpret this as a sign of weakness. Nokia is making a deliberate choice to compete on software and system integration rather than on silicon. That is a legitimate strategic posture. The risk is not that Nokia loses to Ericsson on performance. The risk is that the software differentiation does not materialize, and Nokia becomes a reseller of Nvidia hardware with thin margins. But that risk is manageable if Nokia executes on its software roadmap.

## Ericsson’s Commitment to ASICs Is a Bet on Performance Leadership, but It Carries Its Own Strategic Vulnerabilities

Ericsson has publicly stated that it is not considering a shift away from building ASICs. The company believes that the performance advantages of custom silicon are non-negotiable for carrier-grade networks, especially as Massive MIMO scales. This is not a reflexive conservatism. Ericsson has a long history of investing in proprietary silicon, and its ASIC capabilities are a genuine competitive asset. In a world where every milliwatt and every microsecond matters, custom hardware can deliver outcomes that standard platforms cannot.

But Ericsson’s position is not without vulnerabilities. The most obvious is that the telecom equipment market is not growing. If the total addressable market for radio units is flat or declining, the economics of custom ASICs become harder to justify. Fixed-function silicon requires volume to amortize development costs, and if volumes are not there, the unit economics deteriorate. Ericsson is betting that performance leadership will allow it to capture share even in a stagnant market, but that is a high-conviction bet.

The second vulnerability is strategic flexibility. If the industry moves toward programmable platforms, Ericsson could find itself locked into a hardware architecture that operators no longer want. The risk is not that Ericsson’s ASICs are inferior. The risk is that the market shifts the definition of value from raw performance to operational flexibility, and Ericsson is caught on the wrong side of that shift.

The most interesting question is whether Ericsson will eventually decide to use Nvidia silicon in some segments of its portfolio. The report suggests that Ericsson could do so if the advantages become clear, but that it would take longer because the company lacks familiarity with Nvidia’s architecture. This is not a trivial barrier. Architectural changes in radio units are not like swapping out a server GPU. They require fundamental reengineering of the system-level design. Ericsson’s slower adoption timeline is a feature, not a bug, of its ASIC-first strategy. But it also means that if the market moves faster than expected, Ericsson could be left behind.

## The Report Does Not Fully Resolve the Most Critical Question: How Will Telco Operators Decide Between Flexibility and Performance?

The report identifies the core trade-off: telco customers will need to decide whether flexibility from standard hardware platforms with differentiated software is more valuable than the performance advantages of custom semiconductors. But it does not fully answer how that decision will be made. This is not a minor omission. It is the central strategic question for the entire 6G ecosystem.

Several factors will influence operator decisions, and the report leaves them unexplored. First, operator scale matters. Large operators with dense urban networks may prioritize performance because they need to maximize spectral efficiency in capacity-constrained environments. Smaller operators or those focused on rural coverage may prioritize flexibility and cost. Second, the nature of the use case matters. Fixed wireless access may have different performance requirements than ultra-reliable low-latency communications for industrial automation. Third, the regulatory environment matters. Operators in markets with spectrum scarcity may need every dB of performance they can get, while those in spectrum-rich environments may have more margin for flexibility.

The report also does not address the role of the cloud-native network architecture that many operators are pursuing. If operators are moving toward virtualized RAN and cloud-based processing, the argument for programmable hardware becomes stronger. But if they are doubling down on purpose-built infrastructure for performance reasons, the ASIC path remains viable.

These open questions are not limitations of the analysis. They are the natural boundaries of what can be known before 6G standards are finalized and operator procurement cycles begin. But they are precisely the questions that investors should be asking as they evaluate the long-term positioning of Ericsson and Nokia.

## A Decision Framework for Investors: Three Questions to Evaluate Equipment Supplier Strategy in the 6G Era

The report provides the raw material for a structured decision framework, but it does not synthesize one. Here is a framework that investors can use to evaluate which equipment supplier is better positioned for the 6G transition.

First, ask whether the supplier has a credible software differentiation strategy. Nokia’s bet is that software running on Nvidia hardware will be the source of value. That is credible only if Nokia can demonstrate that its software delivers meaningful performance or operational advantages that are independent of the underlying silicon. If Nokia’s software is simply a thin layer on top of Nvidia’s platform, the value capture will be minimal. If Nokia’s software includes proprietary algorithms, automation, or orchestration capabilities that cannot be replicated, the strategy has legs.

Second, ask whether the supplier’s hardware strategy aligns with operator procurement cycles. Ericsson’s ASIC strategy makes sense if operators are willing to pay a premium for performance and if the qualification cycles for custom hardware remain long. But if operators begin to demand shorter upgrade cycles and greater hardware-software decoupling, Ericsson’s strategy becomes a liability. The key leading indicator is operator procurement behavior in the next 12 to 18 months, particularly among early 6G adopters.

Third, ask whether the supplier has the organizational capability to manage the transition if it decides to change course. Nokia’s existing relationship with Nvidia gives it an advantage if it chooses to extend the partnership to radio units. Ericsson’s lack of familiarity with Nvidia’s architecture is a real barrier, but it is not insurmountable. The question is whether Ericsson’s culture and engineering organization can pivot if the market demands it. Organizational inertia is often the most underestimated risk in technology transitions.

This framework does not provide a simple answer. It provides a structured way to evaluate the evidence as it emerges. The companies that answer these questions most clearly will be the ones that create the most value for shareholders.

## The Full Report Provides the Charts and Data That Make These Decisions Concrete

The analysis above is based on the report’s core insights, but the full report contains the granular data and charts that turn strategic questions into actionable investment decisions. The report includes detailed comparisons of power consumption across silicon architectures, historical cost curves for ASICs versus standard platforms, and operator survey data that reveals how telcos are thinking about the flexibility-performance trade-off. These are not academic exhibits. They are the evidence that separates conviction from speculation.

Investors who rely only on the summary analysis are making decisions with incomplete information. The full report provides the quantitative foundation that allows you to test the assumptions underlying both Nokia’s software-first strategy and Ericsson’s ASIC-first strategy. It also includes the original charts that show how the compute requirements of Massive MIMO scale and where the breakpoints are for different architectural choices.

Join the community to read the full report and review the original charts.

*This article is for learning and discussion only and does not constitute investment advice.*

<p style="color:#999999;font-size:12px;">Personal reading notes and learning share only. Not investment advice.</p>
