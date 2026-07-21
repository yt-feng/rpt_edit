Apple, Inc. | North America

# The Right Chips For the AI Job?

Apple's AI server silicon is potentially facing performance considerations that could (1) affect Siri AI performance and/or (2) lead to greater adoption of NVDA chips in GCP. Our checks indicate no change to M-series builds, with Apple's first ASIC coming in C1H27, followed by a 2nd gen in '28.

## Key Takeaways

Last week The Information reported on the performance of Apple's M2 Ultra AI server chip and that Apple is exploring chip acquisitions.

- Apple will be reliant on these M series AI server chips to process more complex Siri AI workloads not run on-device.

Apple's Baltra ASIC is "on plan" for small volumes in C1H27, with a 2nd gen AI server ASIC to follow in 2028 that could potentially match merchant silicon.

Why does this matter? A lack of power/performant chips in Private Cloud Compute could either (1) affect Siri AI performance or (2) shift more workloads to GCP.

Signposts to track Apple's AI server silicon? SolC bookings at TSMC, CoWoS bookings at TSMC, 2nd-Gen ASIC tape-out progress, and Apple's capex trajectory.

What's new, and what are the potential implications? Last week, The Information reported that Apple is "on the lookout for acquisitions of chip companies to boost its efforts to build server chips for running AI", noting the performance of Apple's M2 Ultra powered AI servers. We have no knowledge of any pending transactions, and Apple has not commented in response to the report. The Information also reported that a future version of Apple's AI server chip, code-named "Baltra" has been delayed, citing people familiar with the project. While Apple's internal AI efforts are still very early days – with Siri AI expected to launch this Fall – and more skewed to on-device inferencing than peers, the risk of not developing a chip capable of powering inference workloads in Apple's Private Cloud Compute (PCC) has two potentially major ramifications – (1) Apple could be forced to use underperforming chips in PCC for a period of time, which could affect the performance/latency of more complex Siri AI queries, and/or (2) Apple would be forced to run more Siri AI workloads in Google Cloud, a likely costly endeavour.

## A history of Apple's silicon efforts, and why AI chips are a new area for Apple.

Apple's silicon expertise has been concentrated in the power-efficient chips used in iPhone, Mac, and iPad – which started with the A4 in 2010, debuting on the original iPad and iPhone 4. These System on a Chip (SoC) solutions – the A series (powering the iPhone, base iPad, etc.), M series (powering the Mac, iPad Pro/Air), S Series (Apple Watch), etc. – are recognized for delivering performance and efficiency (silicon/hardware/software vertical integration helps as well). In fact, Apple's silicon team is so talented that it had TSMC (covered by Charlie Chan) customize an advanced packaging line for the A series chip. However, Apple doesn't have a long history in designing power-hungry but also extremely performant chips, which are required to run AI inferencing workloads in PCC. This is why, for example, the most performant Siri AI workloads are expected to run on NVDA chips on Google's Cloud (NVDA is covered by Joe Moore; Alphabet is covered by Brian Nowak).

## What we know about Apple's M2 Ultra and "Baltra" from our supply chain checks.

Earlier this year, we published that our checks indicated TSMC's SolC (System on Integrated Circuit) output for Apple in 2027 would match AMD's output, indicating strong volumes for what we believed would be Apple's AI server chip. Our checks would still indicate Apple has not cancelled any packaging capacity at TSMC, but SolC technology is also used in Apple's M5 Max and M5 Ultra, its highest performance M-series chips debuted in March '26, which could indicate these volumes are for chips supporting a number of devices – Mac, workstations, AI servers, etc. Furthermore, we learned that the 'Baltra' ASIC (likely produced in partnership with Broadcom – covered by Joe Moore – who Apple just announced a partnership with) was always targeting C1H27 volume production, which will be quite small at first as it is Apple's first high-power chip, and therefore definitionally more experimental. Apple's 2nd Gen AI ASIC is likely to enter volume production in 2028, and we have heard the power envelope will potentially be close to merchant AI GPUs (e.g. NVIDIA's GPUs).

The signposts we are tracking to stay on top of this topic: (1) SolC capacity bookings at TSMC – this remains a key indicator of Apple’s M-series trajectory as well as broader AI ASIC demand; (2) CoWoS capacity bookings at TSMC – while Apple has yet to emerge as a major CoWoS user, moving toward a power envelope closer to NVIDIA’s AI GPUs would likely necessitate HBM adoption, and in turn, CoWoS packaging; (3) Second-generation AI ASIC tape-out progress – as noted, we expect Apple’s second-generation AI ASIC to reach volume production as early as 2028, implying a potential tape-out sometime in 2027; and (4) Apple’s capex trajectory – although capex has already been trending higher, a successful volume ramp of a second-generation AI ASIC would likely drive further acceleration. It’s also worth keeping in mind that Apple may refer to these technologies differently within the foundry ecosystem (i.e. not literally “CoWoS” or “SolC”). That said, our checks suggest that the underlying toolsets and process technologies are broadly comparable, so we use these industry-standard terms for clarity and ease of discussion.
