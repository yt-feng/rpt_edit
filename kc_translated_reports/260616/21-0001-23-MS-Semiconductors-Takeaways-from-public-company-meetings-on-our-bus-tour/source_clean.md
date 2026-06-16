## Semiconductors | North America
# Takeaways from public company meetings on our bus tour
## Key Takeaways

Private company writeups coming later this week – focus on scale-up and low-latency inference

## ALAB

Management expects content per XPU to continue growing from roughly \~\$1,000 today as AI infrastructure becomes more interconnect-intensive. The company is investing across optical, UAL, and NVL, and highlighted that customers are increasingly describing Astera's large PCIe switch as an "NVSwitch for the open ecosystem."

While some workloads and protocols will move elsewhere, PCIe is expected to continue growing for at least the next several years. PCIe remains particularly important in China, where many AI systems are add-in-card-based and therefore PCIe-native. Management sees China as a meaningful opportunity because less powerful GPUs require more interconnect, though it does not expect China to be larger than the U.S. in PCIe scale-up.

For the emerging UAL opportunity, management is confident in its competitive position but does not think the switch opportunity will be winner takes all. First deployments expected next year, with a bigger ramp in 2028.

CXL and memory pooling are still nascent, but management sees growing relevance as inference drives KV-cache offload demand. CXL has not lived up to expectations so far, but management expects revenue in 2027, with both smaller AI platform providers and hyperscalers qualifying systems. Management also noted demand from customers wanting to use DDR4 via CXL to extend server memory lifespans as new CPUs do not support DDR4 directly.

On CPO / NPO, management argued that the most important factor is owning a switch product that optics can attach to. Astera demonstrated PCIe 6 over LPO at Computex and expects NPO deployments first in 2027. If NPO works, it may push out CPO for some customers, while NVDA can move directly to CPO. Astera's

MS & CO. LLC

## Joseph Moore


## Mason Wayne


## Shane Brett


## Nicole Kozhukhov


## Ella Tulchinsky


## SEMICONDUCTORS


MS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.

For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

aiXscale acquisition is expected to generate qualifying revenues in 2027, while CPO for scale-up is more likely a 2028 opportunity at minimum, with perhaps one customer earlier. The company sees an advantage from having electrical IC, PIC, and aiXscale capabilities to produce a full optical engine.

Despite optical enthusiasm, management expects copper to remain relevant inside the rack. Many scale-up links are passive today and may only add retimers, while rack-to-rack connectivity will move to optical because 400G rack-to-rack cannot be copper. This transition should be positive for revenues: even if retimer content is lost when links move to NPO, as the new optical link is materially more valuable. Astera believes its incumbent position in copper links, Cosmos software, and broad suite of standard-specific products reduce the risk of share loss.

Strategically, management contrasted Astera's focus with companies that "invest in everything." Astera is focused on areas where it believes it can win, including a \~\$10bn UAL TAM and NVL Fusion content. The company could build scale-up Ethernet switches, but customers are currently asking it to focus on PCIe. Management framed the 2030 market as roughly \$10bn PCIe TAM and \$10bn Ethernet TAM, with NVL and ICI solutions likely among the largest parts of a broader >\$100bn market, though not quantified.

On custom silicon, management sees opportunities from new XPUs and NVL Fusion. The company wants solutions for all major architectures and is willing to do custom I/O. NVL Fusion is its first custom engagement in this category, but management noted many more requests. ASIC vendors like AVGO will still have influence, through COT programs the hyperscaler can enforce their preferred scale-up architecture.

## In-house SerDes development intended to intercept the optical inflection.

Management wants to be selective about where it invests in custom SERDES, but sees a need around optical, and has the internal team in place. The company's philosophy is to buy IP off the shelf where available to improve opex efficiency, but build internally when required.

Our take: We are OW the stock, and remain very positive heading into the Amazon Trainium 3 scale-up ramp in 2h, and see positive prospects to migrate that to UALink/NVLink Fusion/optical opportunities longer term, though conceding that the strong run-up in the stock price creates a high bar.

## Marvell

Marvell framed the AI opportunity as increasingly interconnect-driven, today most growth is coming from scale-out but there is a significant scale-up / scale-across opportunity still ahead. The company's model contemplates custom growing from \~\$4bn to \~\$10bn, legacy segments starting at a\~\$2.5bn base growing roughly with GDP, and \~\$10bn of connectivity growing \~70% with no near-term slowdown. Management also noted that none of the potential agentic-AI CPU uplift is included in current numbers; more agentic workloads could drive additional NICs, CXL, and switches.

## The core message was that Marvell's breadth is becoming a competitive

advantage. The company positioned itself as one of the few vendors spanning DCI, die-to-die IP, scale-out switching, scale-up switching, optics, SerDes, CXL, NICs, and custom silicon. Management argued this full-stack position matters more as customers confront constrained supply chains and the complexity of integrating switches, optics, third-party IP, and XPUs.

On scale-up, Marvell sees multiple optionality vectors across UAL, ESUN, and NVL Fusion. Management framed scale-up switching as still up for grabs, but scale-up optics as an area where Marvell expects to be number one in merchant solutions. The company also argued that customer preference for non-AVGO alternatives should support Marvell's position, particularly where software, silicon, and optical integration matter.

On XPUs, management sees the potential for upside to its medium-term targets, cautioned investors on over-extrapolating supply-chain datapoints. It continues to focus on higher-margin custom opportunities and believes inference creates more shots on goal.

On supply chain, Marvell says it runs five-year rolling forecasts with suppliers and is getting upside, with interconnect providing more flexibility than custom compute.

Our take: The enthusiasm and confidence both short and long term are very clear, and seem justified to us; however we struggle with the valuation at 2.5x NVDA multiple for a company that has not outgrown NVDA in a long while.

## Intel

For new CEO Lip-Bu Tan, the initial priority was cultural now that focus has shifted toward finding ways to grow the business and executing on the product roadmap.

In CPUs, management highlighted the hiring of Alex Katouzian as important for improving low-power competitiveness and deepening Arm-related expertise.

There were definite changes to be made to the server roadmap, such as bringing back SMT and the P-core / E-core distinction. But management is more confident in the roadmap today, emphasizing that execution is the key variable; if Intel executes, management believes the company can stop losing share in roughly nine months. Agentic AI should be a long-term driver of CPU demand, suggesting that CPU/GPU ratios could reach 4:1 in some contexts.

The x86 ecosystem remains an area of strength Intel is leaning into, where there is potential in vertical markets where x86 customization creates differentiation, which is not something Intel has considered historically.

Lip-Bu has also made the decision to do double down on foundry, believing that the internal product engine and external foundry business should reinforce each other, while external manufacturing remains part of the model where appropriate. Intel wants to remain a top-10 TSMC customer, but believes having both internal and external options create healthy competitive tension and improve customer confidence.

14A is the critical foundry milestone. Management said all Intel-designed products will move to 14A, and early process indicators are improving. Intel is seeing roughly 0.5 defect density and \~40% yield, with a goal of reaching 0.1-0.2 defect density by Q1 next year. Customer conversations are improving and PDF/KLA support was highlighted as part of the effort to accelerate foundry readiness. The 14A 0.5 PDK is out and 0.9 is expected in October. Risk production is framed around 2028 and volume around 2029, broadly comparable to TSMC timing. As an IDM, Intel expects to run internal test chips in 2027, which should give the company a proving ground before external customer volume ramps.

Given the shortage at the leading edge, Lip-Bu said the board is now asking Intel to invest more in capex and that the message has been received. The board is more confident than before, but Intel still needs to prove that incremental spend can translate into customer wins, volume, and margin recovery. Initially, management suggested volume is more important than margin, particularly in foundry, where scale and customer confidence are prerequisites.

On capacity, Intel said Oregon and Arizona have room to expand, and Ohio will be accelerated. Germany has been shut down, but management is now concerned Intel may not have enough capacity if demand continues to improve. TerraFab was discussed as a potential additional platform, though nothing has been announced.

Management also described EMIB as a “secret weapon” with strong technology and large customer potential, but also meaningful complexity and reliability questions. Individual customer opportunities could be worth billions, but execution depends on building the right team, improving automation, and proving reliability at scale.

Management sees advanced packaging as a potential bottleneck across the AI infrastructure ecosystem, which could create an opening for Intel if it can execute. Intel also noted substrate constraints, including the need to prepay in some cases.

We note that our recent Asia checks were a bit mixed on EMIB, and some of the current wins being reported have yet to be completely secured.

The memory shortage is also a focus area for Intel and its partners. Intel does not have the balance sheet of a company like NVDA to secure DRAM, but management said the company needs to be more aggressive in this area.

Our take: We have missed the move in Intel's stock, largely because of concerns on the roadmap, which we still have; we think expectations of share gains vs. AMD seem premature, given AMD's stated ability to procure more wafers for its leadership Venice product. That said, shortages of advanced process nodes, and shortages of CPUs, are certainly a positive backdrop for near-term earnings.

## Valuation Methodology and Risks

## Astera Labs Inc (ALAB.O)

We use 0.53x CY27 EV/sales/growth (\~21x ev/sales), assuming a 40% revenue CAGR. This is a premium to AI peers

## Risks to Upside

■ Increase AI spend to propel data center revenue
■ Quicker upgrade of underlying technology driving content growth
■ New product launches increasing TAM

## Risks to Downside

■ Increased competition reduces Astera's market share meaningfully
■ Pause in AI spend and data center investment halts future revenue growth
■ CXL servers and 1.6T port speeds are significantly delayed, preventing new products from gaining traction

## Intel Corporation (INTC.O)

\~42x EPS CY2027 EPS of \$1.73, 42x is above the high end of the large cap logic semi peer group, reflecting high leverage potential on numbers that are still depressed, and foundry optionality, despite our longer term skepticism

## Risks to Upside

■ Foundry partnerships de-risk the story and further improve the multiple
■ The company regains lost share in desktop and server following CPU shortages

## Risks to Downside

■ AMD competition increasingly becomes more significant, which could lead to further share losses in processors and pressure on ASPs
■ Minimal success in foundry leads to an inflated cost structure

## Marvell Technology Group Ltd (MRVL.O)

\~40X CY27e Base Case MW EPS \$4.98, in-line with high growth AI semis

## Risks to Upside

■ AI opportunities (Inphi optical businesses) realize earlier than expected
■ Cloud custom silicon projects are larger than expected
■ The storage market recovers

## Risks to Downside

■ AI opportunities are smaller than expected
■ The strength we estimate for Storage and Networking surprise to the downside
■ Enterprise DC and Networking continue to weigh on results
