# AI Shopping Is Not Yet Agentic: The Gap Between Discovery and Transaction Remains the Industry's Core Unresolved Problem

The promise of agentic shopping has been one of the most compelling narratives in retail technology since Walmart announced its partnership with ChatGPT last October. Six months later, the reality is sobering: no AI shopping tool today can buy a product in an unsupervised fashion. Every single one requires human intervention at critical points in the purchase funnel. The industry is not approaching agentic commerce. It is still struggling to build a reliable bridge between product discovery and transaction execution.

Our systematic testing of five AI shopping tools—three foundational models (ChatGPT, Gemini, Claude) and two retail-native systems (Amazon Alexa, Walmart Sparky)—reveals a fundamental divide that will shape competitive dynamics for years to come. The foundational models are powerful researchers but powerless buyers. The retail-integrated systems are precise operators but confined prisoners of their own ecosystems. Neither side has solved the integration challenge that would make true agentic shopping possible. And the single most important missing piece is not product identification, pricing accuracy, or inventory data. It is payment.

This matters now because the stakes are rising exponentially. Consumer expectations are being shaped by rapid advances in generative AI capabilities, yet the infrastructure to deliver on those expectations remains fragmented. Retailers who solve the integration problem first will capture disproportionate value. Those who wait risk being disintermediated by platforms that can connect discovery to purchase without ever visiting a retailer's website. The next twelve months will determine which of these scenarios plays out.


![Report chart 1](assets/source_image_01.jpg)

## General-Purpose AI Models Excel at Contextual Understanding but Fail at Transaction Execution

The foundational AI models—ChatGPT, Gemini, and Claude—demonstrate impressive capabilities in the early stages of the shopping funnel. When asked to find a 64-ounce carton of organic whole milk for delivery to a specific ZIP code, these tools correctly identify the product category and provide reasonable recommendations. They can suggest specific brands, estimate price ranges, and even identify delivery options through various services. ChatGPT, for example, correctly recommended Great Value Organic Whole Milk at approximately $3.98 from Walmart and Organic Valley at $4.96 to $6.29, along with estimated delivery times.

The problem emerges precisely where value creation should be highest: at the point of transaction. These models have no direct access to retailers' assortment data, real-time pricing, inventory levels, or fulfillment systems. They rely on workarounds—web scraping, third-party articles, and publicly available information—to generate their recommendations. This means their pricing is often approximate rather than exact. Their delivery estimates are generic rather than personalized. And critically, they cannot add items to a cart or complete a payment.

The strategic implication is clear: general-purpose AI models are currently positioned as product discovery tools, not shopping agents. They create value by helping consumers decide what to buy, but they capture none of the value from the actual purchase. This creates an inherent business model tension. The more effective these tools become at driving purchase intent, the more valuable the transaction data becomes—and the more pressure there will be for them to find ways to participate in the transaction itself. Partnerships like ChatGPT's Agentic Commerce Protocol and Claude's integration with Uber Eats represent early attempts to bridge this gap, but they remain incomplete solutions that still require users to follow links to external websites.


![Report chart 2](assets/source_image_02.jpg)

## Retail-Integrated AI Systems Own the Transaction Funnel but Lack Cross-Platform Flexibility

Amazon Alexa and Walmart Sparky operate from a fundamentally different starting point. Because they are built directly on top of retail ecosystems with access to real-time inventory data, structured catalog information, and fulfillment capabilities, they can manage the entire purchase funnel within their own environments. When we tested Alexa with the same milk request, it provided SKU-level recommendations with exact pricing, delivery windows, and the ability to add items to a cart. Sparky demonstrated similar capabilities, even offering delivery estimates as short as 18 minutes for certain items.

This precision comes with a significant strategic constraint: these systems are confined to their own assortments. Alexa can only recommend products available on Amazon's platform, which means it cannot compare prices across retailers or identify better deals elsewhere. Sparky is similarly limited to Walmart's inventory. For the consumer, this creates a trade-off between convenience and comprehensiveness. For the retailer, it creates a moat—but one that is only as strong as the breadth of their assortment and the stickiness of their ecosystem.

The most revealing finding from our testing is that even these retail-native systems break down at the payment stage. Alexa cannot add Amazon Fresh or Whole Foods products to a cart directly; it directs users to an external link. Sparky requires human engagement to complete the checkout process. This is not a technical limitation that will be solved with better engineering. It is a design choice—or perhaps more accurately, a legal and regulatory constraint—that reflects the complexity of embedding payment authorization within an AI interface. Until this is resolved, the phrase "agentic shopping" remains aspirational.


![Report chart 3](assets/source_image_03.jpg)

## The Grocery Basket Test Reveals a Strategic Trade-Off Between Contextual Intelligence and Operational Precision

Our second test evaluated each tool's ability to build a complete grocery basket for a family of four with specific dietary constraints and a weekly meal plan. This task requires translating meal descriptions into specific quantities, accounting for allergies, avoiding duplicate items, and organizing purchases coherently. The results expose a fundamental strategic trade-off that will define competitive positioning in this space.

The foundational models demonstrated superior contextual intelligence. ChatGPT, Gemini, and Claude all generated comprehensive shopping lists that respected the nut allergy constraint, estimated appropriate quantities for a family of four, and organized items by meal or category. They understood the full complexity of the request in a way that the retail-native systems did not. However, their outputs were lists, not baskets. There was no direct path from recommendation to purchase. The user would need to take the list to a retailer and manually add each item.

Alexa and Sparky took the opposite approach. They provided SKU-level recommendations with accurate pricing and the ability to add items to a cart, but their contextual understanding was weaker. Alexa's capabilities were limited to Amazon's shelf-stable assortment, excluding fresh items entirely. Sparky adopted an interesting workaround: it generated recipes that loosely aligned with the requested meals and allowed users to add all required ingredients from each recipe. This approach was computationally efficient and created a smooth path from idea to purchase, but it sacrificed the flexibility and comprehensiveness that the foundational models offered.

This trade-off has profound implications for how different players will compete. Companies that prioritize contextual intelligence will win the discovery phase but struggle to capture transaction value. Companies that prioritize operational precision will own the transaction but risk being perceived as limited and inflexible. The winners will be those who can combine both capabilities—and that integration challenge is the industry's central strategic problem.

## What the Report Does Not Fully Answer: The Payment Integration Puzzle and the Platform Power Dynamics

For all its analytical rigor, this testing framework leaves several critical questions unresolved. The most important is the payment integration puzzle. Why exactly do even the most advanced retail-native systems fail to complete transactions autonomously? Is this a technical limitation, a regulatory constraint, a liability concern, or a deliberate design choice to maintain human oversight? The answer matters enormously for competitive strategy. If payment integration is technically feasible but legally constrained, then regulatory changes could unlock it overnight. If it is a deliberate design choice to avoid consumer backlash, then consumer education and trust-building become the critical path. If it is a genuine technical challenge, then the first company to solve it will have a durable competitive advantage.

A second unresolved question concerns platform power dynamics. As foundational models like ChatGPT and Gemini build partnerships with retailers and delivery services, who captures the economic value? Is the AI platform a lead generation tool that drives traffic to retailers, or is it a transaction intermediary that could eventually disintermediate retailers entirely? The answer depends on whether these platforms can embed payment capabilities and capture a share of transaction revenue. The current partnership models suggest retailers retain control, but the direction of travel is unclear.

A third question involves the role of consumer behavior. Our testing assumes consumers want fully autonomous shopping. But do they? Many consumers may prefer to retain control over final purchase decisions, especially for groceries where brand preferences, quality concerns, and substitution behaviors are complex. The optimal level of automation may vary by category, occasion, and consumer segment. Understanding this heterogeneity is essential for designing products that consumers actually want to use.

## A Decision Framework for Retailers and Investors Navigating the Agentic Shopping Transition

For executives and investors trying to position for this transition, our analysis suggests a structured decision framework organized around three strategic choices.

The first choice is ecosystem positioning. Retailers must decide whether to build proprietary AI shopping capabilities or partner with general-purpose platforms. Building offers control and data ownership but requires significant investment in AI infrastructure and talent. Partnering offers speed and access to cutting-edge capabilities but risks ceding customer relationships and transaction data to platform companies. The right answer depends on the retailer's scale, technological capabilities, and existing customer relationships.

The second choice is integration depth. Companies must decide how deeply to integrate AI into their shopping experience. Shallow integration—using AI for product discovery and recommendations while maintaining human control over transactions—is lower risk but captures less value. Deep integration—enabling AI to complete purchases autonomously—offers higher potential returns but introduces significant operational, legal, and reputational risks. The optimal depth likely varies by product category, with lower-risk, standardized items being better candidates for deep automation.

The third choice is data strategy. AI shopping tools are only as good as the data they access. Companies must decide what data to share with platform partners, how to protect proprietary data advantages, and how to use data sharing as a competitive lever. Retailers with unique data assets—proprietary customer insights, exclusive product data, or supply chain information—may choose to limit data sharing to maintain their advantage. Those with commoditized data may benefit from broader sharing to improve AI recommendations and drive traffic.

## The Integration Imperative: Why the Next Twelve Months Will Define the Competitive Landscape

The evidence from our testing is clear: no current AI shopping tool can operate as a true agent. Every system breaks down at some point in the purchase funnel, and the most consistent failure point is payment. This is not a temporary limitation that will be solved by incremental improvements. It is a structural gap that reflects the fundamental challenge of connecting AI's cognitive capabilities with the operational infrastructure of commerce.

The companies that close this gap first will capture disproportionate value. They will own the relationship between consumer intent and transaction execution, positioning themselves as indispensable intermediaries in the shopping process. Those that fail to close the gap will be relegated to supporting roles—providing product recommendations that others monetize, or operating fulfillment systems that others control.

The next twelve months will be critical. Partnerships will be formed or broken. Technical architectures will be chosen or foreclosed. Consumer expectations will be set or disappointed. The window for strategic positioning is open now, but it will not remain open indefinitely. Companies that move decisively to integrate discovery and transaction—whether by building, buying, or partnering—will shape the future of commerce. Those that wait will find themselves competing on terms set by others.

Join the community to read the full report and review the original charts.

*This article is for learning and discussion only and does not constitute investment advice.*

<p style="color:#999999;font-size:12px;">Personal reading notes and learning share only. Not investment advice.</p>
