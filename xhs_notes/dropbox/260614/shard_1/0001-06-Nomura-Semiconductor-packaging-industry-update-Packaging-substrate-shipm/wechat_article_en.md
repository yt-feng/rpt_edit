# The Next Packaging War Is Not About Chips—It Is About Control of the Back-End Supply Chain

The semiconductor industry is entering a phase where the most important competitive battles will not be fought over transistor density or lithography. They will be fought over how chips are connected to each other and to the system. The April 2026 packaging substrate shipment data from Japan tells a story that is easy to misinterpret. Shipments rose 20% year-on-year to 23.3 billion yen, but fell from March's record high. A casual reader might see a slowdown. The more strategic reading is that the industry is at the cusp of a structural shift that will rearrange the economics of advanced packaging and, with it, the balance of power among the world's largest semiconductor companies.

The real story is not about a single month's shipment volatility. It is about the emergence of 3.5D packaging and the race to control the back-end process design platform. This race will determine who captures the value from the next generation of AI accelerators, high-bandwidth memory integration, and system-level performance gains. The companies that win this race will not necessarily be the ones with the best front-end manufacturing. They will be the ones that own the packaging architecture, the substrate supply, and the thermal and power management solutions that make 3.5D work.

The data from Japan's Current Survey of Production shows that the average price per square meter for rigid module boards hit a record high of 1.226 million yen in April, up 19% year-on-year. This price increase is not inflation. It is a signal that the market is shifting toward higher-value, more complex substrates that require advanced materials and precision manufacturing. The volume growth in square meter terms was only 1% year-on-year, which means the entire revenue growth came from pricing power. That pricing power will only intensify as 3.5D packaging moves from pilot lines to mass production.

The timing of the current shipment dip is tactical, not structural. The report suggests that shipments of packaging for Rubin processors may have been temporarily sluggish due to the pushing back of server production. This is a supply chain timing issue, not a demand problem. The Blackwell ramp in April 2025 created a high base for comparison, and the Rubin ramp is expected to hit full stride in summer 2026, likely between June and August. The industry is in a lull between product cycles, and that lull is masking the longer-term acceleration that is already being baked into investment plans.


![Report chart 1](assets/source_image_01.jpg)

## 3.5D Packaging Will Reshape the Competitive Landscape by 2028, and the Battle Lines Are Already Being Drawn

The most important development in the packaging world right now is the accelerating timeline for 3.5D packaging. This is not an incremental improvement over 2.5D or 3D packaging. It is a fundamentally different architecture that hybrid-bonds accelerators, HBM memory, and small inference processors together on a single package. The technology requires a complete rethinking of how chips are stacked, how they are connected to the substrate, and how they are cooled and powered.

TSMC has laid out a clear roadmap. At its annual general meeting, the company announced plans to launch a pilot production line for panel-level packaging, which it calls Chip-on-Panel-on-Substrate (CoPoS), in June 2026. Mass production is slated for 2028 after verification work. Separately, TSMC plans to prepare for mass production of glass core substrates with partners including Ibiden over the next two to three years. The sequence matters. TSMC's 3.5D packaging appears to consist of chip stacking using System on Integrated Chips (SoIC), CoPoS, and Flip Chip Ball Grid Array (FC-BGA) using glass core substrates. Glass core substrates will come after CoPoS, not before.

This sequencing creates a window of opportunity for competitors. Intel is pushing its own alternative, Embedded Multi-die Interconnect Bridge Through-Silicon Via (EMIB-T) technology. The report notes that companies are increasingly making moves to place more orders for EMIB-T, perhaps because of uncertainty about when TSMC's CoPoS will go into mass production. The Information reported on 8 June that Google had placed orders for Intel to package at least 3 million TPUs with EMIB-T in 2028, and that Nvidia was considering adopting the technology. These are early signals, but they point to a fundamental strategic question: will the industry standardize on TSMC's back-end platform, or will a multi-platform ecosystem emerge?

The answer to that question will determine the economics of the entire packaging supply chain. If TSMC dominates, then its 3DFabric Alliance becomes the de facto standard, and every accelerator designer must work within that ecosystem. If Intel's EMIB-T gains meaningful share, then the industry fragments, and designers face a choice between two incompatible back-end architectures. That fragmentation creates both risk and opportunity for substrate suppliers, equipment makers, and design tool providers.


![Report chart 2](assets/source_image_02.jpg)

## The Transition to 3.5D Packaging Is Not Just a Technical Challenge—It Is a Supply Chain Control Problem

The most underappreciated aspect of the 3.5D packaging story is that it is not simply about bonding chips together. It is about who controls the back-end process design platform. The report makes this point explicitly: it will not be easy for companies developing accelerators on TSMC's 3DFabric Alliance to transition to EMIB-T, because 3.5D packaging includes key functions such as power supply and heat management.

This is a critical insight. In 2.5D packaging, the interconnect was the main challenge. In 3.5D packaging, the entire system-level integration becomes part of the packaging problem. Power delivery requires vertical power supply or integrated voltage regulators (iVRs) that must be developed jointly with partners. Thermal management requires new cold plates with microchannel mechanisms optimized for cooling each individual chip. These are not off-the-shelf components. They are custom solutions that must be co-developed with the packaging platform.

If a company designs its accelerator on TSMC's platform, it gains access to TSMC's ecosystem of power and thermal partners. If it wants to switch to Intel's EMIB-T, it must either rely on Intel's back-end process design platform or build its own back-end semiconductor process supply chain. The latter option is prohibitively expensive for all but the largest players. The former option creates a dependency on Intel that may be strategically uncomfortable for companies that compete with Intel in other markets.

This is why the Google order for Intel's EMIB-T is so significant. Google is one of the few companies with the scale and internal engineering resources to manage a dual-platform strategy. Most other accelerator designers will have to pick one platform and commit to it. That commitment will lock them into a specific supply chain for years, if not decades.

## The Substrate Bottleneck Is Real, and It Will Force Capacity Decisions That Have Not Yet Been Made

The report highlights one specific constraint: Ibiden does not have the capacity to supply substrates for the packaging of 3 million TPUs per year with EMIB-T technology. The report explicitly states that it does not expect this news to be immediately reflected in Ibiden's earnings forecasts, but it will be watching for any production capacity increase announcements.

This is a classic chicken-and-egg problem. Substrate manufacturers need demand certainty to justify the massive capital expenditures required to build new production lines. But accelerator designers need substrate supply certainty to commit to a specific packaging platform. The 3 million TPU figure from Google is large enough to strain existing capacity, but it is not yet large enough to justify a dedicated factory. The industry is in a waiting game: everyone wants to see who else commits before making their own investment decisions.

The substrate bottleneck is not just about volume. It is also about technology. Glass core substrates are still in development, and the report notes that there are "issues in development" that TSMC and its partners are working through. The transition from organic to glass substrates will require entirely new manufacturing processes, new supply chains, and new quality assurance protocols. The companies that solve these problems first will have a multi-year advantage.

The pricing data from Japan reinforces this point. The average price per square meter for rigid module boards has risen to a record high, and it is likely to go higher as the industry shifts toward more complex, multi-layer substrates. The substrate is no longer a commodity component. It is a strategic asset that determines the performance and cost of the entire package.

## What the Report Does Not Fully Answer: The Economics of Platform Lock-In and the Timing of Capacity Inflection

The report is excellent at describing the technical and competitive dynamics of the 3.5D packaging transition, but it leaves several critical questions unanswered. The most important one is the economics of platform lock-in. How much does it actually cost a company like Nvidia or AMD to switch from TSMC's 3DFabric Alliance to Intel's EMIB-T? The report mentions that it "won't be easy," but it does not quantify the switching costs. Are we talking about hundreds of millions of dollars in redesign costs? Billions? The answer matters because it determines how quickly the industry can converge on a standard.

The second unanswered question is the timing of the capacity inflection. The report suggests that mass production of 3.5D packaging will start in 2028, but it does not say when the substrate capacity will be in place to support that mass production. The substrate manufacturers are unlikely to build capacity before they have firm orders, but the accelerator designers are unlikely to place firm orders before they have verified that the substrates work. This circular dependency could delay the timeline by six to twelve months, which would have significant implications for the revenue forecasts of both packaging companies and their customers.

The third open question is the role of memory vendors. 3.5D packaging involves hybrid bonding of HBM memory directly onto the package. This changes the relationship between memory suppliers and logic suppliers. Will HBM vendors like Samsung and SK Hynix be forced to adapt their memory designs to each packaging platform? Will they have to develop separate HBM variants for TSMC's CoPoS and Intel's EMIB-T? The report does not address this, but it is a critical piece of the puzzle.

## A Decision Framework for Investors: Four Questions to Ask About Every Packaging-Related Investment

For investors trying to navigate this transition, the report provides enough information to construct a decision framework. Every investment thesis in the packaging space should be tested against four questions.

First, whose back-end platform does the company depend on? If a company is tied to TSMC's 3DFabric Alliance, its growth is contingent on TSMC's ability to scale CoPoS and glass core substrates on schedule. If it is tied to Intel's EMIB-T, its growth is contingent on Intel's ability to win enough design wins to justify capacity expansion. The risk profiles are different, and investors need to understand which platform their portfolio companies are betting on.

Second, does the company have a role in power or thermal management? The report makes clear that 3.5D packaging requires co-development of vertical power supply and microchannel cold plates. Companies that provide these solutions will benefit regardless of which packaging platform wins. They are the picks-and-shovels plays of the 3.5D transition.

Third, what is the company's exposure to substrate supply? The substrate bottleneck is real, and it will create winners and losers. Companies that have secured long-term supply agreements with substrate manufacturers will have a competitive advantage. Companies that are relying on spot market purchases will face margin pressure and potential delivery delays.

Fourth, what is the company's switching cost? If a company has designed its accelerator on one platform, how difficult and expensive would it be to move to another? The answer to this question determines the durability of the company's competitive position. Low switching costs mean that the company can adapt to platform shifts. High switching costs mean that the company is locked in, for better or worse.

## The Full Picture Requires the Original Data and Charts

The analysis above draws on the report's key findings, but the full strategic picture requires a deeper dive into the original data. The monthly shipment trends, the pricing trajectory, and the capacity utilization rates all tell a story that cannot be fully captured in a summary. The charts in the original report show the relationship between production value and price per square meter over time, revealing patterns that are invisible in a single month's data.

Join the community to read the full report and review the original charts.

*This article is for learning and discussion only and does not constitute investment advice.*

<p style="color:#999999;font-size:12px;">Personal reading notes and learning share only. Not investment advice.</p>
